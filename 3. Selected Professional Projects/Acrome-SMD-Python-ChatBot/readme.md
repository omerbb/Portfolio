# Acrome SMD Library Q&A Chatbot

This project provides a simple Q&A chatbot interface using Streamlit and Google's Gemini API. The chatbot is designed to answer questions related to the Acrome SMD Python library.

## Features

- **Streamlit Interface**: A web-based interface for easy interaction with the chatbot.
- **Generative AI**: Utilizes Google's Gemini API to generate responses based on the Acrome SMD Python library.
- **Dynamic Input Handling**: Accepts user input to formulate a query for the AI model.
- **Markdown Support**: Formats responses in Markdown for better readability.

## Prerequisites

- Docker
- A Google API Key with access to the Gemini API.
- You can get the Gemini API key from [here](https://ai.google.dev/gemini-api)
- The `.env` file containing the `GOOGLE_API_KEY`.

## Installation

1. **Clone the repository**:

    ```bash
    git clone repolink
    cd acrome-smd-qa-chatbot
    ```

2. **Set up your environment**:

    Change the `.env` file in the project to add your Google API key:

    ```plaintext
    GOOGLE_API_KEY=your_google_api_key_here
    ```

3. **Build the Docker container**:

    ```bash
    docker compose build
    ```

4. **Run the application**:

    ```bash
    docker compose up
    ```

5. **Access the chatbot**:

    Open your web browser and navigate to the URL provided by Docker, typically `http://localhost:8501`.

## Code Overview

- **Streamlit Setup**: The script sets up a simple Streamlit interface for user interaction.
- **Google API Configuration**: The Google Gemini API is configured using the API key provided in the `.env` file.
- **Chatbot Logic**: The input is taken from the user, combined with the preloaded text from Acrome-SMD python library repo , and passed to the Gemini API model for generating a response.
- **Markdown Formatting**: The response is formatted using Markdown for clear and structured display.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://cloud.google.com/vertex-ai/generative-ai/overview)
- [Acrome](https://github.com/Acrome-Smart-Motor-Driver/python-library)
- [RepoToText](https://github.com/JeremiahPetersen/RepoToText)

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.
