from PIL import Image
import statistics

#Update these values for your specific situation
n = 7 #number of photos being processed - always choose an odd number
w = 750 #width
h = 1000 #height

images = [None] * n #creates an empty array to store the images
pixels = [None] * n

#make a blank file for the output image
imageOut = Image.new('RGB', (w, h))
pxOut = imageOut.load()

for i in range(0, n):
	images[i] = Image.open("image" + str(i) + ".ppm")
	pixels[i] = images[i].load()

#loop through each pixel
for x in range(0, w):
	for y in range(0, h):
		#red pixel
		red_px = [None] * n
		for r in range(0, n):
			red_px[r] = pixels[r][x, y][0]
		redPixel = statistics.median(red_px)

		#green pixel
		green_px = [None] * n
		for g in range(0, n):
			green_px[g] = pixels[g][x, y][1]
		greenPixel = statistics.median(green_px)

		#blue pixel
		blue_px = [None] * n
		for b in range(0, n):
			blue_px[b] = pixels[b][x, y][2]
		bluePixel = statistics.median(blue_px)

		#assign the final pixel
		pxOut[x, y] = (redPixel, greenPixel, bluePixel)

imageOut.save("filtered.png")