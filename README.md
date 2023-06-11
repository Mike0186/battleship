![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# BattleShips 

Battleships is a Python Ternminal game. which runs in the code institute mocl terminal on Heroku.
The user plays against the computer in the attempt to sink all the computers ships first. 

### How To Play
By running the code it generates both the players and the computers boards. The players ships are hidden from sight on the screen and the player must guess where they are.
The players ships are visible to the player only and are marked with a @ symbol,. The amin of the game is to try and find the computers ships before the computer finds your. The first one to hit all their oppinents ships wins.


### Features
- The user can deceide what size the gameboard is at the begining of the game. 
- The game automatically calculates the number of ships based on the size of the game board -1. 
- Ships are randomly placed. 
- The computers ships are hiden from sight. 

![ASCI Art](/wireframe-images/Battleship2.JPG)


![ASCI Art](/wireframe-images/battleship1.JPG)
- Takes user input and presents it in other places.

![ASCI Art](/wireframe-images/battleship3.JPG)
- Validates the inmput from the user. 

### Future Features. 
- Allow pleople to place there own ship. 
- Have a fleet of larger ships that can span accross 2 to 3 columns/rows.

### Testing
I have manually tested the game byt completing the follwoing:
- Passed the game invalid strings and numbers to check the validation. 
- Passed the code through the pep8 linter and confirm there are no issues. 

### Bugs
- Only one board would populate
- Both computer and player guessing on the same board.

#### Validator Testing 
- PEP8, no errors found

### Deployment 

This project was deployed using Code Institute's Mock Terminal for Heroku.
1. Steps for deployment
2. create a new Heroku app
3. link the Heroku app to the respository
4. click on deploy

### Credits 
* Code Institute for the deployment terminal
