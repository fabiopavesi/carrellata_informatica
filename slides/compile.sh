#!/bin/bash

while inotifywait -e close_write presentazione.md
do
  pandoc presentazione.md -t beamer -o presentazione.pdf -H make-code-scriptsize.tex --highlight-style=espresso
done

