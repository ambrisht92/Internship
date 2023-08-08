#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
#Sample Text- 'Python Exercises, PHP exercises.'
#Expected Output: Python:Exercises::PHP:exercises:


def replace(text):
    occurences=[' ',',','.']
    for i in occurences:
        text=text.replace(i,':')
    return text
Text='Python Exercises, PHP exercises.'
out=replace(Text)
print(out)


# In[2]:


#Write a Python program to find all words starting with 'a' or 'e' in a given string.
#Sample String= 'Apples and elephants eagerly ate apples'

import re
text='Apples and elephants eagerly ate apples'
word=re.findall(r'\b[ae]\w+',text)
print(word)


# In[3]:


#Question 3- Create a function in python to find all words that are at least 4 characters long in a string.
#The use of the re.compile() method is mandatory.

import re
def word(text):
    pattern=re.compile(r'\b\w{4,}\b')
    wrds=pattern.findall(text)
    return wrds
text='This is a sample sentence with some long words like elephant and computer.'
out=word(text)
print(out)


# In[4]:


#Question 4- Create a function in python to find all three, four, and five character words in a string. 
#The use of the re.compile() method is mandatory.

import re
def word(text):
    pattern=re.compile(r'\b\w{3,5}\b')
    wrds=pattern.findall(text)
    return wrds
text='This is a sample sentence with some long words like elephant and computer.'
out=word(text)
print(out)


# In[5]:


#Question 5- Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.
#Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

import re
def word(text):
    pattern=re.compile(r'\(|\)')
    wrds=[pattern.sub('',i) for i in lst]
    return wrds
lst=["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
out=word(lst)
for i in out:
    print(i)


# In[6]:


#Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
#Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
#Expected Output: ["example", "hr@fliprobo", "github", "Hello", "Data"]
#Note- Store given sample text in the text file and then to remove the parenthesis area from the text.

import re
def word(text):
    pattern=re.compile(r'\([^)]*\)')
    wrds=[pattern.sub('',i) for i in lst]
    return wrds
lst=["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
out=word(lst)
print(out)


# In[7]:


#Question 7- Write a regular expression in Python to split a string into uppercase letters.
#Sample text: “ImportanceOfRegularExpressionsInPython”
#Expected Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]

import re
text="ImportanceOfRegularExpressionsInPython"
word=re.findall(r'[A-Z][a-z]*',text)
print(word)


# In[8]:


#Question 8- Create a function in python to insert spaces between words starting with numbers.
#Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
#Expected Output: RegularExpression 1IsAn 2ImportantTopic 3InPython

import re
def func(text):
    word=re.findall(r'[A-Z0-9][a-zA-Z]*',text)
    return word
Text='RegularExpression1IsAn2ImportantTopic3InPython'
out=func(Text)
print(*out)


# In[9]:


#Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.
#Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
#Expected Output:  Regular Expression 1 Is An 2 Important Topic 3 In Python

import re
def func(text):
    word=re.sub(r'(?<=[a-z0-9])(?=[A-Z0-9])',' ',text)
    return word
Text='RegularExpression1IsAn2ImportantTopic3InPython'
out=func(Text)
print(out)


# In[10]:


#Question 10- Write a python program to extract email address from the text stored in the text file using Regular Expression.
#Sample Text- Hello my name is Data Science and my email address is xyz@domain.com and alternate email address is xyz.abc@sdomain.domain.com. 
#Please contact us at hr@fliprobo.com for further information. 
#Expected Output: ['xyz@domain.com', 'xyz.abc@sdomain.domain.com'] ['hr@fliprobo.com']

import re

def extract(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    emails = re.findall(pattern, text, re.IGNORECASE)
    return emails

Text= 'Hello my name is Data Science and my email address is xyz@domain.com and alternate email address is xyz.abc@sdomain.domain.com.Please contact us at hr@fliprobo.com for further information.'
   

#with open(file_path, 'r') as file:
#    content = file.read()

email_addresses = extract(Text)

for email in email_addresses:
    print(email)


# In[11]:


#Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

import re

test_strings = [
    "ValidString_123",
    "Invalid String",
    "Another_Valid123",
    "Invalid-String"
]

pattern = re.compile(r'^[a-zA-Z0-9_]+$')

for string in test_strings:
    if pattern.match(string):
        print(f"'{string}' is valid.")
    else:
        print(f"'{string}' is not valid.")


# In[12]:


#Question 12- Write a Python program where a string will start with a specific number. 

import re

test_strings = [
    "23ValidString",
    "Invalid String",
    "34Another_Valid",
    "Invalid-String"
]

pattern=re.compile(r'^[0-9]')
for string in test_strings:
    if pattern.match(string):
        print(f"'{string}' is start with specific number")
    else:
        print(f"'{string}' is not start with specific number")


# In[13]:


#Question 13- Write a Python program to remove leading zeros from an IP address

def remove(ip_address):
    parts = ip_address.split('.')
    cleaned_parts = [str(int(part)) for part in parts]
    cleaned_ip = '.'.join(cleaned_parts)
    return cleaned_ip

ip_address = "192.168.001.010"
new_ip_address = remove(ip_address)
print(new_ip_address)


# In[14]:


#Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
#Sample text :'On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
#Expected Output- August 15th 1947

import re

text='On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country.'

pattern = re.compile(r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)?\s+\d{4}\b')

dates=pattern.findall(text)

#with open('sample.txt', 'r') as file:
#    content = file.read()
#   dates = pattern.findall(content)

for date in dates:
    print(date)


# In[15]:


#Question 15- Write a Python program to search some literals strings in a string. 
#Sample text : 'The quick brown fox jumps over the lazy dog.'
#Searched words : 'fox', 'dog', 'horse'

import re
def search(text):
    word=['fox','dog','horse']
    searched=[]
    for i in word:
        searched+=re.findall(i,text)
    return searched
Text='The quick brown fox jumps over the lazy dog.'
out=search(Text)
print(*out)


# In[16]:


#Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
#Sample text : 'The quick brown fox jumps over the lazy dog.'
#Searched words : 'fox'
import re
def search(text):
    word=['fox']
    searched=[]
    for i in word:
        searched+=re.findall(i,text)
    return searched
def search_loc(text,word):
    found_locations = []
    index = text.find(word)
    while index != -1:
        found_locations.append(index)
        index = text.find(word, index + 1)
    return found_locations
Text='The quick brown fox jumps over the lazy dog.'
out=search(Text)
print(*out)

word='fox'
out1=search_loc(Text,word)
print(*out1)


# In[17]:


#Question 17- Write a Python program to find the substrings within a string.
#Sample text : 'Python exercises, PHP exercises, C# exercises'
#Pattern : 'exercises'.

import re
def find_substrings(text, pattern):
    found_substrings=re.findall(pattern,text)
    return found_substrings
sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
found_substrings = find_substrings(sample_text, pattern)
print(found_substrings)


# In[18]:


#Question 18- Write a Python program to find the occurrence and position of the substrings within a string.
import re
def find_substrings(text, pattern):
    found_substrings = [match.start() for match in re.finditer(pattern, text)]
    return found_substrings
sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
found_substrings = find_substrings(sample_text, pattern)
print(f"The pattern '{pattern}' is found at the following positions:")
for position in found_substrings:
    print(position)


# In[19]:


#Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

def convert_date(date):
    parts = date.split('-')
    if len(parts) == 3:
        year, month, day = parts
        converted_date = f'{day}-{month}-{year}'
        return converted_date
    else:
        return "Invalid date format"

input_date = "2023-08-10"
converted_date = convert_date(input_date)
print(f"Converted date: {converted_date}")


# In[20]:


#Question 20- Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. 
#The use of the re.compile() method is mandatory.
import re

def find_number(text):
    pattern = re.compile(r'\b\d+(\.\d{1,2})?\b')
    decimal_numbers = pattern.findall(text)
    return decimal_numbers

Text = "The prices are $12.34, $3.5, and $78.90."
decimal_number = find_number(Text)

for number in decimal_number:
    print(number)


# In[21]:


#Question 21- Write a Python program to separate and print the numbers and their position of a given string.

def func(text):
    number = []
    position = []

    for index, char in enumerate(text):
        if char.isdigit():
            number.append(char)
            position.append(index)

    return number, position

sample_text = "The mango price is 4 rupees and the quantity is 1 kg."
number, position = func(sample_text)

print("Numbers:", number)
print("Positions:", position)


# In[22]:


#Question 22- Write a regular expression in python program to extract maximum/largest numeric value from a string.
#Sample Text:  'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
#Expected Output: 950

import re

def max_num(text):
    numbers = re.findall(r'\d+', text)
    if numbers:
        max_number = max(map(int, numbers))
        return max_number
    else:
        return None

sample_text = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
max_numeric_value = max_num(sample_text)
print(max_numeric_value)


# In[23]:


#Question 23- Create a function in python to insert spaces between words starting with capital letters.
#Sample Text: “RegularExpressionIsAnImportantTopicInPython"
#Expected Output: Regular Expression Is An Important Topic In Python

import re
def func(text):
    word=re.findall(r'[A-Z][a-z]*',text)
    return word
Text='RegularExpression1IsAn2ImportantTopic3InPython'
out=func(Text)
print(*out)


# In[24]:


#Question 24- Python regex to find sequences of one upper case letter followed by lower case letters

import re
pattern = r'[A-Z][a-z]+'
text = "This is a TestSentence with MultipleMatches like ThisOne."
matches = re.findall(pattern, text)
print(matches)


# In[25]:


#Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.
#Sample Text: "Hello hello world world"
#Expected Output: Hello hello world

import re
def remove_duplicates(sentence):
    pattern = r'\b(\w+)\s+\1\b'
    replaced_sentence = re.sub(pattern, r'\1', sentence)
    return replaced_sentence

sample_text = "Hello hello world world"
output = remove_duplicates(sample_text)
print(output)


# In[26]:


#Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character.

import re

def func(input_string):
    pattern = r'\w*[0-9]\b'
    matches = re.findall(pattern, input_string)
    return matches

sample_input = 'abhay12 is a good7 boy'
output = func(sample_input)
print(*output)


# In[27]:


#Question 27-Write a python program using RegEx to extract the hashtags.
#Sample Text:  """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
#Expected Output: ['#Doltiwal', '#xyzabc', '#Demonetization']

import re
def func(text):
    pattern=r'#\w+'
    word=re.findall(pattern,text)
    return word
Text='RT @kapil_kausik: #Doltiwal I mean #xyzabc is hurt by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> acquired funds No wo'
out=func(Text)
print(out)


# In[28]:


#Question 28- Write a python program using RegEx to remove <U+..> like symbols
#Sample Text: "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
#Expected Output: @Jags123456 Bharat band on 28??<ed><ed>Those who  are protesting #demonetization  are all different party leaders

import re

def func(input_text):
    pattern = r'<U\+\w+>'
    cleaned_text = re.sub(pattern, '', input_text)
    return cleaned_text

Text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
output = func(Text)
print(output)


# In[29]:


#Question 29- Write a python program to extract dates from the text stored in the text file.
#Sample Text: Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.

import re

def func(text):
    pattern = r'\d{2}-\d{2}-\d{4}'
    date = re.findall(pattern,text)
    return date

Text='Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.'
output = func(Text)
print(output)


# In[30]:


#Question 30- Create a function in python to remove all words from a string of length between 2 and 4.
#The use of the re.compile() method is mandatory.
#Sample Text: "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
#Expected Output:  following example creates ArrayList a capacity elements. 4 elements added ArrayList ArrayList trimmed accordingly.


import re

def func(text):
    pattern = re.compile(r'\b\w{2,4}\b')
    cleaned_text = pattern.sub('', text)
    return cleaned_text

Text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
output = func(Text)
print(output)


# In[ ]:




