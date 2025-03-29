# BookBot

## Description

BookBot is a simple command-line tool that analyzes text files (books) and generates a report with the following statistics:
- Total word count
- Character frequency count (sorted by frequency)

The program reads a text file, counts the total number of words, and tallies the frequency of each alphabetic character (case-insensitive). It then displays a formatted report in the terminal.

## Features

- Count total words in a text file
- Count frequency of each alphabetic character (case-insensitive)
- Sort characters by frequency (highest to lowest)
- Clean, formatted output display

## Project Structure

```
bookbot/
├── books/                # Directory containing sample books
│   ├── frankenstein.txt
│   ├── mobydick.txt
│   └── prideandprejudice.txt
├── main.py               # Main program entry point
├── stats.py              # Functions for text analysis
└── README.md             # This file
```

## Installation

1. Clone this repository:
```
git clone <repository-url>
cd bookbot
```

2. No additional dependencies are required as BookBot uses only Python standard libraries.

## Usage

Run the program with a path to a text file:

```
python main.py books/frankenstein.txt
```

### Example Output

```
============ BOOKBOT ============

Analyzing book found at books/frankenstein.txt...

----------- Word Count ----------

Found 77986 total words

--------- Character Count -------

e: 46043
t: 30365
a: 26743
o: 25225
i: 24613
n: 24367
s: 21155
r: 20818
h: 19725
l: 12739
d: 12455
c: 9752
u: 9081
m: 8805
f: 8431
p: 7509
g: 6767
w: 6661
y: 6229
b: 5074
v: 3833
k: 1755
x: 677
j: 504
q: 324
z: 243
============= END ===============
```

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements

- [Boot.dev](https://www.boot.dev) for the project inspiration and guidance