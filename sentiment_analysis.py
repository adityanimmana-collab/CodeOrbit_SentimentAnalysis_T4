# CodeOrbit Tech - Artificial Intelligence Internship
# Task 5: Sentiment Analysis on Text Data

# Small sample text dataset
texts = [
    "I love this product",
    "This is an amazing experience",
    "The service is excellent",
    "I am very happy with the result",
    "This is a great movie",
    "I hate this product",
    "This is a terrible experience",
    "The service is very bad",
    "I am disappointed with the result",
    "This movie is boring",
    "The product is okay",
    "The service is average",
    "It is neither good nor bad"
]

# Positive words
positive_words = [
    "love", "amazing", "excellent", "happy",
    "great", "good", "wonderful", "fantastic"
]

# Negative words
negative_words = [
    "hate", "terrible", "bad", "disappointed",
    "boring", "poor", "worst"
]


# Function to analyze sentiment
def analyze_sentiment(text):
    words = text.lower().split()

    positive_count = 0
    negative_count = 0

    for word in words:
        if word in positive_words:
            positive_count += 1
        elif word in negative_words:
            negative_count += 1

    if positive_count > negative_count:
        return "Positive"
    elif negative_count > positive_count:
        return "Negative"
    else:
        return "Neutral"


# Display dataset results
print("===== Sentiment Analysis =====")

for text in texts:
    sentiment = analyze_sentiment(text)

    print(f"Text: {text}")
    print(f"Sentiment: {sentiment}")
    print("-" * 40)


# User input
print("\nEnter your own text for sentiment analysis.")

user_text = input("Enter text: ")

result = analyze_sentiment(user_text)

print("Predicted Sentiment:", result)