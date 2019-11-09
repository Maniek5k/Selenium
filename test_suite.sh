#!/usr/bin/env bash

alias python="python3.7"

start=$(date +%s)

python login.py && python createaccount.py && python addnewaddress.py && python checkout.py

end=$(date +%s)

runtime=$(python -c "print '%u:%02u' % ((${end} - ${start})/60, (${end} - ${start})%60)")

echo "TEST SUITE executed in $runtime"
