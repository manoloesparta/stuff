syntax on

" Vim-Plug installation
if empty(glob('~/.vim/autoload/plug.vim'))
  silent !curl -fLo ~/.vim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

" Nice settings
set noerrorbells
set tabstop=4 softtabstop=4
set shiftwidth=4
set smartindent
set number
set smartcase
set noswapfile
set incsearch

" Realtive no. line
set relativenumber
set rnu

" Non 4 spaces for identattion
autocmd Filetype html setlocal ts=2 sw=2 expandtab
autocmd Filetype css setlocal ts=2 sw=2 expandtab
autocmd Filetype scss setlocal ts=2 sw=2 expandtab
autocmd Filetype javascript setlocal ts=2 sw=2 expandtab
autocmd Filetype yaml setlocal ts=2 sw=2 expandtab
autocmd Filetype yml setlocal ts=2 sw=2 expandtab
autocmd Filetype json setlocal ts=2 sw=2 expandtab

" Plugins to install
call plug#begin('~/.vim/plugged')
	Plug 'romainl/Apprentice'
	Plug 'preservim/nerdtree'
	Plug 'eemed/sitruuna.vim'
call plug#end()

" Selected colorscheme
colorscheme apprentice 

" YCM error checking deactivated
let g:ycm_show_diagnostics_ui = 0

" NERDTree
map <F2> :NERDTreeToggle<CR>
