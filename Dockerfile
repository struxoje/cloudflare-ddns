FROM python:3.13-alpine

LABEL org.opencontainers.image.source=https://github.com/struxoje/cloudflare-ddns

WORKDIR /app

RUN apt update & apk add --no-cache tzdata 

# Set timezone
ENV TZ=Europe/Prague

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY . .


