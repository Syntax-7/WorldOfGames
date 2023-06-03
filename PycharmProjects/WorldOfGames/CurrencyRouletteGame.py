import requests
import json


class Currency:
    difficulty = 1
    conversion_rate = 0
    answer_range = [0, 0]
    user_guess = 0


# gets the currency conversion rate by "apilayer" api, inputs the conversion rate value in "Currency.conversion_rate"
# class variable.
# then it inputs the Currency.answer_range array by the following interval:
# 1st value: currency rate - (total difficulty - chosen difficulty).
# 2nd value: currency rate - (total difficulty + chosen difficulty).
def get_money_interval():
    url = 'https://api.apilayer.com/exchangerates_data/convert?to=ILS&from=USD&amount=1'

    payload = {}
    headers = {
        "apikey": "Bsc1yWc6I8peyeHEEAsI966wfwstDUsj"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    data = response.text

    parse_json = json.loads(data)
    Currency.conversion_rate = parse_json['result']

    Currency.answer_range = [Currency.conversion_rate - (5 - Currency.difficulty),
                             Currency.conversion_rate + (5 - Currency.difficulty)]


# function that prompts input from the user into Currency.user_guess class variable, compares it to the
# "Currency.answer range" class variable and returns a boolean back to "play" function.
def get_guess_from_user():
    Currency.user_guess = input("Please enter your guess for current conversion rate from \"USD\" to \"ILS\": ")
    return Currency.answer_range[0] <= float(Currency.user_guess) <= Currency.answer_range[1]


# calls get_money_interval & get_guess_from_user functions, and prints the boolean from get _guess_from_user function.
def play():
    get_money_interval()
    result = get_guess_from_user()
    print(result)


play()
