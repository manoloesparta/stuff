# ZSH Configuration
ZSH_THEME="robbyrussell"
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export ZSH=$HOME/.oh-my-zsh
export TERM="xterm-256color"

# Git helpers
alias gitlog="git log --all --graph --decorate"
alias minigitlog="git log --all --graph --decorate --oneline"

# Terminal conf
export EDITOR=/usr/bin/vim
export MANPAGER="vim -M +MANPAGER --not-a-term -"

# Typos
alias sl=ls
alias dc=cd

# Get out!
alias cdd="cd .."
alias cddd="cd ../.."
alias cdddd="cd ../../.."

# Random
alias please=sudo
alias huh="grep -rn * -e"

# Functions
function blackformat() {
	git status | grep modified | awk '{ print $2 }' | xargs black
}

function cheat() {
	curl "cheat.sh/$1"
}

function dockerrm() {
	docker rm $(docker ps -aq)
}

function dockerstop() {
	docker stop $(docker ps -aq)
}

function cetys() {
	$HOME/edu/zoom_join/venv/bin/python $HOME/edu/zoom_join/zoom_launcher.py
}

# Linux only
if [[ "$(uname)" == "Linux" ]]; then
	alias open=xdg-open
fi

# WSL only
if [[ -n "$IS_WSL" || -n "$WSL_DISTRO_NAME" ]]; then
	export BROWSER="wslview"
fi

# Stacking dirs
alias pu=pushd
alias po=popd

# Plugins
plugins=(git)

# General setup
source $ZSH/oh-my-zsh.sh

# User local binaries
export PATH=$PATH:$HOME/.local/bin

# Direnv conf
eval "$(direnv hook zsh)"
