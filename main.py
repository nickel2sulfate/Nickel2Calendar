from PIL import Image, ImageDraw, ImageFont

color = (143, 56, 56, 255)
times = []
things = []

for i in range(1, 8):
    # TODO: This could be improved to say the actual days of the week...
    newTime = input(f"What time do you want to stream on day {i} of the week?: ")
    times.append(newTime)
    newThing = input(f"What do you wanna do?: ")
    things.append(newThing)

with Image.open("assets/cal.png") as cal:

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

    output.show()
