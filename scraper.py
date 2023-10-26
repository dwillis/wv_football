import csv
import requests
from bs4 import BeautifulSoup

years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2018, 2019, 2020, 2021, 2022, 2023]

games = []

def state_from_team(team):
    if "(KY)" in team:
        state = "KY"
    elif "(OH)" in team:
        state = "OH"
    elif "(MD)" in team:
        state = "MD"
    elif "(VA" in team:
        state = "VA"
    elif "(PA)" in team:
        state = "PA"
    elif "(NC)" in team:
        state = "NC"
    elif "(ON)" in team:
        state = "ON"
    elif "(CN)" in team:
        state = "CN"
    elif "(SC)" in team:
        state = "SC"
    elif "(DC)" in team:
        state = "DC"
    elif "(DE)" in team:
        state = "DE"
    elif "(NY)" in team:
        state = "NY"
    elif "(NY)" in team:
        state = "NY"
    elif "(TN)" in team:
        state = "TN"
    elif "(NJ)" in team:
        state = "NJ"
    elif "(MI)" in team:
        state = "MI"
    elif "(A)" in team:
        state = "PA"
    else:
        state = "WV"
    return state

for year in years:
    print(year)
    url = f"http://wvtailgatecentral.com/hs/fb{year}/week_schedule.php?startdate={year}-08-01&enddate={year}-12-31"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    rows = soup.find('table').find_all('tr')[1:]
    for row in rows:
        date = row.find_all('td')[0].text
        if "**" in row.find_all('td')[1].text:
            home_team = row.find_all('td')[1].text.replace(" **", "")
            home_team_score = row.find_all('td')[2].text
            home_team_state = state_from_team(home_team)
            visiting_team = row.find_all('td')[3].text
            visiting_team_score = row.find_all('td')[4].text
            visiting_team_state = state_from_team(visiting_team)
        elif "**" in row.find_all('td')[3].text:
            home_team = row.find_all('td')[3].text.replace(" **", "")
            home_team_score = row.find_all('td')[4].text
            home_team_state = state_from_team(home_team)
            visiting_team = row.find_all('td')[1].text
            visiting_team_score = row.find_all('td')[2].text
            visiting_team_state = state_from_team(visiting_team)
        else:
            print("No home team!")
            home_team = row.find_all('td')[1].text.replace(" **", "")
            home_team_score = row.find_all('td')[2].text
            home_team_state = state_from_team(home_team)
            visiting_team = row.find_all('td')[3].text
            visiting_team_score = row.find_all('td')[4].text
            visiting_team_state = state_from_team(visiting_team)
        score_diff = abs(int(home_team_score) - int(visiting_team_score))
        games.append([year, date, home_team, home_team_score, home_team_state, visiting_team, visiting_team_score, visiting_team_state, score_diff])

with open("scores.csv", "w") as f:
    output_file = csv.writer(f)
    output_file.writerow(["year", "date", "home_team", "home_team_score", "home_team_state", "visiting_team", "visiting_team_score", "visiting_team_state", "differential"])
    output_file.writerows(games)
