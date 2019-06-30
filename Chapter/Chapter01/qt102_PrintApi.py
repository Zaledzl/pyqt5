# -*- coding: utf-8 -*- 
'''
    【简介】
	保存PyQt5类的使用手册到本地
   
    
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEnginePage 
from PyQt5.QtWidgets import QWidget

# 啊，还好这个上面有注释的啊，不然根本看不懂是在做什么了啊
out = sys.stdout
sys.stdout = open(r'D:\QWidget.txt' , 'w')
help( QWidget  )
sys.stdout.close()
sys.stdout = out
