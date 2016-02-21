from quickstart import *
from msg import *
import json
import sys
from watson_developer_cloud import ToneAnalyzerV3Beta as ToneAnalyzer
import ast


#~~~PUT MESSAGE ID BELOW~~~

messages = ListMessagesMatchingQuery(build_service(get_credentials()), "me", query='from:pat.lempert@gmail.com')

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
    i+=1

#print convos



tone_analyzer = ToneAnalyzer(username='8793fc64-61e7-4fb0-b96c-df3c1a8a15f6',
                             password='Se0SQXprC9E3',
                             version='2016-02-11')

analyzed_text = []

for c in convos:
    analyzed_text.append(json.dumps(tone_analyzer.tone(text=c), indent=2))

tones = {}

tones["emotion"]=ast.literal_eval(analyzed_text[0])["document_tone"]["tone_categories"][0]["tones"]

tones["language"]=ast.literal_eval(analyzed_text[0])["document_tone"]["tone_categories"][1]["tones"]

tones["social"]=ast.literal_eval(analyzed_text[0])["document_tone"]["tone_categories"][2]["tones"]

values = []
scores = []

for el in tones["emotion"]:
    values.append(el["tone_name"])
for el in tones["language"]:
    values.append(el["tone_name"])
for el in tones["social"]:
    values.append(el["tone_name"])

print values


for el in tones["emotion"]:
    scores.append(el["score"])
for el in tones["language"]:
    scores.append(el["score"])
for el in tones["social"]:
    scores.append(el["score"])
print scores

#print values
#print scores

# print
# print str(analyzed_text[0]["document_tone"]["tone_categories"][1]["tones"])
# print
# print str(analyzed_text[0]["document_tone"]["tone_categories"][2]["tones"])

########################################################################
# Drafts = ListDrafts(build_service(get_credentials()), "me")          #
#                                                                      #
# i = 0                                                                #
# while i<len(drafts):                                                 #
#     draft_id = drafts[i]["message"]["threadId"]                      #
#     print GetDraft(build_service(get_credentials()), "me", draft_id) #
#     i+=1                                                             #
########################################################################

