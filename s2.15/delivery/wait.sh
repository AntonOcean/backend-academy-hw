#!/bin/bash
while ! nc -z 127.0.0.1 5672; do sleep 3; done
python3 delivery/cron.py