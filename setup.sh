#!/bin/bash

sudo tee /etc/udev/rules.d/10-streamdeck.rules << EOF
    SUBSYSTEMS=="usb", ATTRS{idVendor}=="0fd9", GROUP="users"
    EOF


# Reload udev rules to ensure the new permissions take effect
    sudo udevadm control --reload-rules

# Install the latest version of the StreamDeck library via pip
pip3 install streamdeck