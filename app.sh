#!/bin/bash

export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

exec python /app/main.py "$@"