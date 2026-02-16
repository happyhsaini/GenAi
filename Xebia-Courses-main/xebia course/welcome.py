import nltk

# 4 major uses of nltk
# a. Tokenization
# b. Stopword removal
# c. Stemming
# d. Lemmatization

nltk.download("punkt_tab")
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

# For tokenization
from nltk.tokenize import word_tokenize

# For removing stopwords
from nltk.corpus import stopwords

# For stemming and lemmatization
from nltk.stem import PorterStemmer, WordNetLemmatizer

import string

text = "I am learning Python programming, it is very helpful!!!<>"
print("Original text:", text)

# Step-1: Lowercase
text = text.lower()
print("After Lowercase :", text)

# Step-2: Tokenization
tokens = word_tokenize(text)
print("Tokens :", tokens)

# Step-3: Remove punctuations
punc = string.punctuation
punctuation_filter = [word for word in tokens if word not in punc]
print("Removed Punctuations:", punctuation_filter)

# Step-4: Remove stopwords
eng_stopwords = stopwords.words("english")
filtered_tokens = [word for word in punctuation_filter if word not in eng_stopwords]
print("Removed stopwords:", filtered_tokens)

# Step-5: Stemming & Lemmatization
stem = PorterStemmer()
stem.stem("bought")

wnet = WordNetLemmatizer()
print("Playing :", wnet.lemmatize("playing", "v"))
print("Flying :", wnet.lemmatize("flying", "v"))
print("Went :", wnet.lemmatize("went", "v"))
print("Bought :", wnet.lemmatize("bought", "v"))

lemmatized_words = []
for word in filtered_tokens:
    lemmatized_words.append(wnet.lemmatize(word, "v"))

print("Lemmatization:", lemmatized_words)

cleaned_text = " ".join(lemmatized_words)
print("Cleaned Text:", cleaned_text)
