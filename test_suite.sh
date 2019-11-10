#!/usr/bin/env bash

export PYTHONPATH="$PYTHONPATH:$HOME/.python"

alias python="python3.7"

start=$(date +%s)

python tests/newslettersubscribe.py && python tests/login.py && python tests/addtowishlist.py &&  python tests/createaccount.py && python tests/addnewaddress.py && python tests/checkout.py

end=$(date +%s)

runtime=$(python -c "print '%u:%02u' % ((${end} - ${start})/60, (${end} - ${start})%60)")

echo "TEST SUITE executed in $runtime"
