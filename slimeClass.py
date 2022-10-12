import os
import pygame

class slime:

	empCount = 0
	slimesList = []
	#location is tuple and x and y are velocity
	def __init__(self, defaultImage, name, location, x, y):
		self.veloctiy = (x,y)

		if type(name) is str:
			self.name = name
		else:
			print("first attribute name must be a str")
		if type(location) is tuple:
			self.location = location
		else:
			print("second attribute color must be a str")
		slime.empCount += 1
		slime.slimesList.append(self)
		
		#list of string elements that refer to the image file
		self.animation = [defaultImage]
		self.slimeSurface = pygame.image.load(self.animation[0])
		self.rectangle = self.slimeSurface.get_rect(center = location)

	def displayCount(self):
		print ("Total number of slimes %d" % slime.empCount)

	def displaySlime(self):
		print ("Name : ", self.name,  ", Color: ", self.color)

	def reset_animation(self, string):
		self.animation = []

	def set_animation(self, folder):
		 # folder is the string of directory folder of animations (with the correctly ordered names)
		if type(folder) is str:
			for item in sorted(os.listdir("./" + folder)):
				self.animation.append("animation/" + item)
