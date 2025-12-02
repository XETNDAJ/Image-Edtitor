from PIL import Image, ImageOps, ImageEnhance
import os
img = None

print("hello")

while True:
    try:
        command = input("> ")
        words = command.split()
        match words[0]:
            case "quit":
                break
            case "help":
                print(''' 
                quit = exit program
                help = display this message
                open = open the picture
                save = save the picture after editing it
                resize = resize the picture
                ''')
            case "open":
                img = Image.open(words[1] + ".jpg")
                print(f"Image size: {img.size}" ) 
                img.show()
            case "save":
                print(img.filename)
                if img.filename == words[1] + ".jpg":
                    why = input("Do you want to overwrite the previous image > ")
                    if why[0].lower() == "y":
                        img.save(words[1] + ".jpg")
                    else:
                        img.save(words[1] + "_1" + ".jpg")
                else:
                    img.save(words[1] + ".jpg")
            case "resize":
                x =int(words[1])
                y = int(words[2])
                #img.thumbnail((x,y))
                filename = img.filename
                img = img.resize((x,y))
                img.filename = filename
                img.show()
            case "rotate":
                degrees = input("How many degrees do you want to rotate it to? > ")
                print(degrees)
                degree = int(degrees)
                filename = img.filename
                img = img.rotate(degree)
                img.filename = filename
            case "enhance":
                filename = img.filename
                
                qs = input("What would you like to change BRIGHTNESS or CONTRAST? > ")
                if qs[0].upper() == "B":
                    bright = input("How much would you want to change the brightness? > ")
                    bri = float(bright)
                    enhancer = ImageEnhance.Brightness(img)
                    img = enhancer.enhance(bri)
                    img.filename = filename
                else:
                    filename = img.filename
                    contrast = input("How much would you want the image to contrast? > ")
                    con = float(contrast)
                    enhancer = ImageEnhance.Contrast(img)
                    img = enhancer.enhance(con)
                    img.filename = filename
            case "rename":
                newname = input("What would you like to change the name to? > ")
                #img.save(newname + ".jpg")
                os.rename(img.filename, newname + ".jpg")
            case "crop":
                filename = img.filename
                cropp = input("Please enter the left,upper,right,lower pixels you want to crop.> ")
                thing = cropp.split(',')
                other = [int(s) for s in thing]
                pl = tuple(other)
                img = img.crop(pl)
                img.filename = filename
    except Exception as e:
        print(e)
            