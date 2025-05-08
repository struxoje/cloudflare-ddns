#!/bin/bash
set -e

docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --no-cache \
  --provenance=false \
  --sbom=false \
  -t ghcr.io/struxoje/cloudflare-ddns:latest \
  --push \
  .
  