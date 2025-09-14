# text_analyzer.py

A small Python script that reads a plain text file and prints:

- **Total words**
- **Number of unique words**
- **Most frequently used words (Top Words)**
- **Long words (length >= threshold)**

## Features

- **PEP 8**
- **Context managers**
- **Idiomatic counting**
- **List comprehension**
- **Easily readable desgin**
- **Reusable entry point**

## How It Works

1. **Read** the file into a string ('read_text').
2. **Normalize & split** into lowercase words ('split_words').
3. **Count** word frequencies using 'Counter' ('count_words').
4. **Filters** "long" words via list comprehension ("find_long_words').
5. **Report** totals, unique words, top words, and long-word count ('print_report').

## How to Perform

1. Put your input file in the same folder, e.g. 'sample.txt'.
2. Run:
   python3 --version   # to ensure correct python is active
   python3 text_analyzer.py
