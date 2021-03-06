import glob, os #Allows to create or remove or add to directories
from PIL import Image, ImageFilter, ImageEnhance #Allows to use features of the pillow library in this code
import time

#Lists used throghout the code
photos = ["Banana", "Cat", "Chick", "Die", "Fish", "Mouse", "FunnyMeme", "Minecraft", "StolenJpeg", "Shrek"]
mod_List = ["(1) Make png", "(2) View Image Directories", "(3) Choose Thumbnail size", "(4) Rotate Image",  "(5) Make Black and White",  "(6) Blur Image", "(7) Contrast Image"]
image_Choice = ""
directory_List = ["d", "p", "b", "four", "six", "two", "w", "r", "c"]

#Looks for all possible locations an image could be
def look_For_Image_Through_All_Files():

    global modified
    global image_Choice

    try: #Looks through all possible folders until user choice (Which already is a valid file name) is found in them
        modified = Image.open(f"{image_Choice}.jpeg")
    except:
        try:
            modified = Image.open(f"BlackAndWhiteImages/{image_Choice}.")
        except:
            try:
                modified = Image.open(f"Blurred Images/{image_Choice}.")
            except:
                try:
                    modified = Image.open(f"P200 Images/{image_Choice}.")
                except:
                    try:
                        modified = Image.open(f"P400 Images/{image_Choice}.")
                    except:
                        try:
                            modified = Image.open(f"P600 Images/{image_Choice}.")
                        except:
                            try:
                                modified = Image.open(f"PngImages/{image_Choice}.")
                            except:
                                try:
                                    modified = Image.open(f"RotatedImages/{image_Choice}.")
                                except:
                                    try:
                                        modified = Image.open(f"ContrastImages/{image_Choice}.")
                                    except:
                                        pass
 
 #Prints out all images in all directories 
def show_All_Images_In_All_Directories():

    pngfiles = []

    for file in glob.glob("*.jpeg"): #Everything filename in the main directory is appended to the empty list above
        pngfiles.append(file)
        loading(1)
    print("Default Jpeg images are: ")
    loading(1)
    print(pngfiles)
    loading(1)

    try:#This checks to see if the directory exists. If not, there is an error and this is passed
        images = os.listdir("PngImages")
        print("Image in the PngImages Directory are: ")
        loading(1)
        print (images)
        loading(1)
    except:
        pass
    try:
        images = os.listdir("Blurred Images")
        print("Image in the Blurred Images Directory are: ")
        loading(1)
        print (images)
        loading(1)
    except:
        pass
    try:
        images = os.listdir("P400 Images")
        print("Image in the P400 Images Directory are: ")
        loading(1)
        print (images)
        loading(1)
    except:
        pass
    try:
        images = os.listdir("P600 Images")
        print("Image in the P600 Images Directory are: ")
        loading(1)
        print (images)
        loading(1)
    except:
        pass
    try:
        images = os.listdir("P200 Images")
        print("Image in the P200 Images Directory are: ")
        loading(1)
        print (images)
        loading(1)
    except:
        pass
    try:
        images = os.listdir("BlackAndWhiteImages")
        print("Image in the BlackAndWhiteImages Directory are: ")
        loading(1)
        print (images)
        loading(1)
    except:
        pass
    try:
        images = os.listdir("RotatedImages")
        print("Image in the RotatedImages Directory are: ")
        loading(1)
        print (images)
        loading(1)
    except:
        pass
    try:
        images = os.listdir("ContrastImages")
        print("Image in the Contrast Directory are: ")
        loading(1)
        print (images)
        loading(1)
    except:
        pass

def modify():

    global choice

    while True: #Asks user if they want to edit the shown file. Keeps looping until valid input is given.
        choice = input("I presume you would like to edit this beautiful image?(True/False): ")
        if choice.lower() == "true" or choice.lower() == "false":
            break
        else:
            print("Invalid Input")
    if choice.lower() == "false":
        loading(3) #Gives a 3 second pause
        print("Okay, have fun with your image")
    elif choice.lower() == "true":
        do_mod()

def blackWhite():

        global modified 
        global image_Choice
        try: #Ensures an error isn't given if this folder name already exists
            os.mkdir("BlackAndWhiteImages") #Creates a directory for BW images
        except:
            pass
            
        look_For_Image_Through_All_Files()

        trial = modified.convert("L") #Convert image to BW

        print("Here is the modified image")

        loading(2)

        trial.show()

        loading(1)
  
        try:
            trial.save('BlackAndWhiteImages/' + image_Choice + 'BW.jpeg') #Saves a BW version of the chosen image in the new folder, addeing "BW" to the end of the file name
            print(f"This image has been put in the BlackAndWhiteImages folder")

        except:
            print("You have already modified this image")

def rotate_Image():
        global modified
        global image_Choice
        try: #Ensures an error isn't given if this folder name already exists
            os.mkdir("RotatedImages") #Creates a directory for rotated images
        except:
            pass
        while True:
            try:
                turns = int(input("Input degrees to rotate image: "))
                loading(1)
                break
            except:
                print("Invalid input")   
        

        look_For_Image_Through_All_Files()
            
        trial = modified.rotate(turns) #Rotates the image based off how much the user want to rotate it

        print("Here is the modified image")

        loading(2)

        trial.show()
  
        try:
            modified.rotate(turns).save('RotatedImages/' + image_Choice + 'Turned.jpeg') #Saves a turned version of the chosen image in the new folder, addeing "Turned" to the end of the file name
            print(f"This image has been put in the RotatedImages folder")
            loading(1)

        except:
            print("You have already modified this image")
   
def mod_Size():

    global image_Choice

    global modified

    look_For_Image_Through_All_Files()

    p200 = (200, 200)
    p400 = (400, 400)
    p600 = (600, 600)

    while True:
        size_option = input("How big do you want the image to be? (200p, 400p, 600p): ")
        loading(1)
        if size_option == "200p" or size_option == "400p" or size_option == "600p":
            break
        else:
            print("Invalid Input")
    if size_option == "200p":

        try: #Ensures an error isn't given if this folder name already exists
            os.mkdir("P200 Images") #Creates a directory for 200p images
        except:
            pass

        modified.thumbnail(p200)
        print("Here is your 200p thumbnail Image: ")
        loading(3)
        modified.show()
        try:
            modified.save('P200 Images/' + image_Choice + 'P200.jpeg') #Saves a 400p version of the chosen image in the new folder, addeing "p200" to the end of the file name
            print(f"This image has been put in the P200 Images folder")

        except:
            print("You have already modified this image")
    elif size_option == "400p":

        try: #Ensures an error isn't given if this folder name already exists
            os.mkdir("P400 Images") #Creates a directory for 200p images
        except:
            pass

        modified.thumbnail(p400)


        print("Here is your 400p thumbnail Image: ")
        loading(3)


        modified.show()
        try:
            modified.save('P400 Images/' + image_Choice + 'P400.jpeg') #Saves a 400p version of the chosen image in the new folder, addeing "p400" to the end of the file name
            print(f"This image has been put in the P400 Images folder")
            loading(1)

        except:
            print("You have already modified this image")
    elif size_option == "600p":

        try: #Ensures an error isn't given if this folder name already exists
            os.mkdir("P600 Images") #Creates a directory for 600p images
        except:
            pass

        modified.thumbnail(p600)

        print("Here is your 600p thumbnail Image: ")
        loading(3)

        modified.show()
        try:
            modified.save('P600 Images/' + image_Choice + 'P600.jpeg') #Saves a 600p version of the chosen image in the new folder, addeing "p600" to the end of the file name
            print(f"This image has been put in the P600 Images folder")
            loading(1)

        except:
            print("You have already modified this image")
    else:
        print("Invalid Input")

def make_Png():

    global image_Choice

    global modified
    
    look_For_Image_Through_All_Files()

    try: #Ensures an error isn't given if this folder name already exists
        os.mkdir("PngImages") #Creates a directory for Png images
    except:
        pass

    fn, fext = os.path.splitext(f"{image_Choice}.jpeg") #Creates a Png formatting for the modified image
    try:
        modified.save("PngImages/{}.png".format(fn)) #Puts the Png formatted image into the PngImages Folder
    except:
        print("You have already made this image a png")

def blur_Image():

    global image_Choice

    global modified

    try:
        os.mkdir("Blurred Images") #Creates a directory for Blurred images
    except:
        pass

    while True:
        try:
            blur_Factor = float(input("By what factor would you like to blur?(Input number): "))
            break
        except:
            print("Invalid input")
 
    look_For_Image_Through_All_Files()

    blur_Modified = modified.filter(ImageFilter.GaussianBlur(blur_Factor)) #Puts blur on image
    blur_Modified.show()
    blur_Modified.save('Blurred Images/'+image_Choice+'Blurred.jpeg') #Saves the chosen image in the blurred images folder, adding Blurred.jpeg to its name.
    print("Saved in Blurred Images folder")

def contrast():

    global modified
    global image_Choice
    try: #Ensures an error isn't given if this folder name already exists
        os.mkdir("ContrastImages") #Creates a directory for rotated images
    except:
        pass

    look_For_Image_Through_All_Files()

    trial = ImageEnhance.Contrast(modified)

    print("Here is the modified image")

    loading(2)

    trial = trial.enhance(90)
    trial.show()

    try:
        trial.save('ContrastImages/' + image_Choice + 'Contrast.jpeg') #Saves a turned version of the chosen image in the new folder, addeing "Turned" to the end of the file name
        print(f"This image has been put in the ContrastImages folder")
        loading(1)

    except:
        print("You have already modified this image")

def choose_Image_In_Directory():
    #Based off user input, this function shows all images in a directory, and has the user select one until a valid input is given
    global directory_Choice
    global image_Choice
    global modified

    if directory_Choice.lower() == "d":
        defaultFiles = []
        for file in glob.glob("*.jpeg"):
            defaultFiles.append(file)
        print("Default Jpeg images are: ")
        print(defaultFiles)
        while True:
            image_Choice = input ("Choose an image (Case sentistive. Add extensions): ")
            if image_Choice in defaultFiles:
                modified = Image.open(f"{image_Choice}")
                modified.show()
                do_mod()
                break
            else:
                print("Invalid Input")   

    elif directory_Choice.lower() == "p":
        Files = os.listdir("PngImages")
        print("Images in the PngImages Directory are: ")
        print (Files)
        print("")
        while True:
            image_Choice = input ("Choose an image (Case sentistive. Add extensions): ")
            if image_Choice in Files:
                modified = Image.open(f"PngImages/{image_Choice}")
                modified.show()
                do_mod()
                break
            else:
                print("Invalid Input")

    elif directory_Choice.lower() == "b":
        Files = os.listdir("Blurred Images")
        print("Images in the Blurred Images Directory are: ")
        print (Files)
        print("")
        while True:
            image_Choice = input ("Choose an image (Case sentistive. Add extensions): ")
            if image_Choice in Files:
                modified = Image.open(f"Blurred Images/{image_Choice}")
                modified.show()
                do_mod()
                break
            else:
                print("Invalid Input")

    elif directory_Choice.lower() == "two":
        Files = os.listdir("P200 Images")
        print("Images in the P200 Images Directory are: ")
        print (Files)
        print("")
        while True:
            image_Choice = input ("Choose an image (Case sentistive. Add extensions): ")
            if image_Choice in Files:
                modified = Image.open(f"P200 Images/{image_Choice}")
                modified.show()
                do_mod()
                break
            else:
                print("Invalid Input")

    elif directory_Choice.lower() == "four":
        Files = os.listdir("P400 Images")
        print("Images in the P400 Images Directory are: ")
        print (Files)
        print("")
        while True:
            image_Choice = input ("Choose an image (Case sentistive. Add extensions): ")
            if image_Choice in Files:
                modified = Image.open(f"P400 Images/{image_Choice}")
                modified.show()
                do_mod()
                break
            else:
                print("Invalid Input")

    elif directory_Choice.lower() == "six":
        Files = os.listdir("P600 Images")
        print("Images in the P600 Images Directory are: ")
        print (Files)
        print("")
        while True:
            image_Choice = input ("Choose an image (Case sentistive. Add extensions): ")
            if image_Choice in Files:
                modified = Image.open(f"P600 Images/{image_Choice}")
                modified.show()
                do_mod()
                break
            else:
                print("Invalid Input")

    elif directory_Choice.lower() == "w":
        Files = os.listdir("BlackAndWhiteImages")
        print("Images in the BlackAndWhiteImages Directory are: ")
        print (Files)
        print("")
        while True:
            image_Choice = input ("Choose an image (Case sentistive. Add extensions): ")
            if image_Choice in Files:
                modified = Image.open(f"BlackAndWhiteImages/{image_Choice}")
                modified.show()
                do_mod()
                break
            else:
                print("Invalid Input")

    elif directory_Choice.lower() == "r":
        Files = os.listdir("RotatedImages")
        print("Images in the RotatedImages Directory are: ")
        print (Files)
        print("")
        while True:
            image_Choice = input ("Choose an image (Case sentistive. Add extensions): ")
            if image_Choice in Files:
                modified = Image.open(f"RotatedImages/{image_Choice}")
                modified.show()
                do_mod()
                break
            else:
                print("Invalid Input")   

    elif directory_Choice.lower() == "c":
        Files = os.listdir("ContrastImages")
        print("Images in the ContrastImages Directory are: ")
        print (Files)
        print("")
        while True:
            image_Choice = input ("Choose an image (Case sentistive. Add extensions): ")
            if image_Choice in Files:
                modified = Image.open(f"ContrastImages/{image_Choice}")
                modified.show()
                do_mod()
                break
            else:
                print("Invalid Input")            
        loading(1)
    
def loading(seconds): #This function puts a time delay between operations so that the user can follow whats going on
    for i in range(seconds):
        print("")
        time.sleep(0.5)

def find_Image_To_Modify():
    #Tries to list file names from all possible folders. If folder doesn't exist Aka image doesnt exist there is an error which is passed
    global directory_List
    global directory_Choice

    print("Here are all the folder in which your images exist:  ")

    loading(5)

    pngfiles = []
    for file in glob.glob("*.jpeg"):
        pngfiles.append(file)
    print("Default Jpeg images folder(D): ")
    loading(1)
    try:
        images = os.listdir("PngImages")
        print("Image in the PngImages Directory(P): ")
        loading(1)
    except:
        pass
    try:
        images = os.listdir("Blurred Images")
        print("Image in the Blurred Images Directory(B): ")
        loading(1)
    except:
        pass
    try:
        images = os.listdir("P400 Images")
        print("Image in the P400 Images Directory(FOUR): ")
        loading(1)
    except:
        pass
    try:
        images = os.listdir("P600 Images")
        print("Image in the P600 Images Directory(SIX): ")
        loading(1)
    except:
        pass
    try:
        images = os.listdir("P200 Images")
        print("Image in the P200 Images Directory(TWO)): ")
        loading(1)
    except:
        pass
    try:
        images = os.listdir("BlackAndWhiteImages")
        print("Image in the BlackAndWhiteImages Directory(W): ")
        loading(1)
    except:
        pass
    try:
        images = os.listdir("RotatedImages")
        print("Image in the RotatedImages Directory(R): ")
        loading(1)
    except:
        pass
    try:
        images = os.listdir("ContrastImages")
        print("Image in the ContrastImages Directory(C): ")
        loading(1)
    except:
        pass

    while True:
        directory_Choice = input("Which of the following directories has your desired image?")
        if directory_Choice.lower() in directory_List:
            choose_Image_In_Directory()
            break
        else:
            print("Invalid Input")

def main():
    global choice
    global photos
    global image_Choice
    
    while True:
        print(f"The images you can view/manipulate are: ")
        for defaultImg in photos: #Shows all default images
            loading(1)
            print(defaultImg)

        loading(3)
        image_Choice = input("What Image do you want to manipulate? (Case Sensitive): ")
        #Opens the image user wants to manipulate
        if image_Choice in photos:
            chosen_Image = Image.open(f"{image_Choice}.jpeg")
            loading(2)
            print(f"Here is the {image_Choice} image:")
            loading(3)
            chosen_Image.show()
            modify()
            break
        else:
            print("Invalid Input, Try again")
    
    if choice.lower() == "q": #Only runs if user wants to quit program
        return 0
    loading(3)
    print("The images you can now view/manipulate are the following: ")
    loading(3)

    show_All_Images_In_All_Directories()  

    while True:
        if_mod = input("Would you like to modify/view any existing images?(Y/N): ")
        if if_mod.lower() == "y" or if_mod.lower() == "n":
            if if_mod.lower() == "n":
                print("That's too bad. Have a nice day.")
                break
            else:
                loading(3)
                find_Image_To_Modify() #If user wants to edit another image, this function plays
        else:
            print("******Invalid Input*******")
       
def do_mod():
    #Shows possible image modifications and asks user if they want to mod their image
    global choice
    global image_Choice
    global mod_List
    loading(3)
    print(f"Here are possible Image Modifications: ")
    for mod in mod_List:
        loading(1)
        print(mod)
    choice = 9
    while True:
        loading(1)
        choice = input("What would you like to do with the image?(q to go back): ")
        if choice == "q":
            print("That's too bad. Bye.")
            break
        elif choice == "1":
            loading(1)
            make_Png()
            break
        elif choice == "2": 
            break #Once this function ends all possible options are shown anyways. 
        elif choice == "3":
            loading(1)
            mod_Size()
            break
        elif choice == "4":
            loading(1)
            rotate_Image()
            break
        elif choice == "5":
            loading(1)
            blackWhite()
            break
        elif choice == "6":
            loading(1)
            blur_Image()
            break
        elif choice == "7":
            loading(1)
            contrast()
            break
        else:
            loading(1)
            print("Invalid Input: Try Again")

main()

                
