#!/bin/bash

mkdir JPEGImages-resized
for i in *.jpg; do convert "$i" -resize 300x "JPEGImages-resized/$i"; done

