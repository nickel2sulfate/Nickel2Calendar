from PIL import Image, ImageDraw, ImageFont
import datetime

#global variables
color = (143, 56, 56, 255)
week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


def readScheduleFromCLI():
    times = []
    things = []
    for day in week:
        newTime = input(f"What time do you want to stream on {day} of the week?: ")
    #if there is a blank space
        if not newTime:
            newTime = "--"
        times.append(newTime)
        newThing = input(f"What do you wanna do?: ")
    #if there is a blank space
        if not newThing:
            newThing = "--"
        things.append(newThing)
    
    return times, things


def generateScheduleImages(times, things):
    with Image.open("assets/cal.png") as cal, Image.open("assets/calTwiBase.png") as twit:
        #print("width is:" , cal.width)
        #print("height is:" , cal.height)
        
        textLayer = Image.new("RGBA", cal.size, (255, 255, 255, 0))


        fnt = ImageFont.truetype("assets/Manrope-Light.ttf",80)
        tfnt = fnt.font_variant(size=65)

        brush = ImageDraw.Draw(textLayer)

        baseLocation = [245, 360]
        offset = [0, 137]
        i = 0
        for time in times:
            thisOffset = (
                    offset[0] * i + baseLocation[0],
                    offset[1] * i + baseLocation[1]
                )
            brush.text(
                    thisOffset,
                    time, 
                    font=fnt, 
                    fill=color
                )
            i = i + 1

        baseLocation = [700, 385]
        offset = [0, 137]
    #this is for placing the original image on the twitter image in proper coordinate
        twitterOffset = ((twit.width - cal.width)//2 , 0 )
        i = 0
        for thing in things:
            thisOffset = (
                    offset[0] * i + baseLocation[0],
                    offset[1] * i + baseLocation[1]
                )
            brush.text(
                    thisOffset,
                    thing, 
                    font=tfnt, 
                    fill=color
                )
            i = i + 1

        output = Image.alpha_composite(cal, textLayer)
        twit.paste(output, twitterOffset)
        output.show()
        twit.show()
        output.save(f"out/{datetime.datetime.now().strftime('%b-%d-%Y')}.png")
        twit.save(f"out/twitter{datetime.datetime.now().strftime('%b-%d-%Y')}.png")


#when I run this file, run the code inside the if condtion
if __name__ == '__main__':
    times, things = readScheduleFromCLI()
    generateScheduleImages(times,things)
