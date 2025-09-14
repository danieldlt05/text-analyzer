# text_analyzer.py
"""This file analyzes a sample plain text file and outputs:
Total words;
Number of unique words;
Most frequently used words (Top 5);
Long words (4 or more letters).
"""

from collections import Counter

TOP_WORDS = 5     # how many frequent words to display
MIN_LONG_LEN = 4    # treat words with length >= 4 as "long"

def read_text(file_path):
    """Return the entire contents of a text file as a string."""
    with open(file_path, 'r') as f:
        return f.read()

def split_words(text):
    """Return a list of lowercase words (simple whitespace split)."""
    return text.lower().split()

def count_words(words):
    """Return a Counter mapping each word to its frequency."""
    return Counter(words)

def find_long_words(words, min_length=MIN_LONG_LEN):
    """Return a list of words with a length that is >= min_length."""
    return [w for w in words if len(w) >= min_length]


def print_report(word_counts, long_words, top_numbers=TOP_WORDS, min_length=MIN_LONG_LEN):
    """Print the summary stats using f-strings and Counter.most_common()."""
    # total words = sum of all counts; unique words = number of keys in the Counter
    print(f"Total words: {sum(word_counts.values())}")
    print(f"Unique words: {len(word_counts)}")
    print(f"Most frequent words (top {top_numbers}):")
    for word, count in word_counts.most_common(top_numbers):
        print(f"'{word}': {count}")
    print(f"Long words ({min_length} or more letters): {len(long_words)}")


def analyze_file(file_name):
    """Read a text file, 
    count words, 
    show top words, 
    and report long-word count."""

    # 1) Read File
    text = read_text(file_name)
    
    # 2) Normalize and Split Into Words
    words = split_words(text)
    
    # 3) Count Word Frequencies (Counter)
    word_counts = count_words(words)
    
    # 4) Filter Long Words (List Comprehension)
    long_words = find_long_words(words, MIN_LONG_LEN)

    # 5) Report Findings        
    print_report(word_counts, long_words, TOP_WORDS, MIN_LONG_LEN)


# Use Script to Read and Report on File (makes script reusable this way)
if __name__ == "__main__":
    analyze_file("sample.txt")