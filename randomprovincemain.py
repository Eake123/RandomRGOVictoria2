import glob, os
from randomclass import *
########################### enter you directory here ##############################
directory = "D:\Program Files (x86)\steamapps\common\Victoria 2\mod\GFM\history\provinces"
directoryLit = directory.replace("provinces", "countries")
directoryPop = directory.replace("provinces", "pops")
directoryPop = directoryPop + "\\1836.1.1"
def literacy(regionDic):
    os.chdir(directoryLit)
    for file in glob.glob("*.txt"):
        try:
            print("in file",file)
            changeProvince = randomProvince(regionDic[file[:3]], file)
            changeProvince.change_literacy()
        except:
            pass

def changePop(provDic):
    os.chdir(directoryPop)
    for file in glob.glob("*txt"):
        changePop = randomProvince(1, file)
        changePop.get_craftsman(provDic)        

        


def completeRandom(techInput):
    industralize = random.randint(1,5)
    tech = random.randint(1,6)
    if(tech > 4):
        tech = 4
    os.chdir(directory)
    regionDic = {}
    for filename in os.listdir(os.getcwd()):
        singleRegion = directory + '\\' + filename
        os.chdir(singleRegion)
        for file in glob.glob("*.txt"):
            print(file)
            changeProvince = randomProvince(industralize, file)
            tag = changeProvince.create_province(tech)
            print(tag)
            if(tag == "QNG" and "china" not in filename):
                regionDic = regionDic
            elif(tag == "FRA" and "france" not in filename):
                regionDic = regionDic
            elif(tag == "PER" and "central" not in filename):
                regionDic = regionDic
            elif(tag == "POR" and "portugal" not in filename):
                regionDic = regionDic
            elif(tag == "TUR" and "balkan" not in filename):
                regionDic = regionDic
            elif(tag == "RUS" and "soviet" not in filename):
                regionDic = regionDic
            else:
                regionDic[tag] = tech
    try:
        regionDic["SHW"] = regionDic["ZUL"]
    except:
        pass
    print(regionDic)
    if(techInput == "1"):
        literacy(regionDic)

def manualRandom(techInput):
    os.chdir(directory)
    regionDic = {}
    provDic = {}
    for filename in os.listdir(os.getcwd()):
        industralize = float(input("enter the industralization for %s or enter 0 to not make any changes to this region: " %(filename)))
        if(industralize == 0):
            pass
        else:
            if(techInput == "1"):
                tech = float(input("enter the tech level for %s: " %(filename)))
            else:
                tech = False
            singleRegion = directory + '\\' + filename
            os.chdir(singleRegion)
            for file in glob.glob("*.txt"):
                print(file)
                provDic[fileSplit(file)] = tech
                changeProvince = randomProvince(industralize, file)
                tag = changeProvince.create_province(tech)
                if(tag == "QNG" and "china" not in filename):
                    regionDic = regionDic
                elif(tag == "FRA" and "france" not in filename):
                    regionDic = regionDic
                elif(tag == "PER" and "central" not in filename):
                    regionDic = regionDic
                elif(tag == "POR" and "portugal" not in filename):
                    regionDic = regionDic
                elif(tag == "TUR" and "balkan" not in filename):
                    regionDic = regionDic
                elif(tag == "RUS" and "soviet" not in filename):
                    regionDic = regionDic
                else:
                    regionDic[tag] = tech
    try:
        regionDic["SHW"] = regionDic["ZUL"]
        regionDic["SAR"] = regionDic["FRA"]
        regionDic["SIC"] = regionDic["FRA"]
        regionDic["SIC"] = regionDic["NET"]
    except:
        pass
    if(techInput == "1"):
        literacy(regionDic)

def fileSplit(file):
    try:
        provID, Name = file.split("-")
        return provID.strip()
    except:
        return None

def regionRandom(techInput):
    os.chdir(directory)
    regionDic = {}
    for filename in os.listdir(os.getcwd()):
        industralize = random.randint(1,5)
        tech = random.randint(1,6)
        if(tech > 4):
            tech = 4
        singleRegion = directory + '\\' + filename
        os.chdir(singleRegion)
        for file in glob.glob("*.txt"):
            print(file)
            changeProvince = randomProvince(industralize, file)
            tag = changeProvince.create_province(tech)
            print(tag)
            if(tag == "QNG" and "china" not in filename):
                regionDic = regionDic
            elif(tag == "FRA" and "france" not in filename):
                regionDic = regionDic
            elif(tag == "PER" and "central" not in filename):
                regionDic = regionDic
            elif(tag == "POR" and "portugal" not in filename):
                regionDic = regionDic
            elif(tag == "TUR" and "balkan" not in filename):
                regionDic = regionDic
            elif(tag == "RUS" and "soviet" not in filename):
                regionDic = regionDic
            else:
                regionDic[tag] = tech
    try:
        #regionDic["SHW"] = regionDic["ZUL"]
        regionDic["SAR"] = regionDic["FRA"]
        regionDic["SIC"] = regionDic["FRA"]
        regionDic["SIC"] = regionDic["NET"]
    except:
        pass
    if(techInput == "1"):
        literacy(regionDic)

def singleRandom(techInput):
    industralize = float(input("enter an industralize level for the whole world: "))
    tech = float(input("enter a tech level for the whole world: "))
    if(tech > 4):
        tech = 4
    os.chdir(directory)
    regionDic = {}
    provDic = {}
    for filename in os.listdir(os.getcwd()):
        singleRegion = directory + '\\' + filename
        os.chdir(singleRegion)
        for file in glob.glob("*.txt"):
            print(file)
            provDic[fileSplit(file)] = tech
            changeProvince = randomProvince(industralize, file)
            tag = changeProvince.create_province()
            print(tag)
            if(tag == "QNG" and "china" not in filename):
                regionDic = regionDic
            elif(tag == "FRA" and "france" not in filename):
                regionDic = regionDic
            elif(tag == "PER" and "central" not in filename):
                regionDic = regionDic
            elif(tag == "POR" and "portugal" not in filename):
                regionDic = regionDic
            elif(tag == "TUR" and "balkan" not in filename):
                regionDic = regionDic
            elif(tag == "RUS" and "soviet" not in filename):
                regionDic = regionDic
            else:
                regionDic[tag] = tech
    try:
        regionDic["SHW"] = regionDic["ZUL"]
        
    except:
        pass
    print(regionDic)
    if(techInput == "1"):
        literacy(regionDic)
def main():
    manual = input("do you want a completely random world (enter 1) or manually change it for each region (2) or a random world but regions have differing levels (3)\n or set an industry and tech level for the whole world (4): ")
    techInput = input("do you want to change the literacy and civilization level (enter 1) or not change it (enter 2): ")
    if manual == "1":
        completeRandom(techInput)
    elif manual == "2":
        manualRandom(techInput)
    elif manual == "3":
        regionRandom(techInput)
    else:
        singleRandom(techInput)



        


main()
