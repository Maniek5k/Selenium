#!/usr/bin/env bash

export PYTHONPATH="$PYTHONPATH:$HOME/.python"

alias python="python3.7"

start=$(date +%s)

python tests/search.py &&
python tests/newslettersubscribe.py &&
python tests/forgotpassword.py &&
python tests/contactus.py &&
python tests/login.py &&
python tests/changepersonalinfo.py &&
python tests/passwordchange.py &&
python tests/addtowishlist.py &&
python tests/createaccount.py &&
python tests/addnewaddress.py &&
python tests/addtobasket.py &&
# python tests/checkoutwire.py &&
# python tests/checkoutcheck.py

end=$(date +%s)

runtime=$(python -c "print '%u:%02u' % ((${end} - ${start})/60, (${end} - ${start})%60)")

echo -e "\e[32mTEST SUITE executed in \e[1m$runtime"
