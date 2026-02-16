# Intent Classification using NLP and Machine Learning

# First import text processing libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK resources
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

# Second import sklearn dependencies
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Training data with text and corresponding intent labels
training_data = [
    ("hello", "greet"),
    ("hi there", "greet"),
    ("good morning", "greet"),
    ("hey", "greet"),
    ("what's the weather today", "weather"),
    ("tell me weather", "weather"),
    ("is it raining", "weather"),
    ("open", "open_app"),
    ("open google", "open_app"),
    ("open youtube", "open_app"),
    ("bye", "exit"),
    ("goodbye", "exit")
]

# Separate sentences and labels
sentences = []
labels = []

for text, intent in training_data:
    sentences.append(text)
    labels.append(intent)

# Import punctuation list
import string
punc = string.punctuation

# Text preprocessing function
def preprocess_text(sentences):
    cleaned_sentences = []
    for sentence in sentences:
        # Convert text to lowercase
        text = sentence.lower()
        
        # Tokenization
        tokens = word_tokenize(text)
        
        # Remove punctuation
        punctuation_filter = [word for word in tokens if word not in punc]
        
        # Remove stopwords
        eng_stopwords = stopwords.words("english")
        filtered_tokens = [word for word in punctuation_filter if word not in eng_stopwords]
        
        # Lemmatization
        wnet = WordNetLemmatizer()
        lemmatized_words = []
        for word in filtered_tokens:
            lemmatized_words.append(wnet.lemmatize(word, "v"))
        
        # Join words back into sentence
        cleaned_text = " ".join(lemmatized_words)
        cleaned_sentences.append(cleaned_text)
    
    return cleaned_sentences

# Preprocess training data
clean_data = preprocess_text(sentences)

# Convert text into numerical features using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(clean_data)

# Train Logistic Regression model
logistic = LogisticRegression()
logistic.fit(X, labels)

# Take user input
user_input = "hola"

# Preprocess user input
processed = preprocess_text([user_input])

# Vectorize user input
user_vector = vectorizer.transform(processed)

# Predict intent
prediction = logistic.predict(user_vector)
print(prediction)
