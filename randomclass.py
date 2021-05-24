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
            elif("life_rating" in line):
                filetotal += ("life_rating = " + str(randomLife(self.industralize)) + "\n")
            elif("owner" in line and firstLine == False):
                filetotal += line
                tag = findTag(line.strip())
                firstLine == True
            elif("colonial" in line):
                colonial = True
            else:
                filetotal += line
        
        df.close()
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

def findTag(line):
    tag = line.removeprefix("owner = ")
    return tag

def randomCiv(civ):
    if(civ < 1.5):
        return "no"
    elif(civ >= 1.5 and civ <= 2.5):
        randomCivNum = random.rantint(0,100)
        if(randomCivNum <= civ * 0.2):
            return "yes"
        else:
            return "no"
    else:
        return "yes" 

def randomLit(industralize):
    industralize = industralize * 1.5
    lowerBound = round(industralize * 45,0)
    upperBound = round(industralize * 100,0)
    randomLitNum = random.randint(lowerBound, upperBound)
    lit = randomLitNum / 1000
    if(lit > 0.7):
        lit = 0.7
        return lit
    else:
        return lit



def randomResource(INDUSTRALIZE):
    START = 10000
    indu = round(START * INDUSTRALIZE,0)
    indNum = indu - START
    randomNumber = random.randint(0,indu)
    if(randomNumber <= START * 0.1):
        return "cattle"
    elif(randomNumber > START * 0.1 and randomNumber <= START * 0.135):
        return "coffee"
    elif(randomNumber > START * 0.135 and randomNumber <= START * 0.335):
        return "fish"
    elif(randomNumber > START * 0.335 and randomNumber <= START * 0.605):
        return "grain"
    elif(randomNumber > START * 0.605 and randomNumber <= START * 0.655):
        return "tropical wood"
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
        return "precious metal"
    elif(randomNumber > START + (indNum * 0.965) and randomNumber <= START + (indNum)):
        return "dye"

def randomLife(INDUSTRALIZE):
    life = 100
    lifeperc = round(life * (INDUSTRALIZE * 2),0)
    lifeRate = random.randint(0,int(lifeperc))
    lifesub = lifeperc - life
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

