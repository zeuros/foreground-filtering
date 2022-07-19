import unittest
import pathlib
import cv2 as cv
from ..lib.filters.cvBlurFilter2D import blurFilter

"""
For the directory of the script being run:

import pathlib
pathlib.Path(__file__).parent.resolve()

For the current working directory:

import pathlib
pathlib.Path().resolve()
"""

class TestBlur(unittest.TestCase):
    """a few tests to get in touch with cv lib"""

    def test_blur(self):
        """use kernels to apply 2D filter and display results"""

        root = str(pathlib.Path(__file__).parent.resolve())
        cwd = str(pathlib.Path().resolve())
        
        cv.samples.addSamplesDataSearchPath(cwd + '/samples')
        cv.samples.addSamplesDataSearchPath(root + '/samples')

        # Loads an image
        imgContents = cv.imread(cv.samples.findFile('image-000.png'), cv.IMREAD_COLOR)

        for i in range(0, 4):

            result = blurFilter(src=imgContents, ddepth=-1, kernel_size=3 + 2 * i)

            cv.imshow('filter2D Demo', result)
            cv.waitKey(400)


if __name__ == '__main__':
    unittest.main()
