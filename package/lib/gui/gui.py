from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QWidget, QSlider, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import sys
import pathlib
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

from numpy import ndarray

from ..filters.foregroundExtractionByMyself import foreground_extraction


def createLabel(val=""):
    label = QLabel(val)
    label.setAlignment(Qt.AlignLeft)
    
    return label


def createSlider(default, min=0, max=100, tick_interval=0.1, step=1):
    slider = QSlider(Qt.Horizontal)
    slider.setValue(default)
    slider.setFocusPolicy(Qt.StrongFocus)
    slider.setTickPosition(QSlider.TicksAbove)
    slider.setTickInterval(tick_interval)
    slider.setSingleStep(step)
    slider.setMinimum(min)
    slider.setMaximum(max)
    
    return slider


def redraw_main_image(ax, canvas, blur, key_threshold):
    img = foreground_extraction(blur, key_threshold)
    ax.imshow(img, cmap='gray')
    canvas.draw()


class MySuperWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        lay = QVBoxLayout(self.central_widget)

        # main image display

        figure = Figure(figsize=(10, 6))
        main_image_canvas = FigureCanvas(figure)
        ax = figure.subplots()
        ax.set_axis_off()
        
        # Blur
        default_blur = 5
        blur_label = createLabel(f"Blur: {default_blur}")
        blur_slider = createSlider(default=default_blur, min = 1, max=10, tick_interval=1)
        blur_slider.valueChanged.connect(lambda: blur_label.setText(f"Blur: {blur_slider.value()}"))
        blur_slider.valueChanged.connect(lambda: redraw_main_image(ax=ax, canvas=main_image_canvas, blur=blur_slider.value(), key_threshold=key_threshold_slider.value()))

        # Key threshold
        default_key_threshold = 50
        key_threshold_label = createLabel(f"Key threshold: {default_key_threshold}")
        key_threshold_slider = createSlider(default=default_key_threshold, max=255, tick_interval=1)
        key_threshold_slider.valueChanged.connect(lambda: key_threshold_label.setText(f"Key threshold: {key_threshold_slider.value()}"))
        key_threshold_slider.valueChanged.connect(lambda: redraw_main_image(ax=ax, canvas=main_image_canvas, blur=blur_slider.value(), key_threshold=key_threshold_slider.value()))
        
        lay.addWidget(blur_label)
        lay.addWidget(blur_slider)
        
        lay.addWidget(key_threshold_label)
        lay.addWidget(key_threshold_slider)
        
        lay.addWidget(main_image_canvas)
        
        redraw_main_image(ax=ax, canvas=main_image_canvas, blur=blur_slider.value(), key_threshold=key_threshold_slider.value())
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MySuperWindow()
    sys.exit(app.exec_())
