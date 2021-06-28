#!/bin/bash

#while inotifywait -e close_write presentazione.md
#do
#  pandoc presentazione.md -t beamer -o presentazione.pdf -H make-code-scriptsize.tex --highlight-style=espresso
#done

# fswatch presentazione.md | xargs -n1 -I{} pandoc -t beamer -o presentazione.pdf --highlight-style=espresso

pandoc -t beamer presentazione.md -o presentazione.pdf --highlight-style=espresso