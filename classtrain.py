#class 

class ClassName():

	member = 0

	def memberAdd(self, a) :
			self.member = self.member + a

	def memberPrint(self) :
		print(self.member)

# class use

clazz = ClassName()

clazz.memberAdd(5)
clazz.memberAdd(5)
clazz.memberAdd(5)

clazz.memberPrint()


