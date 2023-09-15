from bs4 import BeautifulSoup
import requests, openpyxl

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Premier League Current Table'
sheet.append(['Place', 'Team Name', 'Played', 'Wins', 'Defeats', 'Loses', 'Goals Scored', 'Goals Conceded', 'Goal '
                                                                                                            'Difference',
              'Points'])

try:

    source = requests.get('https://www.skysports.com/premier-league-table', headers=HEADERS)
    source.raise_for_status()
    soup = BeautifulSoup(source.text, 'html.parser')
    # i=1
    for i in range(1, 21):
        positions = soup.find_all('tr', class_='standing-table__row')[i]
        # print(positions)
        # i=i+1
        for position in positions:
            place = positions.find('td', class_='standing-table__cell').text
            name = positions.find('td', class_='standing-table__cell standing-table__cell--name').a.text
            points = positions.find_all('td', class_='standing-table__cell')[9].text
            gd = positions.find_all('td', class_='standing-table__cell')[8].text
            a = positions.find_all('td', class_='standing-table__cell')[7].text
            f = positions.find_all('td', class_='standing-table__cell')[6].text
            l = positions.find_all('td', class_='standing-table__cell')[5].text
            d = positions.find_all('td', class_='standing-table__cell')[4].text
            w = positions.find_all('td', class_='standing-table__cell')[3].text
            pl = positions.find_all('td', class_='standing-table__cell')[2].text
        sheet.append([place, name, pl, w, d, l, f, a, gd, points])

except Exception as e:
    print(e)
excel.save('PremLeagueTable.xlsx')