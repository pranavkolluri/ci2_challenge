#Written by Pranav Kolluri
#To run: simply call the approriate method at the bottom of this file and run this file!
#Notes: I prefer to work in just straight python, as opposed to iPython Notebooks, however I'm more than happy to work with those as well.

import numpy as np
from matplotlib import pyplot as plt
from skimage import exposure

#imports datasets in the .npz file format
def importer(dataset_name):
    #load the dataset
    dataset = np.load(f"../data/{dataset_name}.npz")

    train_images = dataset["train_images"]
    val_images = dataset["val_images"]
    test_images = dataset["test_images"]

    return train_images, val_images, test_images

#This is unnecessary, however it makes the prompt methods far less redundant
def image_retrival(image_num):
    train_images, val_images, test_images = importer("chestmnist")
    image = train_images[image_num]
    return image

#Prompt 1
def grayscale(image):
    plt.imshow(image, cmap='gray')
    plt.savefig('pranav_kolluri_1.png', bbox_inches='tight', pad_inches=0.1)
    plt.show()
    return image

#Prompt 2
def inverter(image):
    inverted_image = 1 - image
    plt.imshow(inverted_image, cmap='gray')
    plt.savefig('pranav_kolluri_2.png', bbox_inches='tight', pad_inches=0.1)
    plt.show()

#Prompt 3
#I thought it might be fun to apply a contrast enhancement filter since that would be useful for a variety of analysis techniques later on
#Utilizing the equalize_hist function from sklearn.exposure to enhance the contrast
def contrast_enhance(image):
    equalized_image = exposure.equalize_hist(image)
    plt.imshow(equalized_image, cmap='gray')
    plt.savefig('pranav_kolluri_3.png', bbox_inches='tight', pad_inches=0.1)
    plt.show()

image = image_retrival(42)
grayscale(image)
inverter(image)
contrast_enhance(image)