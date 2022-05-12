set number " Show file line numbers
set mouse=a " To enable mouse interaction with it
set numberwidth=1 " size of the line numbers
set clipboard+=unnamedplus " enable the nvim clipboard for the clipboard OS
syntax enable " enable hightlights syntaxis
set showcmd " show suggestions commands in this cmd line
set ruler " enable for nvim by default, but not in vim
set colorcolumn=80

" For CoC Plugin
set encoding=utf-8 " encode the plain text 
set hidden
set nobackup
set nowritebackup
set cmdheight=2
set updatetime=300
set shortmess+=c

if has("nvim-0.5.0") || has("patch-8.1.1564")
  set signcolumn=number
else
  set signcolumn=yes
endif


set showmatch " match the parethenses in a function, for example
set sw=4 " Indet with 4 spaces

set relativenumber " for better performance to move the source code

set laststatus=2 " enable the better line botton for information 
set noshowmode " disable to show modes (vim is a text editor based in modes)

"set autochdir

" Plugins!
call plug#begin('~/.vim/plugged')

" Themes
" Plug 'morhetz/gruvbox'
Plug 'dracula/vim',{'as':'dracula'}

" IDE
Plug 'easymotion/vim-easymotion' " To move in the file very faster
Plug 'scrooloose/nerdtree'
Plug 'christoomey/vim-tmux-navigator'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'

Plug 'neoclide/coc.nvim', {'branch': 'release'}

Plug 'mattn/emmet-vim'
Plug 'preservim/nerdcommenter'

Plug 'tpope/vim-fugitive'

call plug#end()


" Setting up for plugins
" colorscheme gruvbox " set the theme
colorscheme dracula

" For NerdTree
let NERDTreeQuitOnOpen=1

" For EasyMotion
let g:EasyMotion_do_mapping=1

" For Airline
let g:airline_powerline_fonts=1
let g:airline#extensions#tabline#enabled = 1

"For CoC
inoremap <silent><expr> <TAB>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ coc#refresh()
inoremap <exp><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

" use <tab> for trigger completion and navigate to the next complete item
function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

" inoremap <silent><expr> <NUL> coc#refresh()
" inoremap <expr> <cr> pumvisible() ? "\<C-y>" : "\<C-g>u\<CR>"

" use <c-space> for trigger completion
if has('nvim')
  inoremap <silent><expr> <c-space> coc#refresh()
else
  inoremap <silent><expr> <c-@> coc#refresh()
endif

inoremap <silent><expr> <cr> pumvisible() ? coc#_select_confirm()
                              \: "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"
" Coc diagnostic
nmap <silent> [g <Plug>(coc-diagnostic-prev)
nmap <silent> ]g <Plug>(coc-diagnostic-next)
" GoTo code navigation.
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)
" Use K to show documentation in preview window.
nnoremap <silent> K :call <SID>show_documentation()<CR>

function! s:show_documentation()
  if CocAction('hasProvider', 'hover')
    call CocActionAsync('doHover')
  else
    call feedkeys('K', 'in')
  endif
endfunction


" Key maps!
let mapleader = " "

nmap <Leader>s <Plug>(easymotion-s2)
nmap <Leader>nt :NERDTreeFind<CR>

" Tab navigation like Firefox or Edge
nmap <Leader>, :bp<CR>
nmap <Leader>. :bn<CR>
nmap <Leader>d :bd<CR>

nmap <Leader>w :w<CR>
nmap <Leader>q :q<CR>
nmap <Leader>x :x<CR>
" nmap <Leader>tt :wq<CR>

nmap <Leader>l :noh<CR>

nmap <Leader>vs :vs<CR>
nmap <Leader>sp :sp<CR>

" Tmux navigation
let g:tmux_navigator_no_mappings = 1

nnoremap <silent> <C-h> :TmuxNavigateLeft<CR>
nnoremap <silent> <C-j> :TmuxNavigateDown<CR>
nnoremap <silent> <C-k> :TmuxNavigateUp<CR>
nnoremap <silent> <C-l> :TmuxNavigateRight<CR>

nnoremap <silent> <C-w>, :vertical resize -10<CR>
nnoremap <silent> <C-w>. :vertical resize +10<CR>

" Change to INSERT mode
:imap jj <Esc>

" For clipboard
vnoremap <C-c> "+y
map <C-v> "+p

" Warning, copy both (nvim and SO)
" vnoremap <C-c> "*y

" For FZF
nmap <Leader>f :Files<CR>

" =========================
" For the problem characters
if !exists('g:airline_symbols')
        let g:airline_symbols = {}
    endif

    " unicode symbols
    let g:airline_left_sep = '»'
    let g:airline_left_sep = '▶'
    let g:airline_right_sep = '«'
    let g:airline_right_sep = '◀'
    let g:airline_symbols.crypt = '🔒'
    let g:airline_symbols.linenr = '☰'
    let g:airline_symbols.linenr = '␊'
    let g:airline_symbols.linenr = '␤'
    let g:airline_symbols.linenr = '¶'
    let g:airline_symbols.maxlinenr = ''
    let g:airline_symbols.maxlinenr = '㏑'
    let g:airline_symbols.branch = '⎇'
    let g:airline_symbols.paste = 'ρ'
    let g:airline_symbols.paste = 'Þ'
    let g:airline_symbols.paste = '∥'
    let g:airline_symbols.spell = 'Ꞩ'
    let g:airline_symbols.notexists = 'Ɇ'
    let g:airline_symbols.whitespace = 'Ξ'

    " powerline symbols
    let g:airline_left_sep = ''
    let g:airline_left_alt_sep = ''
    let g:airline_right_sep = ''
    let g:airline_right_alt_sep = ''
    let g:airline_symbols.branch = ''
    let g:airline_symbols.readonly = ''
    let g:airline_symbols.linenr = '☰'
    let g:airline_symbols.maxlinenr = ''
