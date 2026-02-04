def word_counter(text):
    # Remove punctuation and convert to lowercase
    import string
    
    # Clean up the text
    clean_text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    
    # Split into words
    words = clean_text.split()
    
    # Count the occurrences of each word
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

# Sample text
sample_text = """
Python is great for data analysis and machine learning. 
Python is also widely used in web development. 
The versatility of Python makes it an excellent choice for beginners and experienced programmers alike.
"""

# OUTPUT
result = word_counter(sample_text)
print("Word Count:")
for word, count in result.items():
    print(f"{word}: {count}")
Word Count:
python: 3
is: 2
great: 1
for: 2
data: 1
analysis: 1
and: 2
machine: 1
learning: 1
also: 1
widely: 1
used: 1
in: 1
web: 1
development: 1
the: 1
versatility: 1
of: 1
makes: 1
it: 1
an: 1
excellent: 1
choice: 1
beginners: 1
experienced: 1
programmers: 1
alike: 1


