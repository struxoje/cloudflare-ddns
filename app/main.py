import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load values from .env

API_TOKEN = os.getenv('API_KEY')
ZONE_ID = os.getenv('ZONE_ID')

HEADERS = {
    'Authorization': f'Bearer {API_TOKEN}',
    'Content-Type': 'application/json',
}

def get_dns_record_value(record_type, record_name):
    url = f'https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records'
    params = {
        'type': record_type,
        'name': record_name
    }

    response = requests.get(url, headers=HEADERS, params=params)
    if response.status_code == 200:
        results = response.json().get("result", [])
        if results:
            return results[0]["content"]  # IP address or record content
        else:
            print(f"No {record_type} record found for {record_name}")
    else:
        print(f"Error: {response.status_code} - {response.text}")
    return None

def get_current_ip():
    response = requests.get("https://api.ipify.org")
    if response.status_code == 200:
        return response.text.strip()
    else:
        raise Exception("Failed to fetch current IP address.")

def update_dns_record(record_id, record_type, record_name, new_ip):
    url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{record_id}"
    data = {
        "type": record_type,
        "name": record_name,
        "content": new_ip,
        "ttl": 1,
        "proxied": False
    }
    response = requests.put(url, headers=HEADERS, json=data)
    if response.status_code == 200:
        print(f"Updated {record_type} record for {record_name} to {new_ip}")
    else:
        print(f"Failed to update {record_type} record for {record_name}: {response.text}")

dns_records = os.getenv("DNS_RECORDS")
if dns_records:
    current_ip = get_current_ip()
    for entry in dns_records.split(","):
        type_, name = entry.split(":")
        url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records"
        params = {"type": type_, "name": name}
        response = requests.get(url, headers=HEADERS, params=params)
        if response.status_code == 200:
            results = response.json().get("result", [])
            if results:
                record = results[0]
                if record["content"] != current_ip:
                    update_dns_record(record["id"], type_, name, current_ip)
                else:
                    print(f"{type_} record for {name} is up to date.")
            else:
                print(f"No {type_} record found for {name}")
        else:
            print(f"Error fetching record for {name}: {response.status_code} - {response.text}")
else:
    print("No DNS_RECORDS found in environment.")