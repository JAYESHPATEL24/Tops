# 1) Write a Python script to fetch a random joke from an API and display it on the console:

#    - **Overview**:
#      - We'll use the [Official Joke API](https://official-joke-api.appspot.com/) to fetch a random joke.
#      - The API provides joke data in JSON format, which we will parse and display.

#    **Python Script**:
import requests

def fetch_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"

    try:
        # Make a GET request to the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # print(response.text)

        # Parse the JSON response
        joke_data = response.json()

        # Extract and print the joke
        setup = joke_data.get("setup", "No setup found")
        punchline = joke_data.get("punchline", "No punchline found")

        print("Here's a random joke for you:")
        print(f"{setup}")
        print(f"{punchline}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the joke: {e}")

fetch_random_joke()

# output:
# Here's a random joke for you:
# Why don’t skeletons fight each other?
# They don’t have the guts.

