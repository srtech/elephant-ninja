from EmailM import *
from FilterM import *
from SmartVacationResponderM import *
import json
import urllib.request

myResponder = SmartVacationResponder()
myResponder.setGeneralResponse("I'm on a vacation!\n(This is a general response.)");

myResponder.addFilters()
