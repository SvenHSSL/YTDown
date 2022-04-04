import urllib.request
import re
from pytube import YouTube 
import time



    
i=0
videoName = input("Name of Vids pls : ")
 
def findURL (videoName) :
    global i
    webUrl = urllib.request.urlopen('https://www.youtube.com/results?search_query='+videoName)
    videoListe= re.findall (r"watch\?v=(\S{11})", webUrl.read().decode())



    link = "https://www.youtube.com/watch?v="+videoListe[i]
    yt = YouTube(link)
     
     
    print("Voulez vous download cette vidéo:"+ yt.title)
    print("taper oui pour la download")
    print("taper non pour stopper le téléchargement")
    print("taper suivante pour télécharger la vidéo suivante")
    choix = input("?")
    if ( choix  == "oui"):
        return yt

    elif ( choix== "non"):
        print("annulation")
        if (input("Souhaitez vous quittez l'application? ") == "oui"):
            quit()
        else:
            findURL(videoName)

    elif ( choix == "suivante"):
        i=i+1


    findURL(videoName)


def Download (yt) : 

    audio = yt.streams.filter(only_audio=True)
    audio[0].download()
    


Download(findURL(videoName))
time.sleep(5)
print("Download sucessfull")