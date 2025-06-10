import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py number_of_bitcoins")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument must be a number")

    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin",
                                headers={"Authorization": "20ffe73e23cccb1ae140205fb266425d3a96cbd38eb0ab050cb2136dce010285" })
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price")
    except (KeyError, TypeError, ValueError):
        sys.exit("Unexpected response format from API")

    total = bitcoins * price
    print(f"${total:,.4f}")

if __name__ == "__main__":
    main()



