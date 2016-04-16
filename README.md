# Collatz Sequence Toolkit

**by Troy P. Kling**

## Description

The Collatz sequence is defined by the following iterative process: Take any positive integer *n*. If *n* is even, divide it by 2; otherwise, multiply it by 3 and add 1. Repeat indefinitely. The Collatz conjecture states that no matter what number you start with, the sequence will eventually reach 1. No proof for this conjecture has been discovered yet, making this one of many intriguing open problems in mathematics.

## Installation

Start by ensuring that all dependencies are installed. The Collatz Sequence Toolkit requires the csv, time, and docopt packages.

Next, clone this repository.

    > git clone https://gitlab.com/CoronalRain/Collatz.git

Once the repo is successfully cloned, navigate to the Collatz directory and install the package.

    > python setup.py install

You're now ready to use the Collatz Sequence Toolkit!

## How to Use

You can interface with the tool in two different ways: through Python and through the terminal/command prompt.

### Python

Load the available functions using the following line of code:

    > from collatz import collatz, multiple_collatz, collatz_tree

### Terminal

View the documentation for the Collatz Sequence Toolkit using the following shell command:

    > python collatz.py --help
	
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
