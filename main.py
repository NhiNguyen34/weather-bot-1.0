import random
import re
import requests
import streamlit as st
from transformers import pipeline

# Intent Identification Function
def identify_intent(user_input):
    user_input = user_input.lower()
    if any(greet in user_input for greet in ["hello", "hi", "hey"]):
        return "greet"
    elif any(bye in user_input for bye in ["bye", "goodbye", "exit", "quit"]):
        return "farewell"
    elif any(weather in user_input for weather in ["weather", "forecast", "rain", "sunny", "temperature"]):
        return "weather"
    return "unknown"

# Extract City Name from User Input
def extract_city(user_input):
    match = re.search(r"in (\w+)", user_input)
    if match:
        return match.group(1)
    return "Hanoi"  # Default to Hanoi if no city is mentioned

# Weather API Response
def get_weather_from_api(city):
    api_key = "your_actual_api_key"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        description = data['weather'][0]['description'].capitalize()
        temp = data['main']['temp']
        return f"The weather in {city} is {description} with a temperature of {temp}°C."
    else:
        return f"Sorry, I couldn't find weather information for {city}."

# Generate Open-Ended Response Using GPT-2
generator = pipeline('text-generation', model='distilgpt2')

def generate_response(prompt):
    response = generator(prompt, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']


def main():
    st.title("Conversational AI Weather Chatbot")
    st.write("Ask me about the weather, or just chat with me!")

    if 'history' not in st.session_state:
        st.session_state['history'] = []
    if 'user_name' not in st.session_state:
        st.session_state['user_name'] = None  # Store the user's name

    # Asking for the user's name if not provided yet
    if st.session_state['user_name'] is None:
        user_name_input = st.text_input("Please enter your name to start the conversation:")  # Prompt for the user's name

        if user_name_input:  # If user has input their name
            st.session_state['user_name'] = user_name_input
            response = f"Nice to meet you, {user_name_input}! How can I assist you today?"
            st.session_state['history'].append({"user": user_name_input, "bot": response})

    else:
        # Main conversation flow after name is provided
        user_input = st.text_input(f"Hello {st.session_state['user_name']}, how can I help you today?", key="input")

        if user_input:
            intent = identify_intent(user_input)

            if intent == "greet":
                response = random.choice([
                    f"Hello {st.session_state['user_name']}! How can I help you today?", 
                    f"Hi there {st.session_state['user_name']}! Need any weather updates?", 
                    f"Hey {st.session_state['user_name']}! What’s on your mind?"
                ])
            elif intent == "weather":
                city = extract_city(user_input)
                response = get_weather_from_api(city)
            elif intent == "farewell":
                response = random.choice([
                    "Goodbye! Stay safe!", 
                    "Take care! See you next time!", 
                    "Bye! Have a nice day!"
                ])
            else:
                response = generate_response(user_input)

            st.session_state['history'].append({"user": user_input, "bot": response})

    # Display conversation history
    st.write("### Chat History")
    for chat in st.session_state['history']:
        st.markdown(f"**You:** {chat['user']}")
        st.markdown(f"**Chatbot:** {chat['bot']}")

if __name__ == "__main__":
    main()
