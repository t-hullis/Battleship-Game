# Batttleships Game

Battleships is a terminal game, based on the classic board game, which  runs on the code institute mock terminal on Heroku.
The game is won when a player finds all the opponents ships before they find yours.

<img src="images/amirespon.png" width = 70%>

## The Rules

    1,  Choose the size of the board (between 3 and 15) and the number of battleships
        you would like to be placed on the board.

    2,  Guess the coordinates of the ships on the computer board.

    3,  You can see where the shots have been placed on your board,
        denoted by the X for a hit and O a miss.
    
    4,  If you place a shot in the same place twise, you will lose
        that go, so make sure you shot to different coordinates 
        each time.
    
    4,  The first one to find all the oppostions battleships
        wins!

## Features

<br/>
- Board is generated at the users request. The size of the board and the number of ships is up to the player with inputs at the start.
- The ships placed for the computer are hidden from the user but the user can see where his own ships were placed.
<br/>

<img src="images/start.png" width="49%">
<img src="images/first-round.png" width="49%"> 

<br/>
- The programme counts the hits ships after each round and deplays the score for the computer and the user.
- If the user selects a coordinate for their shot which isnt applicable, the programme returns an error and asks for new coordinates for that shot.

<br/>
<img src="images/scores-exitloop.png" width="49%">
<img src="images/error-feedback.png" width="49%">
<br/>

- Once there is winner, the porgram will anounce that winner and ask the user if they would like to replay the game or exit the programme.

## Data Model
I have used a Gameboard class to set up the board, using 4 instances for a hidden and display board for both the user and the computer. In this class you can set the board size and ship number with the methods within, ie: create_ships, print_board. There is also a method called fire_shots which places the shots on the board and a method called count_ships, which adds up the hit ships at the end of each round, to give the score of the game.

## Testing

- Passed python Pep8 online code validator.
- Tested within github on my terminal with no problems as well as on Heroku.

<img src="images/pep8.png" width=70%>

### Bugs
- I only found two bugs during this project, 
    - The x axis of the player boards was displaying the number of ships rather than the size of the board. this was due to my start_game function returning its  variables in the wrong order for the run_game function.
    - The axis' of the ship hit function were the wrong way round so it wasnt detecting wether the right ship was hit.



