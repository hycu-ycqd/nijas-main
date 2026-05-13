#!/usr/bin/env bash
# QA build script
set -euo pipefail

echo "[QA] Starting build..."
pip install -r requirements.txt
python -m pytest tests/ -v --tb=short
echo "[QA] Build complete."
