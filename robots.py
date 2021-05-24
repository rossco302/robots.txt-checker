def robots_reader(url):
	import urllib.robotparser
	import re

	print()

	if len(re.findall('^https.+?org/', url)) > 0:
		robots_url = robots_url[0] + 'robots.txt'
	elif len(re.findall('^https.+?com/', url)) > 0:
		robots_url = robots_url[0] + 'robots.txt'


	print('robots url: ' + robots_url)
	print()

	rp = urllib.robotparser.RobotFileParser()
	rp.set_url(robots_url)
	rp.read()
	
	if rp.can_fetch('*', url) == True:
		can_scrape = 'You can scrape this website'
	elif rp.can_fetch('*', url) == False:
		can_scrape = 'You cannot scrape this website'
	return can_scrape

robots_reader(input('check url: '))