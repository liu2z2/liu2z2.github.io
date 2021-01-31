#!/bin/bash

bash scripts/save.sh "${1:-Update at $(date +%Y-%m-%dT%H:%M:%S%z)}"
bash scripts/build.sh
ghp-import output -r origin -b main
git push origin main
git checkout pelican-src
