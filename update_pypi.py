#!/bin/bash

username="$(op item get 'pypi.org' --format json --fields 'username' | jq -r '.value')"
password="$(op item get 'pypi.org' --format json --fields 'password' | jq -r '.value')"
python3 -m poetry publish --build -u "${username}" -p "${password}"

