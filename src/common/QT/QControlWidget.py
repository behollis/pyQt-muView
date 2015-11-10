from PyQt5.QWidgets import QWidget, QGridLayout, QRadioButton, QLabel, QDoubleSpinBox, QCheckBox
from PyQt5.QWidgets import QPushButton, QGroupBox, QMenuBar, QSlider
from PyQt.QWidgets import QMenuBar, QSpinBox, QSlider
from common.QT import *
from PyQt5.Qt import Horizontal

#include <QT/QDoubleSlider.h>
#include <QT/QExtendedVerticalSlider.h>

class QControlWidget(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
    
        self.layout = None
        self.row = None
        self.mb = None 
        
        self.init()
    
    def init(self):
        self.layout = QGridLayout( )
        self.setLayout( self.layout )
        self.row = 0

        self.mb = QMenuBar( self )
        self.row += 1; self.layout.addWidget(self.mb, self.row, 0, 1, 2 )
        self.row -= 1; self.layout.setRowStretch( self.row, 0 )
        self.layout.setRowStretch( self.row,   1 )
        
    def menuBar(self):
        return self.mb
    
    def addRadioButton(self, title ):
        rb = QRadioButton( title )
        self.row += 1; self.layout.addWidget(rb, self.row, 0, 1, 2 )
        self.row -= 1; self.layout.setRowStretch( self.row, 0 )
        self.layout.setRowStretch( self.row, 1 )
        return rb
    
    def addIntSpinBox(self, label ):
        lbl = QLabel(label)
        spn = QSpinBox()
        self.layout.addWidget(lbl, self.row,   0, 1, 1 )
        self.row += 1; self.layout.addWidget(spn, self.row, 1, 1, 1 )
        self.row -= 1; self.layout.setRowStretch( self.row, 0 )
        self.layout.setRowStretch( self.row,   1 )
        return spn
    
    def addDblSpinBox(self, label ):
        lbl = QLabel(label)
        spn = QDoubleSpinBox( )
        self.layout.addWidget(lbl, self.row,   0, 1, 1 )
        self.row += 1; self.layout.addWidget(spn, self.row, 1, 1, 1 )
        self.row -= 1; self.layout.setRowStretch( self.row, 0 )
        self.layout.setRowStretch( self.row, 1 )
        return spn
    
    def addHorizontalSlider(self, label ):
        lbl = QLabel(label)
        sld = QSlider( Horizontal )
        self.layout.addWidget(lbl, self.row, 0, 1, 1 )
        self.row += 1; self.layout.addWidget(sld, self.row, 1, 1, 1 )
        self.row -= 1; self.layout.setRowStretch( self.row, 0 )
        self.layout.setRowStretch( self.row, 1 )
        return sld
    
    def addVerticalSlider(self, label ):
        '''
        sld = QT.QExtendedVerticalSlider( label )
        self.row += 1; self.layout.addWidget( sld, self.row, 0, 1, 2 )
        self.row -= 1; self.layout.setRowStretch( self.row, 0 )
        self.layout.setRowStretch( row, 1 )
    
        return sld
        '''
        
        return None
    
    def addHorizontalDoubleSlider(self, label ):
        lbl = QLabel(label)
        '''
        sld = QT.QDoubleSlider( Qt.Horizontal )
        self.layout.addWidget(lbl,row,   0, 1, 1 )
        self.row += 1; self.layout.addWidget(sld,row++, 1, 1, 1 )
        self.row -= 1; self.layout.setRowStretch( row-1, 0 )
        self.layout.setRowStretch( row,   1 )
        return sld
        '''
        return None
    
    def addVerticalDoubleSlider(self, label ):
        lbl = QLabel(label)
        '''
        sld = QT.QDoubleSlider( Qt.Vertical )
        self.layout.addWidget(lbl, self.row,   0, 1, 1 )
        self.row += 1; self.layout.addWidget(sld, self.row, 1, 1, 1 )
        self.row -= 1; self.layout.setRowStretch( self.row, 0 )
        self.layout.setRowStretch( self.row,   1 )
        return sld
        '''
        
        return None
    
    def addCheckbox(self, label ):
        chk = QCheckBox( label )
        self.row += 1; self.layout.addWidget( chk, self.row, 0, 1, 2 )
        self.row -= 1; self.layout.setRowStretch( self.row, 0 )
        self.layout.setRowStretch( self.row, 1 )
        return chk
    
    def addButton( self, label ):
        btn = QPushButton( label )
        self.row += 1; self.layout.addWidget( btn, self.row, 0, 1, 2 )
        self.row -= 1; self.layout.setRowStretch( self.row, 0 )
        self.layout.setRowStretch( self.row, 1 )
        return btn
    
    def addGroupControlWidget( self, title ):
        gcw = QGroupControlWidget( title )
        self.row += 1; self.layout.addWidget( gcw, self.row, 0, 1, 2 )
        self.row -= 1; self.layout.setRowStretch( self.row, 0 )
        self.layout.setRowStretch( self.row, 1 )
        return gcw

class QGroupControlWidget(QGroupBox):
    def __init__(self):
        super(QGroupBox, self).__init__()

        self.layout = None #QGroupLayout
        self.row = None #int
        
        self.init()

    def init( self, title, parent ):
        self.layout = QGridLayout()
        self.setLayout( self.layout )
        self.row = 0
    
    def addRadioButton( self, title ):
        rb = QRadioButton( title )
        self.row += 1; self.layout.addWidget(rb, self.row, 0, 1, 2 )
        self.row -= 1; self.layout.setRowStretch( self.row, 0 )
        self.layout.setRowStretch( self.row, 1 )
        return rb
    
    def addSpinBox( self, label ):
        lbl = QLabel(label)
        spn = QDoubleSpinBox( )
        self.layout.addWidget(lbl, self.row,   0, 1, 1 )
        self.row += 1; self.layout.addWidget(spn, self.row, 1, 1, 1 )
        self.layout.setRowStretch( self.row, 1 )
        return spn
    
    def addCheckbox( self, label ):
        chk = QCheckBox( label )
        self.row += 1; self.layout.addWidget( chk, self.row, 0, 1, 2 )
        self.row -= 1; self.layout.setRowStretch( self.row, 0 )
        self.layout.setRowStretch( self.row, 1 )
        return chk
    
    def addButton( self, label ):
        btn = QPushButton( label )
        self.row += 1; self.layout.addWidget( btn, self.row, 0, 1, 2 )
        self.row -= 1; self.layout.setRowStretch( self.row, 0 )
        self.layout.setRowStretch( self.row, 1 )
        return btn
    