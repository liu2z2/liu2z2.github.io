#!/bin/bash

git add .
git commit -a -m "${1:-Update at $(date +%Y-%m-%dT%H:%M:%S%z)}"
git push -u origin pelican-src
pelican content -o output -s pelicanconf.py
ghp-import output -r origin -b main
git push origin main
git checkout pelican-src
