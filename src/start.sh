#!/bin/bash

gunicorn --log-level=debug \
         --threads=4 \
         --workers 3 \
         --bind=0.0.0.0:8000 \
         main.wsgi:application
