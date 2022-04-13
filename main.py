from PIL import Image, ImageDraw, ImageFont

tSunday = input("What Time are you streaming on Sunday?: ") 

with Image.open("assets/cal.png") as cal: 

    textLayer = Image.new("RGBA", cal.size, (255,255,255,0))

    fnt = ImageFont.truetype("assets/lucon.ttf",100)

    brush = ImageDraw.Draw(textLayer)

    brush.text((285,360), tSunday, font=fnt, fill=(225,255,255,255))

    output = Image.alpha_composite(cal,textLayer)

    output.show()






