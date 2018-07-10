from urllib.request import urlopen
from multiprocessing.dummy import Pool as ThreadPool

urls = [
    'http://192.168.123.23/',
    'http://192.168.123.23/hello.txt',
    'http://192.168.123.23/',
    'http://192.168.123.23/yellow.jpg',
    'http://192.168.123.23/',
    'http://192.168.123.23/',
    'http://192.168.123.23/hello.txt',
    'http://192.168.123.23/',
    'http://192.168.123.23/'
]

# make the pool of workers
pool = ThreadPool(5)

# open the urls in their own threads and return the results
results = pool.map(urlopen, urls)

url = 'http://192.168.123.23/'
for i in range(1, 100):

# close the pool and wait for the work to finish
pool.close()
pool.join()
