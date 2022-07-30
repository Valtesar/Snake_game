<h1 alighn ="center">A simple snake game from your childhood.</h1>
This is a simple snake game on your personal computer.  Written using the <b>pygame</b> framework.  

This repository is written using a single master branch, because the development was conducted by one developer (don't hate me). Further updates will be released in new branches and then uploaded to the master branch.

You can always <b>get the current version of the game in the master branch</b>.

<h2 align="center">Install</h2>
<h3>Linux</h3>

		1. Open the terminal
    
		2. Go to the directory with the downloaded game using the 'cd /folder path' command
    
		3. Run the file main.py (bash script to run using python is integrated) 
    
Windows

		1. Open a command prompt using the WIN + R command and type 'cmd'
    
		2. Navigate to the folder with the downloaded game using the 'cd/folder path' command
    
		3. Run the main.py using the python pointer as the 'python main.py'
<h2 align="center">Gameplay</h2>

<b>Main menu</b>

After starting the game, you will be taken to the main menu of the game. At the moment, one command is available in the main menu — it is pressing the ENTER key that starts the gameplay.

<b>Playing field</b>

The snake itself consisting of 1 block will be displayed on the playing field in the center of the screen. The player needs to determine the location of the food block on the playing field, then take control using the up, down, left, right keys. 
The player needs to direct the snake to the block with food to absorb it. For absorption, it is necessary to get to the coordinates of the food block with the snake's head. For each absorbed object of food, the snake will increase in length, thereby complicating the further game.

<b>Scoring</b>

Once you launch the game on your PC, you will have a text file created in the folder (directory) with the game, which is necessary to account for rating points.
If at the end of the game a player scores more points than his current maximum value, the scoring file is overwritten, the value is updated.

<b>Attention</b>

* If the player allows the snake's head to collide with the edge of the playing field, the game will be over!
* If the player allows the snake's head to collide with its body, the game will be over!

<h2 align="center">Future updates</h2>

<b>In future updates, it is expected:</b>
1. Updating the menu
2. Changing the difficulty of the game (speed, boundaries)
3. Adding sound effects
4. Adding animation
5. The ability to play through the web application
6. <s>Launching a visual display of the AI solution when playing snake!</s>
