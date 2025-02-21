import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter


reviews = [
    "The product is amazing! I love it.",
    "Terrible experience. The quality is so bad.",
    "Fast delivery, good packaging, and excellent product.",
    "Not satisfied with the quality of the item.",
    "The item is okay, but the shipping took too long."
]

#Removing Stop Words
stop_words=set(stopwords.words("english"))
punctuation=set(string.punctuation)

# Tokenize, clean, and preprocess the text
filtered_words=[]
for review in reviews:
    words=word_tokenize(review.lower())
    words=[word  for word in words if word not in stop_words and word not in punctuation]
    filtered_words.extend(words)

# Count word frequency
word_freq=Counter(filtered_words)

# Get the top 3 most frequent words
top_three_words=word_freq.most_common(3)
print(top_three_words)



