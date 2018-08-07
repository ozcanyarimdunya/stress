from multiprocessing import Pool
from multiprocessing import cpu_count

def f(x):
    while True:
        x*x

if __name__ == '__main__':
    processes = int(cpu_count()/2)
    print('utilizing %d cores\n' % processes)
    try:
    	pool = Pool(processes)
    	pool.map(f, range(processes))
    except:
    	import sys
    	sys.exit(0)
