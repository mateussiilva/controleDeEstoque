from PyQt6.QtWidgets import (
    QApplication,QWidget,
    QMainWindow, QGridLayout, QLineEdit, QPushButton, QLabel
)


class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)
        # self.setGeometry(1,1,600,600)
        
        self.grid_layout = QGridLayout()
        
        self.lbl_descricao = QLabel(text='Produto')
        self.inp_descricao = QLineEdit()
        
        self.grid_layout.addWidget(self.lbl_descricao,0,0)
        self.grid_layout.addWidget(self.inp_descricao,0,1)


        
        self.main_widget = QWidget()
        
        # CONFIGURANDO O LAYOUT
        self.main_widget.setLayout(self.grid_layout)

        self.setCentralWidget(self.main_widget)
    
        


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow('Meu app')
    window.show()
    app.exec()
