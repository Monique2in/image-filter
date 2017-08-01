# image-filter
Remove unwanted moving objects from images

### What image-filter does
If you have a series of photos with moving objects (e.g. tourists, cars) that you don't want, you can remove them and return an image of just the background/still objects behind them. Images need to be stabilized (i.e. taken on a tripod) and all the size size.

### How to Use
Convert your images to .ppm format using a free image editor like GIMP. Save the images into a directory with the names "image0.ppm", "image1.ppm", etc. Update the three variables at the top of the Python file (number of photos being processed, height and width) and run `image_filter.py` in the directory. The program will output a new PNG file with the moving objects removed!
