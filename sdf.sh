#!/bin/bash

read -p "Enter a domain: " domain

curl -s "https://crt.sh/?q=%25.${domain}&output=json" | jq -r '.[].name_value' | sort -u
