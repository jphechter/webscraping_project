from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

import main

"""
Frist Website URL format: https://fristartmuseum.org/calendar#S=20181215&E=20191221&P=0
"""

def get_frist_events():
    # TODO: use datetime to create this URL relative to currents
    # just using a URL I know will work for now
    url_root = 'https://fristartmuseum.org/calendar#S=20181215&E=20191221&P=0'
    frist_calendar = main.simple_get(url_root)
    if frist_calendar is not None:
        html = BeautifulSoup(frist_calendar, 'html.parser')
        events = set()
        for div in html.select('div'):
            for event in div.text.split('\n'):
                if len(event) > 0:
                    events.add(event.strip())
        print(events)
        return list(events)
    # Raise an exception if we failed to get any data from the url
    raise Exception('Error retrieving contents at {}'.format(url))
