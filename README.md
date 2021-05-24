# RandomRGOVictoria2
Python script that randomizes rgo in victoria 2 depending on user preference or rng
This script is meant to be run outside of victoria 2 so please do not import it into you game files. I run it on visual studio code.
This script changes your history files so please make a copy of the base ones unless you want to redownload them everytime


You run this script using randomprovincemain.py

############################# YOU HAVE TO CHANGE THE DIRECTORY TO MATCH YOURS ON LINE 4 IN randomprovincemain.py ################################################################
To find the directory right click on victoria 2 in steam and click properties and then browse in local files. After which you go to the history file and then open up the provinces file. After which right click on the properties of africa. Then copy and paste the location into line 4 in randomprovincemain.py
You do the same if you are using a mod but instead you would go to mod, then history, then province.

This script has 4 options that randomize the RGOs in your Victoria 2 game. 

The script uses a variable that's named industralization and tech. The script uses import random and depending on the industralization it will increase the likelihood of a province having an industrial rgo (coal, iron, sulphur, timber, cotton, precious metal, and dye). it also increases the potential life rating. if the industrial variable is 1 then there is 0 chance of industrial rgo's in that region, and the maximum liferating is 25. The tech variable changes the literacy and the civilization of nations. if the tech is below 1.5 then the country is always uncivilized. If it is between 1.5 and 2.5 then it's a scaling random chance if it's civilized or not. Finally if it is above 2.5 then it is always civilized. The higher the tech the higher the literacy.

The first option creates a world with a random industrial and tech variable that effects the regions the same

The second option you manually enter the industrial and tech variable for each region. Do not make the number lower than 1 for a region. It's recommended that the highest you make it is 4ish but you can make it as high as you want.

The third option is similar to the first but it's a random industrial variable for each region

The fourth option you select the tech and industrial level for the whole world

non industrial resources are selected from a base of 10000
for example the chance of cattle in a 1 industrial region would be 10%. Industrial rgo's are selected from the excess
so if the industrial score is 2 then theoretically there would be 50% industrial goods and 50% other goods. 
because the upperbound would be 20000 (10000 * 2). so if randomNumber is <= 10000 then it's a non industrial good
where if it's > 10000 then it would be an industrial rgo. Each good chance is based on a percentage.
more common goods have a higher chance of appearing.

If you want the whole world to be just coal delete line 16 in randomclass and copy and paste
filetotal += ("trade_goods = " + "coal" + "\n")
or if you want it to be all opium then paste 
filetotal += ("trade_goods = " + "opium" + "\n")
it's not limited to those two, I just used them to give you some examples. Just replace the "coal" with any resource you want.
