import pathlib
import numpy as np
from matplotlib import image, pyplot as plt


def foreground_extraction(blur_amount=5, key_threshold=50) -> np.ndarray:

    projectRoot = str(pathlib.Path().resolve())

    # Load background and background_with_subject images (green channels)
    background_green = image.imread(
        projectRoot + '/samples/image-000.png')[:, :, 1]
    background_and_subject_green = image.imread(
        projectRoot + '/samples/image-001.png')[:, :, 1]

    # Normalize data 0-255 (Absolute value to get the diff only)
    diff = np.absolute(background_and_subject_green - background_green)
    diff *= 255.0 / diff.max()

    # Average it a bit for smooth pixel transitions smoothing noise and edges
    kernel_size = blur_amount
    kernel = np.ones(kernel_size) / kernel_size
    diff_convolved_5 = np.convolve(diff.flatten(), kernel, mode='same')

    # get the mask from it by filtering diff
    mask = diff_convolved_5.reshape(diff.shape).copy()

    # plt.imshow(mask, cmap='gray')
    # plt.title('BW diff')
    # plt.show()

    # make the 255 or 0 mask using threshold
    mask[mask < key_threshold] = 0
    mask[mask >= key_threshold] = 255

    return mask
    # plt.imshow(mask, cmap='gray')
    # plt.title('BW mask')
    # plt.show()
