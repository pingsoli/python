# 13.8 Creating and Unpacking Archives

# common formats(.tar, .tgz, .zip)

import shutil
# shutil.unpack_archive('Python-3.6.3.tgz')
# shutil.make_archive('py63', 'zip', 'Python-3.6.3')

# Check out all supported formats
#print(shutil.get_archive_formats())
# [
#  ('gztar', "gzip'ed tar-file"), 
#  ('tar', 'uncompressed tar file'), 
#  ('zip', 'ZIP file')
# ]
