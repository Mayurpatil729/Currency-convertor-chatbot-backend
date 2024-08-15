from flask import Flask, request, jsonify
import requests

# Initialize Flask app
app = Flask(__name__)

# FreeCurrencyAPI key (should be stored securely in environment variables or a config file)
API_KEY = 'fca_live_sNBc1ui17MMyIeaKlFYKXBtz4qINHeEd7lZJRQ9s'


def fetch_conversion_factor(source, target):
    """
    Fetch the conversion factor from the source currency to the target currency using FreeCurrencyAPI.
    """
    url = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}&base_currency={source}&currencies={target}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['data'].get(target)
    else:
        print(f"Error fetching conversion factor: {response.status_code}")
        return None


@app.route('/', methods=['POST'])
def index():
    """
    Handle incoming POST requests to convert currencies.
    """
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']

    cf = fetch_conversion_factor(source_currency, target_currency)
    if cf:
        final_amount = round(amount * cf, 2)
        response = {
            'fulfillmentText': f"{amount} {source_currency} is {final_amount} {target_currency}"
        }
    else:
        response = {
            'fulfillmentText': f"Sorry, I couldn't convert {source_currency} to {target_currency} at this time."
        }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
