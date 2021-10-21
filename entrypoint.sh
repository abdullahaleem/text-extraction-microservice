#!/bin/bash

RUN_PORT = ${PORT:-8000}
# The platform will set the port and incase it doesn't the backup port will be 8000

# Having the entry here the benefit is we can test it locally
/usr/local/bin/gunicorn --worker-tmp-dir /dev/shm -k uvicorn.workers.UvicornWorker app.main:app --bind "0.0.0.0:${RUN_PORT}"
