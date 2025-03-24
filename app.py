import tkinter as tk
from tkinter import Scrollbar, Text, Entry, Button, END
import random
import json
import pickle
import numpy as np

import nltk


from nltk import WordNetLemmatizer
from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open("intents.json").read())

words = pickle.load(open("words.pkl", "rb"))
classes = pickle.load(open("classes.pkl", "rb"))
model = load_model("chatbotmodel.h5")


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]), verbose=0)[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def get_response(intents_list, intents_json):
    tag = intents_list[0]["intent"]
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i["tag"] == tag:
            result = random.choice(i["responses"])
            break
    return result


class ChatApp:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot GUI")

        # Create a Text widget for displaying the chat
        self.chat_display = Text(master, state=tk.DISABLED, wrap="word")
        self.chat_display.pack(padx=10, pady=10)

        # Create a Scrollbar
        scrollbar = Scrollbar(master, command=self.chat_display.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_display.config(yscrollcommand=scrollbar.set)

        # user input
        self.user_input = Entry(master)
        self.user_input.pack(padx=10, pady=10)

        # Send button
        send_button = Button(master, text="Send", command=self.send_message)
        send_button.pack()

        self.user_input.bind("<Return>", lambda event: self.send_message())

        # Initialize the chatbot
        self.initialize_chatbot()

    def initialize_chatbot(self):
        pass

    def send_message(self):
        # Get user input from Entry widget
        user_message = self.user_input.get()

        # Display user message in the chat display with a "user" tag for color
        self.display_message("You: " + user_message, "user")

        # Get and display chatbot response with a "bot" tag for color
        bot_response = self.get_bot_response(user_message)
        self.display_message("Bot: " + bot_response, "bot")

        # Clear the user input Entry widget
        self.user_input.delete(0, END)

    def get_bot_response(self, user_message):
        # Get the chatbot response using the existing logic
        intents_list = predict_class(user_message)
        bot_response = get_response(intents_list, intents)
        return bot_response

    def display_message(self, message, sender):
        # Display messages in the chat display with different colors based on sender
        self.chat_display.config(state=tk.NORMAL)

        # Configure tags for "user" and "bot" with different colors
        self.chat_display.tag_configure("user", foreground="#90e0ef")
        self.chat_display.tag_configure("bot", foreground="#0077b6")

        # Add the message with the corresponding tag
        self.chat_display.insert(tk.END, message + "\n", sender)

        # Disable the text widget to make it read-only
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
