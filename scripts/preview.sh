#!/bin/bash
# Build and local host to preview

bash scripts/build.sh
printf "\n\n\nOpen link http://localhost:8000/ \n\n\n"
pelican --autoreload --listen 