from EmailM import *
import json
from FilterM import *
import urllib.request

class SmartVacationResponder:
	__Filters = []
	__GeneralResponse = ""
	__FileName = "filters.txt"

	def clearFilters(self):
		self.__Filters[:] = []
	
	#Deprecated	
	def addFilter(self, filter):
		self.__Filters.append(filter)		

	def getResponse(self, email):
		for filter in self.__Filters:
			if filter.match(email) != 0:
				return filter.getRespondText()
		return self.__GeneralResponse

	def setGeneralResponse(self, text):
		self.__GeneralResponse = text

	def getGeneralResponse(self):
		return self.__GeneralResponse

	def addFilters(self):
		link = "http://lxzworks.com/SVR/" + self.__FileName
		urllib.request.urlretrieve(link, self.__FileName)

		self.clearFilters()
		filtersInfo = []
		f = open(self.__FileName, "r")
		for line in f:
			filtersInfo.append(line)

		for finfo in filtersInfo:
			finfo = json.loads(finfo)
			newFilter = Filter()

			newFilter.setFromDomain(finfo["from"])
			newFilter.setToEmail(finfo["to"])
			newFilter.setSubject(finfo["subject"])
			newFilter.setHasWords(finfo["hasw"])
			newFilter.setHasNotWords(finfo["hasnotw"])
			newFilter.setRespondText(finfo["rsptext"])

			newFilter.printFilster()
			self.__Filters.append(newFilter)
