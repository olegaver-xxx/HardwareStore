#!/bin/bash

export DJANGO_SETTINGS_MODULE=main.settings
celery -A main beat --loglevel=INFO
