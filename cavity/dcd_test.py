""" File made for testing dominant colour distribution (DCD) """

import cv2
import numpy as np
from skimage import io
import matplotlib.pyplot as plt

# Image must be read in this way
#img = io.imread("test_images/img.png")[:, :, :-1]


def determine_dominant_colours(image):
    # TODO document and test
    """ Gets the dominant colours of an image.
    Derived from https://stackoverflow.com/questions/43111029/how-to-find-the-average-colour-of-an-image-in-python-with-opencv
    :param image:
    :return:
    """

    pixels = np.float32(image.reshape(-1, 3))

    n_colors = 5
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags = cv2.KMEANS_RANDOM_CENTERS

    _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)

    # TODO return as object or something
    return palette, labels


# TODO maybe remove?
def plot_dominant_coloirs(pyplot, image, palette, labels):
    # TODO document
    """ Plots the dominant colours of an image. Not particularly useful aside from testing or demoing.
    Derived from https://stackoverflow.com/questions/43111029/how-to-find-the-average-colour-of-an-image-in-python-with-opencv
    :param pyplot: a matplotlib pyplot
    :param image: the image that the dominant colours are being plotted for
    :param palette:
    :param labels:
    :return:
    """
    _, counts = np.unique(labels, return_counts=True)

    indices = np.argsort(counts)[::-1]
    freqs = np.cumsum(np.hstack([[0], counts[indices] / float(counts.sum())]))
    rows = np.int_(image.shape[0] * freqs)

    dom_patch = np.zeros(shape=image.shape, dtype=np.uint8)
    for i in range(len(rows) - 1):
        dom_patch[rows[i]:rows[i + 1], :, :] += np.uint8(palette[indices[i]])

    fig, ax1 = pyplot.subplots(1, 1)
    ax1.imshow(dom_patch)
    ax1.set_title('Dominant colors')
    ax1.axis('off')
    pyplot.show()
