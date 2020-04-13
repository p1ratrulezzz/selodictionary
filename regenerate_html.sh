#!/usr/bin/env bash

wd=$(pwd -P)
cd $(dirname $0)

if [ -z $(which pyvenv-3.4) ]; then
    echo "Please, install python3-venv first. Exiting."
    exit 1;
fi

INSTALL_PACKETS="no"
if [ ! -d "venv" ]; then
    echo "Creating virtual env venv";
    python3 -m venv venv
    INSTALL_PACKETS="yes"
else
    echo "Virtual env already exists"
fi

source venv/bin/activate

if [[ "$INSTALL_PACKETS" = "yes" ]]; then
    echo "Installing python3 packets";
    pip3 install markdown
    pip3 install mako
    pip3 install transliterate
    pip3 install pathvalidate
fi

echo "Regenerating index.html...";
python3 create_html.py
