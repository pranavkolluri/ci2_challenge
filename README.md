# UCSF ci2 Summer 2023 Internship Coding Challenge
This is my response to the UCSF ci2 coding challenge. I elected to do this in a regular python file as I have found that this allows code to scale better than iPython.
In order to run my code, all you have to do run the file! Ensure that you have numpy, matplotlib, and skimage installed.

# Prompt Response Details
1. This simply uses matplotlib to plot the image as a figure and then saves this figure with no padding.
2. This inverts the image by subtracting it from 1. It is then plotted and saved.
3. I elected to apply a type of contrast enhancement on the image. In particular, I elected to use histogram equalization. Histogram equalization functions by redistributing the intesity values of the image such that the histogram of the resulting image is as flat as possible. This acts as an simple, yet effective contrast enhancer.
