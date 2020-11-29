# mpmp19-python

Matt Parker's Math Puzzles: The 19 Challenge - http://www.think-maths.co.uk/19challenge 

## Challenge 

[![Matt Parker](http://img.youtube.com/vi/tBXGIXEV7tI/0.jpg)](http://www.youtube.com/watch?v=tBXGIXEV7tI "The 19 Challenge")


"If you square all of the first 19 primes and add them you get a multiple of 19.
            Enter any number n where the first n primes squared, add to a multiple of n. Any n ≠ 1 counts, but bigger is better!"

## Approach
Instead of generating the primes (which would be resource intensive), I downloaded lists of the first 50 million primes from [PrimePages](https://primes.utm.edu/lists/small/millions/).

Required python libraries: 
- [numpy](https://numpy.org/)
- [tqdm](https://github.com/tqdm/tqdm)

Average run time: ~1 min 14 seconds

## Results
All n (for the first 50 million primes) in which <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;(\sum_{i=1}^{n}&space;p^2&space;)&space;%&space;n&space;=&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;(\sum_{i=1}^{n}&space;p^2&space;)&space;%&space;n&space;=&space;0" title="(\sum_{i=1}^{n} p^2 ) % n = 0" /></a> is met:

[1, 19, 37, 455, 509, 575, 20597, 65440, 77492, 232688, 608672, 801215, 903876, 1005824, 1159850, 1163264, 1227456, 1752576, 1825280, 1974432, 2105344, 2490368, 2536192, 2781784, 3536896, 3665920, 3932208, 4104624, 4339200, 4431872, 5144576, 5177344, 5207700, 5514992, 6368032, 6373376, 6529536, 6646546, 7124992, 8388608, 8777728, 8912896, 9144320, 9961472, 16777216, 17170432, 17955840, 19038208, 21020800, 21379165, 24481792, 24579072, 25059328, 26374144, 28755160, 28835840, 30277632, 32505856, 33554432, 34554156, 36225024, 40101134, 40828928]
