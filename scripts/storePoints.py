
'''
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Window(QMainWindow):
   def __init__(self):
       super().__init__()
 
       self.setGeometry(300, 300, 600, 400)
       self.setWindowTitle("PyQt5 window")
       self.show()
 
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())

import webview

webview.create_window('Woah dude!', html='<h1>Woah dude!<h1>')
webview.start()
'''


import webview

def custom_logic(window):
    window.toggle_fullscreen()
    window.evaluate_js('alert("Nice one brother")')

window = webview.create_window('Woah dude!', html='<h1>Woah dude!<h1>')
webview.start(custom_logic, window)
# anything below this line will be executed after program is finished executing
pass

