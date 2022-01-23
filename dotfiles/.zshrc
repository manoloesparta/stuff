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
	$HOME/projects/stuff/joinclass/venv/bin/python $HOME/projects/stuff/joinclass/join_class.py
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

# Env managers
export SDKMAN_DIR="$HOME/.sdkman"
[[ -s "$HOME/.sdkman/bin/sdkman-init.sh" ]] && source "$HOME/.sdkman/bin/sdkman-init.sh"

export NVM_DIR="$HOME/.nvm"
[ -s "/usr/local/opt/nvm/nvm.sh" ] && \. "/usr/local/opt/nvm/nvm.sh"
[ -s "/usr/local/opt/nvm/etc/bash_completion.d/nvm" ] && \. "/usr/local/opt/nvm/etc/bash_completion.d/nvm"

[[ -s "/Users/ohno/.gvm/scripts/gvm" ]] && source "/Users/ohno/.gvm/scripts/gvm"

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
