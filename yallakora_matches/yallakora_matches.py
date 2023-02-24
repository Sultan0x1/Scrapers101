import requests
from bs4 import BeautifulSoup
import csv

date = input("please enter a date: MM/DD/YY")
page = requests.get(f"https://www.yallakora.com/match-center?date={date}")

def main(page):
    
    src = page.content
    soup = BeautifulSoup(src, "lxml") #lxml parser
    matches_details = []
    championships = soup.find_all("div", {'class': 'matchCard'}) #fa method, no3 eltag, dic(key:class, value: class name) 

    def get_match_info(championships):
        championship_title = championships.contents[1].find("h2").text.strip()
        matches = championships.contents[3].find_all('li')
        number_of_matches = len(matches)

        for i in range(number_of_matches):
            #get teams names
            team_A =  matches[i].find('div', {'class' : 'teamA'}).text.strip()
            team_B =  matches[i].find('div', {'class' : 'teamB'}).text.strip()
            #get teams Score
            match_result = matches[i].find('div', {'class' : 'MResult'}).find_all('span', {'class' : 'score'})
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"
            #match time
            match_time = matches[i].find('div', {'class' : 'MResult'}).find('span', {'class' : 'time'}).text.strip()
            #add match info to matches_details
            matches_details.append({"نوع البطولة":championship_title, "الفريق الأول":team_A, "الفريق الثاني":team_B,"ميعاد المباراة":match_time,"النتيجة":score})
    for i in range(len(championships)):
        get_match_info(championships[i])
    #print(matches_details)

    keys = matches_details[0].keys()

    with open('matches_details.csv', 'w', encoding="utf8") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(matches_details)
        print("file created")


main(page)
