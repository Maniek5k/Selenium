#!/usr/bin/env bash

export PYTHONPATH="$PYTHONPATH:$HOME/.python"

alias python="python3.7"

start=$(date +%s)

python tests/newslettersubscribe.py &&
python tests/login.py &&
python tests/addtowishlist.py &&
python tests/createaccount.py &&
python tests/addnewaddress.py &&
python tests/addtobasket.py &&
python tests/checkout-wire.py &&
python tests/checkout-check.py

end=$(date +%s)

runtime=$(python -c "print '%u:%02u' % ((${end} - ${start})/60, (${end} - ${start})%60)")

echo -e "\e[32mTEST SUITE executed in \e[1m$runtime"
