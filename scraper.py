import requests
import scraperwiki
from pyquery import PyQuery as pq

BASE = 'http://www.isrctn.com'

i = 1
while i > 0:
    url = '%s/search?pageSize=100&q=&page=%s' % (BASE, i)
    req = requests.get(url)
    doc = pq(req.text)
    titles = doc('.ResultsList_item_title a')
    for title in titles:
        num = title.text.split(':')[0].strip()
        scraperwiki.sqlite.save(unique_keys=['id'],
                                data={"id": num})
    print i, len(titles)
    if len(titles):
        i += 1
    else:
        i = 0


# scraperwiki.sql.select("* from data where 'name'='peter'")
