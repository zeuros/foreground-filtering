import unittest
from matplotlib import image, pyplot as plt
from package.lib.filters.foregroundExtractionByMyself import foreground_extraction


class TestForegroundExtractionByMyself(unittest.TestCase):
    """a few tests to get in touch with cv lib"""

    def test_foreground_extraction():
        mask = foreground_extraction(blur_amount=5, key_threshold=50)

        plt.imshow(mask, cmap='gray')
        plt.title('BW mask')
        plt.show()


if __name__ == '__main__':
    TestForegroundExtractionByMyself.test_foreground_extraction()
