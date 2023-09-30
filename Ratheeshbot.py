import requests
from bs4 import BeautifulSoup
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import openai
import json

# Initialize the OpenAI API client with your API key
openai.api_key = "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"  # Replace with your actual OpenAI API key

# Create a chatbot
chatbot = ChatBot("Ratheesh")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Load the list of search engines from a JSON file
with open("search_engines.json", "r") as f:
    search_engines = json.load(f)

# Define the search query
query = "Python programming"

# Loop through the list of search engines and perform searches
for engine in search_engines:
    search_url = engine["url"] + query
    
    # Display the search engine being used
    print(f"Searching on {engine['name']} for '{query}':")
    
    # Send an HTTP GET request to the search engine
    response = requests.get(search_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the search results using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract and display the search results
        results = soup.find_all("div", class_="result")
        print(f"Search results from {engine['name']} for '{query}':")
        for i, result in enumerate(results, 1):
            title = result.find("h3").get_text()
            link = result.find("a")["href"]
            print(f"{i}. {title}")
            print(link)
    else:
        # Handle errors here
        print(f"Failed to perform the search on {engine['name']}")

# Continue with the rest of your code...
import requests
from bs4 import BeautifulSoup
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import openai
import json

# Initialize the OpenAI API client with your API key
openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your actual OpenAI API key

# Create a chatbot
chatbot = ChatBot("Ratheesh")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Load the list of search engines from a JSON file
with open("search_engines.json", "r") as f:
    search_engines = json.load(f)

# Define the search query
query = "Python programming"

# Loop through the list of search engines and perform searches
for engine in search_engines:
    search_url = engine["url"] + query
    
    # Display the search engine being used
    print(f"Searching on {engine['name']} for '{query}':")
    
    # Send an HTTP GET request to the search engine
    response = requests.get(search_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the search results using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract and display the search results
        results = soup.find_all("div", class_="result")
        print(f"Search results from {engine['name']} for '{query}':")
        for i, result in enumerate(results, 1):
            title = result.find("h3").get_text()
            link = result.find("a")["href"]
            print(f"{i}. {title}")
            print(link)
    else:
        # Handle errors here
        print(f"Failed to perform the search on {engine['name']}")


