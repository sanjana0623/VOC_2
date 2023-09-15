#!/usr/bin/env python
# coding: utf-8

# Write a program to count word frequencies in a given text.

# In[1]:


import string

def count_word_frequencies(text):
    # Remove punctuation and convert text to lowercase
    text = text.lower().translate(str.maketrans('', '', string.punctuation))

    # Split the text into words
    words = text.split()

    # Create an empty dictionary to store word frequencies
    word_counts = {}

    # Iterate through the words and count frequencies
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

# Example text
sample_text = "It is hoped the research will now influence mental health provision and influence therapeutic give to clients.Theresearch further shows that it might be more important to focus on increasing happiness rather than reducing anxiety and stress, which is of course also important, just not as much."

# Call the function to count word frequencies
word_frequencies = count_word_frequencies(sample_text)

# Print the word frequencies
for word, count in word_frequencies.items():
    print(f"{word}: {count}")


# In[ ]:




