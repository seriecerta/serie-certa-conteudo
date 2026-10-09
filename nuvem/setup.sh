#!/bin/bash
# Setup script do ambiente de nuvem do Claude Code (cole no campo "Script de configuração" do ambiente).
# Roda como root no Ubuntu 24.04 e fica em cache entre sessões.
set -e
apt-get update -qq
apt-get install -y -qq ffmpeg fonts-noto-color-emoji fonts-dejavu-core
pip install -q requests numpy scipy playwright google-api-python-client google-auth google-auth-oauthlib
python -m playwright install --with-deps chromium
