from flask import Flask, Response
import requests


app = Flask(__name__)
@app.route('/<country>')
def hello_world(country):
      country = country
      response = requests.get('https://restcountries.eu/rest/v2/name/' + country + '?fullText=true')
      status_code = response.status_code
      if status_code == 404:
          return Response(
              "Country is not found",
              status=400,
          )
      response=response.json()
      name = response[0]['name']
      capital = response[0]['capital']
      language = response[0]['languages'][0]['name']
      language_native = response[0]['languages'][0]['nativeName']
      currency = response[0]['currencies'][0]['name']
      currency_code = response[0]['currencies'][0]['code']
      response = requests.get(
            'http://data.fixer.io/api/latest?access_key=0f74f9e3e64cb0c2ce6ec5230dc7592d&format=1&symbols=' + currency_code).json()

      rate = response['rates'][currency_code]

      result = f"Name: {name} |     " \
               f"     Capital:            {capital}|     " \
               f"     Language: {language} ({language_native})|      " \
               f"     Currency: {currency} ({currency_code})|      " \
               f"     Rate: 1 EUR =  {rate} {currency_code}|      "

      return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')







