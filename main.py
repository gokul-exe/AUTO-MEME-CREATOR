# Auto Meme Creator
# Developed by [Gokul]
# Version: 1.1



from singleimage import singleproc
from doubleimage import doublproc
from splitvideo  import crop_and_split_video
from rename import rename_files
from video  import vdeoproc,about

def main():
    opt = welcome()
    if opt == "1":                
        singleproc()
    elif opt =="2":
        doublproc()
    elif opt=="3":
        crop_and_split_video()
    elif opt=="4":
        about()
        vdeoproc()
    else: print("WRONG CHOICE RUN AGAIN  ")


def welcome():
    print("""███    ███ ███████ ███    ███ ███████      ██████  ███████ ███    ██ ███████ ██████   █████  ████████  ██████  ██████  
████  ████ ██      ████  ████ ██          ██       ██      ████   ██ ██      ██   ██ ██   ██    ██    ██    ██ ██   ██ 
██ ████ ██ █████   ██ ████ ██ █████       ██   ███ █████   ██ ██  ██ █████   ██████  ███████    ██    ██    ██ ██████  
██  ██  ██ ██      ██  ██  ██ ██          ██    ██ ██      ██  ██ ██ ██      ██   ██ ██   ██    ██    ██    ██ ██   ██ 
██      ██ ███████ ██      ██ ███████      ██████  ███████ ██   ████ ███████ ██   ██ ██   ██    ██     ██████  ██   ██ 
                                                                                                                       
                                                                                                                       """)
    rename=input("IF YOU WANT TO RENAME THE MEMES FOLDER FILES? Y/N :")
    if rename.lower()=='y':
        try :
            rename_files()
        except:
            print("ERROR RENAMING FILES")
            quit()

    option = input("""ENTER THE OPTION: 
                   TYPE-1: SINGLE IMAGE MEME
                   TYPE-2: DOUBLE IMAGE MEME
                   TYPE-3: VIDEO SPLITTER 
                   TYPE-4: IMAGE AND VIDEO COLLAGE  
                   ENTER YOUR CHOICE :  """)
    return option



if __name__ == "__main__":
    main()
