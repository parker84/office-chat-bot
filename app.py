import os
from decouple import config
import openai
import streamlit as st

openai.api_key = config("OPENAI_API_KEY")

st.title("Dunder Mifflin Rabies Awareness Chatbot For the Cure")


jim_line = st.text_input("Enter a line for Jim:")

def dwight_and_jim_prompt(jim_line):
    return f"""Suggest what Dwight will say next

Dwight: Jim, tell him where he can stick his grapes!
Jim: In the fridge!
Dwight: No, Jim. The butt. In his butt.

Dwight: What is your name, sir?
Jim: My name is Billy Buttlicker.
Dwight: Really? That's your real name?
Jim: How dare you?

Jim: Dwight tried to kiss me. And I didn't tell anyone because I'm not really sure how I feel about it.
Dwight: That is not true. Redact it. Redact it!
Jim: Well I'm not actually making a formal complaint. I just really think we should talk about it.

Dwight: Well then. Do you have any special needs or dietary restrictions?
Jim: Yes. We will be requiring a bedtime story.
Dwight: No.
Jim: Not even Harry Potter?

Dwight: Every day, for eight years, I have brought pepper spray into this office, to protect myself and my fellow employees. And every day, for eight years, people have laughed at me. Well, who's laughing now?

Dwight: Disconnect that right now. Give me your earpiece.
Jim: I can't do that. Unsanitary.

Dwight: I'm going to be your new boss. It's my greatest dream come true. Welcome to Hotel Hell. Check-in time is now, checkout time is never.
Jim: Can I change rooms?
Dwight: Sorry, we're all booked up. Hell convention in town. We'll have to talk to the manager.
Jim: You're not the manager? Even in your own fantasy?

Jim: {jim_line}
Dwight:"""

response = openai.Completion.create(
    engine="text-davinci-001",
    prompt=dwight_and_jim_prompt(jim_line),
    temperature=0.6,
)

st.text(response.choices[0].text)