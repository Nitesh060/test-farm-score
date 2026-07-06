#!/usr/bin/env bash
set -e

echo "Building and deploying Farm Credit Platform..."
docker-compose build
docker-compose up -d
