#!/bin/bash

directories=$(ls -d ./*/)
target="readme.md"

for dir in $directories
do
  text=$(head -n 1 $dir/$target)
  url="https://github.com/pingsoli/python/blob/master/python_cookbook_3rd/$(basename $dir)"
  echo "[$text]($url)    " >> $target
done
