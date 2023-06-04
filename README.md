#Seabattles

###Seabattles is a Python termnal game, wich runs in the Code Institute mock terminal on Heroku.

Users can try to beat the computer by finding all five battleships with the 10 opportunities the game offers. Each battleship occupies one square on the board.

Here is the live version of my project





#How to play

Seabattles is based on the classic pen-and-paper game. You can read more about it on Wikipedia.

In this version, the player guess and choose a combination of a letter in a range from A to H for the columns and a number from 1 to 8 for the rows to coordinate an attack on the hidden and randomly generated battleships on the playing board.

The guesses are marked with an X for a hit on a ship and - for a miss.

When and if the player hits all the five ships, then the player wins and the game is over, or if the player miss to hit all the five ships with the ten tries, then the game is also over.

#Features

###Existing Features

RAndom board generation

Ships are randomly placed on the screenboard.
The player can not see where the computers ships are.





Play against the computers

Accepts user input

Maintains scores






Input validation and error-checking
you cannot enter coordinates outside the size of the grid
You muste enter numbers
You cannot enter the same guess twice







Data maintained 





#Testing

I have manually tested this project by doing the following:

Passed the code throug a PEP8 linter and confirmed there are no problems.
Given invalid inputs: strings when numberes are expected, out of bounds inputs, same input twice.
TEsteted in my local terminal and the Conde Institute Heroku terminal

#Bugs

####Solved Bugs
When I wrote the project, I was getting indentation problems, and coding problems that I needed to fix along the way.

#Remaining Bugs

No bugs remains

#Validator Testing

Pep8
No errors were returned from PEP8 after corrections.

#Deployment

This project was deployed using Code Institute´s mock terminal for Heroku.

Steps for deployment:

Clone this repository
Create a new Heroku app
Set the buildbacks to Python and NodeJs in taht order
Link the Heroku app to the repository
Click on Deploy

#Credits 

Code Institute for the deployment terminal
Wikipedia for the details of the Seabattles game
copyassignments webpage for explication and information about what codes function and why:
("https://copyassignment.com/battleship-game-code-in-python/") and also ("https://www.youtube.com/watch?v=tF1WRCrd_HQ")




## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`


If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!


## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
