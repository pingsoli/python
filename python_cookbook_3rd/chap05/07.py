# 5.7 Reading and Writing Compressed Datafiles

# gzip and bz2 compression

# gzip compression
import gzip
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

# bz compression
import bz2
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()

# The operations on compressed file is same as regular.

# Specify compression level
with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write(text)
