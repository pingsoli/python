# 13.7 Copying or Moving Files and Directories

import shutil

# Copy src to dst (cp src dst)
shutil.copy(src, dst)

# Copy files, but preserve metadata (cp -p src dst)
shutil.copy2(src, dst)

# Copy directory tree (cp -R src dst)
shutil.copytree(src, dst)

# Move src to dst (mv src dst)
shutil.move(src, dst)

# copytree() optionally allows you to ignore certain files
# and directories during copy process

def ignore_pyc_files(dirname, filenames):
    return [name in filenames if name.endswith('.pyc'))]

shutil.copytree(src, dst, ignore=ignore_pyc_files)
shutil.copytree(src, dst. ignore=shutil.ignore_patterns('*~', '*.pyc'))
