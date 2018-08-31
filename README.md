# Scrapper---A-Social-Shopping-Chrome-Extention
A chrome extension for Social Shoppong

This is a chrome extention developed to collect the trending tweets from a perticular region and then scrap the related
products from popular shopping e-commerce sites.

In this perticular project I have scrapped Flipkart.

This process includes following steps:- 
1. First creating twitter api key's and then use them to authenticate.
2. After Authenticating extract the trending tweets and store them in a list.
3. Now use <b>Beautiful Soup</b> python library for scrapping the desired website.
4. This all has been implemented in <b><i>scrap.py</b></i> file.
5. Store all the scrapped data in </b>JSON</b> format.
6. Use this JSON data to create the php webpage that will be used for chrome extention.

<h3>Link to chrome Extention</h3>
https://chrome.google.com/webstore/detail/srapper/hbeghfjjfnjoljaphigckfegcgicopai

To use this repository as a extention clone or download it. Then zip the downloaded file and go to:-

1. Chrome settings.
2. Settings --> More Tools
3. More Tools --> Extentions
4. In extentions select <b><u>load unpacked</b></u> and select the zip file created.
