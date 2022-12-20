import random
import pygame
class Player():
	def __init__(self):
		self.cards = []
		self.score = 0
	def countPoints(self):
		count = 0
		for i in self.cards:
			current = i
			if current < 4:
				count += 11
			elif current < 8:
				count += 4
			elif current < 12:
				count += 3
			elif current < 16:
				count += 2
			elif current < 20:
				count += 10
			elif current < 24:
				count += 9
			elif current < 28:
				count += 8
			elif current < 32:
				count += 7
			elif current < 36:
				count += 6
			elif current < 40:
				count += 5
			elif current < 44:
				count += 4
			elif current < 48:
				count += 3
			elif current < 52:
				count += 2
		self.score = count
	def addCardToHand(self,deck):
		self.cards.append(deck.pop())
		self.countPoints()	
	def info(self):
		print(self.cards, " ", self.score)
	def getCards(self):
		return self.cards
	def getScore(self):
		return self.score

class Draw():
	def __init__(self):
		self.images = []
		for i in range(52):
			currentImage = pygame.image.load("cards//"+str(i)+".jpg").convert()
			currentImage = pygame.transform.scale(currentImage,  
												 (int(currentImage.get_size()[0]//2), 
												  int(currentImage.get_size()[1]//2)))

			self.images.append(currentImage)
	def drawCard(self,screen,numbers,x,y):
		count = 0
		for i in numbers:
			screen.blit(self.images[i], (x+count*80, y))
			count += 1

class Button():
	def __init__(self,screen,x,y,w,h,text):
		self.font = pygame.font.SysFont('Arial', 25)
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.screen = screen
		self.text = self.font.render(text, True, (255,0,0))
		self.rect = pygame.draw.rect(self.screen, (0,0,0), (self.x, self.y, self.w, self.h), 2)
		self.screen.blit(self.text,(self.x, self.y))

	def checkClick(self,pos):
		return self.rect.collidepoint(pos)
	def draw(self):
		self.rect = pygame.draw.rect(self.screen, (0,0,0), (self.x, self.y, self.w, self.h), 2)
		self.screen.blit(self.text,(self.x, self.y))
class Score():
	def __init__(self,screen,x,y,text):
		self.x = x
		self.y = y
		self.font = pygame.font.SysFont('Arial', 25)
		self.text = self.font.render(text, True, (255,0,0))  
		self.screen = screen
		self.screen.blit(self.text,(self.x,self.y))
	def update(self,text):
		self.text = self.font.render(text, True, (255,0,0)) 
		self.screen.blit(self.text,(self.x,self.y)) 

class Game():
	def __init__(self,screen):
		self.screen = screen
		self.deck = list(range(52))
		random.shuffle(self.deck)
		self.p1 = Player()
		self.p2 = Player()
		self.buttonCheck = Button(self.screen,25,550,150,40,"Check")
		self.buttonDone = Button(self.screen,180,550,150,40,"Done")
		self.buttonRetry = Button(self.screen,335,550,150,40,"Retry")
		self.Pen = Draw()
		self.score = Score(screen,700, 550, str(self.p1.getScore()))
		self.turn = True
		self.end = False


	def start(self):
		self.p1.addCardToHand(self.deck)
		self.p1.addCardToHand(self.deck)
		self.p2.addCardToHand(self.deck)
		self.p2.addCardToHand(self.deck)
		self.Pen.drawCard(self.screen,self.p1.getCards(),100,400)
		self.Pen.drawCard(self.screen,self.p2.getCards(),0,0)
		self.score.update(str(self.p1.getScore()))
	
	def checkClick(self,pos):
		if self.turn:
			if self.buttonCheck.checkClick(pos):
				self.p1.addCardToHand(self.deck)
				self.Pen.drawCard(self.screen,self.p1.getCards(),100,400)
				self.score.update(str(self.p1.getScore()))
			if self.buttonDone.checkClick(pos):
				self.turn = False
		if self.buttonRetry.checkClick(pos):
			self.deck = list(range(52))
			random.shuffle(self.deck)
			self.p1 = Player()
			self.p2 = Player()
			self.buttonCheck = Button(self.screen,25,550,150,40,"Check")
			self.buttonDone = Button(self.screen,180,550,150,40,"Done")
			self.buttonRetry = Button(self.screen,335,550,150,40,"Retry")
			self.Pen = Draw()
			self.score = Score(self.screen,700, 550, str(self.p1.getScore()))
			self.turn = True
			self.end = False
			self.start()
		
	def checkScore(self):

		if self.p1.getScore() > 21:
			font = pygame.font.SysFont('Arial', 50)
			text = font.render("You Lose", True, (255,0,0)) 
			self.screen.blit(text,(100,250))
			self.turn = False
		elif not self.turn:
			self.roundAi()
		if self.end:
			scoreP1 = self.p1.getScore()
			scoreP2 = self.p2.getScore()
			if scoreP1 < 22 and scoreP2 < 22:
				if scoreP1 > scoreP2:
					font = pygame.font.SysFont('Arial', 50)
					text = font.render("You Win", True, (255,0,0)) 
					self.screen.blit(text,(100,250))
				elif scoreP1 < scoreP2:
					font = pygame.font.SysFont('Arial', 50)
					text = font.render("You Lose", True, (255,0,0)) 
					self.screen.blit(text,(100,250))
				else:
					font = pygame.font.SysFont('Arial', 50)
					text = font.render("The Draw", True, (255,0,0)) 
					self.screen.blit(text,(100,250))
			elif  scoreP1 > 21 and scoreP2 > 21:
				font = pygame.font.SysFont('Arial', 50)
				text = font.render("The Draw", True, (255,0,0)) 
				self.screen.blit(text,(100,250))
			elif scoreP1 < 22:
				font = pygame.font.SysFont('Arial', 50)
				text = font.render("You Win", True, (255,0,0)) 
				self.screen.blit(text,(100,250))
			else:
				font = pygame.font.SysFont('Arial', 50)
				text = font.render("You Lose", True, (255,0,0)) 
				self.screen.blit(text,(100,250))


	def draw(self):
		self.Pen.drawCard(self.screen,self.p1.getCards(),100,400)
		self.Pen.drawCard(self.screen,self.p2.getCards(),0,0)
		self.score.update(str(self.p1.getScore()))
		self.buttonCheck.draw()
		self.buttonDone.draw()
		self.buttonRetry.draw()

	def roundAi(self):
		self.end = True
		if self.p2.getScore() < 18:
			self.p2.addCardToHand(self.deck)
			self.end = False

			


