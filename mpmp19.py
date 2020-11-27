"""Matt Parker's Maths Puzzles: The 19 Challenge

"If you square all of the first 19 primes and add them you get a multiple of 19.
Enter any number n where the first n primes squared, add to a multiple of n. Any n ≠ 1 counts, but bigger is better!"

More info: http://www.think-maths.co.uk/19challenge
"""

__author__ = "Chad Ross"
__email__ = "chadrt21@gmail.com"
__date__ = "2020-11-27"

import numpy
import sympy
from datetime import datetime
from tqdm import tqdm   # progress bar (may need to install package from: https://github.com/tqdm/tqdm)

start = datetime.now()

# Download & unzip prime numbers files from: https://primes.utm.edu/lists/small/millions/
num_files = 50
prime_files = ['primes{}.txt'.format(f) for f in range(1,num_files+1)]

n_array = []

file_count = 0
n_count = 1
for c in tqdm(range(1,len(prime_files))):

    primes = numpy.loadtxt(prime_files[file_count],skiprows=1)
    primes = primes.flatten()

    primes_sq = numpy.power(primes,2)
    primes_cumsum = numpy.cumsum(primes_sq)

    for n in range(1,1000000):
        if((primes_cumsum[n-1] % n_count) == 0):
            # print('n:',n_count)
            # print('primes:',primes[:n])
            # print('primes_sq:',primes_sq[:n])
            # print('sum primes_sq:',primes_cumsum[n-1])
            # print('sum primes_sq / n:',primes_cumsum[n-1]/n)
            # print('sum primes_sq % n:',primes_cumsum[n-1]%n)
            n_array.append(n_count)
        n_count += 1

    file_count += 1

print()
print("Durtation:",datetime.now()-start)
print('n_array:',n_array)
print('len(n_array):',len(n_array))
print()
print('max n:',f'{n_array[-1]:,}')
numpy.savetxt('mpmp19_out.txt',n_array)
