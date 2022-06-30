# #practice with inheritance
# class Rectangle:
# 	def __init__(self, length, width):
# 		self.length = length
# 		self.width = width
# 	def area(self):
# 		return self.length * self.width
# 	def perimeter(self):
# 		return self.length*2 + self.width*2

# class Square(Rectangle):
# 	def __init__(self,length):
# 		self.length = length
# 		self.width = length

# class Cube(Square):
# 	def __init__(self,length):
# 		self.length = self.height = self.width = length
# 	def volume(self):
# 		face_area = self.area()
# 		return face_area * self.height

# mycube = Cube(6)
# print(mycube.volume())

# class Bat:
# 	def __init__(self,length,hit_power):
# 		self.length = length
# 		self.hit_power = hit_power
# class WoodenBat(Bat):
# 	def __init__(self,length,hit_power,wood_type):
# 		super().__init__(length,hit_power)
# 		self.wood_type = wood_type

# mywoodenbat = WoodenBat(9,"high","cherry wood")
		

# class FirstClass():
# 	__someattr = "hello"
# 	def __init__(self):
# 		self.__somevar = 0
# 		self.firstvar = 1
# 		self.secondvar = 2
# 		self.thirdvar = 3
# 		self.fourthvar = 4
# 		self.fifthvar = 5
# 	def __str__(self):
# 		return "Hello! My number is " + str(self.fifthvar) + "!"
# 	def add(self):
# 		return self.firstvar + self.secondvar + self.thirdvar
# 	def multiply(self):
# 		return self.secondvar * self.fifthvar

# class SecondClass(FirstClass):
# 	def __init__(self,sixthvar,seventhvar):
# 		super().__init__()
# 		self.sixthvar = sixthvar
# 		self.seventhvar = seventhvar


# class ExampleClass:
#     __counter = 0
#     def __init__(self, val = 1):
#         self.__first = val
#         ExampleClass.__counter += 1

#  #class variables do not show up in an object's __dict__ attribute
# newobj = SecondClass(6,7)
# print(newobj)

# class MyCustomError(Exception):
# 	def __init__(self,message):
# 		super().__init__(message)

# def divider(numer,denom):
# 	try:
# 		numer/denom
# 	except ZeroDivisionError:
# 		raise MyCustomError(str(numer) + " can't be divided by zero bro!")
# 	else:
# 		return numer/denom

# try:
# 	divider(4,0)
# except MyCustomError as mycust:
# 	print(mycust)


# class somerange:
# 	def __init__(self,numer,denom,numiters):
# 		self.numiters = numiters
# 		self.startval = numer/denom
# 		self.adder = numer/denom
# 		self.count = 0
# 	def __iter__(self):
# 		return self
# 	def __next__(self):
# 		self.count += 1
# 		if self.count <= self.numiters:
# 			if self.count == 1:
# 				return self.startval
# 			else:
# 				self.startval += self.adder
# 				return self.startval
# 		else:
# 			raise StopIteration

# print(list(somerange(1,2,10)))

# class GreaterZeroError(Exception):
# 	def __init__(self,message):
# 		super().__init__(message)

# def customize(number):
# 	if number > 0:
# 		raise GreaterZeroError("Sorry! Your number is greater than zero. Try another number.")
# 	else:
# 		print("Your number is ", str(number) + "!")

# try:
# 	customize(1)
# except GreaterZeroError as gze:
# 	print(gze)

# line = "this is some string"
# line.split(" ")

# newvar = line.split(" ")
# print(newvar)

# somelist = [i/2 for i in range(1,11)]
# for i in somelist:
# 	if i%2 == 0:
# 		i += 100
# 		print("manipulated")

# someotherlist = [4 if i%2 == 0 else 0 for i in range(1,11)]
# for i in someotherlist:
# 	if i == 4:
# 		i += 1
# print(someotherlist)

# class MyClass:
# 	def __init__(self,num1,num2):
# 		self.num1 = num1
# 		self.num2 = num2
# 	def addnums(self):
# 		return self.num1 + self.num2

# example = MyClass(1,2)
# print(example.addnums())

#practice with the calendar function
# import calendar
# calendar.setfirstweekday(calendar.WEDNESDAY)
# print(calendar.month(2022, 10))
# print(calendar.weekheader(2))
# print(calendar.isleap(2022))








