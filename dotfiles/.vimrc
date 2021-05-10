"全ユーザーに適用する場合は [/etc/vim/vimrc] に記述

"文字コードをUFT-8に設定
set fenc=utf-8
"ファイルを上書きする前にバックアップを作ることを無効化
set nowritebackup
"ファイルを上書きする前にバックアップを作ることを無効化
set nobackup
"スワップファイルを作成しない
set noswapfile
"Vimの編集、検索、履歴などの情報・設定が保存されたファイルを作成しない
set viminfo=
"vim の矩形選択で文字が無くても右へ進める
set virtualedit=block
"挿入モードでバックスペースで削除できるようにする
set backspace=indent,eol,start
"----------------------------------------
" 検索
"----------------------------------------
"検索するときに大文字小文字を区別しない
set ignorecase
"小文字で検索すると大文字と小文字を無視して検索
set smartcase
"検索がファイル末尾まで進んだら、ファイル先頭から再び検索
set wrapscan
"インクリメンタル検索 (検索ワードの最初の文字を入力した時点で検索が開始)
set incsearch
"検索結果をハイライト表示
set hlsearch
"Escの2回押しでハイライト消去
nnoremap <Esc><Esc> :nohlsearch<CR><ESC>
"----------------------------------------
"表示設定
"----------------------------------------
"行番号を表示
set number
"現在の行を強調表示
set cursorline
"現在の行を強調表示（縦）
set cursorcolumn
"エラーメッセージの表示時にビープを鳴らさない
set noerrorbells
"コードの色分け
syntax on
"行番号を表示する
set number
"編集中のファイル名を表示
set title
"括弧入力時の対応する括弧を表示
set showmatch
"コードの色分け
syntax on
"入力モードでTabキー押下時に半角スペースを挿入
set expandtab
"インデント幅
set shiftwidth=2
"タブキー押下時に挿入される文字幅を指定
set softtabstop=2
"ファイル内にあるタブ文字の表示幅
set tabstop=2
"オートインデント
set smartindent
"コメントの色を水色
hi Comment ctermfg=3

set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" PHP用辞書の追加
autocmd FileType php,ctp :set dictionary=~/.vim/dict/php.dict

" Vundleの導入 
Plugin 'VundleVim/Vundle.vim'

" 導入したいプラグインを以下に列挙
" Plugin '[Github Author]/[Github repo]' の形式で記入
Bundle 'Shougo/neocomplcache'
Bundle 'Shougo/unite.vim'
Bundle 'thinca/vim-ref'
Bundle 'thinca/vim-quickrun'

call vundle#end()
filetype plugin indent on

"その他のカスタム設定を以下に書く
" バックスペースで補完のポップアップを閉じる
"inoremap <expr><BS> neocomplete#smart_close_popup()."\<C-h>"
"inoremap <expr><CR>  neocomplcache#smart_close_popup() . "\<CR>"
inoremap <expr><TAB>  pumvisible() ? "\<C-n>" : "\<TAB>"
