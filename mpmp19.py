"""Matt Parker's Maths Puzzles: The 19 Challenge

"If you square all of the first 19 primes and add them you get a multiple of 19.
Enter any number n where the first n primes squared, add to a multiple of n. Any n ≠ 1 counts, but bigger is better!"

More info: http://www.think-maths.co.uk/19challenge
"""

__author__ = "Chad Ross"
__email__ = "chadrt21@gmail.com"
__date__ = "2020-11-30"

import numpy
import sympy
from tqdm import tqdm   # progress bar (may need to install package from: https://github.com/tqdm/tqdm)


# Download & unzip prime numbers files from: http://www.primos.mat.br/2T_en.html
# Each file contains 10 million primes (~101 MB) -> total of 2 billion primes (~20 GB)
num_files = 200
prime_files = ['2T_part{}.txt'.format(f) for f in range(1,num_files+1)]

n_array = []

file_count = 0
n_count = 1
for c in tqdm(range(1,len(prime_files))):

    primes = numpy.loadtxt(prime_files[file_count])
    primes = primes.flatten()

    primes_sq = numpy.power(primes,2)
    primes_cumsum = numpy.cumsum(primes_sq)

    for n in range(1,len(primes)):
        if((primes_cumsum[n-1] % n_count) == 0):
            n_array.append(n_count)
        n_count += 1

    file_count += 1

print()
print('n_array:',n_array)
print('len(n_array):',len(n_array))
print()
print('max n:',f'{n_array[-1]:,}')
numpy.savetxt('mpmp19_out.txt',n_array, fmt='%d',header='All n of the first {:,} primes'.format(n_count))
