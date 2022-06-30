#create a point class for hypotenuse and distance calculation according to OpenEDG3.4.1.14
import math
class Point:
	def __init__(self,__x = 0.0,__y = 0.0):
		self.__point = (__x,__y)
		for coord in self.__point:
			if type(coord) not in [float, int]:
				print("Cannot accept coordinates provided.")
				break
			else:
				self.__x = self.__point[0]
				self.__y = self.__point[1]
	def get_x(self):
		return self.__x
	def get_y(self):
		return self.__y
	def distance_from_xy(self,x,y):
		point = (x,y)
		for coord in point:
			if type(coord) == float or type(coord) == int:
				return math.sqrt((x - self.__x)**2 + (y - self.__y)**2)
			else:
				return print("Cannot accept coordinates provided.")
				break
	def distance_from_point(self,point):
		return math.sqrt((point.__x - self.__x)**2 + (point.__y - self.__y)**2)

#verify that the class works as intended
if __name__ == "__main__":
	print("Let's run some tests to verify that the methods work correctly:")
	exampleobject = Point(2,6)
	print(exampleobject.distance_from_xy(-2,0))
	print(exampleobject.distance_from_point(Point(-2,0)))

	point = Point(2,5)
	point2 = Point(-2,4)
	print(point.distance_from_xy(-3,3))
	print(point.distance_from_point(point2))




