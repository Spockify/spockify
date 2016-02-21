from quickstart import *
from msg import *


#~~~PUT MESSAGE ID BELOW~~~
print GetMessage(build_service(get_credentials()), "me", "<message_id>")
