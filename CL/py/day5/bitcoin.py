import sys
import requests
import json


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    coins = sys.argv[1]
    if  not coins.isdigit():
        sys.exit("Command-line argument is not a number")

    rate = get_bitcoin_price()
    print(f"${(float(coins) * float(rate.replace(',', ''))):,.4f}")

"""
{
    "time": {
        "updated": "Feb 2, 2024 02:13:05 UTC",
        "updatedISO": "2024-02-02T02:13:05+00:00",
        "updateduk": "Feb 2, 2024 at 02:13 GMT"
    },
    "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
    "chartName": "Bitcoin",
    "bpi": {
        "USD": {
            "code": "USD",
            "symbol": "&#36;",
            "rate": "43,187.569",
            "description": "United States Dollar",
            "rate_float": 43187.5688
        },
        "GBP": {
            "code": "GBP",
            "symbol": "&pound;",
            "rate": "33,886.953",
            "description": "British Pound Sterling",
            "rate_float": 33886.9531
        },
        "EUR": {
            "code": "EUR",
            "symbol": "&euro;",
            "rate": "39,720.73",
            "description": "Euro",
            "rate_float": 39720.7299
        }
    }
}

"""
def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        rata = response.json()
        return rata["bpi"]["USD"]["rate"]
    except requests.RequestException:
        sys.exit("Error fetching data from URL")

if __name__ == "__main__":
    main()
