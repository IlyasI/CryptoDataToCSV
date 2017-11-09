#!/usr/bin/env python
# -*- coding: utf-8 -*-

from crycompare import History, Social, News
import csv
import json
import io

def news_to_csv(firstRun=True):
    newsTemp = News
    newsResponse = newsTemp().getNews()
    newsDataFile = io.open('NewsData.csv', 'a', newline='', encoding='utf-8')
    header = ['title', 'source', 'url', 'published_on', 'body', 'tags']
    newsWriter = csv.DictWriter(newsDataFile, header, extrasaction='ignore')
    if firstRun == True:
        count = 0
    else:
        count = 1
    if count == 0:
        newsWriter.writeheader()
        count += 1
    newsWriter.writerows(newsResponse)
    newsDataFile.close()

news_to_csv()

#Returns various social stats to CSV, not sure how often some of these update from the API. The only responsive ones seem to be the CyptoCompare stats.
def social_to_csv(cryptoid, firstRun=True):
    socialTemp = Social
    socialResponse = socialTemp().socialStats(cryptoid)
    socialData = socialResponse['Data']
    socialDataParsed = [{"CoinName": socialData["General"]["Name"],
                "CryptoComparePageViews": socialData["CryptoCompare"]["PageViews"],
                "CryptoCompareComments": socialData["CryptoCompare"]["Comments"],
                "CryptoComparePoints": socialData["CryptoCompare"]["Points"],
                "CryptoComparePosts": socialData["CryptoCompare"]["Posts"],
                "TwitterFollowers": socialData["Twitter"]["followers"],
                "TwitterPoints": socialData["Twitter"]["Points"],
                "TwitterLists": socialData["Twitter"]["lists"],
                "RedditSubs": socialData["Reddit"]["subscribers"],
                "RedditUsers": socialData["Reddit"]["active_users"],
                "RedditPostsPerHour": socialData["Reddit"]["posts_per_hour"],
                "RedditPostsPerDay": socialData["Reddit"]["posts_per_day"],
                "RedditCommentsPerHour": socialData["Reddit"]["comments_per_hour"],
                "RedditCommentsPerDay": socialData["Reddit"]["comments_per_day"],
                "FacebookLikes": socialData["Facebook"]["likes"],
                "FacebookPoints": socialData["Facebook"]["Points"],
                "CodeStars": socialData["CodeRepository"]["List"][0]["stars"],
                "CodeForks": socialData["CodeRepository"]["List"][0]["forks"],
                "CodeIssues": socialData["CodeRepository"]["List"][0]["open_total_issues"],
                "CodeSubscribers": socialData["CodeRepository"]["List"][0]["subscribers"],
                "CodeSize": socialData["CodeRepository"]["List"][0]["size"],
                "CodePoints": socialData["CodeRepository"]["Points"]}]
    socialDataFile = open(cryptoid+'_SocialData.csv', 'a', newline='')

    header = ['CoinName', 'CryptoComparePageViews', 'CryptoCompareComments', 'CryptoComparePoints', 'CryptoComparePosts',
              'TwitterFollowers', 'TwitterPoints', 'TwitterLists', 'RedditSubs', 'RedditUsers', 'RedditPostsPerHour',
              'RedditPostsPerDay', 'RedditCommentsPerHour', 'RedditCommentsPerDay', 'FacebookLikes', 'FacebookPoints',
              'CodeStars', 'CodeForks', 'CodeIssues', 'CodeSubscribers', 'CodeSize', 'CodePoints']

    socialWriter = csv.DictWriter(socialDataFile, header, lineterminator='\n')
    if firstRun == True:
        count = 0
    else:
        count = 1
    if count == 0:
        socialWriter.writeheader()
        count += 1
    socialWriter.writerows(socialDataParsed)
    socialDataFile.close()

#crycompare functions return json, documentation here: https://www.cryptocompare.com/api/#-api-data-histohour-
#crycompare is a python wrapper for the cryptocompare API
def minute_to_csv(crypto, dataPoints, firstRun=False, exchangeCurrency='USD'):
    '''Minute Data JSON to CSV, minute data is only stored for 7 days on CryptoCompare
    set parameter dataPoints to 1440 for minute data over a period of 24 hours, useful
    if used for a scheduler task, the max for dataPoints is 2000.
    If this is the first run, set firstRun argument to True.
    Set crypto parameter to appropriate abreviation for the coin you want data for.
    exchangeCurrency default is USD.'''
    historyTemp = History
    minuteResponse = historyTemp().histoMinute(crypto, exchangeCurrency, limit=dataPoints)
    minuteData = minuteResponse['Data']
    minuteDataFile = open(crypto+'MinuteData.csv', 'a', newline='')
    minuteWriter = csv.writer(minuteDataFile)
    if firstRun == True:
        count = 0
    else:
        count = 1
    for data in minuteData:
        if count == 0:
            header = data.keys()
            minuteWriter.writerow(header)
            count += 1
        minuteWriter.writerow(data.values())
    minuteDataFile.close()

minute_to_csv('BTC', 1440, firstRun=True)

def hourly_to_csv(dataPoints, crypto, exchangeCurrency='USD'):
    '''Hourly Data JSON to CSV, 2000 is the max for the datapoints parameter: stretching back
    83.33 days. Set to 24 to run as a daily task.'''
    historyTemp = History
    hourlyResponse = historyTemp().histohour(crypto, exchangeCurrency, limit=dataPoints)
    hourlyData = hourlyResponse['Data']
    #Write JSON data to CSV file
    hourlyDataFile = open(crypto+'MinuteData.csv', 'a', newline='')
    hourlyWriter = csv.writer(minuteDataFile)
    if firstRun == True:
        count = 0
    else:
        count = 1
    for data in hourlyData:
        if count == 0:
            header = data.keys()
            hourlyWriter.writerow(header)
            count += 1
        hourlyWriter.writerow(data.values())
    hourlyDataFile.close()

def daily_to_csv(crypto, exchangeCurrency='USD'):
    '''Daily Data JSON to CSV, downloads all daily data available
    for the selected cryptocurrency.'''
    historyTemp = History
    dailyResponse = historyTemp().histoDay(crypto=crypto, exchangeCurrency=exchangeCurrency, allData=True)
    dailyData = dailyResponse['Data']
    dailyDataFile = open(crypto+'DailyData.csv', 'a', newline='') #append mode, ensures old data is not overwritten
    dailyWriter = csv.writer(dailyDataFile)
    count = 0
    for data in DailyData:
        if count == 0:
            header = data.keys()
            dailyWriter.writerow(header)
            count += 1
        dailyWriter.writerow(data.values())
    dailyDataFile.close
