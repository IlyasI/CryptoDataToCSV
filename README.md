# CryptoDataToCSV

Current Functionality:

- CryptoID: Find the CryptoCompare.com ID for your chosen cryptocurrency. Useful for other functions.

`coinid_to_csv("BTC")` or `coinid_to_csv("XMR")`

___
- News: save recent cryptocurrency news to a csv file. Useful for sentiment analysis.

`news_to_csv(firstRun=True)` will save to NewsData.csv

Set `firstRun=False` if you dont want to write the headers. Useful if calling news_to_csv multiple times.

___
- Social Stats: saves various cryptocurrency social media stats to a csv file. Includes CryptoCompare, Twitter, Reddit, Facebook, and Source Code info.

`social_to_csv(cryptoid="1182", firstRun=True)` will save to 'cryptoid'_SocialData.csv.

For the cryptoid parameter above, enter the CryptoCompare.com ID for your chosen cryptocurrency as a string. The ID can be obtained with `coinid_to_csv("BTC")`.

___
- Historical Price Data: saves minute, hourly, and daily CryptoCurrency price data to csv. Useful for time-series analysis.

`daily_to_csv(crypto="BTC", exchangeCurrency="USD")` will save all daily data available to a CSV file

`hourly_to_csv(dataPoints="2000", crypto="BTC", exchangeCurrency="USD")` will save hourly data to a CSV file. 
The maximum dataPoints per API call is 2000 (A CryptoCompare limitation).

`minute_to_csv(crypto="BTC", dataPoints="2000", firstRun=True, exchangeCurrency="USD")` will save minute data to a CSV file.
The maximum dataPoints per API call is 2000 (A CryptoCompare limitation).
___

Powered by the CryptoCompare API.
Uses a modified version of the [cryCompare](https://github.com/stefs304/cryCompare) Python wrapper for the CryptoCompare API by stefs304.

cryptodatatocsv.py functions take the JSON responses returned by the CryptoCompare API and save them to appropriately named .csv files.
I am planning to use the data from this project to explore deep learning applications in cryptocurrency trading.

CryptoCompare API Documentation can be found at https://www.cryptocompare.com/api/#introduction
