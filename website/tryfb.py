import urllib2, time, json

def fb_messages():
    #~~~PUT EXTENDED ACCESS TOKEN BELOW~~~
    url="https://graph.facebook.com/v2.3/me/inbox?access_token=<extended_access_token"
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)
    return r

print fb_messages();
