#!/bin/bash
set -e

# Allows future additions like secrets/env config
python -m app.main --port 8080 --batch 16