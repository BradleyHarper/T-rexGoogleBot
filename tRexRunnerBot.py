 #http://www.trex-game.skipser.com/
 #thats the game you use with this program.
 #the variables in the class "coordinates" only work with 1920x1080 display
 #SEE IMAGE FILE FOR CORRECT SCREEN ORIENTATION, as this program clicks on a certain pixel coordinate on the screen


 from PIL import ImageOps  #import imageops from pillow
from PIL import ImageGrab  #import imagegrab from pillow
import pyautogui #import pyautogui
import time #import time used for delays in this program
from numpy import *  #import * (multiplication)


class coordinates():   #holds our coordinate variables
    replayButton = (480,460) #this is where the replay button is located on the screen
    dinosaur = (208,471)  #this is the tip of the nose coordinate on the dinosaur (top left part of box, you'll see more about this in imageGrab)
    #treeSensor = (229,484) ## random coordinate where i wanted the box to detect the trees/cactus in the game. dont focus on it, theres a reason why it's hashed out

def restartGame():  #function that will be called when we want our game to initialize
    pyautogui.click(coordinates.replayButton) # pyautogui clicks wherever replayButton coordinates are specified

def pressSpace(): # function that will specify how we want our space bar to be actuated
    pyautogui.keyDown('space') #press space(spacebar) down
    time.sleep(0.02) #wait a fraction of a millisecond
    pyautogui.keyUp('space') #now release the key
    print("Jumped") #finally, once the key cycle is finished it will print to the console, "Jumped"

 def imageGrab(): #defines the little box that will detect the difference between black and white. (white when safe, black when you need to jump)
    box = (coordinates.dinosaur[0]+100,coordinates.dinosaur[1],coordinates.dinosaur[0]+200,coordinates.dinosaur[1]+100) #(x1,y1,x2,y2) makes a box x1y1 is top left and x2y2 is bottom right
    #box = (214,472,265,513) ##again, just another experiment, use the top left coordinate from the dinosaur instead of "free balling" a random box
    image = ImageGrab.grab(box) #grab function gets the image in the box
    grayImage = ImageOps.grayscale(image) #this converts it to greyscale, its a lot faster to register only black and white compared to all the colors under the sun (rgb)
    a = array(grayImage.getcolors()) #tells python to get the value of the color of whatever your box is surrounding
    return a.sum() #returns the number to python to be used as an int

def main(): #main function to rule them all! aka, now we get to actually use this stuff above ^
        restartGame() #the game will start!
        while True: #WHILE the game is started
            if(imageGrab()>5000): #IF image grab is greater than 5000(mine is set to 5000 because i made my box too big and it registers random values of +-3000 from the little bumps in the ground) then...
                pressSpace() #press the space bar how we told you to, python!
                time.sleep(0.1) #and then  wait a millisecond
main()# the program sees this first and will execute the funcions within!

###credits to someone else, i dont know. point is i did NOT make this. I followed a tutorial to gain more knowledge and wanted to explain everything so that I was more than certain that I learned what I was supposed to, thank you!











