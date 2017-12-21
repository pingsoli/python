#!/bin/bash

directories=$(ls -d ./*/)
target="readme.md"

for dir in $directories
do
  text=$(head -n 1 $dir/$target)
  link=$(echo $text | sed 's/ //' | tr '[A-Z]' '[a-z]' | sed 's/,//g' | sed 's/ /-/g')
  url="https://github.com/pingsoli/python/blob/master/python_cookbook_3rd/$(basename $dir)$link"
  echo "[$text]($url)    " >> $target
done
