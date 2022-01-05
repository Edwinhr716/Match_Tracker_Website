#No longer works as it now requires Captcha verification

import requests
from bs4 import BeautifulSoup
#Use Selenium instead of request because the page is dynamically loaded
from selenium import webdriver
import SQL_Connection


databaseData = []
    
def getData(results):
    soup = BeautifulSoup(results,'html.parser')
    tables = soup.find_all("tr",{"class" : "matchrow"})
    print(soup)
    print(tables)
    allData = []

    for table in tables:
        teamData = {}
        texts = table.find_all("a")
        teamData["competition"] = texts[0].text.strip()
        teamData["date"] = texts[1].text.strip()
        teamData["score"] = texts[2].text.strip()
        allData.append(teamData)

    databaseData.append(allData)



if __name__ == "__main__":

    browser = webdriver.PhantomJS("C:\\Users\\edand\\Downloads\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
    browser.get("https://www.livesoccertv.com/countries/guatemala/")
    html = browser.page_source
    getData(html)

    browser.get("https://www.livesoccertv.com/countries/honduras/")
    html = browser.page_source
    getData(html)

    browser.get("https://www.livesoccertv.com/teams/united-states/austin/")
    html = browser.page_source
    getData(html)

    sqlConnection = SQL_Connection.mySQLServer()
    print(databaseData)
    sqlConnection.setData('guatemala' , databaseData[0])
    sqlConnection.setData('honduras',databaseData[1])
    sqlConnection.setData('austin_fc',databaseData[2])



