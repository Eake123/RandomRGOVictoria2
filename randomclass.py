import random
class randomProvince:
    def __init__(self,industralize,file):
        self.industralize = industralize
        self.file = file
    def create_province(self):
        df = open(self.file, "r")
        line = df.readline()
        df.seek(0)
        filetotal = ""
        while line != "":
            line = df.readline()
            if("trade_goods" in line):
                filetotal += ("trade_goods = " + randomResource(self.industralize) + "\n")
            elif("life_rating" in line):
                filetotal += ("life_rating = " + str(randomLife(self.industralize)) + "\n")
            else:
                filetotal += line
        df.close()
        dw = open(self.file, "w")
        dw.write(filetotal)
        dw.close

def randomResource(INDUSTRALIZE):
    START = 10000
    indu = round(START * INDUSTRALIZE,0)
    indNum = indu - START
    randomNumber = random.randint(0,indu)
    if(randomNumber <= 1000):
        return "cattle"
    elif(randomNumber > 1000 and randomNumber <= 1350):
        return "coffee"
    elif(randomNumber > 1350 and randomNumber <= 3350):
        return "fish"
    elif(randomNumber > 3350 and randomNumber <= 6050):
        return "grain"
    elif(randomNumber > 6050 and randomNumber <= 6550):
        return "tropical wood"
    elif(randomNumber > 6550 and randomNumber <= 6800):
        return "opium"
    elif(randomNumber > 6800 and randomNumber <= 7800):
        return "fruit"
    elif(randomNumber > 7800 and randomNumber <= 8800):
        return "wool"
    elif(randomNumber > 8800 and randomNumber <= 9150):
        return "silk"
    elif(randomNumber > 9150 and randomNumber <= 9500):
        return "tea"
    elif(randomNumber > 9500 and randomNumber <= 10000):
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