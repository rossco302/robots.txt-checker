def robots_reader(url, robots_url):
	import urllib.robotparser

	rp = urllib.robotparser.RobotFileParser()
	rp.set_url(robots_url)
	rp.read()
	
	return print(rp.can_fetch('*', url))

robots_reader('https://docs.python.org/3/library/urllib.robotparser.html', 'https://docs.python.org/robots.txt')

