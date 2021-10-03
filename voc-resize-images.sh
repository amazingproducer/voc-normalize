#!/bin/bash

#mkdir JPEGImages-resized-w
#mkdir JPEGImages-resized-w/JPEGImages-resized-wh
#for i in *.jpg; do convert "$i" -resize 300x "JPEGImages-resized-w/$i"; done
#cd JPEGImages-resized-w
#for j in *.jpg; do convert "$j" -resize x300 "JPEGImages-resized-wh/$j"; done

mkdir JPEGImages-resized
for i in *.jpg; do convert "$i" -resize 300x300 "JPEGImages-resized/$i"; done
