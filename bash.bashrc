#!/bin/bash
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
	command_not_found_handle() {
		/data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
	}
fi

adduser(){
	python $PREFIX/login/readduser.py
}
falselogin(){
	python $PREFIX/login/db_falselogin.py
}
changepass(){
	python $PREFIX/login/changepass.py
}
clear
python $PREFIX/login/.login.py
clear
neofetch
PS1='\e[0;37m\]┌─\[\e[1;37m\][\[\e[0;36m\]root\[\e[0;37m\]@\[\e[1;31m\]aji\[\e[1;37m]\[\e[1;30m\]\w\n\[\e[0;37m\]└─╼\[\e[1;31m\]$ \[\e[0;32m\]'