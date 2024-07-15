import nasapy
import os
from datetime import datetime
import urllib.request
from IPython.display import Image,display,Audio
from gtts import gTTS
from dotenv import load_dotenv
from pandas import DataFrame

load_dotenv ()
d = datetime.today().strftime('%Y-%m-%d')
api_key = os.getenv('api_key')
nasa = nasapy.Nasa(key = api_key)

apod = nasa.picture_of_the_day(date=d, hd=True)
def fetchAPOD():
    if(apod["media_type"] == "image"):

    #POINT B:
    #Displaying hd images only:
        if("hdurl" in apod.keys()):
            #POINT C:
            #Saving name for image:
            title = d + "_" + apod["title"].replace(" ","_").replace(":","_") + ".jpg"

            #POINT D:
            #Path of the directory:
            image_dir = "./Astro_Images"

            #Checking if the directory already exists?
            dir_res = os.path.exists(image_dir)

            #If it doesn't exist then make a new directory:
            if (dir_res==False):
                os.makedirs(image_dir)

            #If it exist then print a statement:
            else:
                print("Directory already exists!\n")

            #POINT E:
            #Retrieving the image:
            urllib.request.urlretrieve(url = apod["hdurl"] , filename = os.path.join(image_dir,title))

            #POINT F:
            #Displaying information related to image:

            if("date" in apod.keys()):
                print("Date image released: ",apod["date"])
                print("\n")
            if("copyright" in apod.keys()):
                print("This image is owned by: ",apod["copyright"])
                print("\n")
            if("title" in apod.keys()):
                print("Title of the image: ",apod["title"])
                print("\n")
            if("explanation" in apod.keys()):
                print("Description for the image: ",apod["explanation"])
                print("\n")
            if("hdurl" in apod.keys()):
                print("URL for this image: ",apod["hdurl"])
                print("\n")

            #POINT G:
            #Displaying main image:
            display(Image(os.path.join(image_dir,title)))

            #Point H:
            #Text to Speech Conversion:
            #Take input from user:
            print("\n")
            choice = input("Press * to hear the audio explanation : ")

            if(choice=="*"):
                #Text to be converted:
                mytext = apod["explanation"]
                #mytext="Good Evening Pratik."

                #Creating an object:
                myobj = gTTS(text=mytext, lang="en", slow=False) 

                #Generating audio file name:
                audio_title = d + "_" + apod["title"] + ".mp3"

                #Save the converted file:
                myobj.save(os.path.join(image_dir,audio_title)) 

                #Name of sound file:
                sound_file = os.path.join(image_dir,audio_title)

                # Playing the converted file 
                display(Audio(sound_file, autoplay=True))

        else:
            print("Sorry, Image not available!")
            # Add your indented block of code here

def apod_by_date():
    d = input("Enter date in YYYY-MM-DD format : ")

#Get the image data:
apod = nasa.picture_of_the_day(date=d, hd=True)

#POINT A:
#Check the media type available:
if(apod["media_type"] == "image"):

    #POINT B:
    #Displaying hd images only:
    if("hdurl" in apod.keys()):

        #POINT C:
        #Saving name for image:
        title = d + "_" + apod["title"].replace(" ","_").replace(":","_") + ".jpg"

        #POINT D:
        #Path of the directory:
        image_dir = "Astro_Images"

        #Checking if the directory already exists?
        dir_res = os.path.exists(image_dir)

        #If it doesn't exist then make a new directory:
        if (dir_res==False):
            os.makedirs(image_dir)

        #If it exist then print a statement:
        else:
            print("Directory already exists!\n")

        #POINT E:
        #Retrieving the image:
        urllib.request.urlretrieve(url = apod["hdurl"] , filename = os.path.join(image_dir,title))

        #POINT F:
        #Displaying information related to image:

        if("date" in apod.keys()):
            print("Date image released: ",apod["date"])
            print("\n")
        if("copyright" in apod.keys()):
            print("This image is owned by: ",apod["copyright"])
            print("\n")
        if("title" in apod.keys()):
            print("Title of the image: ",apod["title"])
            print("\n")
        if("explanation" in apod.keys()):
            print("Description for the image: ",apod["explanation"])
            print("\n")
        if("hdurl" in apod.keys()):
            print("URL for this image: ",apod["hdurl"])
            print("\n")

        #POINT G:
        #Displaying main image:
        display(Image(os.path.join(image_dir,title)))

        #Point H:
        #Text to Speech Conversion:
        #Take input from user:
        print("\n")
        choice = input("Press * to hear the audio explanation : ")

        if(choice=="*"):
            #Text to be converted:
            mytext = apod["explanation"]
            #mytext="Good Evening Pratik."

            #Creating an object:
            myobj = gTTS(text=mytext, lang="en", slow=False) 

            #Generating audio file name:
            audio_title = d + "_" + apod["title"] + ".mp3"

            #Save the converted file:
            myobj.save(os.path.join(image_dir,audio_title)) 

            #Name of sound file:
            sound_file = os.path.join(image_dir,audio_title)

            # Playing the converted file 
            display(Audio(sound_file, autoplay=True))



#POINT I:
#If media type is not image:
else:
    print("Sorry, Image not available!")
    
if __name__ == "__main__":
    fetchAPOD()
