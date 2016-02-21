from quickstart import *
from msg import *


#~~~PUT MESSAGE ID BELOW~~~

messages = ListMessagesMatchingQuery(build_service(get_credentials()), "me", query='jgpeconomopolis@gmail.com')


#print messages[0]

i = 0
#while (i<len(messages)):
while(i<1):
    msg_id = messages[i]["id"]
    msg_info = GetMessage(build_service(get_credentials()), "me", msg_id)
    print msg_info["payload"]["headers"][16]["value"]
    i+=1




