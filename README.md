# Weather App

This is a simple **Weather App** built with Python and Tkinter that allows users to get real-time weather information for any city by entering the city name. The app fetches data from the **OpenWeatherMap API**.

## Features
- **City Weather Lookup**: Get weather details like temperature and weather conditions.
- **User-Friendly GUI**: Built with Tkinter for easy interaction.
- **Real-time Weather Data**: Fetches weather data from OpenWeatherMap API.

## Requirements
- **Python 3.x**
- **Tkinter** (Pre-installed with Python)
- **requests** library

## Install Required Libraries
To install the required libraries, run the following command:
```bash
  pip install requests
```
## Setup
  - Get an API Key:
  - Go to [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) and sign up to get an API key.
     - After logging in, go to [API Keys](https://home.openweathermap.org/api_keys) and generate a new key.

  - Add Your API Key to the Code:
      - Replace the placeholder `your_actual_api_key_here` with your generated API key in the code:
        ```python
        API_KEY = "your_actual_api_key_here"
        ```

  - Run the Application:
      - After setting up the API key, run the following command:
        ```bash
        python weather_app.py
        ```

  - Enter a City Name:
      - Enter the name of a city (e.g., "London") and click on **Get Weather** to see the weather data.

## How_it_works
  - The app takes a city name as input.
  - It sends a request to the **OpenWeatherMap API** with the city name and your API key.
  - The response contains data about the weather in that city, including temperature and weather description.
  - The app displays this information in the GUI.

## Sample Output
  - City: London
  - Temperature: 15°C
  - Condition: Clear sky

## Troubleshooting
  - Invalid API Key:
      - Ensure the API key is correctly copied from OpenWeatherMap and there are no extra spaces.
  
  - City Not Found:
      - Double-check the spelling of the city.
      - Try entering the city with the country code, like "London,GB".

## License
  - This project is open-source and available under the MIT License.

## Author
  - AnupamaUshetti

