Battleship Game
In this game the player needs to guess where the battleships are hidden on the board that the computer had created. 
The player needs to choose a number between 1 and 8 and a letter between A and H to try to hit the battleship with the choosed coordinators. This game was created to complete the third portfolioprodject for Code Insitute's Full Stack Software Developer course.

How to play
The player must type a choosed number and then press enter.
The player must select a letter and then press enter.
If the combination gives the right coordination to hit a battleship, the computer will tell the player so, if it is a miss, the computer will tell the player so as well.

The player will have a welcome message in the beginning and after every shot.

The player can only guess with numbers and letters, nothing else.

The player can only guess the same combination of number and letter once, in case of repeating the same combination of number and letter,  the game will not accept that guess and will tell the player that this is a repeated guess. 

If the player guesses a number or letter outside the stipulated range, the computer will give a message of the error and let the player try to choose again. 

If the player is unable to guess the location of the 5 battleships in 10 attempts, then the game is over. To replay the game, the player will need to press enter and the game will restart.

The player has 10 attempts to hit all the 5 battleships that are hidden in the board.
The computer will end the game after 10 tries. 

If the player can guess the location of one battleship, the player will receive a congratulations message and if the player can guess the location of all the 5 battleships the player will receive a congratulations message and will win the game. If the player wins the game, the game will be over. To replay the game, the player will need to press enter and and the game will restart. 

Features
Existing Features

Live 
![Playing the game live](https://vimeo.com/833591245/04b2c715d4)

Random board generation

Ships are randomly placed on the screenboard.
The player can not see where the computers ships are.
![Image of board before starting to play](../seabattle-game/images/before_playing.png)

Play against the computer
Accepts users input
Maintains scores
Shows message of where the user missed

![Image of first miss](../seabattle-game/images/first%20miss.png)

Shows message of where the user hit

![Image of first hit](../seabattle-game/images//first%20hit.png)

Input validation and error-checking
you cannot enter coordinates outside the stipuleted values. 

![Image: You must enter a number](../seabattle-game/images//wrong%20number.png)

![Image: You must enter a letter](../seabattle-game/images//wrong%20letter.png)

You cannot enter the same guess twice
![Image: You already guessed that one](../seabattle-game/images//already-guessed.png)

Game over
![Game over](../seabattle-game/images//missed-game-over.png)



Technologies used
Language Python
Frameworks, Deployement & Libraries
Github
Gitpod

Testing
Testing was done throughout the project mainly by running the program in the terminal as well as python debugger. I committed the codes to github after writing every new list or code.

I used the deployed site to manually type correct and incorrect data to validate and see how the program responded.

Accessibility
The whole project was built using python, therefore no other languages were used.
Issues and bugs
I had indentation issues and problems with the formulation of codes but I corrected the issues along the way.
Fixed bugs
problem: I had problems with indentation and missing whitespaces.
Solution: I contacted the tutor who helped me and suggested pages where I could read about it.

Validator Testing
Pep8
No bigger errors were returned from PEP8 after corrections.

Deployment
I followed the below steps when deploying my project to Heroku, based on the Code Institute instructions:

In HEROKU after creating the account:

"Create new App"

Give the App a unique name and enter region

Click on "Create App"

Click on "Settings" on your new App Dashboard

Scroll down to Config Vars where in my instance I only inserted KEY: PORT and VALUE: 8000 since I have no creds.json files to add.

Press Add-button

Scroll down to Buildpacks and press the icon for Python, click Save Changes, then press the icon for Nodejs and save changes. These Buildpacks need to be in below order:

Python NodeJS

Go to Deploy section tab and scroll down to Deployment Method. I connected to my Github pages and could thereafter search for my Github Repository "Parents Allowance Calculator" and then click connect.

Scroll down to Automatic and Manual Deploys sections. I clicked on Automatic Deployment so that my changes that I push to github automatically updates in Heroku.

Then in the Manual Deploy section, press Deploy Branch.

After project has been deployed successfully I clicked the View-button to see the program run in the terminal.

Credits
[PRANJAL DEV] https://copyassignment.com/battleship-game-code-in-python and also [KnowledgeMavens]https://www.youtube.com/watch?v=tF1WRCrd_HQ
 My whole project is based on his youtube tutorial. however, I have tried to change a bit but have largely coded with him in his video and also with the tution from copyassigment.

Pages I used to solve errors and other problems and some code: https://stackoverflow.com/  https://www.w3schools.com/python/python_conditions.asp https://www.geeksforgeeks.org/python-docstrings/

Gratitude

A big thank you to tutor suport who helped me through this project with a lot of patience and always nice treatment.

A special thanks my mentor Martina Terlević for her support and advices that helped me through my process to make it.
