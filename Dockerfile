FROM python:3.13-alpine

LABEL org.opencontainers.image.source=https://github.com/struxoje/cloudflare-ddns

# Set timezone
ENV TZ=Europe/Prague

# Set working directory
WORKDIR /app

# Install only essential packages
RUN apk add --no-cache tzdata curl

# Copy files and app logic
COPY app/ requirements.txt ./
COPY run.sh /etc/periodic/15min/run.sh

# Make entry script executable and install dependencies
RUN chmod +x /etc/periodic/15min/run.sh && pip install --no-cache-dir -r requirements.txt

# Default command
CMD ["crond", "-f"]