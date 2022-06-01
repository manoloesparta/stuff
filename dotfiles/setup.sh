#!/bin/bash
DOTFILES_PATH=$(pwd)

FILES=( .zshrc .vimrc .tmux.conf .gitconfig )

for FILE in "${FILES[@]}"
do
	ln -s $DOTFILES_PATH/$FILE $HOME/$FILE
done

touch $HOME/.env

