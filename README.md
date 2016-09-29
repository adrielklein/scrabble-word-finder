[![Build Status](https://travis-ci.org/adrielklein/scrabble-word-finder.svg?branch=master)](https://travis-ci.org/adrielklein/scrabble-word-finder)

## Welcome to Scrabble Word Finder :smile:
Scrabble word finder is a web app that turns novice scrabble players into champions!

### Routes
- `GET /`: Returns HTML. This is the main route for interacting with the application.
- `GET /words/<letters>`: Takes in a string of scrabble letters as a URI param and returns all scrabble words formed from them.

### Build Instructions
1. Download and install [Python 3.5](https://www.python.org/downloads/release/python-350/)
1. Clone this repository to your machine
1. Open a terminal and change into the root of the repository
1. Install virtualenv `pip install virtualenv`
1. Create a virtual environment `virtualenv venv`
1. Activate the virtual environment `source venv/bin/activate`
1. Install dependencies `pip install -r requirements.txt`

### Running the server
- Run `python start_server.py`

### Running the tests
- Run `py.test tests`

### Implementation Details

The server is written in Python and uses [Flask](http://flask.pocoo.org/) as a web framework.

The business logic of the application can be categorized into three main parts

1. **Anagram Finder**

   Takes in strings and returns anagrams using a special hash table. The hash table maps alphagrams to words. 
2. **Word Finder**

   Finds all combinations of string of lengths `2, 3, .., n` where `n` is the length of the string. Then uses the Anagram Finder to get words for those strings.
3. **Word Finder Route**

   Verifies that the input string is valid and asks the Word Finder for the corresponding words.


