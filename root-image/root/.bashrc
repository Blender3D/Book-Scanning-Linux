#
# ~/.bashrc
#

# If not running interactively, don't do anything

[[ $- != *i* ]] && return

alias ls='ls -a --color=auto'

function cd {
    builtin cd "$@" && ls
}

# uncompress depending on extension...
extract() {
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xvjf $1        ;;
      *.tar.gz)    tar xvzf $1     ;;
      *.bz2)       bunzip2 $1       ;;
      *.rar)       unrar x $1     ;;
      *.gz)        gunzip $1     ;;
      *.tar)       tar xvf $1        ;;
      *.tbz2)      tar xvjf $1      ;;
      *.tgz)       tar xvzf $1       ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1  ;;
      *.7z)        7z x $1    ;;
      *.tar.xz)    tar Jxf $1     ;;
      *)           echo "'$1' cannot be extracted via >extract<" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}

EDITOR="nano"
PATH="/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin:/usr/bin/core_perl"

PS1='\[\033[01;31m\]\u\[\033[01;34m\] \W \$\[\033[00m\] '

echo -en "\e[1;37mBook Scanning\033[00m \033[01;34mLinux\033[00m \e[1;37m`uname -m`\033[00m\n\n"
