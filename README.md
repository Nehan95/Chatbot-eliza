# Chatbot-eliza

The program is a chat bot named eliza which responds using word spotting
eliza does word spotting using regular expressions.
It is robust.
It will continue until the user says 'quit'.
just run the file 'eliza.py' anf eliza will start chatting
User input is required whenever the output screen says 'You:'
intially eliza will greet using current time from system and then ask for user name.
once user enters name, the input is checked for matching regex; for a correct match , name of user is extracted from user input.
then Eliza will ask next question and user has to answer the question, and the input is checked for matching regex. 
for every correct match the regex is substituted by a set of responses.
A functionality is added where eliza responds after 2 seconds delay to make it look like eliza is typing and then responding.
