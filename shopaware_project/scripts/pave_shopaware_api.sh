#!/bin/bash

# This script will destroy your database and lay down a fresh one for
# core_api development.
# By default, it will use the database "core_api".   Specify the name of your core_api database
# via the first positional argument, e.g.

# ./pave_core_shopaware_api.sh my_db my_username

set -e

# Colorize output
RED='\033[0;31m'
GREEN='\033[0;32m'
NOCOLOR='\033[0m'


DB=${1:-"shopaware_db"}
USER=${2:-"test"}

function run() {
    echo '----------------------------------------------------------------------'
    echo "Running command: $1"
    cmd_output=$(eval $1)
    return_value=$?
    if [ $return_value != 0 ]; then
        echo -e "${RED}Command $1 failed.${NOCOLOR}"
        exit -1
    else
        echo "output: $cmd_output"
        echo -e "${GREEN}Command succeeded!${NOCOLOR}"
    fi
    return $return_value
}

if [ ! -f manage.py ]; then
    echo "Change into directory containing manage.py first."
    exit -1
fi

echo "Paving database: $DB"

run "dropdb --if-exists $DB"
run "createdb $DB"

# Django's test runner requires user permission to create DBs
run "(echo 'ALTER USER $USER CREATEDB NOSUPERUSER NOCREATEROLE' | psql -d $DB && ./manage.py migrate --run-syncdb)"

# TODO: Create a superuser
