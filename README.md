# Sentiment Analysis on Text Data

## CodeOrbit Tech – Artificial Intelligence Internship

### Task 5: Sentiment Analysis on Text Data

## 📌 Project Description

This project implements a simple sentiment analysis system using Python.

The program analyzes text and classifies it into three categories:

* Positive
* Negative
* Neutral

A small sample text dataset is used for testing. The program also allows the user to enter their own text and receive a predicted sentiment.

## 🎯 Objectives

* Understand the basic concept of sentiment analysis.
* Work with a small text dataset.
* Identify positive and negative words.
* Classify text as Positive, Negative, or Neutral.
* Accept user input and predict its sentiment.

## 🛠️ Technologies Used

* Python
* String processing
* Lists
* Functions
* Conditional statements
* Basic rule-based sentiment analysis

## ⚙️ How It Works

The program contains lists of positive and negative words.

For each input sentence:

1. The text is converted to lowercase.
2. The sentence is split into individual words.
3. Positive words are counted.
4. Negative words are counted.
5. The counts are compared.
6. The final sentiment is predicted.

### Sentiment Rules

* Positive count > Negative count → Positive
* Negative count > Positive count → Negative
* Positive count = Negative count → Neutral

## 📊 Example

### Positive

Input:

```text
I love this movie
```

Output:

```text
Positive
```

### Negative

Input:

```text
I hate this movie
```

Output:

```text
Negative
```

### Neutral

Input:

```text
The movie is okay
```

Output:

```text
Neutral
```

## ▶️ How to Run

Open the terminal inside the project folder and run:

```bash
python sentiment_analysis.py
```

## 📂 Project Structure

```text
CodeOrbit_SentimentAnalysis/
│
├── sentiment_analysis.py
├── README.md
│
└─  ├── output1.png
    ├── output2.png
    └── output3.png
```

## 🎓 Learning Outcome

Through this project, I learned the basics of text processing and sentiment classification using Python. I also learned how simple word-based rules can be used to classify text into positive, negative, and neutral categories.

## 👨‍💻 Internship Task

**Organization:** CodeOrbit Tech

**Internship:** Artificial Intelligence Internship

**Task:** Task 5 – Sentiment Analysis on Text Data
