#!/bin/bash 

user="user"
passwd0="password0"
passwd1="password1"

for ip in `cat host.txt`;do
/usr/bin/expect << EOF
set timeout 10
spawn ssh  $user@$ip

expect "*password:"
send "$passwd0\r"

expect "*<*>*"
send "super\r" 

expect "*Password:"
send   "$passwd1\r"

expect "*level is 3*"
send  "dis logb\r"

expect "*More*"
send  "\r    "

expect "*More*"
send  "\r   "

expect eof
EOF
exit
echo "搞掂一台"
done
