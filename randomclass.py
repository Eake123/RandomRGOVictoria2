import random
class randomProvince:
    def __init__(self,industralize,file):
        self.industralize = industralize
        self.file = file
    def create_province(self):
        df = open(self.file, "r")
        line = df.readline()
        df.seek(0)
        colonial = False
        firstLine = False
        filetotal = ""
        while line != "":
            line = df.readline()
            if("trade_goods" in line):
                filetotal += ("trade_goods = " + randomResource(self.industralize) + "\n")
                #+ if you want the whole world to be a single resource delete the #+ in the line below and put a # in the line above. change the "coal" to any resource you want
                #+filetotal += ("trade_goods = " + "coal" + "\n")
            elif("life_rating" in line):
                if(firstLine == True):
                    filetotal += ("life_rating = " + str(randomLife(self.industralize,False)) + "\n")
                else:
                    filetotal += ("life_rating = " + str(randomLife(1,True)) + "\n")
            elif("owner" in line and firstLine == False):
                filetotal += line
                tag = findTag(line.strip())
                firstLine == True
            elif("colonial" in line):
                colonial = True
            else:
                filetotal += line
        
        df.close()
        #if(tech > 3.5):
        #    filetotal += buildState()
        dw = open(self.file, "w")
        dw.write(filetotal)
        dw.close
        try:
            if(colonial == False):
                return tag.strip()
            else:
                return "colonized"
        except:
            return "uncolonized"
    def change_literacy(self):
        df = open(self.file, "r")
        line = df.readline()
        df.seek(0)
        filetotal = ""
        while line != "":
            line = df.readline()
            if("literacy = " in line):
                filetotal += ("literacy = " + str(randomLit(self.industralize)) + "\n")
                filetotal += ("civilized = " + randomCiv(self.industralize) + "\n")
            elif("civilized" in line):
                filetotal = filetotal
            else:
                filetotal += line
        df.close()
        dw = open(self.file, "w")
        dw.write(filetotal)
        dw.close


    def get_craftsman(self,provDic):
        df = open(self.file, "r")
        line = df.readline()
        df.seek(0)
        filetotal = ""
        totalFile = df.readlines()
        count = 0
        for i in range(len(totalFile)):
            if(count < len(totalFile) - 1):
                if("POPS" in totalFile[count]):
                    try:
                        provID, useless = totalFile[count + 1].split("=")
                        newPop, menNew = changePop(provDic.get(provID.strip()),totalFile[count])
                        if isinstance(newPop,bool) == False:
                            filetotal += newPop
                            for o in totalFile[count + 1: count + 7]:
                                filetotal += o
                            filetotal += '\tcraftsman = {\n'
                            for j in totalFile[count + 3:count+5]:
                                filetotal += j
                            filetotal += '\t\tsize = ' + str(menNew) + '\n' + '\t}\n'
                            count += 7
                        else:
                            filetotal += line
                    except:
                        filetotal += line
                elif("craftsman" in totalFile[count]):
                    count += 6
                else:
                    filetotal += totalFile[count]
                count += 1
        df.close()
        dw = open(self.file, "w")
        dw.write(filetotal)
        dw.close
            

def changePop(tech,province):
    try:
        name, population = province.split("(")
        popNum, POPS = population.split(" ")
        women, men = popNum.split("/")
        try:
            if(tech >= 2.5):
                menNew = round(int(men) * (1.0075 ** tech),0)
                newWomen = round(menNew / 0.25,0)
                menNew = int(menNew)
                newWomen = int(newWomen)
                newPop = name + "(" + str(newWomen) + "/" + str(menNew) + " " + POPS
                return newPop, menNew - int(men)
            else:
                return False,False
        except:
            return False, False
    except:
        return False, False
    
    


                


def findTag(line):
    tag = line.removeprefix("owner = ")
    return tag
#+ makes the country civilized or not depending on the tech level entered
def randomCiv(civ):
    #+ if the tech is below 1.5 it will always be uncivilized
    if(civ < 1.5):
        return "no"
    #+ if the tech level is between 1.5 and 2.5 there is a chance that it will be civilized or not
    elif(civ >= 1.5 and civ <= 2.5):
        randomCivNum = random.rantint(0,100)
        if(randomCivNum <= civ * 0.2):
            return "yes"
        else:
            return "no"
    # if the tech level is above 2.5 it will always be civilized
    else:
        return "yes" 

def buildState():
    facList = [
        "state_building = {\n	level = 1\n	building = lumber_mill\n	upgrade = yes\n}\n",
        "state_building = {\n	level = 1\n	building = cement_factory\n	upgrade = yes\n}\n",
        "state_building = {\n	level = 1\n	building = furniture_factory\n	upgrade = yes\n}\n",
        "state_building = {\n	level = 1\n	building = paper_mill\n	upgrade = yes\n}",
        "state_building = {\n	level = 1\n	building = liquor_distillery\n	upgrade = yes\n}\n",
        "state_building = {\n	level = 1\n	building = fabric_factory\n	upgrade = yes\n}\n",
    ]
    doesBuild = random.randint(0,3)
    if(doesBuild <= 2):
        return ""
    else:
        facWord = ""
        for factory in facList:
            whatFac = random.randint(0,5)
            if(whatFac == 1):
                facWord += factory
            else:
                facWord = facWord
        return facWord





#+ changes the literacy for a country depending on the tech level entered
def randomLit(industralize):
    industralize = industralize * 1.5
    #+ lowest literacy is 0.045
    lowerBound = round(industralize * 45,0)
    upperBound = round(industralize * 100,0)
    randomLitNum = random.randint(lowerBound, upperBound)
    lit = randomLitNum / 1000
    if(lit > 0.7):
        lit = 0.7
        return lit
    else:
        return lit


#+ this function is where the resources are selected. non industrial resources are selected from a base of 10000
#+ for example the chance of cattle in a 1 industrial region would be 10%. Industrial rgo's are selected from the excess
#+ so if the industrial score is 2 then theoretically there would be 50% industrial goods and 50% other goods.
#+ because the upperbound would be 20000. so if randomNumber is <= 10000 then it's a non industrial good
#+ where if it's > 10000 then it would be an industrial rgo. Each good chance is based on a percentage.
#+ more common goods have a higher chance of appearing.
def randomResource(INDUSTRALIZE):
    START = 10000
    indu = round(START * INDUSTRALIZE,0)
    indNum = indu - START
    randomNumber = random.randint(0,indu)
    #+ to change the percentage chance of a good appearing you change the number after START * 
    #+ for example if you wanted coffee to have a 15% chance of spawning then you would do
    #+ elif(randomNumber > START * 0.1 and randomNumber <= START * 0.25):
    #+ you would have to change the rest of the non industrial good percentages so they end up summing to 1
    if(randomNumber <= START * 0.1):
        return "cattle"
    elif(randomNumber > START * 0.1 and randomNumber <= START * 0.135):
        return "coffee"
    elif(randomNumber > START * 0.135 and randomNumber <= START * 0.335):
        return "fish"
    elif(randomNumber > START * 0.335 and randomNumber <= START * 0.605):
        return "grain"
    elif(randomNumber > START * 0.605 and randomNumber <= START * 0.655):
        return "tropical_wood"
    elif(randomNumber > START * 0.655 and randomNumber <= START * 0.68):
        return "opium"
    elif(randomNumber > START * 0.68 and randomNumber <= START * 0.78):
        return "fruit"
    elif(randomNumber > START * 0.78 and randomNumber <= START * 0.88):
        return "wool"
    elif(randomNumber > START * 0.88 and randomNumber <= START * 0.915):
        return "silk"
    elif(randomNumber > START * 0.915 and randomNumber <= START * 0.95):
        return "tea"
    elif(randomNumber > START * 0.95 and randomNumber <= START):
        return "tobacco"
    elif(randomNumber > START and randomNumber <= START + (indNum * 0.195)):
        return "coal"
    elif(randomNumber > START + (indNum* 0.195) and randomNumber <= START + (indNum * 0.365)):
        return "iron"
    elif(randomNumber > START + (indNum * 0.365) and randomNumber <= START + (indNum * 0.465)):
        return "sulphur"
    elif(randomNumber > START + (indNum* 0.465) and randomNumber <= START + (indNum * 0.815)):
        return "timber"
    elif(randomNumber > START + (indNum * 0.815) and randomNumber <= START + (indNum * 0.915)):
        return "cotton"
    elif(randomNumber > START + (indNum * 0.915) and randomNumber <= START + (indNum * 0.965)):
        return "dye"
    elif(randomNumber > START + (indNum * 0.965) and randomNumber <= START + indNum):
        return "precious_metal"

#+ life rating function. It follows the same logic as the resource one so you change it the same way you would with the resource function
def randomLife(INDUSTRALIZE,colonize):
    life = 100
    lifeperc = round(life * (INDUSTRALIZE * 1.5),0)
    lifeRate = random.randint(0,int(lifeperc))
    lifesub = lifeperc - life
    if(colonize == True):
        if(lifeRate <= life * 0.2):
            return 15
        elif(lifeRate > life * 0.2 and lifeRate <= life * 0.55):
            return 20
        elif(lifeRate > life * 0.55 and lifeRate <= life):
            return 25
        elif(lifeRate > life and lifeRate <= life + lifesub * 0.5):
            return 30
        elif(lifeRate > life + lifesub * 0.5 and lifeRate <= life + lifesub * 0.85):
            return 35
        elif(lifeRate > life + lifesub * 0.85 and lifeRate <= life + lifesub * 0.925):
            return 40
        elif(lifeRate > life + lifesub * 0.925 and lifeRate <= life + lifesub * 0.975):
            return 45
        elif(lifeRate > life + lifesub * 0.975 and lifeRate <= life + lifesub):
            return 50
    else:
        if(lifeRate <= life * 0.25):
            return 10
        elif(lifeRate > life * 0.25 and lifeRate <= life * 0.50):
            return 15
        elif(lifeRate > life * 0.5 and lifeRate <= life):
            return 20

