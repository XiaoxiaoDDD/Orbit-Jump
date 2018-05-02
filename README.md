# Orbit-Jump
Group Members: Xiaoxiao Du,Rustem Tursyn
a spanceship is revolving around a planet. Once the player hit the keyboard,
the propeller will push the spaceship along the tangent line, aiming at the target planet.
If the spaceship miss the orbit of the next planet, the player loses. 
Else, it would jump to the next orbit and continue revolving around it.
Some planets have special features,i.e. the size of the orbit/the velocity of revolving.
Once the spaceship arrives at the final planet, the player wins.


Features of the game:

The player's spaceship automatically lands on the orbit of the first left planet at the start of the game, and it starts rotating. When the player presses SHIFT button, the spaceship accelerates. In the game it is shown as the spaceship is firing. 
When the player presses SHIFT the spaceship rotates on orbit with increasing speed. When the player releases the SHIFT button,
the spaceship shoots on direction of line tangent to the center of that orbit circle. Spaceship flies until it touches the orbit of another planet. When spaceship touches the orbit of planet, it starts revolving on the orbit of that new planet.
The spaceship in each Level shall get into the BlackHole's orbit. When Spaceship touches the orbit of blackhole, spaceship starts to revolve around that orbit. The orbit's radius starts to decrease once the spaceship gets on the orbit of Blackhole. When the radius of Blackhole's orbit is zero (Spaceship gets to the center of Blackhole), the spaceship "transfers" to the next Level (New level pops up, spaceship lands on the new blackhole's orbit in that new level). Each level has different features and difficulties.   

Common features for all levels:
Background of the game is black with stars. There are small falling stars, which creates illusion that these falling stars
are far and that the environment is indeed a galaxy. 


Levels:
The game itself consists of 3 stages. 1st level- easy, 2nd level-medium, 3rd level-hard levels. 
1st level- there are 8 planets displayed. Planets are spread out in the canvas with no particular pattern. 
Every planet has an orbit. In this stage the orbits are still (not moving). 
2nd level- there are 10 planets displayed. The difference between 1st level is that some planet's orbits are shrinking and expanding (radius of orbits are increasing and then decrasing to some particular level). When spaceship gets into the orbit of a planet, then it starts to revolve in either clockwise or anticlockwise direction (as we programmed). This way it is more difficult for player to play.
3rd level- all features of 2nd level. Also, few planet's orbits are denoted with RED color. When spaceship gets into orbit of those planets, then spaceship revolves with very high speed (making player hard to shoot with precision).

The program has other Three "levels": level 0, level 4, level5
Level 0: this is the "menu" of the game. When the code runs, it first shows Level 0. There are two options: "PLay" and "Scores". When the user clicls Play, then it transfers to Level 1 of actual game. When user clicks "Score", then the scores of previous players show up as Level 4. 
Level5: the results page. When the user either loses the game or wins tha game, the game shows the number of points it earned during that game and asks for inputting the name of the user. After inputting the name and pressing ENTER, the user trnasfers to Level 0(Menu level).



Features to be added:

- Sound: we will add the background sound and the sound when the user wins the game and loses the game.
- Further complicate Level3. We will add moving images of asteroids. These asteroids will be flying among planets. The user should not hit the asteroid when shooting the spacehip. 
- Right now the program recognizes blackholes from which spaceship emerges as "planets", spaceship can jump back to the blackhole while game is still on. This will be fixed







 
