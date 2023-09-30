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
    # Tableau de correspondance des couleurs
    couleurs_minecraft = {
        (0,0,0): "0",
        (127, 178, 56): "1",
        (247, 233, 163): "2",
        (199, 199, 199): "3",
        (255, 0, 0): "4",
        (160, 160, 255): "5",
        (167, 167, 167): "6",
        (0, 124, 0): "7",
        (255, 255, 255): "8",
        (164, 168, 184): "9",
        (151, 109, 77): "10",
        (112, 112, 112): "11",
        (64, 64, 255): "12",
        (143, 119, 72): "13",
        (255, 252, 245): "14",
        (216, 127, 51): "15",
        (178, 76, 216): "16",
        (102, 153, 216): "17",
        (229, 229, 51): "18",
        (127, 204, 25): "19",
        (242, 127, 165): "20",
        (76, 76, 76): "21",
        (153, 153, 153): "22",
        (76, 127, 153): "23",
        (127, 63, 178): "24",
        (51, 76, 178): "25",
        (102, 76, 51): "26",
        (102, 127, 51): "27",
        (153, 51, 51): "28",
        (25, 25, 25): "29",
        (250, 238, 77): "30",
        (92, 219, 213): "31",
        (74, 128, 255): "32",
        (0, 217, 58): "33",
        (129, 86, 49): "34",
        (112, 2, 0): "35",
        (209, 177, 161): "36",
        (159, 82, 36): "37",
        (149, 87, 108): "38",
        (112, 108, 138): "39",
        (103, 117, 53): "40",
        (186, 133, 36): "41",
        (57, 41, 35): "42",
        (160, 77, 78): "43",
        (87, 92, 92): "44",
        (135, 107, 98): "45",
        (76, 62, 92): "46",
        (122, 73, 88): "47",
        (76, 82, 42): "48",
        (76, 50, 35): "49",
        (37, 22, 16): "50",
        (142, 60, 46): "51",
        (148, 63, 97): "52",
        (189, 48, 49): "53",
        (22, 126, 134): "54",
        (92, 25, 29): "55",
        (86, 44, 62): "56",
        (58, 142, 140): "57",
        (100, 100, 100): "58",
        (20, 180, 133): "59",
        (216, 175, 147): "60",
        (127, 167, 150): "61"
        # ... (ajoutez les autres couleurs ici)
    }

    # Recherche de la couleur la plus proche dans le tableau
    couleur_proche = min(couleurs_minecraft.keys(), key=lambda c: sum(abs(a - b) for a, b in zip(c, (r, g, b))))
    #print(couleur_proche)
    # Récupération de l'ID du bloc Minecraft correspondant à la couleur trouvée
    bloc_minecraft_id = couleurs_minecraft.get(couleur_proche, "Inconnu")
    return bloc_minecraft_id
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
    im_thumb = expand2square(im, (0, 0, 0))
    ims = im_thumb.size
    #print(ims)
    mywidth = 128
    wpercent = (mywidth/float(im_thumb.size[0]))
    hsize = int((float(im_thumb.size[1])*float(wpercent)))
    im_thumb = im_thumb.resize((mywidth,hsize), Image.LANCZOS)
    return im_thumb
def colorcv(r , g , b):
    bloc_minecraft_id = determine_bloc_minecraft(r, g, b)
    # Faire quelque chose avec le bloc Minecraft obtenu
    #print("Pixel RGB:", (r, g, b), "Color Minecraft ID:", bloc_minecraft_id)
    chiffre = int(bloc_minecraft_id)*4+2
    return abs(chiffre)
def imgtodat(frame,exportname):
    liste = []
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    image = convimg(image)
    x , y = image.size
    #print("taille x : ",x,"taille y : ",y)
    im = image.load()
    for i in range(y):
        for j in range(x):
            r,g,b = im[j,i]
            liste += [colorcv(r,g,b)]
    #convert list to string
    byar = bytes(liste)
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
    if not cap.isOpened():
        print("Erreur : Impossible d'ouvrir la vidéo.")
        return
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
            print(outputname)
            imgtodat(frame, outputname)  # Appel avec deux arguments
            outputnum += 1
        frame_count += 1
video_path = input("Chemain de la vidéo (path/to/video.mp4): ")
videoname = input("Nom de la vidéo (Nom que vous voulez pour le datapack): ") + 'Futiaxmovie'
num = int(input("Quelle numéro pour la première map (allez dans le dossier data de votre monde et chercher le fichier map_XX.dat le plus élevée et ajouter 1) ? "))
cmd = "Xcopy /E /I " + '"ne pas toucher" ' + videoname 
os.system(cmd) 
process_video(video_path,num,videoname)
print("Conversion terminée, ne fermez pas la fenêtre tout de suite, les instructions suivantes vont vous permettre de mettre le datapack dans votre monde")
sleep(500)
print("Vous obtener un dossier dedans il y a un dossier datapack avec un autre dossier movie qu'il faut mettre dans le dossier datapack de votre monde.")
sleep (5000)
print("Enfin vous devez mettre les fichiers map_XX.dat dans le dossier data du dossier générer dans le dossier data de votre monde.")
sleep(5000)
print("Une fois cela fait pouvez fermer la fenêtre.")