#!/usr/bin/env python3
   
import requests
from bs4 import BeautifulSoup

def progress_mail():
	return requests.post(
		"https://api.mailgun.net/v3/<domain-name>.mailgun.org/messages",    #edit
		auth=("api", "key-<key_here>"),                                     #edit
		data={"from": "Lord_Voldemort <voldi@hogwarts.com>",
			"to": ["<to-mail>"],                                            #edit
			"subject": "Congratulations",
			"text": "WOW you made a new progress, keep rocking 👏🕵🏻"})

def nchallange_mail():
	return requests.post(
		"https://api.mailgun.net/v3/<domain-name>.mailgun.org/messages",    #edit
		auth=("api", "key-<key_here>"),                                     #edit
		data={"from": "Lord_Voldemort <voldi@hogwarts.com>",
			"to": ["<to-mail>"],                                            #edit
			"subject": "Congratulations",
			"text": "WOW you completed a new challange, keep rocking 👏🕵🏻"})

def main():
	try:
		#parse the page and get the current score
		page = requests.get(f"https://cyberdefenders.org/<user_name>")      #edit
		src = page.content
		soup = BeautifulSoup(src, "lxml") #lxml parser
		scores = soup.find_all("div", {'class': 'py-2 h-full w-full sm:w-1/3 xl:w-[22%] bg-cd_smooth dark:bg-cd_light rounded-xl flex flex-col justify-evenly items-center'})
		challanges = soup.find_all("div", {'class': 'py-2 h-full w-full sm:w-1/3 xl:w-[34%] bg-cd_smooth dark:bg-cd_light rounded-xl flex flex-col justify-evenly items-center'})
		online_points = scores[0].find('p', {'class' : 'text-white'}).text.strip()
		online_challenges = challanges[0].find('p', {'class' : 'text-white'}).text.strip()

		#read the saved score
		with open('score.txt', 'r') as value:
				saved_data = value.readlines()
			
		#compare the two scores if change found update the file
		if online_points != saved_data[0].strip():
			saved_data[0] = online_points + '\n'
			#progress_mail()
			print("There is new progress, mail sent") 

		#compare the two challanges if change found update the file
		if online_challenges != saved_data[1].strip():
			saved_data[1] = online_challenges
			#nchallange_mail()
			print("There is new challange, mail sent")
		
		#write the changes to the score.txt file
		with open('score.txt', 'w') as value:
			value.writelines(saved_data)

	except Exception as e:
		print(f"An error occurred: {e}")

main()
