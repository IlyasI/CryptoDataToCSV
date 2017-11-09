# CryptoDataToCSV

Current Functionality:
- News: save recent cryptocurrency news to a csv file. Useful for sentiment analysis.

`news_to_csv(firstRun=True)` will save to NewsData.csv

Set `firstRun=False` if you dont want to write the headers. Useful if calling news_to_csv multiple times.

- Social Stats: saves various cryptocurrency social media stats to a csv file. Includes CryptoCompare, Twitter, Reddit, Facebook, and Source Code info.

`social_to_csv('cryptoid', firstRun=True)` will save to 'cryptoid'_SocialData.csv.
Enter cryptoid as a string (include the '' around the id)



Powered by the CryptoCompare API.
Uses a modified version of the [cryCompare](https://github.com/stefs304/cryCompare) Python wrapper for the CryptoCompare API.

cryptodatatocsv.py functions take the JSON responses returned by the CryptoCompare API and save them to appropriately named .csv files.
I am planning to use the data from this project to explore deep learning applications in cryptocurrency trading.

CryptoCompare API Documentation can be found at https://www.cryptocompare.com/api/#introduction
