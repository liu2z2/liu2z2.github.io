#!/bin/bash
# Simply commit and push

git add .
git commit -a -m "${1:-Update at $(date +%Y-%m-%dT%H:%M:%S%z)}"
git push -u origin pelican-src