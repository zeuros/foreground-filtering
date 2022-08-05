import unittest
import pathlib
import cv2 as cv
import numpy as np


def blurFilter(src, ddepth, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), dtype=np.float32)
    kernel /= (kernel_size * kernel_size)

    return cv.filter2D(src, ddepth, kernel)
