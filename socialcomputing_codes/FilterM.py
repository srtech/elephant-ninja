class Filter:
	__TextToRespond = ""
	
	__FromDomain = ""
	__ToEmail = ""
	
	__Subject = ""
	__HasWords = []
	__HasNotWords = []

	def printFilster(self):
		print("\n==============Filter info=============:")
		print("From: " + self.__FromDomain)
		print("To: " + self.__ToEmail)
		print("Subject: " + self.__Subject)
		print(self.__HasWords)
		print(self.__HasNotWords)
		print("RspText: " + self.__TextToRespond)

	def match(self, email):
		if self.matchFrom(email.getFrom()):
			print("from matches")
			return 1

		if self.matchTo(email.getTo()):
			print("to matches")
			return 2

		if self.matchSubject(email.getSubject()):
			print("subject matches")
			return 3

		if self.hasWords(email.getContents()):
			print("hasw matches")
			return 4

		if self.hasNotWords(email.getContents()):
			print("hasnw matches")
			return 5

		return 0

	def hasWords(self, c):
		for word in self.__HasWords:
			if c.find(word) != -1:
				return True
		return False

	def hasNotWords(self, c):
		if not self.__HasNotWords:
			return False
		for word in self.__HasNotWords:
			if c.find(word) != -1:
				return False
		return True

	def matchSubject(self, s):
		if s == self.__Subject:
			return True
		return False

	def matchFrom(self, f):		
		if f.split("@")[1] == self.__FromDomain:
			return True
		return False

	def matchTo(self, t):
		if t == self.__ToEmail:
			return True
		return False

	#Setters
	def setRespondText(self, textToRespond):
		self.__TextToRespond = textToRespond

	def setFromDomain(self, domain):
		self.__FromDomain = domain

	def setToEmail(self, email):
		self.__ToEmail = email		

	def setSubject(self, subject):
		self.__Subject = subject

	def setHasWords(self, words):
		words = words.strip(";")
		self.__HasWords = words.split(";")

	def setHasNotWords(self, words):	
		words = words.strip(";")
		self.__HasNotWords = words.split(";")

	#Getters
	def getRespondText(self):
		return self.__TextToRespond

	def getFromDomain(self):
		return self.__FromDomain

	def getToEmail(self):
		return self.__ToEmail

	def getSubject(self):
		return self.__Subject

	def getHasWords(self):
		return self.__HasWords

	def getHasNotwords(self):
		return self.__HasNotWords