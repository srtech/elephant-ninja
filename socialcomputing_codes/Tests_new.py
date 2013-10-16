from EmailM import *
from FilterM import *
from SmartVacationResponderM import *

#This is our smart responder!
myResponder = SmartVacationResponder()
myResponder.setGeneralResponse("I'm on a vacation!\n(This is a general response.)");

myResponder.addFilters()

myEmail1 = Email()
myEmail1.setFrom("xli357@gatech.edu")
myEmail1.setTo("socialcomputing@gmail.com")
myEmail1.setSubject("reminder")
myEmail1.setContents("Hi, how are you?\nThis is a kind reminder that your homework is due tomorrow.")
myEmail1.setDate("12/09/2013")

response = myResponder.getResponse(myEmail1)
print("Message to respond: " + response)