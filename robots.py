def robots_reader(url):
	import urllib.robotparser
	import re

	robots_url = re.findall('^https.+?org', url)
	robots_url = robots_url[0]

	rp = urllib.robotparser.RobotFileParser()
	rp.set_url(robots_url)
	rp.read()
	
	return print(rp.can_fetch('*', url))

robots_reader('https://docs.python.org/3/library/urllib.robotparser.html')