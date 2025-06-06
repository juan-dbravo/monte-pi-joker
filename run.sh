#!/bin/bash
docker build -t monte-pi-joker .
docker run --env-file .env monte-pi-joker
