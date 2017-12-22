#!/bin/bash

directories=$(ls -d ./*/)
target="readme.md"
prefix="https://github.com/pingsoli/python/blob/master/python_cookbook_3rd"
title="# Python Cookbook, 3rd Edition\n## Table of Contents"

# Empty readme.md
>$target
echo -e $title >> $target

for dir in $directories
do
  text=$(head -n 1 $dir/$target | xargs)
  # upper-case to lower-case, next remove special characters(\/,+$^),
  # next strip, next change whitespace to '-'.
  link=$(echo $text | tr '[A-Z]' '[a-z]' | sed 's/[\/\\+,^$#]//g' | xargs | sed 's/  */-/g')

  url="$prefix/$(basename $dir)#$link"
  echo "[$text]($url)    " >> $target
done
