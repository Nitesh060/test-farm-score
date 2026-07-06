#!/usr/bin/env bash
set -e

echo "Setting up backend..."
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd ..

echo "Setting up frontend..."
cd frontend
npm install
cd ..

echo "Dev environment ready."
