#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)
if [ -f $SCRIPT_DIR/start_worker_local.sh ]; then
    source $SCRIPT_DIR/start_worker_local.sh
fi
export DJANGO_SETTINGS_MODULE=main.settings
celery -A main worker --loglevel=INFO -n worker-@%n
