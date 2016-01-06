#! coding:utf-8
"""
janome-app.py

Janome v0.2 documentation
http://mocobeta.github.io/janome/

Created by 0160929 on 2016/01/06 16:16
"""
__version__ = '0.0'

__app_name__ = 'janome'

import sys

from PySide.QtGui import *

from UI_ import *


class MyWindow(QWidget, Ui_window):
    interval_time = 1000

    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(
            QApplication.translate("Widget", "%s %s" % (__app_name__, __version__), None, QApplication.UnicodeUTF8))

    def analysis_janome(self, s):
        print s

def main():
    app = QApplication(sys.argv)
    app.setStyle('plastique')
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    # from janome.tokenizer import Tokenizer
    # t = Tokenizer()
    # for token in t.tokenize(u'すもももももももものうち'):
    #     print(token)
