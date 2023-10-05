import os
os.system("pip install nbt")
os.system("pip install Pillow")
os.system("pip install numpy")
os.system("pip install opencv-python")
os.system("pip install time")
from time import sleep
from PIL import Image
from nbt import nbt
import numpy as np
import cv2
def determine_bloc_minecraft(r, g, b):
    couleurs_minecraft = {
        ( 90, 126, 40, ) : "4",
        ( 109, 153, 48, ) : "5",
        ( 127, 178, 56, ) : "6",
        ( 67, 94, 30, ) : "7",
        ( 175, 165, 116, ) : "8",
        ( 212, 200, 140, ) : "9",
        ( 247, 233, 163, ) :  "10",
        ( 131, 123, 86, ) :  "11",
        ( 141, 141, 141, ) :  "12",
        ( 171, 171, 171, ) :  "13",
        ( 199, 199, 199, ) :  "14",
        ( 105, 105, 105, ) :  "15",
        ( 181, 0, 0, ) :  "16",
        ( 219, 0, 0, ) :  "17",
        ( 255, 0, 0, ) :  "18",
        ( 135, 0, 0, ) :  "19",
        ( 114, 114, 181, ) :  "20",
        ( 138, 138, 219, ) :  "21",
        ( 160, 160, 255, ) :  "22",
        ( 85, 85, 135, ) :  "23",
        ( 119, 119, 119, ) :  "24",
        ( 144, 144, 144, ) :  "25",
        ( 167, 167, 167, ) :  "26",
        ( 89, 89, 89, ) :  "27",
        ( 0, 88, 0, ) :  "28",
        ( 0, 107, 0, ) :  "29",
        ( 0, 124, 0, ) :  "30",
        ( 0, 66, 0, ) :  "31",
        ( 181, 181, 181, ) :  "32",
        ( 219, 219, 219, ) :  "33",
        ( 255, 255, 255, ) :  "34",
        ( 135, 135, 135, ) :  "35",
        ( 116, 119, 131, ) :  "36",
        ( 141, 144, 158, ) :  "37",
        ( 164, 168, 184, ) :  "38",
        ( 87, 89, 98, ) :  "39",
        ( 107, 77, 55, ) :  "40",
        ( 130, 94, 66, ) :  "41",
        ( 151, 109, 77, ) :  "42",
        ( 80, 58, 41, ) :  "43",
        ( 80, 80, 80, ) :  "44",
        ( 96, 96, 96, ) :  "45",
        ( 112, 112, 112, ) :  "46",
        ( 59, 59, 59, ) :  "47",
        ( 45, 45, 181, ) :  "48",
        ( 55, 55, 219, ) :  "49",
        ( 64, 64, 255, ) :  "50",
        ( 34, 34, 135, ) :  "51",
        ( 102, 84, 51, ) :  "52",
        ( 123, 102, 62, ) :  "53",
        ( 143, 119, 72, ) :  "54",
        ( 76, 63, 38, ) :  "55",
        ( 181, 179, 174, ) :  "56",
        ( 219, 217, 211, ) :  "57",
        ( 255, 252, 245, ) :  "58",
        ( 135, 134, 130, ) :  "59",
        ( 153, 90, 36, ) :  "60",
        ( 186, 109, 44, ) :  "61",
        ( 216, 127, 51, ) :  "62",
        ( 114, 67, 27, ) :  "63",
        ( 126, 54, 153, ) :  "64",
        ( 153, 65, 186, ) :  "65",
        ( 178, 76, 216, ) :  "66",
        ( 94, 40, 114, ) :  "67",
        ( 72, 109, 153, ) :  "68",
        ( 88, 132, 186, ) :  "69",
        ( 102, 153, 216, ) :  "70",
        ( 54, 81, 114, ) :  "71",
        ( 163, 163, 36, ) :  "72",
        ( 197, 197, 44, ) :  "73",
        ( 229, 229, 51, ) :  "74",
        ( 121, 121, 27, ) :  "75",
        ( 90, 145, 18, ) :  "76",
        ( 109, 175, 22, ) :  "77",
        ( 127, 204, 25, ) :  "78",
        ( 67, 108, 13, ) :  "79",
        ( 172, 90, 117, ) :  "80",
        ( 208, 109, 142, ) :  "81",
        ( 242, 127, 165, ) :  "82",
        ( 128, 67, 87, ) :  "83",
        ( 54, 54, 54, ) :  "84",
        ( 65, 65, 65, ) :  "85",
        ( 76, 76, 76, ) :  "86",
        ( 40, 40, 40, ) :  "87",
        ( 109, 109, 109, ) :  "88",
        ( 132, 132, 132, ) :  "89",
        ( 153, 153, 153, ) :  "90",
        ( 81, 81, 81, ) :  "91",
        ( 54, 90, 109, ) :  "92",
        ( 65, 109, 132, ) :  "93",
        ( 76, 127, 153, ) :  "94",
        ( 40, 67, 81, ) :  "95",
        ( 90, 45, 126, ) :  "96",
        ( 109, 54, 153, ) :  "97",
        ( 127, 63, 178, ) :  "98",
        ( 67, 33, 94, ) :  "99",
        ( 36, 54, 126, ) : "100",
        ( 44, 65, 153, ) : "101",
        ( 51, 76, 178, ) : "102",
        ( 27, 40, 94, ) : "103",
        ( 72, 54, 36, ) : "104",
        ( 88, 65, 44, ) : "105",
        ( 102, 76, 51, ) : "106",
        ( 54, 40, 27, ) : "107",
        ( 72, 90, 36, ) : "108",
        ( 88, 109, 44, ) : "109",
        ( 102, 127, 51, ) : "110",
        ( 54, 67, 27, ) : "111",
        ( 109, 36, 36, ) : "112",
        ( 132, 44, 44, ) : "113",
        ( 153, 51, 51, ) : "114",
        ( 81, 27, 27, ) : "115",
        ( 18, 18, 18, ) : "116",
        ( 22, 22, 22, ) : "117",
        ( 25, 25, 25, ) : "118",
        ( 13, 13, 13, ) : "119",
        ( 178, 169, 55, ) : "120",
        ( 215, 205, 66, ) : "121",
        ( 250, 238, 77, ) : "122",
        ( 132, 126, 41, ) : "123",
        ( 65, 155, 151, ) : "124",
        ( 79, 188, 183, ) : "125",
        ( 92, 219, 213, ) : "126",
        ( 49, 116, 113, ) : "127",
        ( 53, 91, 181, ) : "128",
        ( 64, 110, 219, ) : "129",
        ( 74, 128, 255, ) : "130",
        ( 39, 68, 135, ) : "131",
        ( 0, 154, 41, ) : "132",
        ( 0, 187, 50, ) : "133",
        ( 0, 217, 58, ) : "134",
        ( 0, 115, 31, ) : "135",
        ( 92, 61, 35, ) : "136",
        ( 111, 74, 42, ) : "137",
        ( 129, 86, 49, ) : "138",
        ( 68, 46, 26, ) : "139",
        ( 80, 1, 0, ) : "140",
        ( 96, 2, 0, ) : "141",
        ( 112, 2, 0, ) : "142",
        ( 59, 1, 0, ) : "143",
        ( 148, 126, 114, ) : "144",
        ( 180, 152, 138, ) : "145",
        ( 209, 177, 161, ) : "146",
        ( 111, 94, 85, ) : "147",
        ( 113, 58, 26, ) : "148",
        ( 137, 71, 31, ) : "149",
        ( 159, 82, 36, ) : "150",
        ( 84, 43, 19, ) : "151",
        ( 106, 62, 77, ) : "152",
        ( 128, 75, 93, ) : "153",
        ( 149, 87, 108, ) : "154",
        ( 79, 46, 57, ) : "155",
        ( 80, 77, 98, ) : "156",
        ( 96, 93, 119, ) : "157",
        ( 112, 108, 138, ) : "158",
        ( 59, 57, 73, ) : "159",
        ( 73, 83, 38, ) : "160",
        ( 89, 101, 46, ) : "161",
        ( 103, 117, 53, ) : "162",
        ( 55, 62, 28, ) : "163",
        ( 132, 94, 26, ) : "164",
        ( 160, 114, 31, ) : "165",
        ( 186, 133, 36, ) : "166",
        ( 99, 70, 19, ) : "167",
        ( 40, 29, 25, ) : "168",
        ( 49, 35, 30, ) : "169",
        ( 57, 41, 35, ) : "170",
        ( 30, 22, 19, ) : "171",
        ( 114, 55, 55, ) : "172",
        ( 138, 66, 67, ) : "173",
        ( 160, 77, 78, ) : "174",
        ( 85, 41, 41, ) : "175",
        ( 62, 65, 65, ) : "176",
        ( 75, 79, 79, ) : "177",
        ( 87, 92, 92, ) : "178",
        ( 46, 49, 49, ) : "179",
        ( 96, 76, 70, ) : "180",
        ( 116, 92, 84, ) : "181",
        ( 135, 107, 98, ) : "182",
        ( 72, 57, 52, ) : "183",
        ( 54, 44, 65, ) : "184",
        ( 65, 53, 79, ) : "185",
        ( 76, 62, 92, ) : "186",
        ( 40, 33, 49, ) : "187",
        ( 87, 52, 62, ) : "188",
        ( 105, 63, 76, ) : "189",
        ( 122, 73, 88, ) : "190",
        ( 65, 39, 47, ) : "191",
        ( 54, 58, 30, ) : "192",
        ( 65, 71, 36, ) : "193",
        ( 76, 82, 42, ) : "194",
        ( 40, 43, 22, ) : "195",
        ( 54, 36, 25, ) : "196",
        ( 65, 43, 30, ) : "197",
        ( 76, 50, 35, ) : "198",
        ( 40, 26, 19, ) : "199",
        ( 26, 16, 11, ) : "200",
        ( 32, 19, 14, ) : "201",
        ( 37, 22, 16, ) : "202",
        ( 20, 12, 8, ) : "203",
        ( 101, 43, 33, ) : "204",
        ( 122, 52, 40, ) : "205",
        ( 142, 60, 46, ) : "206",
        ( 75, 32, 24, ) : "207",
        ( 105, 45, 69, ) : "208",
        ( 127, 54, 83, ) : "209",
        ( 148, 63, 97, ) : "210",
        ( 78, 33, 51, ) : "211",
        ( 134, 34, 35, ) : "212",
        ( 163, 41, 42, ) : "213",
        ( 189, 48, 49, ) : "214",
        ( 100, 25, 26, ) : "215",
        ( 16, 89, 95, ) : "216",
        ( 19, 108, 115, ) : "217",
        ( 22, 126, 134, ) : "218",
        ( 12, 67, 71, ) : "219",
        ( 65, 18, 21, ) : "220",
        ( 79, 22, 25, ) : "221",
        ( 92, 25, 29, ) : "222",
        ( 49, 13, 15, ) : "223",
        ( 61, 31, 44, ) : "224",
        ( 74, 38, 53, ) : "225",
        ( 86, 44, 62, ) : "226",
        ( 46, 23, 33, ) : "227",
        ( 41, 101, 99, ) : "228",
        ( 50, 122, 120, ) : "229",
        ( 58, 142, 140, ) : "230",
        ( 31, 75, 74, ) : "231",
        ( 71, 71, 71, ) : "232",
        ( 86, 86, 86, ) : "233",
        ( 100, 100, 100, ) : "234",
        ( 53, 53, 53, ) : "235",
        ( 14, 128, 94, ) : "236",
        ( 17, 155, 114, ) : "237",
        ( 20, 180, 133, ) : "238",
        ( 11, 95, 70, ) : "239",
        ( 153, 124, 104, ) : "240",
        ( 186, 150, 126, ) : "241",
        ( 216, 175, 147, ) : "242",
        ( 114, 93, 78, ) : "243",
        ( 90, 119, 106, ) : "244",
        ( 109, 144, 129, ) : "245",
        ( 127, 167, 150, ) : "246",
        ( 67, 89, 80, ) : "247",
        ( 1000, 1000, 1000, ) : "0"
    }

    couleur_proche = min(couleurs_minecraft.keys(), key=lambda c: sum(abs(a - b) for a, b in zip(c, (r, g, b))))
    #print(couleur_proche)
    # Récupération de l'ID du bloc Minecraft correspondant à la couleur trouvée
    bloc_minecraft_id = couleurs_minecraft.get(couleur_proche, "Inconnu")
    z = int(bloc_minecraft_id)
    return r , g , b , z 
def expand2square(pil_img, background_color):
        width, height = pil_img.size
        if width == height:
            return pil_img
        elif width > height:
            result = Image.new('RGB', (width, width), background_color)
            result.paste(pil_img, (0, (width - height) // 2))
            return result
        else:
            result = Image.new('RGB', (height, height), background_color)
            result.paste(pil_img, ((height - width) // 2, 0))
            return result
def convimg(im):
    im_thumb = expand2square(im, (1000, 1000, 1000))
    mywidth = 128
    wpercent = (mywidth/float(im_thumb.size[0]))
    hsize = int((float(im_thumb.size[1])*float(wpercent)))
    im_thumb = im_thumb.resize((mywidth,hsize), Image.LANCZOS)
    return im_thumb
def imgtodat(frame,exportname):
    lr = 999999
    lg = 999999
    lb = 999999
    lastid = 0 
    listeID = []
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    image = convimg(image)
    x , y = image.size
    im = image.load()
    for i in range(y):
        for j in range(x):
            r,g,b = im[j,i]
            colorvalue = abs( r - lr ) + abs( g - lg ) + abs( b - lb )
            if colorvalue- 15 <= colorvalue <= colorvalue + 15:
                listeID.append(lastid)
            else:
                lr ,lg , lb , lastid = determine_bloc_minecraft(r, g, b)
                listeID.append(lastid)
        
    byar = bytes(listeID)
    nbtfile = nbt.NBTFile("data.dat", 'dat')
    if "data" not in nbtfile:
        nbtfile["data"] = nbt.TAG_Compound()
    if "colors" not in nbtfile["data"]:
        nbtfile["data"]["colors"] = nbt.TAG_Byte_Array()
    nbtfile["data"]["colors"].value = byar
    nbtfile.write_file(exportname)
def process_video(video_path,outputnum,videoname):
    basenum = outputnum
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_skip = int(fps / 10)
    frame_count = 0
    print("Attendez la fin de la conversion pour fermer la fenêtre ...")
    while True:
        ret, frame = cap.read()
        tempnum = int(outputnum-basenum)
        filename = videoname +"/datapack/movie/data/fmm/functions/tree/"+ str(tempnum) + ".mcfunction"    
        if not ret:
            with open(os.path.join(filename), "w") as f:
                f.write("schedule function fmm:tree/0 1t")
            break
        if frame_count % frame_skip == 0:
            with open(os.path.join(filename), "w") as f:
                cmd =  "data modify entity @e[limit=1,tag=screen1] Item set value {id:\"minecraft:filled_map\",tag:{map:" + str(outputnum) + "},Count:1b}"
                f.write(cmd + "\n")
                f.write("schedule function fmm:tree/" + str(tempnum+1) + " 2t")
            
            outputname = videoname + "/data/map_" + str(outputnum) + ".dat"
            imgtodat(frame, outputname)  # Appel avec deux arguments
            outputnum += 1
        frame_count += 1
video_path = input("Chemain de la vidéo (path/to/video.mp4): ")
videoname = input("Nom de la vidéo (Nom que vous voulez pour le datapack): ") + 'Futiaxmovie'
num = int(input("Quelle numéro pour la première map (allez dans le dossier data de votre monde et chercher le fichier map_XX.dat le plus élevée et ajouter 1) ? "))
cmd = "Xcopy /E /I " + 'warning ' + videoname 
os.system(cmd) 
process_video(video_path,num,videoname)
print("Conversion terminée, ne fermez pas la fenêtre tout de suite, les instructions suivantes vont vous permettre de mettre le datapack dans votre monde")
sleep(5)
print("Vous obtener un dossier dedans il y a un dossier datapack avec un autre dossier movie qu'il faut mettre dans le dossier datapack de votre monde.")
sleep (5)
print("Enfin vous devez mettre les fichiers map_XX.dat dans le dossier data du dossier générer dans le dossier data de votre monde.")
sleep(5)
print("Une fois cela fait pouvez fermer la fenêtre.")
