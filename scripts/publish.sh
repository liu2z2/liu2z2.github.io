#!/bin/bash

bash scripts/save.sh
bash scripts/build.sh
ghp-import output -r origin -b main
git push origin main
git checkout pelican-src