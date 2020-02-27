#!/usr/bin/env python
# author: Cruz Jean
# common utility submodule for all AlphaVantage interactions used in this project

import urllib.request, urllib.parse
import json

apikey = '0J7H5BAGZRLZHBYP'

def apicall(**args):
	'''
	forwards all keyword args to alphavantage and returns the result (py object).
	if an apikey is not specified, uses a (valid) default.
	'''
	if 'apikey' not in args:
		args['apikey'] = apikey
	url = f'http://www.alphavantage.co/query?{urllib.parse.urlencode(args)}'
	with urllib.request.urlopen(url) as response:
		return json.loads(response.read().decode('utf-8'))
