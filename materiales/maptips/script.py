import urllib
import json

@qgsfunction(args="auto", group="Custom")
def wikipediaSummary(name, feature, parent):
	baseurl = 'https://en.wikipedia.org/w/api.php?'
	params={
			'action': 'query',
			'format': 'json',
			'titles': name,
			'prop': 'extracts',
			'exintro': True,
			'explaintext': True,
			}
	url = baseurl + urllib.parse.urlencode(params)
	response = urllib.request.urlopen(url)  

	if response.getcode() == 404:
		return "No wikipedia entry was found"
	else:
			try:
				sresults = response.read()
				results = json.loads(sresults)
				extract = list(results['query']['pages'].values())[0]['extract']
				return extract
			except Exception:
				return "No wikipedia entry was found"
			
'''
<style>
p {width: 300px;}
</style>
<p>
[% wikipediaSummary(“wikipedia”) %]
</p>
'''
