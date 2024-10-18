# Dzongkha Spell Checker

## Project Overview
This project is mainly about downloading docs file into txt file from the link provided by sir using last three numbers of our student id.It is used to clean dictionary by removing english characters from the given dictionary and creating clean and  new dictionary without english characters.It is used to check if the spellings in the given input txt is right against the new clean dictionary. 

## Table of Content
- [usage](#usuage)
- [Implementation Details](#implementation-details)
- [Data Structures](#data-structures)
- [Algorithms](#algorithms)
- [Challenges and Solutions](#challenges-and-solutions)
- [Future Improvements](#future-improvements)
- [References](#references)

## Usuage
This project can be used to check any spellings for any Dzongkha written.It is designed to take an input file containing input text, which is then checked against a dictionary to check spelling to correct it.

```bash 
python SWE_CAPI_02240359.py 359.txt
```
## Implementation Details
This Dzongkha spell checker includes the following steps:
1. Downloads the docs file into txt file.
2. Download and removes English characters, numbers, and punctuation from the downloaded dictionary.
3. Creates and saves a new Dzongkha dictionary.
4. Checks the spelling of the words in the downloaded txt file against the new dzongkha dictionary.

## Data Structures
I utilized file operations to open, read, and write to the files, using:
1. 'with open': to enable line-by-line reading and binary writing
2. Set: To store dictionary words for efficient lookups.
3. List: To hold lines from the input text file for an ordered collection and to track spelling errors.
4. String: For processing text, including the contents of both the dictionary and input files.
5. Regular Expressions (re): For identifying and cleaning non-Dzongkha characters from text files.

## Algorithms
1. File Download Algorithm: Downloads a text file from a specified URL and writes its content to a local file.
- Input: URL of the file, local file path.
- Output: Local file with downloaded content.
- Process: Uses the requests library to send a GET request to the URL and writes the content in binary mode to a local file.

2. Text Cleaning Algorithm: Utilizes regular expressions to remove non-Dzongkha characters, including English letters, punctuation, and numbers, from the text.
- Input: Path to the input text file, path to the output cleaned text file.
- Output: Cleaned text file with only Dzongkha characters.
- Process: Reads the input file, uses a regular expression to filter out unwanted characters, and writes the cleaned text to the output file.

3. Dictionary Creating Algorithm: Creates a dictionary of unique Dzongkha words from the cleaned text file.
- Input: Path to the cleaned text file, path to the dictionary file.
- Output: Dictionary file containing unique Dzongkha words.
- Process: Reads the cleaned text file, extracts words using regular expressions, stores unique words in a set, and writes these words to the dictionary file.

4. Dictionary Reading Algorithm: Reads the cleaned dictionary file and stores the words in a set for fast lookups.
- Input: Path to the dictionary file.
- Output: Set of dictionary words.
- Process: Opens the dictionary file, reads words line by line, and stores them in a set.

5. Input Reading Algorithm: Reads the input file line by line for spell checking.
- Input: Path to the input file.
- Output: Lines of text from the input file.
- Process: Opens the input file and reads its content line by line.

6. Spell Checking Algorithm: Go through again each word in the input file, verifies its presence in the dictionary, and records any spelling errors.
- Input: Path to the input file, set of dictionary words.
- Output: List of spelling errors with their positions.
- Process: Reads the input file, splits lines into words, checks each word against the dictionary, and records the line number, word number, and misspelled word for any errors.

## Performance Analysis
1. Scalability: Efficiently handles large text files with line-by-line processing and set lookups.
2. Maintainability: Modular design and single-responsibility functions make the code easy to modify.
3. Usability: User-friendly class structure simplifies running the entire pipeline.
4. Flexibility: Easily adaptable regex and preprocessing steps for various requirements.
5. Error Handling: Basic error handling; can be improved for robustness.
6. Portability: Python-based, compatible across operating systems with standard dependencies.

## Challenges and Solutions
1. Some of the challenges I faced during this project is that it was challenging reading the input and dictionary file which are in dzongkha so, I used the 'encoding = utf-8' which really helped me read the dzongkha characters from the input and output files
2. It was while spell checking through each word in both the input txt file and the dictionary txt file and under the opening file operation I used for loops

## References
1. Dzongkha unicode https://dzongkha.gov.bt/dz/article/dzongkha_website-tech_features
2. Youtube video https://youtu.be/JVQNywo4AbU?si=PtYUpKHH74CwbFfo
3. Requests lib in python https://pypi.org/project/requests/
4. ChatGPT 