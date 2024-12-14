import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class ImageStickerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.sticker_window = None  # 用于存储显示的图片窗口
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle("简易准星")
        self.setGeometry(200, 200, 400, 200)
        
        # 创建输入框和按钮
        self.image_path_input = QLineEdit(self)
        self.image_path_input.setPlaceholderText("请输入图片路径或点击浏览……")
        
        self.browse_button = QPushButton("浏览", self)
        self.browse_button.clicked.connect(self.browse_image)
        
        self.display_button = QPushButton("显示", self)
        self.display_button.clicked.connect(self.toggle_image_display)

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.image_path_input)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.display_button)
        self.setLayout(layout)

    def browse_image(self):
        # 打开文件选择对话框
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "选择图片", "", "图片文件 (*.png *.jpg *.jpeg *.bmp *.gif)")
        if file_path:
            self.image_path_input.setText(file_path)

    def toggle_image_display(self):
        if self.sticker_window and self.sticker_window.isVisible():
            # 当前图片窗口显示中，隐藏图片并更新按钮文本
            self.sticker_window.hide()
            self.display_button.setText("显示")
        else:
            # 显示图片窗口
            self.display_image()

    def display_image(self):
        # 获取输入的图片路径
        image_path = self.image_path_input.text()
        if not image_path:
            return

        if not self.sticker_window:
            # 如果还没有创建图片窗口，则创建一个
            self.sticker_window = QLabel()
            self.sticker_window.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
            self.sticker_window.setAttribute(Qt.WA_TranslucentBackground, True)

        # 加载图片
        pixmap = QPixmap(image_path)
        self.sticker_window.setPixmap(pixmap)
        
        # 获取屏幕大小
        screen = QApplication.primaryScreen()
        screen_rect = screen.availableGeometry()
        screen_width = screen_rect.width()
        screen_height = screen_rect.height()
        
        # 设置窗口大小和位置
        img_width = pixmap.width()
        img_height = pixmap.height()
        x_position = (screen_width - img_width) // 2
        y_position = (screen_height - img_height) // 2
        self.sticker_window.setGeometry(x_position, y_position, img_width, img_height)
        
        # 显示窗口
        self.sticker_window.show()
        
        # 更新按钮文本
        self.display_button.setText("隐藏")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = ImageStickerApp()
    main_window.show()
    sys.exit(app.exec_())
