pypoker
============

Found an amazing poker game engine written in javascript at https://github.com/yannlombard/node-poker. The project aims to re-write this poker game engine in Python. 

| Build Status |
| ------------ |
| [![Build Status](https://travis-ci.org/ueg1990/pypoker.svg?branch=master)](https://travis-ci.org/ueg1990/pypoker)|

Setup
====
Clone the public repository by running the following command in the terminal:

    $ git clone https://github.com/ueg1990/pypoker.git
    
Once you have a copy of the source, you can copy the pypoker subfolder (pypoker/pypoker) into your project folder and start using the game engine. Check out example.py on how to run a sample round during a game of poker

Tests
=====

To run all the tests, under the pypoker parent folder, just do:

    $ python -m unittest discover tests -v

To run individual tests, under the pypoker parent folder,

    $ python -m unittest tests.<module name>
    
Author
====
Usman Ehtesham Gul - <uehtesham90@gmail.com>
