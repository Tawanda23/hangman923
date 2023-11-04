import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier

# Define the training data
train_data = {
    'query': ['Hi there', 'Hello', 'Goodbye', 'See you later'],
    'category': ['greeting', 'greeting', 'goodbye', 'goodbye']
}

# Create a DataFrame from the training data
df = pd.DataFrame(train_data)

# Vectorize the text data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['query'])

# Create the decision tree classifier
classifier = DecisionTreeClassifier()
classifier.fit(X, df['category'])

# Assistant function to classify user queries
def classify_query(query):
    query_vector = vectorizer.transform([query])
    prediction = classifier.predict(query_vector)
    return prediction[0]

# Test the assistant
user_query = input("Enter your query: ")
category = classify_query(user_query)
print("Category:", category)
