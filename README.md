<!-- @format -->

# Currency Converter Chatbot Backend

This project is the backend implementation for a **Currency Converter Telegram bot**, using **Google Dialogflow** for natural language processing and **Flask** to handle webhook requests and responses. The bot allows users to convert currencies in real-time by interacting through Telegram.

## Features

- **Currency Conversion**: Converts currency from one type to another in real-time using the Free Currency API.
- **Dialogflow Integration**: Uses Dialogflow to process user queries, identify intents, and extract relevant data such as currency codes and amounts.
- **Flask Webhook**: Connects Dialogflow to the Flask API to process requests and return responses.
- **Ngrok Integration**: Exposes your local Flask server to the internet using Ngrok for webhook testing.
- **Telegram Bot**: Integrates with Telegram to enable users to interact with the bot via messages.

---

## Key Components

### 1. **Dialogflow Agent**

A **Dialogflow Agent** is a virtual assistant that processes user inputs to understand their intent and fulfill their request. In this project, the agent is configured to handle currency conversion queries.

### 2. **Intents**

**Intents** represent the user's purpose for interacting with the chatbot. In this project, an intent is created to handle currency conversion requests.

- **Example Intent**: `ConvertCurrencyIntent`
- **Purpose**: Detects when a user wants to convert from one currency to another.
- **Training Phrases**: Sample user queries that trigger the intent.
  - Example:
    - "Convert 100 USD to EUR"
    - "How much is 50 GBP in INR?"
    - "Can you tell me the value of 10 CAD in JPY?"
- **Action**: Once an intent is matched, the bot uses Flask to trigger a webhook request that processes the currency conversion.

### 3. **Entities**

**Entities** represent key pieces of information extracted from user input. For this project, entities include currency codes and amounts that are necessary for processing the conversion.

- **System Entities**: Predefined entities provided by Dialogflow.
  - **Example**: `@sys.number` to extract numbers like "100" or "50".
- **Custom Entities**: Created to extract specific values such as currency codes.
  - **Example**: `@currency_code` to recognize currencies like "USD," "EUR," "INR," etc.

### 4. **Training Phrases**

**Training Phrases** are examples of user queries that help train the agent to understand different ways users might ask for the same thing. The more varied the training phrases, the better the bot becomes at understanding diverse queries.

- **Examples**:
  - "What is 100 dollars in euros?"
  - "Convert 250 yen to rupees."
  - "I want to know how much 30 euros is in pounds."

### 5. **Fulfillment**

Fulfillment enables the chatbot to execute external logic (e.g., call an API, query a database). In this case, after identifying the user's intent and extracting entities, the bot sends a webhook request to a Flask API, which processes the currency conversion using the Free Currency API.

---

## Prerequisites

- **Python 3.x**
- **Dialogflow Account**: Set up your Dialogflow agent and configure intents and entities.
- **Flask**: For handling webhook requests from Dialogflow.
- **Ngrok**: To create a public URL for local development.
- **Free Currency API**: Sign up at [freecurrencyapi](https://github.com/everapihq/freecurrencyapi-python) to obtain an API key.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/currency-converter-chatbot-backend.git
   cd currency-converter-chatbot-backend
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables for Dialogflow and Free Currency API:

   ```bash
   export DIALOGFLOW_PROJECT_ID=<your-dialogflow-project-id>
   export FREECURRENCY_API_KEY=<your-free-currency-api-key>
   ```

4. Run Ngrok to expose your local Flask server:

   ```bash
   ngrok http 5000
   ```

5. Start the Flask server:

   ```bash
   python app.py
   ```

6. Configure the Dialogflow webhook:
   - Go to **Fulfillment** in Dialogflow.
   - Set the webhook URL to your Ngrok forwarding address (e.g., `https://<ngrok_url>/webhook`).
   - Enable webhook fulfillment in the appropriate intents (e.g., `ConvertCurrencyIntent`).

---

## Dialogflow Integration Details

### Intents Setup

1. **Create an Intent**:

   - Name the intent (e.g., `ConvertCurrencyIntent`).
   - Add **Training Phrases** that represent different ways users might request currency conversion.
   - Define **Entities** to capture the amounts and currency codes in the user’s request.

2. **Add Fulfillment**:
   - Enable fulfillment for the intent in the **Fulfillment** section.
   - When this intent is matched, Dialogflow sends a webhook request to your Flask server.

### Entities Setup

- **Create a Custom Entity** for currency codes (e.g., `@currency_code`).
  - Add currency symbols like USD, EUR, INR, etc., to help the agent understand the user's request.
- Use **System Entities** like `@sys.number` to capture numeric values (e.g., amounts to be converted).

---

## Usage

1. **Telegram Bot Setup**:

   - Create a Telegram bot using [BotFather](https://core.telegram.org/bots#botfather) and obtain the API key.
   - Enable the Telegram integration in Dialogflow and provide the API key.

2. **Testing**:
   - Interact with the bot on Telegram by sending currency conversion queries like:
     - "Convert 100 USD to EUR."
     - "How much is 50 GBP in INR?"

---
# Currency-convertor-chatbot-backend
# Currency-convertor-chatbot-backend
# Currency-convertor-chatbot-backend
# Currency-convertor-chatbot-backend
