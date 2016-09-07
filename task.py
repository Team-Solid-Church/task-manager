import datetime

class Task (object):

	def __init__(self):
		self.name = ""
		self.created_date = ""

	def __str__(self):
		return self.name