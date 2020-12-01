"""Primes downloader

Downloads 2 billion primes from http://www.primos.mat.br/2T_en.html for a total of 20 GB
"""

__author__ = "Chad Ross"
__email__ = "chadrt21@gmail.com"
__date__ = "2020-11-30"

import os
import py7zr
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm   # progress bar (may need to install package from: https://github.com/tqdm/tqdm)


# Download & unzip prime numbers files from: http://www.primos.mat.br/2T_en.html
# Each file contains 10 million primes (~101 MB) -> total of 2 billion primes (~20 GB)
num_files = 2
prime_files_URL = ['http://www.primos.mat.br/dados/2T_part{}.7z'.format(f) for f in range(1,num_files+1)]
prime_files = ['2T_part{}.7z'.format(f) for f in range(1,num_files+1)]
# TODO Check OS

# TODO Check 7z

# Confirm download of 20 GB
print()
print("NOTE: Depending on internet speed this may take a up to a few hours.")
ask = input("Do you want to download 2 billion primes which would take up 20 GB (y/n):")
if (ask.upper() == 'Y'):

    # TODO Download files
    print('Downloading files')
    for c in tqdm(range(0,len(prime_files))):
        file = requests.get(prime_files_URL[c], allow_redirects=True)
        open(prime_files[c],'wb').write(file.content)


    # TODO Unzip files to current directory
    print('Unzipping files')
    for c in tqdm(range(0,len(prime_files))):
        py7zr.SevenZipFile(prime_files[c],mode='r').extractall()

    # # TODO remove zip files
    print('Removing zipped files')
    for c in tqdm(range(0,len(prime_files))):
        os.remove(prime_files[c])
