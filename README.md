# **weather-bot-1.0**

## **Introduction**
This is a **Weather Chatbot** built with **Streamlit** that integrates with the OpenWeather API to provide weather updates. The chatbot can:
- Recognize user intents such as **greetings**, **weather inquiries**, or **farewell messages**.
- Provide weather information based on the city mentioned by the user (defaults to Hanoi if no city is specified).
- Generate open-ended responses using **GPT-2** from Hugging Face’s `transformers` library.


## **Setup**

### **1. System Requirements**
- Python >= 3.8
- Conda (for virtual environment management)
- Docker (optional if you want to run the project in a container)
- API key from OpenWeather (replace it in the code)

### **2. Local Setup Using Conda**

1. Clone the repository:

   ```
   git clone <repository-url>
   cd project/
    ```
   
2. Create a Conda virtual environment:
     
     ```
    conda create --name weather-chatbot python=3.8
    conda activate weather-chatbot
    ```
3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Run the application:
    ```
    streamlit run main.py
    ```
5. Access the chatbot. Open a browser and go to:
    ```
    http://localhost:8501
    ```
### **3. Running with Docker**

1. Build the Docker image:

   ```
    docker build -t weather-chatbot .
    ```
3. Run the Docker container:

   ```
    docker run -p 8501:8501 weather-chatbot
    ```
5. Access the chatbot in the browser:

   ```
    http://localhost:8501
    ```

## **Usage Instructions**


1. Enter Your Name: When the app starts, you will be prompted to enter your name to begin the conversation.
2. Interact with the Chatbot: You can:
    - Greet the bot using: "hello", "hi", or "hey".
    - Ask for the weather in any city, e.g., "What’s the weather in Hanoi?" or "Tell me the forecast for London."
    - End the conversation with: "bye", "exit", or "quit".

## **Key Components Explained**
- Intent Identification: The `identify_intent()` function classifies user input into three main intents: greeting, weather inquiry, or farewell.

- Weather API Integration: The `get_weather_from_api()` function calls the OpenWeather API to fetch weather information based on the city name. If the city is not found, it returns an error message.

- Open-Ended Responses with GPT-2: The distilgpt2 model from Hugging Face generates responses for inputs that don’t match predefined intents.

** Important Notes
- Replace the API key in the code with your own key from OpenWeather: `api_key = "your_actual_api_key"`
- For any questions or issues, please contact me or open an issue on the GitHub repository.


