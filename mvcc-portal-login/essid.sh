#!/bin/bash

if [ "$(iwlist wlp107s0 scanning | grep ESSID | cut -d '"' -f 2)" == "MVCC Public" ]
then
   python ~/.config/mvcc-portal-login/autologin.py
fi
