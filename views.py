from django.shortcuts import render

def index(request):
	return render(request, 'personal/home.html')

def contact(request):
	return render(request, 'personal/basic.html', {'content': ['If you would like to contact me', 'edmondye502@gmail.com']})


def projects(request, proj):
	if proj == 'personalpage':
		content = {'Name': 'Personal Page', 'Description': "A Personal Website I set up to tell you more about myself and the projects I've worked on. This page was set up using Python and Django.", 'Links' : {'Link': '/', 'Github': 'https://github.com/edmondye502/personal'}}
	elif proj == 'budget':
		content = {'Name': 'Budget', 'Description': "A cronjob script I set up that takes specific emails about a purchase and automatically inserts it into my budget sheet. I made this script to help me keep track of my expenses by sending a simple text to a email I set up.", 'Links' : {'Github': 'https://github.com/edmondye502/budget'}}
	elif proj == 'edohub':
		content = {'Name': 'EdoHub', 'Description': "I realized whenever I first turn on my computer I visit the same sites each time just to look at a couple things. I decided to make a site that would gather all the data from each of those sites and display it all in one place. This project was made using Python, Django, and a bunch of APIs.", 'Links' : {'Github': 'https://github.com/edmondye502/edohub'}}
	elif proj == 'foodpicker':
		content = {'Name': 'Food Picker', 'Description': "A Simple Django site I created that utilizes Yelp's APIs to pick a random restaurant based off certain information provided.", 'Links' : {'Link': '/foodpicker'}}
	elif proj == 'ilios':
		content = {'Name': 'Ilios Project', 'Description': "The Ilios Curriculum Visualizer was a project I worked on with UCSF Medical Center. It is an interactive graphical representation of important aspects of curricula in the medical and health professions education. This project was implemented using HTML/CSS/JS and D3 Library.", 'Links' : {'Github': 'https://github.com/edmondye502/IliosProject'}}
	elif proj == 'hellrun':
		content = {'Name': 'HellRun', 'Description': "Hell Run was a 2D Platformer I worked on with a team of four. It included multiple levels, different types of AI enemies, save points, and a decent attacking mechanism. This project built using Unity and C#.", 'Links' : {'Github': 'https://github.com/JayhawkForLife/HellRunV3'}}
	elif proj == '5devgame':
		content = {'Name': '5Dev Game', 'Description': "The 5Dev Game was a series of mini-games built by me and a team of 4 others. We entered this game into the 2014 Austism App Jam and ended up winning Most Entrepreneurial Award. This Android App was designed using Java.", 'Links' : {'Github': 'https://github.com/EyeWumbo/5Dev'}}
	else:
		content = {}

	return render(request, 'personal/proj_template.html', content)