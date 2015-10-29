"""
Collatz Sequence Toolkit 1.0

Usage:
  collatz.py [options]
  collatz.py multiple [options]
  collatz.py tree [options]
  collatz.py (-h | --help)
  collatz.py --version

Options:
  -n --num <int>       Generate the Collatz sequence for this integer. If the 
                       "multiple" argument was specified, generate all Collatz 
                       sequences for integers less than/equal to this integer.
  -o --output <file>   File for outputting multiple Collatz sequences.
  -h --help            Show this screen.
  -v --verbose         Show runtime info.
  --version            Show version.
"""

from docopt import docopt

import csv
import time

def collatz(n):
    if n < 1:
        return []
    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n+1
        seq.append(n)
    
    return seq

def multiple_collatz(n):
    if n < 1:
        return []
    sequences = []
    for i in range(1,n+1):
        c = i
        seq = [c]
        while c != 1:
            if c % 2 == 0:
                c = c/2
            else:
                c = 3*c+1
            if c < i:
                seq += sequences[c-1]
                break
            seq.append(c)
        sequences.append(seq)
    
    return sequences

def collatz_tree():
    pass



if __name__ == '__main__':
    arguments = docopt(__doc__, version = "Collatz Sequence Toolkit 1.0")
    
    n = int(arguments["--num"])
    multiple = arguments["multiple"]
    tree = arguments["tree"]
    verbose = arguments["--verbose"]
    output = arguments["--output"]
    
    if not multiple and not tree:
        c = collatz(n)
        print "Collatz sequence for n=%s: %s" % (str(n), str(c))
    if multiple:
        if verbose:
            print "Calculating Collatz sequences for n=1 to %s..." % str(n)
        start = time.time()
        c = multiple_collatz(n)
        elapsed = time.time() - start
        if verbose:
            print "Elapsed time: %s seconds." % elapsed
            print "Time per sequence: %s milliseconds" % str(1000*elapsed/n)
        if output != None:
            with open(output, "wb") as f:
                if verbose:
                    print "Writing results to %s..." % output
                writer = csv.writer(f)
                writer.writerows(c)
    elif tree:
        print "Tree method not yet implemented."
