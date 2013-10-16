class Email:
	__From = ""
	__To = ""
	__Subject = ""
	__Contents = ""
	__Date = ""
	__Priority = 2  #Priorities of 1 - 3 where 3 represents the highest priority

	def printEmail(self):
		print("From: " + self.__From)
		print("To: " + self.__To)
		print("Subject: " + self.__Subject)
		print("Contents: " + self.__Contents)
		print("Date: " + self.__Date);

	#Setters
	def setFrom(self, From):
		self.__From = From

	def setTo(self, To):
		self.__To = To

	def setSubject(self, Subject):
		self.__Subject = Subject

	def setDate(self, Date):
		self.__Date = Date

	def setContents(self, Contents):
		self.__Contents = Contents

	#Getters
	def getFrom(self):
		return self.__From

	def getTo(self):
		return self.__To

	def getSubject(self):
		return self.__Subject

	def getContents(self):
		return self.__Contents

	def getDate(self):
		return self.__Date