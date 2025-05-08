# cloudflare-ddns

## What is it?

This project provides a lightweight Alpine-based Docker container that runs a Python script every 15 minutes. The script checks if your public IP address (assigned by your ISP) has changed, and if so, updates your DNS records on Cloudflare accordingly.

## Who is it for?

Anyone hosting services from a home network and needing reliable, public DNS updates.

## How to use it

1. From your Cloudflare account, obtain your **Zone ID** and generate a custom API token with the following permissions:
   - **All Zones**:
     - Zone Settings: Read
     - Zone: Read
     - DNS: Edit

2. Copy the `.env.dev` file and update it with your credentials.

3. Specify the DNS record type and names you want monitored and updated. For example:

   ```
   DNS_RECORDS=A:mail.my.domain,A:my.domain
   ```

### Running the container

```bash
docker run -d \
  --name cloudflare-ddns \
  --init \
  --env-file .env.dev \
  --restart unless-stopped \
  ghcr.io/struxoje/cloudflare-ddns:latest
```

## Building from source

If you prefer to build the container yourself:

1. Clone the repository:

   ```
   git clone https://github.com/struxoje/cloudflare-ddns.git
   ```

2. Modify `build-container.sh` to push the container to your preferred registry.

3. Run `build-container.sh` on a Linux system or Apple Silicon Mac.

4. Update the `.env.dev` file as described above and start the container using the provided `docker run` command.

---

Feel free to reach out with any questions or issues.