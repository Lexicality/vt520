
if &term == "vt520"
    hi SignColumn term=NONE
    hi LineNr term=NONE
    hi ALEErrorSign term=bold,reverse
    hi ALEWarningSign term=NONE

    hi pythonBuiltinFunc term=bold,underline
    hi Include term=bold
endif


nnoremap <F9> :echo "hi<" . synIDattr(synID(line("."),col("."),1),"name") . '> trans<'
            \ . synIDattr(synID(line("."),col("."),0),"name") . "> lo<"
            \ . synIDattr(synIDtrans(synID(line("."),col("."),1)),"name") . ">"<CR>



