# 🤖 Chatbot Project

This is a simple AI-powered chatbot built using Python, TensorFlow, and Tkinter for the GUI. The chatbot processes user input, predicts the intent using a trained deep learning model, and provides responses accordingly.

## 🚀 Features

Uses NLP techniques for text processing

Deep learning model for intent recognition

GUI built with Tkinter

Supports multiple intents with varied responses

## 🛠 Installation

### Prerequisites

Make sure you have Python installed. You can install the required dependencies using:

```bash
pip install numpy tensorflow nltk pickle-mixin
```

Additionally, download the NLTK resources:
```bash
import nltk
nltk.download('punkt')
nltk.download('wordnet')
```
## 📂 Files Overview

chatbot.py: Core chatbot logic for handling user input, intent prediction, and response generation.

app.py: Tkinter-based GUI application for the chatbot.

intents.json: Defines various intents and corresponding responses.

chatbotmodel.h5: Trained deep learning model for intent classification.

words.pkl and classes.pkl: Preprocessed data used for prediction.

## ▶️ Running the Chatbot

### Command Line Interface (CLI)
```bash
To run the chatbot in the terminal: python chatbot.py
```

### Graphical User Interface (GUI)

```bash
To launch the GUI version: python app.py
```

## Training the Model

If you need to retrain the chatbot, ensure you have a script that processes the intents.json file, tokenizes text, and trains a neural network. You can create a script like train.py for this purpose.

## Repository Structure
```bash
chatbot-project/

│-- chatbot.py

│-- app.py

│-- intents.json

│-- chatbotmodel.h5

│-- words.pkl

│-- classes.pkl

│-- README.md

│-- .gitignore

```
## .gitignore File

To avoid pushing unnecessary files, create a .gitignore file and add:

__pycache__/

*.pkl

*.h5

venv/

.env

## Future Improvements

Enhance the NLP pipeline for better intent recognition

Add more intents and responses

Improve the chatbot's conversational abilities with a larger dataset

## License

Feel free to use and modify this project for **educational purposes!**
