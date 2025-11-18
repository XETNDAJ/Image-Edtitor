from PIL import Image, ImageOps
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
            case Resize:
                x = words[1]
                y = words[2]
                img.thumbnail((x,y))
                
    except Exception as e:
        print(e)
            