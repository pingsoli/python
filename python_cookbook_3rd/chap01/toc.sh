#!/bin/bash

files=`ls | grep '\.py$'`

for file in $files
do
  head -n 1 $file >> readme.md
done
