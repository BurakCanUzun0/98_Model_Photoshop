import os
import sys
from PyQt5.QtWidgets import QAction,qApp,QMainWindow,QWidget,QApplication,QTextEdit,QLabel,QPushButton,QHBoxLayout,QFileDialog,QVBoxLayout
from PyQt5.QtGui import QPixmap
from PIL import Image,ImageFilter

class Photo_Editor(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.ac = QPushButton("Open")
        self.kaydet = QPushButton("Save")
        self.resim = QLabel(self)
        self.resim.setText("Press Ctrl+A to add a photo")
        self.blur = QPushButton("Blur")
        self.keskinlestir = QPushButton("Sharpen")
        self.rotate_ = QPushButton("Rotate 90°")
        self.geri_al = QPushButton("Undo")
        self.aslina = QPushButton("Restore Original")
        self.b_and_w = QPushButton("Black & White")

        v_box = QVBoxLayout()
        v_box.addWidget(self.b_and_w)
        v_box.addWidget(self.blur)
        v_box.addWidget(self.keskinlestir)
        v_box.addWidget(self.rotate_)
        v_box.addWidget(self.geri_al)
        v_box.addWidget(self.aslina)
        v_box.addWidget(self.ac)
        v_box.addWidget(self.kaydet)


        h_box = QHBoxLayout()
        h_box.addWidget(self.resim)
        h_box.addLayout(v_box)

        self.setLayout(h_box)
        self.rotate_.clicked.connect(self.rotate)
        self.keskinlestir.clicked.connect(self.sharpen)
        self.ac.clicked.connect(self.resim_ac)
        self.ac.setShortcut("Ctrl+A")
        self.geri_al.clicked.connect(self.geri_al_resim)
        self.geri_al.setShortcut("Ctrl+Z")
        self.blur.clicked.connect(self.blur_resim)
        self.kaydet.clicked.connect(self.resim_kaydet)
        self.aslina.clicked.connect(self.aslina_dondur)
        self.b_and_w.clicked.connect(self.black_white)

        self.setWindowTitle("PhotoShop CC98")
        self.setGeometry(650,300,300,300)
        self.show()

        self.original_resim = None
        self.asil_resim = None

    def resim_ac(self):
        dosya_adi, _ = QFileDialog.getOpenFileName(self, "Open File", os.getenv("HOME"))
        if dosya_adi:
            self.resim_yukle = Image.open(dosya_adi)
            self.original_resim = self.resim_yukle.copy()
            self.asil_resim = self.resim_yukle.copy()
            self.goster_resim()

    def goster_resim(self):
        self.resim_yukle.save("Photo_Editor_Save.png")
        pixmap = QPixmap("Photo_Editor_Save.png")
        self.resim.setPixmap(pixmap)

    def resim_kaydet(self):
        dosya_adi, _ = QFileDialog.getSaveFileName(self, "Resim Kaydet", "", "Resim dosyaları (*.png)")
        if dosya_adi:
            self.resim_yukle.save(dosya_adi)
    def black_white(self):
        self.original_resim = self.resim_yukle.copy()
        self.resim_yukle = self.resim_yukle.convert("L")
        self.goster_resim()
    def blur_resim(self):
        self.original_resim = self.resim_yukle.copy()
        self.resim_yukle = self.resim_yukle.filter(ImageFilter.BLUR)
        self.goster_resim()
    def sharpen(self):
        self.original_resim = self.resim_yukle.copy()
        self.resim_yukle = self.resim_yukle.filter(ImageFilter.SHARPEN)
        self.goster_resim()

    def rotate(self):
        self.original_resim = self.resim_yukle.copy()
        self.resim_yukle = self.resim_yukle.rotate(90)
        self.goster_resim()
    def geri_al_resim(self):
        if self.original_resim is not None:
            self.resim_yukle = self.original_resim.copy()
            self.goster_resim()
    def aslina_dondur(self):
        if self.asil_resim is not None:
            self.resim_yukle = self.asil_resim.copy()
            self.goster_resim()
app = QApplication(sys.argv)
photo_editor = Photo_Editor()
sys.exit(app.exec_())
