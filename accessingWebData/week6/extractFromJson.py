import urllib.error, urllib.request, urllib.parse
import json
counts = list()
while True:
    address = input('Enter location')
    if len(address) < 1 : break
    print ('Retrieving', address)
    data= urllib.request.urlopen(address).read()
    
    print ('Retrieved',len(data),'characters')
    try: js = json.loads(data)
    except: js = None
    comments = js['comments']
    for comment in comments:
        counts.append(comment['count'])
    print ('Count', len(comments))
    print ('Sum', sum(counts))

#    http://py4e-data.dr-chuck.net/comments_494586.json