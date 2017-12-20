#!/bin/bash

files=`ls | grep '\.py$'`

for file in $files
do
  text=`head -n 1 $file`
  url="https://github.com/pingsoli/python/blob/master/python_cookbook_3rd/chap01/$file"
  echo "[$text]($url)  " >> readme.md
done
