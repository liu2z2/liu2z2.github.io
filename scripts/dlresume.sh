#!/bin/bash
# Update resume, pulled from my other repo

curl -s https://api.github.com/repos/liu2z2/resume/releases/latest | grep "browser_download_url.*pdf" | cut -d '"' -f 4 | wget -O content/extra/resume.pdf -qi -
