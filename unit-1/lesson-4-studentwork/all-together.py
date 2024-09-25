import sys
from PIL import Image 



### Part 1 review
## first 100 x 100
## then test 400 x 400

# img = Image.new("RGB", (400,400) )

# for y in range(400):

#     for x in range(400):

#         r = 0
#         g = 0
#         b = 0
#         if x % 150 > 25:
#             print("for pixel at coordinate "+ str(y) + " " + str(x) + " make the Red channel 120")
#             r = 120

#         if y % 40 > 25:
#             print("for pixel at coordinate "+ str(y)  + " " + str(x) + " make the Blue channel 15")
#             b = 15

#         if x % 150 > 50 and y % 150 > 50:
#             print("for pixel at coordinate "+ str(y)  + " " + str(x) + " make the Green channel 255")
#             g = 255

        
#         pixel = (r, g, b)
#         print(x,y,pixel)
#         img.putpixel( (x,y), pixel )

# img.save("part-1-review.jpg")








# ### Part 2 review

if len(sys.argv) != 3:
    exit("This program requires two arguments: the name of two image files to combine.")

# open both images
img1 = Image.open( sys.argv[1] )
img2 = Image.open( sys.argv[2] )

# resize both images so they are no bigger than 800 x 400
# don't preserve aspect ration , just crop
img1.resize( (800,400) )
img2.resize( (800,400) )
img1.convert("RGBA")
img2.convert("RGBA")
# make a new image 600x600, with a white background
# Note that this image now has an "alpha" component
## make 800 width by 400 height
new_image = Image.new( "RGBA", (800,400), "red" )

img1.putalpha(220)
img2.putalpha(50)

# paste in the first image to the upper-left corner (0,0)
new_image.paste(img1, (0,0) )

# dont composite but just add image without transparency
# new_image.paste(img2, (400,0) )

# paste in the second image, preserving its new transparency
new_image.alpha_composite(img2, (200,50) )

# save the resulting image
# Note that we must convert it to RGB with no alpha to save it as a JPEG
new_image.convert("RGB").save("algo-1-final.jpg")









# # ### 1 ... LANCZOS? try w/o
# if len(sys.argv) != 5:
#     exit("This program requires four arguments")

# # Open images
# images = [Image.open(arg) for arg in sys.argv[1:]]

# # Create a new blank image with a white background
# collage_width = 600
# collage_height = 600
# collage = Image.new("RGB", (collage_width, collage_height), (255, 255, 255))

# # Calculate positions for each image
# positions = [(0, 0), (300, 0), (0, 300), (300, 300)]

# for i, img in enumerate(images):
#     # Resize each image to cover half of the collage space
#     img = img.resize((300, 300), Image.LANCZOS)
#     collage.paste(img, positions[i])

# collage.save("collage-1.jpg")




# 3
# if len(sys.argv) != 5:
#     exit("This program requires 4 arguments: the name of 4 image files to combine.")

# img1 = Image.open( sys.argv[1] )
# img2 = Image.open( sys.argv[2] )
# img3 = Image.open( sys.argv[3] )
# img4 = Image.open( sys.argv[4] )

# img1.thumbnail( (200, 200) )
# img2.thumbnail( (200, 200) ) 
# img3.thumbnail( (200, 200) )
# img4.thumbnail( (200, 200) )

# new_image = Image.new( "RGBA", (200, 200), "black" )

# new_image.paste(img1, (0,0) )

# img2.putalpha(120)
# img3.putalpha(90)
# img4.putalpha(100)

# new_image.alpha_composite(img2, (0,0) )
# new_image.alpha_composite(img3, (0,0) )
# new_image.alpha_composite(img4, (0,0) )

# new_image.save("collaging1-saved-for-demo.png")














# # ## 2 use with images 1/2/3/4, in original only uses 2,3,4
# img1 = Image.open( sys.argv[1] )
# img2 = Image.open( sys.argv[2] )
# img3 = Image.open( sys.argv[3] )
# img4 = Image.open( sys.argv[4] )

# ### next resize  images so they are no bigger than 400x400
# # but preserve the original aspect ratio
# img1.thumbnail( (400,400) )
# img2.thumbnail( (400,400) )
# img3.thumbnail( (400,400) )
# img4.thumbnail( (400,400) )

# new_image = Image.new( "RGBA", (400,400), "white" )
# # img1.putalpha(128)
# img2.putalpha(128)
# img3.putalpha(225)
# img4.putalpha(45)
# # new_image.alpha_composite(img1, (0,0) )
# new_image.alpha_composite(img2, (0,0) )
# new_image.alpha_composite(img3, (0,0) )
# new_image.alpha_composite(img4, (0,0) )
# new_image.convert("RGB").save("new-saved-for-demooo.png")








### broken code, missing put alpha for first image


# if len(sys.argv) != 3:
#     exit("This program requires two arguments: the name of two image files to combine.")

# img1 = Image.open( sys.argv[1] )
# img2 = Image.open( sys.argv[2] )


# img1.thumbnail( (400,400) )
# img2.thumbnail( (400,400) )

# # make a new image 600x600, with a white background
# # Note that this image now has an "alpha" component
# new_image = Image.new( "RGBA", (400,400), "white" )


# new_image.paste(img1, (0,0) )

# img2.putalpha(180)

# new_image.alpha_composite(img2, (0,0) )

# new_image.convert("RGB").save("overlay-transparent3.jpg")













# if len(sys.argv) != 3:
#     exit("This program requires two arguments: the name of two image files to combine.")

# # open both images
# img1 = Image.open( sys.argv[1] )
# img2 = Image.open( sys.argv[2] )

# img1.convert("RGBA")
# img2.convert("RGBA")

# # resize both images so they are no bigger than 400x400
# # but preserve the original aspect ratio
# img1.thumbnail( (400,400) )
# img2.thumbnail( (400,400) )

# # make a new image 600x600, with a white background
# # Note that this image now has an "alpha" component
# new_image = Image.new( "RGBA", (150,150), "white" )

# ## rae changed 400 to 150 

# # paste in the first image to the upper-left corner (0,0)
# new_image.paste(img1, (0,0) )

# # add some transparency (alpha) to the second image
# img2.putalpha(128)


# # paste in the second image, preserving its new transparency
# new_image.alpha_composite(img2, (0,0))
# ## rae used tuple instead of img1 here


# # save the resulting image
# # Note that we must convert it to RGB with no alpha to save it as a JPEG
# new_image.convert("RGB").save("overlay-transparent-again.jpg")













# if len(sys.argv) != 3:
#     exit("This program requires two arguments: the name of two image files to combine.")

# # open both images
# img1 = Image.open( sys.argv[1] )
# img2 = Image.open( sys.argv[2] )

# # resize both images so they are no bigger than 400x400
# # but preserve the original aspect ratio
# img1.thumbnail( (400,400) )
# img2.thumbnail( (400,400) )

# # make a new image 600x600, with a white background
# # Note that this image now has an "alpha" component
# new_image = Image.new( "RGBA", (400,260), "white" )

# # paste in the first image to the upper-left corner (0,0)
# new_image.paste(img1, (0,0) )

# # add some transparency (alpha) to the second image
# img2.putalpha(150)

# # paste in the second image, preserving its new transparency
# new_image.alpha_composite(img2, (0,0) )

# # save the resulting image
# # Note that we must convert it to RGB with no alpha to save it as a JPEG
# new_image.convert("RGB").save("overlay-transparent-again-again.jpg")
