import re
import sys
import glob

sys.path.insert(0, '/mnt/PhD/data')

def list_obs():
    route = re.findall('.*/.*?', sys.argv[0] )
    #route = (str(route[0]) + "data/*.IMG")
    route = ("*.IMG")
    img_names = glob.glob(route)
    file = open("../../data/list.txt", "r+")

    for i in range (0,len(img_names)):
        img_names[i]=img_names[i][5:]
        file.writelines(img_names[i])
        file.writelines('\n')

    file.close()

list_obs()