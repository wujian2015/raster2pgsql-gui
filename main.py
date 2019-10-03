# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    # import pydevd
    # pydevd.settrace('192.168.251.174', port=53108, stdoutToServer=True, stderrToServer=True)

    from src.WdgRasterLoader import WdgRasterLoader
    app = QApplication(sys.argv)

    wdg = WdgRasterLoader(None, None)
    wdg.m_pUpdateBtn.hide()
    wdg.show()

    sys.exit(app.exec_())
