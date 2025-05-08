# cloudflare ddns

Container must be run with:

docker run -d \
  --name cloudflare-ddns \
  --init \
  --env-file .env \
  --restart unless-stopped \
  ghcr.io/struxoje/cloudflare-ddns:latest

so that environmnet variables are set
 