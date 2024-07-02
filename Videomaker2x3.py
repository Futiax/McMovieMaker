import os
import importlib.util
import random
#def is_library_installed(library_name):
#    spec = importlib.util.find_spec(library_name)
#    if spec==None:
#        return False
#    else:
#        return True
#if not is_library_installed('numpy') :
#    os.system("pip install numpy")
#if not is_library_installed('nbt'):
#    os.system("pip install nbt")
#if not is_library_installed('Pillow'):
#    os.system("pip install Pillow")
#if not is_library_installed('opencv-python'):
#    os.system("pip install opencv-python")
#if not is_library_installed('moviepy'):
#    os.system("pip install moviepy")
from moviepy.editor import VideoFileClip
from time import *
from PIL import Image
from nbt import nbt
import numpy as np
import cv2
# Tableau de correspondance des couleurs
cmc = {( 90, 126, 40, ) : "4",( 109, 153, 48, ) : "5",( 127, 178, 56, ) : "6",( 67, 94, 30, ) : "7",( 175, 165, 116, ) : "8",( 212, 200, 140, ) : "9",( 247, 233, 163, ) :  "10",( 131, 123, 86, ) :  "11",( 141, 141, 141, ) :  "12",( 171, 171, 171, ) :  "13",( 199, 199, 199, ) :  "14",( 105, 105, 105, ) :  "15",( 181, 0, 0, ) :  "16",( 219, 0, 0, ) :  "17",( 255, 0, 0, ) :  "18",( 135, 0, 0, ) :  "19",( 114, 114, 181, ) :  "20",( 138, 138, 219, ) :  "21",( 160, 160, 255, ) :  "22",( 85, 85, 135, ) :  "23",( 119, 119, 119, ) :  "24",( 144, 144, 144, ) :  "25",( 167, 167, 167, ) :  "26",( 89, 89, 89, ) :  "27",( 0, 88, 0, ) :  "28",( 0, 107, 0, ) :  "29",( 0, 124, 0, ) :  "30",( 0, 66, 0, ) :  "31",( 181, 181, 181, ) :  "32",( 219, 219, 219, ) :  "33",( 135, 135, 135, ) :  "35",( 116, 119, 131, ) :  "36",( 141, 144, 158, ) :  "37",( 164, 168, 184, ) :  "38",( 87, 89, 98, ) :  "39",( 107, 77, 55, ) :  "40",( 130, 94, 66, ) :  "41",( 151, 109, 77, ) :  "42",( 80, 58, 41, ) :  "43",( 80, 80, 80, ) :  "44",( 96, 96, 96, ) :  "45",( 112, 112, 112, ) :  "46",( 59, 59, 59, ) :  "47",( 45, 45, 181, ) :  "48",( 55, 55, 219, ) :  "49",( 64, 64, 255, ) :  "50",( 34, 34, 135, ) :  "51",( 102, 84, 51, ) :  "52",( 123, 102, 62, ) :  "53",( 143, 119, 72, ) :  "54",( 76, 63, 38, ) :  "55",( 181, 179, 174, ) :  "56",( 219, 217, 211, ) :  "57",( 255, 252, 245, ) :  "58",( 135, 134, 130, ) :  "59",( 153, 90, 36, ) :  "60",( 186, 109, 44, ) :  "61",( 216, 127, 51, ) :  "62",( 114, 67, 27, ) :  "63",( 126, 54, 153, ) :  "64",( 153, 65, 186, ) :  "65",( 178, 76, 216, ) :  "66",( 94, 40, 114, ) :  "67",( 72, 109, 153, ) :  "68",( 88, 132, 186, ) :  "69",( 102, 153, 216, ) :  "70",( 54, 81, 114, ) :  "71",( 163, 163, 36, ) :  "72",( 197, 197, 44, ) :  "73",( 229, 229, 51, ) :  "74",( 121, 121, 27, ) :  "75",( 90, 145, 18, ) :  "76",( 109, 175, 22, ) :  "77",( 127, 204, 25, ) :  "78",( 67, 108, 13, ) :  "79",( 172, 90, 117, ) :  "80",( 208, 109, 142, ) :  "81",( 242, 127, 165, ) :  "82",( 128, 67, 87, ) :  "83",( 54, 54, 54, ) :  "84",( 65, 65, 65, ) :  "85",( 76, 76, 76, ) :  "86",( 40, 40, 40, ) :  "87",( 109, 109, 109, ) :  "88",( 132, 132, 132, ) :  "89",( 153, 153, 153, ) :  "90",( 81, 81, 81, ) :  "91",( 54, 90, 109, ) :  "92",( 65, 109, 132, ) :  "93",( 76, 127, 153, ) :  "94",( 40, 67, 81, ) :  "95",( 90, 45, 126, ) :  "96",( 109, 54, 153, ) :  "97",( 127, 63, 178, ) :  "98",( 67, 33, 94, ) :  "99",( 36, 54, 126, ) : "100",( 44, 65, 153, ) : "101",( 51, 76, 178, ) : "102",( 27, 40, 94, ) : "103",( 72, 54, 36, ) : "104",( 88, 65, 44, ) : "105",( 102, 76, 51, ) : "106",( 54, 40, 27, ) : "107",( 72, 90, 36, ) : "108",( 88, 109, 44, ) : "109",( 102, 127, 51, ) : "110",( 54, 67, 27, ) : "111",( 109, 36, 36, ) : "112",( 132, 44, 44, ) : "113",( 153, 51, 51, ) : "114",( 81, 27, 27, ) : "115",( 18, 18, 18, ) : "116",( 22, 22, 22, ) : "117",( 25, 25, 25, ) : "118",( 13, 13, 13, ) : "119",( 178, 169, 55, ) : "120",( 215, 205, 66, ) : "121",( 250, 238, 77, ) : "122",( 132, 126, 41, ) : "123",( 65, 155, 151, ) : "124",( 79, 188, 183, ) : "125",( 92, 219, 213, ) : "126",( 49, 116, 113, ) : "127",( 53, 91, 181, ) : "128",( 64, 110, 219, ) : "129",( 74, 128, 255, ) : "130",( 39, 68, 135, ) : "131",( 0, 154, 41, ) : "132",( 0, 187, 50, ) : "133",( 0, 217, 58, ) : "134",( 0, 115, 31, ) : "135",( 92, 61, 35, ) : "136",( 111, 74, 42, ) : "137",( 129, 86, 49, ) : "138",( 68, 46, 26, ) : "139",( 80, 1, 0, ) : "140",( 96, 2, 0, ) : "141",( 112, 2, 0, ) : "142",( 59, 1, 0, ) : "143",( 148, 126, 114, ) : "144",( 180, 152, 138, ) : "145",( 209, 177, 161, ) : "146",( 111, 94, 85, ) : "147",( 113, 58, 26, ) : "148",( 137, 71, 31, ) : "149",( 159, 82, 36, ) : "150",( 84, 43, 19, ) : "151",( 106, 62, 77, ) : "152",( 128, 75, 93, ) : "153",( 149, 87, 108, ) : "154",( 79, 46, 57, ) : "155",( 80, 77, 98, ) : "156",( 96, 93, 119, ) : "157",( 112, 108, 138, ) : "158",( 59, 57, 73, ) : "159",( 73, 83, 38, ) : "160",( 89, 101, 46, ) : "161",( 103, 117, 53, ) : "162",( 55, 62, 28, ) : "163",( 132, 94, 26, ) : "164",( 160, 114, 31, ) : "165",( 186, 133, 36, ) : "166",( 99, 70, 19, ) : "167",( 40, 29, 25, ) : "168",( 49, 35, 30, ) : "169",( 57, 41, 35, ) : "170",( 30, 22, 19, ) : "171",( 114, 55, 55, ) : "172",( 138, 66, 67, ) : "173",( 160, 77, 78, ) : "174",( 85, 41, 41, ) : "175",( 62, 65, 65, ) : "176",( 75, 79, 79, ) : "177",( 87, 92, 92, ) : "178",( 46, 49, 49, ) : "179",( 96, 76, 70, ) : "180",( 116, 92, 84, ) : "181",( 135, 107, 98, ) : "182",( 72, 57, 52, ) : "183",( 54, 44, 65, ) : "184",( 65, 53, 79, ) : "185",( 76, 62, 92, ) : "186",( 40, 33, 49, ) : "187",( 87, 52, 62, ) : "188",( 105, 63, 76, ) : "189",( 122, 73, 88, ) : "190",( 65, 39, 47, ) : "191",( 54, 58, 30, ) : "192",( 65, 71, 36, ) : "193",( 76, 82, 42, ) : "194",( 40, 43, 22, ) : "195",( 54, 36, 25, ) : "196",( 65, 43, 30, ) : "197",( 76, 50, 35, ) : "198",( 40, 26, 19, ) : "199",( 26, 16, 11, ) : "200",( 32, 19, 14, ) : "201",( 37, 22, 16, ) : "202",( 20, 12, 8, ) : "203",( 101, 43, 33, ) : "204",( 122, 52, 40, ) : "205",( 142, 60, 46, ) : "206",( 75, 32, 24, ) : "207",( 105, 45, 69, ) : "208",( 127, 54, 83, ) : "209",( 148, 63, 97, ) : "210",( 78, 33, 51, ) : "211",( 134, 34, 35, ) : "212",( 163, 41, 42, ) : "213",( 189, 48, 49, ) : "214",( 100, 25, 26, ) : "215",( 16, 89, 95, ) : "216",( 19, 108, 115, ) : "217",( 22, 126, 134, ) : "218",( 12, 67, 71, ) : "219",( 65, 18, 21, ) : "220",( 79, 22, 25, ) : "221",( 92, 25, 29, ) : "222",( 49, 13, 15, ) : "223",( 61, 31, 44, ) : "224",( 74, 38, 53, ) : "225",( 86, 44, 62, ) : "226",( 46, 23, 33, ) : "227",( 41, 101, 99, ) : "228",( 50, 122, 120, ) : "229",( 58, 142, 140, ) : "230",( 31, 75, 74, ) : "231",( 71, 71, 71, ) : "232",( 86, 86, 86, ) : "233",( 100, 100, 100, ) : "234",( 53, 53, 53, ) : "235",( 14, 128, 94, ) : "236",( 17, 155, 114, ) : "237",( 20, 180, 133, ) : "238",( 11, 95, 70, ) : "239",( 153, 124, 104, ) : "240",( 186, 150, 126, ) : "241",( 216, 175, 147, ) : "242",( 114, 93, 78, ) : "243",( 90, 119, 106, ) : "244",( 109, 144, 129, ) : "245",( 127, 167, 150, ) : "246",( 67, 89, 80, ) : "247"}
#Palette
palette = [90,126,40,109,153,48,127,178,56,67,94,30,175,165,116,212,200,140,247,233,163,131,123,86,141,141,141,171,171,171,199,199,199,105,105,105,181,0,0,219,0,0,255,0,0,135,0,0,114,114,181,138,138,219,160,160,255,85,85,135,119,119,119,144,144,144,167,167,167,89,89,89,0,88,0,0,107,0,0,124,0,0,66,0,181,181,181,219,219,219,135,135,135,116,119,131,141,144,158,164,168,184,87,89,98,107,77,55,130,94,66,151,109,77,80,58,41,80,80,80,96,96,96,112,112,112,59,59,59,45,45,181,55,55,219,64,64,255,34,34,135,102,84,51,123,102,62,143,119,72,76,63,38,181,179,174,219,217,211,255,252,245,135,134,130,153,90,36,186,109,44,216,127,51,114,67,27,126,54,153,153,65,186,178,76,216,94,40,114,72,109,153,88,132,186,102,153,216,54,81,114,163,163,36,197,197,44,229,229,51,121,121,27,90,145,18,109,175,22,127,204,25,67,108,13,172,90,117,208,109,142,242,127,165,128,67,87,54,54,54,65,65,65,76,76,76,40,40,40,109,109,109,132,132,132,153,153,153,81,81,81,54,90,109,65,109,132,76,127,153,40,67,81,90,45,126,109,54,153,127,63,178,67,33,94,36,54,126,44,65,153,51,76,178,27,40,94,72,54,36,88,65,44,102,76,51,54,40,27,72,90,36,88,109,44,102,127,51,54,67,27,109,36,36,132,44,44,153,51,51,81,27,27,18,18,18,22,22,22,25,25,25,13,13,13,178,169,55,215,205,66,250,238,77,132,126,41,65,155,151,79,188,183,92,219,213,49,116,113,53,91,181,64,110,219,74,128,255,39,68,135,0,154,41,0,187,50,0,217,58,0,115,31,92,61,35,111,74,42,129,86,49,68,46,26,80,1,0,96,2,0,112,2,0,59,1,0,148,126,114,180,152,138,209,177,161,111,94,85,113,58,26,137,71,31,159,82,36,84,43,19,106,62,77,128,75,93,149,87,108,79,46,57,80,77,98,96,93,119,112,108,138,59,57,73,73,83,38,89,101,46,103,117,53,55,62,28,132,94,26,160,114,31,186,133,36,99,70,19,40,29,25,49,35,30,57,41,35,30,22,19,114,55,55,138,66,67,160,77,78,85,41,41,62,65,65,75,79,79,87,92,92,46,49,49,96,76,70,116,92,84,135,107,98,72,57,52,54,44,65,65,53,79,76,62,92,40,33,49,87,52,62,105,63,76,122,73,88,65,39,47,54,58,30,65,71,36,76,82,42,40,43,22,54,36,25,65,43,30,76,50,35,40,26,19,26,16,11,32,19,14,37,22,16,20,12,8,101,43,33,122,52,40,142,60,46,75,32,24,105,45,69,127,54,83,148,63,97,78,33,51,134,34,35,163,41,42,189,48,49,100,25,26,16,89,95,19,108,115,22,126,134,12,67,71,65,18,21,79,22,25,92,25,29,49,13,15,61,31,44,74,38,53,86,44,62,46,23,33,41,101,99,50,122,120,58,142,140,31,75,74,71,71,71,86,86,86,100,100,100,53,53,53,14,128,94,17,155,114,20,180,133,11,95,70,153,124,104,186,150,126,216,175,147,114,93,78,90,119,106,109,144,129,127,167,150,67,89,80]

def reformatframe(frame, bg_color,target_width, target_height):
    target_width = target_width*128                                                             # Largeur souhaitée
    target_height = target_height*128                                                           # Hauteur souhaitée

    height, width, _ = frame.shape                                                              # Récupérer les dimensions de l'image d'origine
    scale_width = target_width / width                                                          # Calculer le facteur d'échelle pour la largeur et la hauteur
    scale_height = target_height / height       
    scale = min(scale_width, scale_height)                                                      # Utiliser le facteur d'échelle le plus petit pour éviter la déformation
    new_width = int(width * scale)                                                              # Calculer les nouvelles dimensions
    new_height = int(height * scale)        
    resized_frame = cv2.resize(frame, (new_width, new_height))                                  # Redimensionner l'image sans déformation
    result = np.full((target_height, target_width, 3), (bg_color), dtype=np.uint8)              # Créer une image vide avec la couleur d'arrière-plan souhaitée
    x_offset = (target_width - new_width) // 2                                                  # Calculer la position pour centrer l'image redimensionnée dans l'image video
    y_offset = (target_height - new_height) // 2
    result[y_offset:y_offset + new_height, x_offset:x_offset + new_width] = resized_frame       # Placer l'image redimensionnée dans l'image video
    pil_image = Image.fromarray(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))                        # Appliquer la palette à l'image 
    palette_image = Image.new('P', (1, 1))
    palette_image.putpalette(palette + [255] * (768 - len(palette)))
    quantized_image = pil_image.quantize(palette=palette_image, dither=Image.NONE)
    frameout = cv2.cvtColor(np.array(quantized_image.convert('RGB')), cv2.COLOR_RGB2BGR)
    return frameout

def imgtodat(frame,outputnum, height ,width):
    nbrmap = height*width
    for i in range(0,nbrmap):
        listeID = []
        ligne = int(i/width)
        colonne = i%width
        pixeldl = ligne*128
        pixeldc = colonne*128
        for y in range(pixeldl,pixeldl+128):
            for x in range(pixeldc,pixeldc+128):
                r,g,b = frame[y,x]                                                              # Cas noire et blanc
                if r == 0 and g == 0 and b == 0:
                    listeID.append(119)
                elif r == 255 and g == 255 and b == 255:
                    listeID.append(34)
                else:
                    lastid = cmc[(b,g,r)]                                                       #Autres Couleurs
                    listeID.append(int(lastid))
        outputname = videoname + "/data/map_" + str(outputnum+i-1-height*width) + ".dat"
        byar = bytes(listeID)
        nbtfile = nbt.NBTFile("map_0.dat", 'dat')
        if "data" not in nbtfile:
            nbtfile["data"] = nbt.TAG_Compound()
        if "colors" not in nbtfile["data"]:
            nbtfile["data"]["colors"] = nbt.TAG_Byte_Array()
        nbtfile["data"]["colors"].value = byar
        nbtfile.write_file(outputname)
def process_video(video_path , num , videoname , width , height, framerate):
    basenum = num
    capture = cv2.VideoCapture(video_path)
    framenbr = capture.get(cv2.CAP_PROP_FPS)
    frame_skip = framenbr/framerate-1
    print("Attendez la fin de la conversion pour fermer la fenêtre ...")
    totalframecount=0
    global frame_count
    while (capture.isOpened()):
        totalframecount+=1
        readability, frame = capture.read()
        tempnum = int((num-basenum)/(width*height))
        filename = videoname +"/datapack/movie/data/fmm/functions/tree/"+ str(tempnum) + ".mcfunction"    
        if not readability:
            with open(os.path.join(filename), "w") as f:
                f.write("schedule function fmm:tree/0 1t")
            with open(os.path.join(videoname +"/datapack/movie/data/fmm/functions/load.mcfunction"), "w") as f:
                for h in range(1,width*height+1):
                    texte =str("give @p item_frame{display:{Name:'"+'{"text":"Screen {h}","color":"gray","bold":true}'+"'"+'},EntityTag:{Tags:["screen{h}"]}'+'} 1\n')
                    f.write(texte.replace("{h}",str(h)))
                tellraw = str('tellraw @a ["",{"text":"Run\\"","color":"red"},{"text":"/function ffm:tree/1","color":"yellow"},{"text":"\\" to start video after place item frame.","color":"red"}]')
                f.write(tellraw)
            break
        if int(frame_count % frame_skip) == 0:
            with open(os.path.join(filename), "w") as f:
                for i in range(1,width*height+1):
                    if version :
                        cmd =  'data modify entity @e[limit=1,tag=screen' + str(i) + '] Item set value {components:{"minecraft:map_id":'+str(num-1)+'},count:1,id:"minecraft:filled_map"}'
                    else:
                        cmd =  'data modify entity @e[limit=1,tag=screen' + str(i) + '] Item set value {id:"minecraft:filled_map",tag:{map:'+str(num-1)+'},Count:1b}'
                    f.write(cmd + "\n")
                    num += 1
                if framerate == 5:
                    f.write("schedule function fmm:tree/" + str(tempnum+1) + " 4t")
                else:
                    f.write("schedule function fmm:tree/" + str(tempnum+1) + " 2t")
                
            newframe = reformatframe(frame, (0, 0, 0),width,height )
            imgtodat(newframe, num, height, width)  # Appel avec deux arguments
        frame_count += 1
        print(round(totalframecount/capture.get(cv2.CAP_PROP_FRAME_COUNT)*100,2),'%')

frame_count = 0
video_path = input("Video path (path/to/video.mp4): ")
videoname = input("Video name (the name you want for the datapack): ") #+ 'Futiaxmovie'
width = int(input("Video width (in number of maps) (not too high):  "))
height = int(input("Video height (in number of maps) (not too high): "))
num = int(input("What's the number of the first map (go to your world's data folder and look for the highest map_XX.dat file and add 1)? "))
version = bool(input("Are you playing a version greater than or equal to 1.20.6 ? "))
framerate = 0
while framerate != 5 and framerate != 10:
    framerate = int(input("Frame rate (5 or 10) (the higher the value, the faster the video, but the longer the conversion time): "))
#get time when programm starts
time1 =int(time())
cmd = "Xcopy /E /I " + 'warning ' + videoname 
os.system(cmd) 
clip = VideoFileClip(video_path)
audio_clip = clip.audio
audio_clip.write_audiofile(videoname + "/texture_pack/sound/assets/minecraft/sounds/records/wait.ogg")
process_video(video_path , num , videoname , width , height, framerate)
capture = cv2.VideoCapture(video_path)
duration = capture.get(cv2.CAP_PROP_POS_MSEC)
temps = int(time())-time1
print ("Conversion to " + str((temps//60)) + " minutes and " + str(temps%60) + " seconds for a total of " + str(frame_count) + " maps,or one map every " + str(temps/frame_count) + " secondes.")
print("Conversion complete, don't close the window just yet, the following instructions will allow you to put the datapack into your world")
sleep(2)
print("You'll get a datapack folder with the movie folder, which you'll need to put in your world's datapack folder.")
sleep (10)
print("A data folder with mapxx.dat files to add to your world's data folder.")
sleep(10)
print("And finally, a texture pack that changes the disc wait to the audio of your video.")
sleep(5)
print("Once you've done that, close the window.")
