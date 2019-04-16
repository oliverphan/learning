from random import randint
loss = 'You lost.'
win = 'You won!'
draw = 'It\'s a draw.'

if __name__ == '__main__':
	play = True
	while play is True:
		print('This is a game of rock-paper-scissors.')
		print('You\'ll be playing against a randomized computer.')
		print('Pick your move. Rock, Paper, or Scissors')
		player_move = raw_input().lower()
		
		#Randomize the move of the computer
		moves = ['rock', 'paper', 'scissors']
		random_move = moves[randint(0, 2)]
		
		print ("Computer move: " + random_move.upper())
		if player_move == random_move:
			print draw
		elif player_move == 'rock':
			if random_move == 'paper':
				print loss
			else:
				print win
		elif player_move == 'paper':
			if random_move == 'rock':
				print win
			else:
				print loss
		elif player_move == 'scissors':
			if random_move == 'paper':
				print win
			else:
				print loss
		else:
			print "Spelling error!"
		print('Play again? Y/N')
		replay = raw_input().upper()
		if replay == 'N':
			play = False