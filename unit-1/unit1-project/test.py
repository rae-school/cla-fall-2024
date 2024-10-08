from os import listdir, path
import sys
import random
from PIL import Image


currentDirectory = sys.argv[1]
# import random file from shells folder
files = listdir(currentDirectory)
# print(files)

# files.remove(".DS_Store")

randomImage1 = random.choice(files)
randomImage2 = random.choice(files)


Image.open(path.join(currentDirectory, randomImage1))
Image.open(randomImage2)
print(randomImage1, randomImage2)
randomImage1.resize((400,400))
randomImage2.resize((400, 400))
randomImage1.convert("RGBA")
randomImage2.convert("RGBA")
blendedRandomImage = Image.blend(randomImage1, randomImage2, 0.5)

# print(randoooomfile)

randomImage1.convert("RGBA")
randomImage2.convert("RGBA")
# img = Image.open( path.join("images",random_file) )