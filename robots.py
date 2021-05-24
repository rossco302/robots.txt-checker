def robots_reader(url):
	import urllib.robotparser
	import re
	global robots_url
	
	print()

	if len(re.findall('^https.+?org/', url)) > 0:
		robots_url = re.findall('^https.+?org/', url)
		robs_url = robots_url[0] + 'robots.txt'
	elif len(re.findall('^https.+?com/', url)) > 0:
		robots_url = re.findall('^https.+?com/', url)
		robs_url = robots_url[0] + 'robots.txt'
	elif len(re.findall('^https.+?com', url)) > 0:
		robots_url = re.findall('^https.+?com', url)
		robs_url = robots_url[0]
	else:
		return print('url didnt work, check and try again.')

	print('robots url: ' + robs_url)
	print()

	rp = urllib.robotparser.RobotFileParser()
	rp.set_url(robs_url)
	rp.read()
	
	if rp.can_fetch('*', url) == True:
		can_scrape = 'You can scrape this website'
	elif rp.can_fetch('*', url) == False:
		can_scrape = 'You cannot scrape this website'
	
	return print(can_scrape+'\n')

robots_reader('https://www.upwork.com')