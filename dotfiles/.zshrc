# ZSH Configuration
export ZSH="/home/manolo/.oh-my-zsh"
ZSH_THEME="robbyrussell"

# Git helpers
alias gitlog="git log --all --graph --decorate"
alias minigitlog="git log --all --graph --decorate --oneline"

# Docker helpers
alias killdocker="docker kill $(docker ps -q)"
alias rmdocker="docker rm $(docker ps -a -q)"
alias rmidocker="docker rm $(docker images -q)"

# Get out!
alias cdd="cd .."
alias cddd="cd ../.."
alias cdddd="cd ../../.."

# Random
alias please='sudo'
alias open=xdg-open

# Plugins
plugins=(git)

# General setup
source $ZSH/oh-my-zsh.sh

# Go setup
export PATH=$PATH:/usr/local/go/bin
