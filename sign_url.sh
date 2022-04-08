#!/bin/bash

export PATH=/home/vcap/deps/0/bin:/usr/local/bin:/usr/bin:/bin
export LD_LIBRARY_PATH=/home/vcap/deps/0/lib

python /home/vcap/app/cli.py "$@"