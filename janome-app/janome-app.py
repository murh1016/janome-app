#! coding:utf-8
"""
janome-app.py

Janome v0.2 documentation
http://mocobeta.github.io/janome/

(2015/01/05) ver1.0 たたき台完成

Created by 0160929 on 2016/01/06 16:16
"""
__version__ = '1.0'
__app_name__ = 'janome'

import sys
import os
import csv

from PySide.QtGui import *

from PySide.QtCore import *

from janome.tokenizer import Tokenizer
from UI_ import *


class MyWindow(QWidget, Ui_window):
    loaded_words = Signal(str)
    refresh_words = Signal()

    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(
            QApplication.translate("Widget", "%s %s" % (__app_name__, __version__), None, QApplication.UnicodeUTF8))

        self.jacome_token = Tokenizer()
        self.words_container = []

    @Slot()
    def analysis_janome(self, s):
        # デバッグ用に解析文章をstdout
        print s

        # 解析結果の表示要素を初期化(クリア)
        self.refresh_words.emit()
        # 解析結果格納配列を初期化(csv保存用)
        self.words_container = []
        # 形態素解析を実行
        tokens = self.jacome_token.tokenize(s)

        for token in tokens:
            # 解析結果をstring(UNICODE)型へキャスト
            print_str = str(token).decode('utf8')
            # csv保存用に解析結果を格納
            self.words_container.append(print_str)

        # 解析結果を出力
        self.loaded_words.emit('\n'.join(self.words_container))

    @Slot()
    def save_csv(self):
        filename = 'result.csv'
        filename = os.path.normpath(filename)

        # OSを判定してエンコードを設定
        if os.name is 'nt':
            code = 'cp932'
        else:
            code = 'utf-8'
        print 'save_csv: code = %s' % code

        with open(filename, 'wb') as f:  # 'wb'じゃないと変な改行入る。
            writer = csv.writer(f, delimiter=',')
            for words in self.words_container:
                out_word = words.encode(code)
                writer.writerow([out_word])


def main():
    app = QApplication(sys.argv)
    app.setStyle('plastique')
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
