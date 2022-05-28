#!/bin/bash

export PATH=/home/vcap/deps/0/bin:/usr/local/bin:/usr/bin:/bin
export LD_LIBRARY_PATH=/home/vcap/deps/0/lib
export PYTHONPATH=/home/vcap/app

python /home/vcap/app/flow_client/cli.py "$@"