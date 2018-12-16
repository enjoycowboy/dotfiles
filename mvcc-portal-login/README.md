# Wireless Captive Portal Login - MVCC #

A small python script to automatically login to MVCC's wireless portal
by headless Firefox browser on connect to wireless access point ESSID - "MVCC
Wireless"

### Dependencies ###
   Firefox
   Python 3.7
   Selenium module (python)

### Notes ###
Until I work out the kinks with python grabbing a GPG encrypted portal login
password with gnupg, I can only recommend you use the included config.py file
to store and import your password. After doing so, you can at least lock down
the file permissions on that one particular file.

### Use ###
   1. Edit the autologin.py script to include your login name where specified.
   2. Edit the included config.py file with the your login password. After
      which lock the file permissions down with chmod 700.
      a. I will enable encryption by GPG shortly to avoid the use of a password
      in clear text.
   3. Enclosed is also an essid.sh script. Depending on your distribution,
      within your network configuration files, there is usually a directory
      which enables the autoexecution of script files within certain
      directories when certain wireless adapters are used. See "dispatcher.d"

