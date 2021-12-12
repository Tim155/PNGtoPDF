import sys, os
from PIL import Image
#import img2pdf

argLen = len(sys.argv)
pngPath = 0
savePath = os.getcwd() + "/"
homePath = str(os.path.expanduser("~")) + "/"
ready = True

def exiter():
    print("Exiting...")
    exit()

if argLen == 3:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]

    if "/" in arg1 and arg1[len(arg1) - 4:] == ".png":
        if arg1[0] == "/":
            pngPath = homePath + arg1[1:]
        elif arg1[0] != "/":
            pngPath = homePath + arg1

    elif "/" not in arg1 and arg1[len(arg1) - 4:] == ".png":
        pngPath = str(os.getcwd()) + "/" + arg1
    else:
        print("Something went wrong")
        ready = False
        exiter()

    #if pngPath:
    #    print(pngPath)

    if "/" == arg2[0] and arg2[len(arg2) - 4:] == ".pdf" and arg2.count("/") >= 2:
        savePath = homePath + arg2[1:]
    elif "/" not in arg2 and arg2[len(arg2) - 4:] == ".pdf":
        savePath = os.getcwd() + "/" + arg2
    else:
        print("Something went wrong again")
        ready = False
        exiter()

    try:

        if ready:
            img = Image.open(f"{pngPath}")
            PDF = img.convert("RGB")
            PDF.save(f"{savePath}")
            #img = img2pdf.convert(pngPath)
            #pdf = open("testqr.pdf", "wb")
            #pdf.write(img)
            #pdf.close()
            print("Saved file to: ", savePath)

    except FileNotFoundError:
        print("Path does not exist")
        exiter()
    
else:
    print("Wrong or no arguments were given")
    exiter()