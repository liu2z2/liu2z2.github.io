#!/bin/bash

bash scripts/build.sh
pelican --listen
xdg-open http://localhost:8000/
