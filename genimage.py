from PIL import Image, ImageFont, ImageDraw
from inky import InkyPHAT


#Create the image to be displayed on the hat
def genimage(display, stoptimes, todisplay, height, width):
    img = Image.new("P", (width, height))
    draw = ImageDraw.Draw(img)
    f1 = ImageFont.load_default()

    #Counts where we are printing from
    printheight = 0

    for stop in stoptimes: 
        name = stop['name']
        #Print the name 
        draw.text((5,printheight), name, display.BLACK, f1)
        printheight += 10

        shown = 0
        #Print the times 
        for time in stop['times']:
            ttl = str(time['timeToLeave'])
            if (ttl == "0"):
                ttl = "DUE"
            
            if shown >= todisplay: 
                break
            draw.text((5,printheight), (str(time['serviceName']) + " " + time['destination'] + ": " + str(time['timeToLeave'])), display.BLACK, f1)
            printheight += 10
            shown += 1
          
    return img
