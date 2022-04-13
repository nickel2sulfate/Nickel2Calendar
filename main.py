from PIL import Image, ImageDraw, ImageFont

color = (225, 100, 100, 255)
# TODO: This process should be repeated for the "command" section
times = []
for i in range(1, 8):
    # TODO: This could be improved to say the actual days of the week...
    newTime = input(f"What time do you want to stream on day {i} of the week?: ")
    times.append(newTime)

with Image.open("assets/cal.png") as cal:

    textLayer = Image.new("RGBA", cal.size, (255, 255, 255, 0))

    fnt = ImageFont.truetype("assets/lucon.ttf", 100)

    brush = ImageDraw.Draw(textLayer)

    # TODO: This process should be repeated for the "command" section
    baseLocation = [285, 360]
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

    output = Image.alpha_composite(cal, textLayer)

    output.show()
