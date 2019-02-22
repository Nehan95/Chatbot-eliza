# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 08:10:24 2019

@author: nagar
"""


# The program is a chat bot named eliza which responds using word spotting
# word spotting using regular expressions
# User input is required whenever the output screen says 'You:'
#intially eliza will greet using current time from system and then ask for user name
#once user enters name, the input is checked for matching regex; for a correct match , name of user is extracted from user input
#then Eliza will ask next question and user has to answer the question, and the input is checked for matching regex 
# for every correct match the regex is substituted by a set of responses
#The loop will continue until the user says quit
#d a functionality is added where eliza responds after 2 seconds delay to make it look like eliza is typing and then responding
#Example conversation is given below
##############################################################

#Please enter/type- quit if you wish to exit the conversation.
#Eliza -> Hi there! Good Evening 
# I am Eliza, your psychotherapist
# What is your name?
#You: My name is neha
#Eliza -> Hi neha!

#Eliza -> How can i help you today?
#You: I want to dance
#Eliza -> Neha, What do you like about dancing? 

#You: quit
#Eliza -> Thank you for talking to me!!
#         Goodbye

##################################################################

import re
import datetime
import random
import time

#List of questions to be chosen : We are spotting words (in last loop ) like - I, you, because,to, to go to, feeling, craving, what, not?, and world that end with e such as rule,crave,dance, etc.
list_responses=[r"Why do you want to \2 \4?",r"what if you dont get to \2 \4?",r"What do you like about \3ing \4?"]
list_responsest=[r"Why do you want to \2 \3?",r"what if you dont get to \2 \3?"]
list_responses1=[r"Why do you want to go to \2?",r"what if you dont get to go to \2?",r"what do you like about \2?"]  
list_responses2=[r"And how long have you been feeling \4",r"Of what does feeling \4 remind you?",r"Why do you think you are feeling \4 ?",r"When do you feel \4?",r"How often do you feel \4?"]
list_responses3=[r"I dont understand. Can you please rephrase?",r"Oh I see. Please tell me more... ",r"I understand. And do you feel that often?",r"Could you elaborate on that?"]
list_responses4=[r"What other reasons there might be?",r"Is it the only reason?",r"Are there any other reasons?"]
list_responses5=[r"Are you sure?",r"You seem quite sure",r"okay,but can you please elaborate?"]
list_responses6=[r"Why do you say that?",r"Perhaps you can answer your own question",r"Why dont you tell me?"]

print("Please enter/type- quit if you wish to exit the conversation.")
# Next part of the program includes greeting and name extraction
#This loop contains regular expressions to check name strings entered by user:- words spotting done for - I am, my name is, this is, I'm
m_flag=0
while (m_flag != 1):
    if m_flag==1:
        break
    flag1=0
    m=0
    while (flag1 !=1):
        if flag1==1:
            break
        if m !=1:
            currentTime = datetime.datetime.now()   
            if currentTime.hour < 12 :
                msg = input("Eliza -> Good Morning.\nI am Eliza, your psychotherapist\n What is your name?\nYou: ")
            elif 12 <= currentTime.hour < 18:
                msg = input("Eliza -> Good Afternoon.\nI am Eliza, your psychotherapist\n What is your name?\nYou: ")
            else :
                msg = input("Eliza -> Hi there! Good Evening \n I am Eliza, your psychotherapist\n What is your name?\nYou: ")
        if re.match(r"quit",msg,flags=re.IGNORECASE):
            m_flag=1
            break
        if re.match("(.*)?\s?((i am)|(my name is)) (.*)",msg,flags=re.IGNORECASE):
            y1=re.sub(r"(.*)?\s?((i am)|(my name is)) (.*)",r"Eliza -> Hi \5!", msg,flags=re.IGNORECASE)
            print(y1)
            #sleep function which delays eliza's reply by 2 seconds
            time.sleep(2)
            found = re.match(r"Eliza -> Hi (.*)!", y1,flags=re.IGNORECASE)
            name = found.group(1)
            msg1=input("Eliza -> How can i help you today?\nYou: ")
            if re.match(r"quit",msg1,flags=re.IGNORECASE):
                m_flag=1
                break 
            flag1=1
        elif re.match("(hi+ )?(this is )(.*)",msg,flags=re.IGNORECASE):
            y1=re.sub(r"(hi+ )?(this is )(.*)",r"Eliza -> Hi \3!", msg,flags=re.IGNORECASE)
            print(y1)
            time.sleep(2)
            found = re.match(r"Eliza -> Hi (.*)!", y1,flags=re.IGNORECASE)
            name = found.group(1)
            msg1=input("Eliza -> How can i help you today?\nYou: ")
            if re.match(r"quit",msg1,flags=re.IGNORECASE):
                m_flag=1
                break 
            flag1=1
        elif re.match("(.*)?\s?(I'm) (.*)",msg,flags=re.IGNORECASE):
            y1=re.sub(r"(.*)?\s?(I'm) (.*)",r"Eliza -> Hi \2!", msg,flags=re.IGNORECASE)
            print(y1)
            time.sleep(2)
            found = re.match(r"Eliza -> Hi (.*)!", y1,flags=re.IGNORECASE)
            name = found.group(1)
            msg1=input("Eliza -> How can i help you today?\nYou: ")
            if re.match(r"quit",msg1,flags=re.IGNORECASE):
                m_flag=1
                break 
            flag1=1
        elif re.match(r"(\b[a-zA-Z]*\b)(.*)?",msg,flags=re.IGNORECASE):
            y1=re.sub(r"(\b[a-zA-Z]*\b)(.*)?",r"Eliza -> Hello! \1", msg,flags=re.IGNORECASE)
            print(y1)
            time.sleep(2)
            found = re.match(r"Eliza -> Hello! (.*)", y1,flags=re.IGNORECASE)
            name = found.group(1)
            msg1=input("Eliza -> How can i help you today?\nYou: ")
            if re.match(r"quit",msg1,flags=re.IGNORECASE):
                m_flag=1
                break  
            flag1=1
        else:
            if re.match(r"\s?",msg,flags=re.IGNORECASE):
                time.sleep(2)
                msg=input("Eliza -> Please enter your name: ")
                m=1
                if re.match(r"quit",msg,flags=re.IGNORECASE):
                    m_flag=1
                    break 
                continue
        msg=msg1
    if m_flag==1:
        break
    flag2=0
    # Next part of the program includes responses for user input
    #This loop contains regular expressions to check the input strings entered by user
    #please enter quit if user wishes to exit the conversation
    while flag2 != 1:
        y2=""
        if re.match(r"(.*)? ?(\bi\b)\s(.* (\bi\b)\s)?(\b([a-z]*)e\b) ?(.*)",msg1,flags=re.IGNORECASE):
            time.sleep(2)
            y2=re.sub(r"(.*)? ?(\bi\b)\s(.* (\bi\b)\s)?(\b([a-z]*)e\b) ?(.*)",r"Eliza ->"+r" "+name.capitalize()+r", "+"Tell me more about \6ing...", msg1,flags=re.IGNORECASE)
        elif re.match(r"(.*) \bto\b\s(\b([a-z]*)e\b)\s?(.*)?",msg1,flags=re.IGNORECASE):
            time.sleep(2)
            y2=re.sub(r"(.*) \bto\b\s(\b([a-z]*)e\b)\s?(.*)?",r"Eliza ->"+r" "+name.capitalize()+r", "+random.choice(list_responses), msg1,flags=re.IGNORECASE)
        elif re.match(r"(.*) \bto\b\s(\b[a-z]*\b)\s?(.*)?",msg1,flags=re.IGNORECASE):
            time.sleep(2)
            y2=re.sub(r"(.*) \bto\b\s(\b[a-z]*\b)\s?(.*)?",r"Eliza ->"+r" "+name.capitalize()+r", "+random.choice(list_responsest), msg1,flags=re.IGNORECASE)
        elif re.match("(.*) \bto go to\b (.*)",msg1,flags=re.IGNORECASE):
            time.sleep(2)
            y2=re.sub(r"(.*) \bto go to\b (.*)",r"Eliza ->"+r" "+name.capitalize()+r", "+random.choice(list_responses1), msg1,flags=re.IGNORECASE)  
        elif re.match(r"(.*)?\s?\b(feel(ing)?\b\s(.*))",msg1,flags=re.IGNORECASE):
            time.sleep(2)
            y2= re.sub(r"(.*)?\s?\b(feel(ing)?\b\s(.*))",r"Eliza ->"+r" "+name.capitalize()+r", "+random.choice(list_responses2),msg1,flags=re.IGNORECASE)      
        elif re.match(r"(.*) what (.*)?",msg1,flags=re.IGNORECASE):
            time.sleep(2)
            y2= re.sub(r"(.*) what (.*)?",r"Eliza -> What do you think?",msg1,flags=re.IGNORECASE)
        elif re.match(r"(.*)?I (\b[a-zA-Z]*\b) you\s?(.*)?",msg1,flags=re.IGNORECASE):
            time.sleep(2)
            y2= re.sub(r"(.*)?I (\b[a-zA-Z]*\b) you\s?(.*)?",r"Eliza -> Perhaps in your fantasy we \2 each other",msg1,flags=re.IGNORECASE)
        elif re.match(r"(.*)?\s?you\s?(.*)?",msg1,flags=re.IGNORECASE):
            time.sleep(2)
            y2= re.sub(r"(.*)?\s?you\s?(.*)?",r"Eliza ->"+r" "+name.capitalize()+r", "+r"You're not really talking about me - are you?",msg1,flags=re.IGNORECASE)
        elif re.match(r"(.*)? ?(\bi\b)\s(.* (\bi\b)\s)?(\b[a-z]*\b) (.*)",msg1,flags=re.IGNORECASE):
            time.sleep(2)
            y2=re.sub(r"(.*)? ?(\bi\b)\s(.* (\bi\b)\s)?(\b[a-z]*\b) (.*)",r"Eliza -> Tell me more...", msg1,flags=re.IGNORECASE)
        elif re.match(r"(.*)? ?(not?) ?(.*)?",msg1,flags=re.IGNORECASE):
            time.sleep(2)
            y2= re.sub(r"(.*)? ?(not?) ?(.*)?",r"Eliza -> Why \2?",msg1,flags=re.IGNORECASE)
        elif re.match(r"(.*)? ?because (.*)?",msg1,flags=re.IGNORECASE):
            time.sleep(2)
            y2= re.sub(r"(.*)? ?because (.*)?",r"Eliza ->"+r" "+random.choice(list_responses4),msg1,flags=re.IGNORECASE)
        elif re.match(r"yes",msg1,flags=re.IGNORECASE):
            time.sleep(2)
            y2= re.sub(r"yes",r"Eliza ->"+r" "+random.choice(list_responses5),msg1,flags=re.IGNORECASE)
        elif re.match(r".*\?",msg1,flags=re.IGNORECASE):
            time.sleep(2)
            y2=re.sub(r".*\?",r"Eliza ->"+r" "+random.choice(list_responses6),msg1,flags=re.IGNORECASE)
        elif re.match(r"(.*)",msg1,flags=re.IGNORECASE):
            time.sleep(2)
            y2=re.sub(r"(.*)",r"Eliza ->"+r" "+random.choice(list_responses3),msg1,flags=re.IGNORECASE)
        if y2==y1 or y2=="" or msg1=="" or y2==msg1:
            time.sleep(2)    
            y3=re.sub(r".*",random.choice(list_responses3),y2,flags=re.IGNORECASE)
            msg2=input("You: ")
            if re.match(r"quit",msg2,flags=re.IGNORECASE):
                    flag2=1
                    m_flag=1
                    break
            msg1=msg2
            continue
        else:
            print(y2)
            msg2=input("You: ")
            if re.match(r"quit",msg2,flags=re.IGNORECASE):
                flag2=1
                m_flag=1
                break
            msg1=msg2
            continue
    if m_flag==1:
        break
time.sleep(2)
print("Eliza -> Thank you for talking to me!!")
print("         Goodbye")


