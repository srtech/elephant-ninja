from EmailM import *
from FilterM import *
from SmartVacationResponderM import *
import json

#This is our smart responder!
myResponder = SmartVacationResponder()
myResponder.setGeneralResponse("I'm on a vacation!\n(This is a general response.)");



#Use Case 1---------------Response to a classmate----------------------
#Construct a new filter. Information comes from the web UI.
myFilter1 = Filter()
myFilter1.setRespondText("Hi!\nI'm on a vacation!\nPlease contact Shashank!\n----Am I smart?")
myFilter1.setFromDomain("gatech.edu")
myFilter1.setHasWords("homework")
#Add this rule to the smart responder
myResponder.addFilter(myFilter1)

#Construct an email. Information comes from gmail server.
myEmail1 = Email()
myEmail1.setFrom("usecase1@gatech.edu")
myEmail1.setTo("socialcomputing@gmail.com")
myEmail1.setSubject("reminder")
myEmail1.setContents("Hi, how are you?\nThis is a kind reminder that your homework is due tomorrow.")
myEmail1.setDate("12/09/2013")

#Pass the email into the function. It will return a string based on the existing filters.
response = myResponder.getResponse(myEmail1)
print("\nUseCase1==================\nSmartResponder will respond the following message:\n" + response)
#---------------End of Use Case 1---------------------





#Use Case 2---------------Response to a family member----------------------
#Construct a new filter. Information comes from the web UI.
myFilter2 = Filter()
myFilter2.setRespondText("Hi!\nI'm on a vacation!\nPlease call me at 000-000-1234\n----Am I smart?")
myFilter2.setHasWords("mom;dad;Nancy;")
#Add this rule to the smart responder
myResponder.addFilter(myFilter2)

#Construct an email. Information comes from gmail server.
myEmail2 = Email()
myEmail2.setFrom("usecase2@gmail.com")
myEmail2.setTo("socialcomputing@gmail.com")
myEmail2.setSubject("Hello from mom")
myEmail2.setContents("Hi, how are you?\nI miss you.\n----Your mom")
myEmail2.setDate("12/09/2013")

#Pass the email into the function. It will return a string based on the existing filters.
response = myResponder.getResponse(myEmail2)
print("\nUseCase2==================\nSmartResponder will respond the following message:\n" + response)
#---------------End of Use Case 2---------------------





#Use Case 3---------------Regular sender. No filter is found.----------------------
#Construct an email. Information comes from gmail server.
myEmail3 = Email()
myEmail3.setFrom("usecase3@gmail.com")
myEmail3.setTo("socialcomputing@gmail.com")
myEmail3.setSubject("Package Notice")
myEmail3.setContents("Hi, how are you?\nYou have a package.")
myEmail3.setDate("12/09/2013")

#Pass the email into the function. It will return a string based on the existing filters.
response = myResponder.getResponse(myEmail3)
print("\nUseCase3==================\nSmartResponder will respond the following message:\n" + response)
#---------------End of Use Case 3---------------------



myResponder.clearFilters()
