import os
from decouple import config
import openai
import streamlit as st

openai.api_key = config("OPENAI_API_KEY")

st.title("Name my pet")
animal = st.text_input("Enter an animal")

def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )

response = openai.Completion.create(
    engine="text-davinci-001",
    prompt=generate_prompt(animal),
    temperature=0.6,
)

st.text(response.choices[0].text)