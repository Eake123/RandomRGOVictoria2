import glob, os
from randomclass import *
########################### enter you directory here ##############################
directory = "D:\Steam\steamapps\common\Victoria 2\mod\HPM\history\provinces"

def completeRandom():
    industralize = random.randint(1,3)
    os.chdir(directory)
    for filename in os.listdir(os.getcwd()):
        singleRegion = directory + '\\' + filename
        os.chdir(singleRegion)
        for file in glob.glob("*.txt"):
            changeProvince = randomProvince(industralize, file)
            changeProvince.create_province()

def manualRandom():
    os.chdir(directory)
    for filename in os.listdir(os.getcwd()):
        industralize = float(input("enter the industralization for %s: " %(filename)))
        singleRegion = directory + '\\' + filename
        os.chdir(singleRegion)
        for file in glob.glob("*.txt"):
            changeProvince = randomProvince(industralize, file)
            changeProvince.create_province()

def regionRandom():
    os.chdir(directory)
    for filename in os.listdir(os.getcwd()):
        industralize = random.randint(1,3)
        singleRegion = directory + '\\' + filename
        os.chdir(singleRegion)
        for file in glob.glob("*.txt"):
            changeProvince = randomProvince(industralize, file)
            changeProvince.create_province()
def main():
    manual = input("do you want a completely random world (enter 1) or change it for each region (2) or random world but regions have differing levels (3): ")
    if manual == "1":
        completeRandom()
    elif manual == "2":
        manualRandom()
    else:
        regionRandom()



        


main()