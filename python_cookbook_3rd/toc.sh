#!/bin/bash

directories=$(ls -d ./*/)
target="readme.md"
prefix="https://github.com/pingsoli/python/blob/master/python_cookbook_3rd"

for dir in $directories
do
  text=$(head -n 1 $dir/$target)
  link=$(echo $text | xargs | tr '[A-Z]' '[a-z]' | sed 's/ //; s/,/ /g; s/  */-/g')
  url="$prefix/$(basename $dir)$link"
  echo "[$text]($url)    " >> $target
done
