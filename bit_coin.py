import requests

def main():
    currency = 'USD'
    BTC = 100.0
    converted = convert_BTC_to_target(BTC, currency)
    display_result(BTC, currency, converted)


def convert_BTC_to_target(BTC, target_currency):
    exchange_rate = get_exchange_rate(target_currency)
    converted = convert(BTC, exchange_rate)
    return converted


def get_exchange_rate(currency):
    response = request_rates(currency)
    rate = extract_rate(response)
    return rate


def request_rates(currency):
    url = 'https://blockchain.info/ticker'
    data = requests.get(url).json()
    print(data[currency])
    return data[currency]



def extract_rate(rates):
    new_rate = rates['buy']
    return new_rate


def convert(amount, exchange_rate):
    return amount * exchange_rate


def display_result(BTC, currency, converted):
    print(f'{BTC:.2f} Bitcoin is equivalent to {currency} {converted:.2f}')


if __name__ == '__main__':
    main()
