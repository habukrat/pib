# --------------------- OBJECT ORIENTED PROGRAMMING ----------------------
class Ship:
	'Common base class for all ships'
	shipCount = 0

	def __init__():
		shipCount += 1
		#TODO		


# --------------------- FUNCTIONS THAT MAY BE USEFUL ----------------------
# These functions will still be helpful once you implement that AI
# But they may need to be updated later on


# Name: getHumanShipInput()
# Description: This function prompts the user to enter ship placements and
# places the ships in the human side matrix
# Input: Human Ship Matrix - contains locations of the ships
# Output: humanShips - the list of ships
def getHumanShipInput(playerBottomMatrix):
	# TODO
	# Prompt user to enter ship locations
		# Check to see that ships are of size 2, 3, 3, 4, 5
		# Check to make sure ships are not overlapping
	# For each input, create Ship object
		# Place ship on the first players matrix in the correct locations
		# Place ship in a list that will contain all of this players ships
	#return list of players ships


# Name: humanTurn()
# Description: This function prompts user to input their next target and 
# Input: playerTopMatrix - need to check that for previous moves
# Output: Target row/column
def humanTurn(playerTopMatrix):
	# TODO
	# Prompt user to enter target location
		# Check to see that location was not already targeted
	# Return inputted locations


# Name: isGameOver()
# Description: This function checks to see if the game is over. Called after
# each human or Ai turn
# Input: ship list - list containing the human/ai ships
# Output: True - game is over if all ships have been sunk
#         False - game is not over because not all ships have been sunk
def isGameOver(shipsList):
	# TODO


# ------------------------------ MAIN CODE -------------------------------

#TODO - Create 4 empty matrices for each players perspective 
	# player1matrixBottom
	# player1matrixTop
	# player2matrixBottom
	# player2matrixTop

# First player places ships
player1Ships = getHumanShipInput(player1BottomMatrix)

# Second player places ships
player2Ships = getHumanShipInput(player2BottomMatrix)


While game is not over
	# First players turn
	humanTurn(player1TopMatrix)
	updateBoards()
	isGameOver()

	# Second players turn
	humanTurn(player2TopMatrix)
	updateBoards()
	isGameOver()
