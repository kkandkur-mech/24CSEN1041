def reverse_sentences(paragraph):
    # Split paragraph into sentences
    sentences = paragraph.split('. ')
    
    # Reverse each sentence
    reversed_sentences = [sentence[::-1] for sentence in sentences]
    
    return '. '.join(reversed_sentences)

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

# Sample paragraph
sample_paragraph = """
Python is widely recognized as a versatile programming language. 
It is used for web development, data science, and artificial intelligence.
"""

# Reverse sentences
reversed_paragraph = reverse_sentences(sample_paragraph)
print("Reversed Paragraph:")
print(reversed_paragraph)

# Count vowels
vowel_count = count_vowels(sample_paragraph)
print("Total Vowels:", vowel_count)
#OUTPUT
Reversed Paragraph:
egaugnal gnimmargorp elitasrev a sa dezingocer ylediw si nohtyP
. 
.ecnegilletni laicifitra dna ,ecneics atad ,tnempoleved bew rof desu si tI

Total Vowels: 47
