#!/usr/bin/env python
# author: Cruz Jean
# a super short demo to show how easy AlphaVantage would be to use

import AlphaVantage as av

content = av.apicall(function='TIME_SERIES_DAILY', symbol='GOOG')
print(repr(content))
