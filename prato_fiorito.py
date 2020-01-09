import random
import math

class Game:
	
	def __init__(self,height,width,bombs):
		self.height = height
		self.width = width
		self.bombs = bombs


	def create_grid(self):
		self.grid = []
		for i in range(self.height):
			self.grid.append([0 for j in range(self.width)]) 


	def add_bomb(self):
		colonna_scelta = random.randint(0,self.width-1)
		riga_scelta = random.randint(0,self.height-1)
		if self.grid[riga_scelta][colonna_scelta] == 'B':
			self.add_bomb()
		else:
			self.grid[riga_scelta][colonna_scelta] = 'B'
		
		
	def fill_bombs(self):
		for i in range(self.bombs):
			self.add_bomb()

	def check_square(self,line,column):
		num = 0
		for i in [-1,0,1]:
			for j in [-1,0,1]:
				try:
					if line+i >= 0 and column+ j >= 0:
						if self.grid[line+i][column+j] == 'B':
							num += 1
				except:
					pass
		return num

	def complete_grid(self):
		for i in range(self.height):
			for j in range(self.width):
				if self.grid[i][j]!='B':
					self.grid[i][j] = str(self.check_square(i,j))

	def show_grid(self):
		for inner_list in self.grid:
			print(inner_list)
			

game = Game(16,32,99)
game.create_grid()
game.fill_bombs()
game.complete_grid()
game.show_grid()