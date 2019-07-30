import bs4, requests
    #This is code I had to add so Chrome could use Amazon without getting a 503 error
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }
def getWeatherTemp(url):
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elems = soup.select('#current_conditions-summary > p.myforecast-current-lrg')
        return elems[0].text.strip()
        
        
price = getWeatherTemp('https://forecast.weather.gov/MapClick.php?x=320&y=186&site=ctp&zmx=&zmy=&map_x=320&map_y=186#.Wvh-4YgvyUk')
print('The temperature of Philadelphia is ' + price)



