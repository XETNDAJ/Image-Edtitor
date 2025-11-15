from PIL import Image
img = None

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
                img = Image.open(words[1])
                print(f"Image size: {img.size}" )
    except Exception as e:
        print(e)
            