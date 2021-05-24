# RandomRGOVictoria2
Python script that randomizes rgo in victoria 2 depending on user preference or rng

You run this script using randomprovincemain.py

############################# YOU HAVE TO CHANGE THE DIRECTORY TO MATCH YOURS ON LINE 4 IN randomprovincemain.py ##################################################################

This script has 3 options that randomize the RGOs in your Victoria 2 game. This may effect saves, I have not tried it yet. If you're concerned about that then create a copy of your provinces file and run it from there

The script uses a variable that's named industralization. The script uses import random and depending on the industralization it will increase the likelihood of a province having an industrial rgo (coal, iron, sulphur, timber, cotton, precious metal, and dye). it also increases the potential life rating. if the industrial variable is 1 then there is 0 chance of industrial rgo's in that region, and the maximum liferating is 25.

The first option creates a world with a random industrial variable that effects the regions the same

The second option you manually enter the industrial score for each region. Do not make the number lower than 1 for a region. It's recommended that the highest you make it is 4ish but you can make it as high as you want

The third option is similar to the first but it's a random industrial variable for each region

