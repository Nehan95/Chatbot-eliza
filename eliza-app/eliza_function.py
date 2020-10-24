import re
import datetime
import random


#List of questions to be chosen : We are spotting words (in last loop ) like - I, you, because,to, to go to, feeling, craving, what, not?, and world that end with e such as rule,crave,dance, etc.
list_responses=[r"Why do you want to \2 \4?",r"what if you dont get to \2 \4?",r"What do you like about \3ing \4?"]
list_responsest=[r"Why do you want to \2 \3?",r"what if you dont get to \2 \3?"]
list_responses1=[r"Why do you want to go to \2?",r"what if you dont get to go to \2?",r"what do you like about \2?"]  
list_responses2=[r"And how long have you been feeling \4",r"Of what does feeling \4 remind you?",r"Why do you think you are feeling \4 ?",r"When do you feel \4?",r"How often do you feel \4?"]
list_responses3=[r"I dont understand. Can you please rephrase?",r"Oh I see. Please tell me more... ",r"I understand. And do you feel that often?",r"Could you elaborate on that?"]
list_responses4=[r"What other reasons there might be?",r"Is it the only reason?",r"Are there any other reasons?"]
list_responses5=[r"Are you sure?",r"You seem quite sure",r"okay,but can you please elaborate?"]
list_responses6=[r"Why do you say that?",r"Perhaps you can answer your own question",r"Why dont you tell me?"]


def greet():
    currentTime = datetime.datetime.now()   
    if currentTime.hour < 12 :
        msg = ("Good Morning. I am Eliza, your psychotherapist. What is your name?")
    elif 12 <= currentTime.hour < 18:
        msg = ("Good Afternoon. I am Eliza, your psychotherapist. What is your name? ")
    else :
        msg = ("Hi there! Good Evening. I am Eliza, your psychotherapist. What is your name?")
    return msg

def username(msg):
    if re.match("(.*)?\s?((i am)|(my name is)) (.*)",msg,flags=re.IGNORECASE):
        y2=re.sub(r"(.*)?\s?((i am)|(my name is)) (.*)",r"Hi \5! How can I help you today?", msg,flags=re.IGNORECASE)
    elif re.match("(hi+ )?(this is )(.*)",msg,flags=re.IGNORECASE):
        y2=re.sub(r"(hi+ )?(this is )(.*)",r" Hi \3! How can I help you today?", msg,flags=re.IGNORECASE)
    elif re.match("(.*)?\s?(I'm) (.*)",msg,flags=re.IGNORECASE):
        y2=re.sub(r"(.*)?\s?(I'm) (.*)",r"Hi \2! How can I help you today?", msg,flags=re.IGNORECASE)
    elif re.match(r"(\b[a-zA-Z]*\b)(.*)?",msg,flags=re.IGNORECASE):
        y2=re.sub(r"(\b[a-zA-Z]*\b)(.*)?",r"Hi \1! How can I help you today?", msg,flags=re.IGNORECASE)
    else:
        y2=re.sub(r"(.*)",r"Hi \1! How can I help you today?", msg,flags=re.IGNORECASE)
    return y2


def bot(msg):
    if re.match(r"(.*)? ?(\bi\b)\s(.* (\bi\b)\s)?(\b([a-z]*)e\b) ?(.*)",msg,flags=re.IGNORECASE):
        y2=re.sub(r"(.*)? ?(\bi\b)\s(.* (\bi\b)\s)?(\b([a-z]*)e\b) ?(.*)","Tell me more about \6ing...", msg,flags=re.IGNORECASE)
    elif re.match(r"(.*) \bto\b\s(\b([a-z]*)e\b)\s?(.*)?",msg,flags=re.IGNORECASE):
        y2=re.sub(r"(.*) \bto\b\s(\b([a-z]*)e\b)\s?(.*)?",random.choice(list_responses), msg,flags=re.IGNORECASE)
    elif re.match(r"(.*) \bto\b\s(\b[a-z]*\b)\s?(.*)?",msg,flags=re.IGNORECASE):
        y2=re.sub(r"(.*) \bto\b\s(\b[a-z]*\b)\s?(.*)?",random.choice(list_responsest), msg,flags=re.IGNORECASE)
    elif re.match("(.*) \bto go to\b (.*)",msg,flags=re.IGNORECASE):
        y2=re.sub(r"(.*) \bto go to\b (.*)",random.choice(list_responses1), msg,flags=re.IGNORECASE)  
    elif re.match(r"(.*)?\s?\b(feel(ing)?\b\s(.*))",msg,flags=re.IGNORECASE):
        y2= re.sub(r"(.*)?\s?\b(feel(ing)?\b\s(.*))",random.choice(list_responses2),msg,flags=re.IGNORECASE)      
    elif re.match(r"(.*) what (.*)?",msg,flags=re.IGNORECASE):            
        y2= re.sub(r"(.*) what (.*)?",r"What do you think?",msg,flags=re.IGNORECASE)
    elif re.match(r"(.*)?I (\b[a-zA-Z]*\b) you\s?(.*)?",msg,flags=re.IGNORECASE):
        y2= re.sub(r"(.*)?I (\b[a-zA-Z]*\b) you\s?(.*)?",r"Perhaps in your fantasy we \2 each other",msg,flags=re.IGNORECASE)
    elif re.match(r"(.*)?\s?you\s?(.*)?",msg,flags=re.IGNORECASE):
        y2= re.sub(r"(.*)?\s?you\s?(.*)?",r"You're not really talking about me - are you?",msg,flags=re.IGNORECASE)
    elif re.match(r"(.*)? ?(\bi\b)\s(.* (\bi\b)\s)?(\b[a-z]*\b) (.*)",msg,flags=re.IGNORECASE):
        y2=re.sub(r"(.*)? ?(\bi\b)\s(.* (\bi\b)\s)?(\b[a-z]*\b) (.*)",r"Tell me more...", msg,flags=re.IGNORECASE)
    elif re.match(r"(.*)? ?(not?) ?(.*)?",msg,flags=re.IGNORECASE):
        y2= re.sub(r"(.*)? ?(not?) ?(.*)?",r"Why \2?",msg,flags=re.IGNORECASE)
    elif re.match(r"(.*)? ?because (.*)?",msg,flags=re.IGNORECASE):
        y2= re.sub(r"(.*)? ?because (.*)?",random.choice(list_responses4),msg,flags=re.IGNORECASE)
    elif re.match(r"yes",msg,flags=re.IGNORECASE):
        y2= re.sub(r"yes",random.choice(list_responses5),msg,flags=re.IGNORECASE)
    elif re.match(r".*\?",msg,flags=re.IGNORECASE):
        y2=re.sub(r".*\?",random.choice(list_responses6),msg,flags=re.IGNORECASE)
    elif re.match(r"(.*)",msg,flags=re.IGNORECASE):
        y2=re.sub(r"(.*)",random.choice(list_responses3),msg,flags=re.IGNORECASE)
    return y2

            