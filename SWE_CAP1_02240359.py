##################

# Sonam Choden
# 1st SWE A
# 02240359
##################

#REFERENCES
#Youtube
#ChatGPT
#Dzongkha unicode 

# Problem:
# You are tasked with creating a spell checker for the Dzongkha language. Your program should read a Dzongkha text file (dzo.txt) that contains multiple spelling errors which will be provided by the tutor (refer Accessing Input File section). The program should identify and report these errors.


#####################
#SOLUTION
#####################


import requests

file_url = 'https://csf101-server-cap1.onrender.com/get/input/359'
response = requests.get(file_url)

# wb refers to write binary
with open('359.txt','wb') as file:
    data = file.write(response.content)  

print('Downloaded 359.txt')


import re
import os

def remove_english_characters(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    #Removing english character from the dictionary.txt
    cleaned_dictionary_text = re.sub(r'[^\u0F00-\u0FFF\s]', '', text)
    cleaned_dictionary_text = '\n'.join(cleaned_dictionary_text.split())
    
    # Writing the cleaned text to a new file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_dictionary_text)

input_file_path = 'dictionary.txt'
output_file_path = 'new_dictionary.txt'

remove_english_characters(input_file_path, output_file_path)

print(f"Your dictionary is successfully cleaned and saved to '{output_file_path}'.")

# Check spelling
import re

def read_dictionary(dictionary_file_path):
    "Read the new dictionary into a set."
    with open(dictionary_file_path, 'r', encoding='utf-8') as file:
        dictionary = set(word.strip() for word in file if word.strip())
    return dictionary

def spell_check(input_file_path, dictionary):
    "Check the spelling of words in the input file(359.txt) against the dictionary."
    errors = []

    with open(input_file_path, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, start=1):
            # Split line into words, remove unwanted characters
            words = re.findall(r'[\u0F00-\u0FFF]+', line)
            for word_num, word in enumerate(words, start=1):    
                if word not in dictionary:
                    errors.append((line_num, word_num, word))
    
    return errors

dictionary_file_path = 'new_dictionary.txt'
input_file_path = '359.txt'

# Reading dictionary
dictionary = read_dictionary(dictionary_file_path)

# spelling error check
spelling_error_words = spell_check(input_file_path, dictionary)

# Output using if-else function
if spelling_error_words:
    print("spelling error words found:")
    for line_num, word_num, word in spelling_error_words:
        print(f"Line {line_num}, Word {word_num}: {word} is spelled wrong")
else:
    print("No spelling error words found.")
