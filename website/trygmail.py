from quickstart import *
from msg import *


#~~~PUT MESSAGE ID BELOW~~~
#print GetMessage(build_service(get_credentials()), "me", "15301ccbcfd9c8be")

print ListMessagesMatchingQuery(build_service(get_credentials()), "me", query='jgpeconomopolis@gmail.com')
