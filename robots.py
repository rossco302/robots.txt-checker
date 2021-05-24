def robots_reader(url):
	import urllib.robotparser
	import re

	robots_url = re.findall('^https.+?org/', url)
	if len(robots_url) > 0:
		robots_url = robots_url[0] + 'robots.txt'
	robots_url = re.findall('^https.+?com/', url)
	if len(robots_url) > 0:
		robots_url = robots_url[0] + 'robots.txt'

	print(robots_url)

	rp = urllib.robotparser.RobotFileParser()
	rp.set_url(robots_url)
	rp.read()
	
	return print(rp.can_fetch('*', url))

robots_reader(input('check url: '))