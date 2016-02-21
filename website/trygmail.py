from quickstart import *
from msg import *


#~~~PUT MESSAGE ID BELOW~~~

messages = ListMessagesMatchingQuery(build_service(get_credentials()), "me", query='jgpeconomopolis@gmail.com')


#print messages[0]

convos = []

i = 0
while (i<len(messages)):
    msg_id = messages[i]["threadId"]
    msg_info = GetMimeMessage(build_service(get_credentials()), "me", msg_id)
    #print msg_info
    #TODO: Find a better way to get the message string, ex: by newlines
    index1 = str(msg_info).index("Content-Type: text/plain; charset=UTF-8")
    index1 += len("Content-Type: text/plain; charset=UTF-8")
    index2 = str(msg_info).index("Content-Type: text/html; charset=UTF-8")
    index2 -= len("--001a113d38862b78c0052be7b244")
    msg_content = str(msg_info)[index1:index2]
    convos.append(msg_content)
    print i
    i+=1

print convos

