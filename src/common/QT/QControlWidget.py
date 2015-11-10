#ifndef QT_QCONTROLWIDGET_H
#define QT_QCONTROLWIDGET_H

#include <QWidget>
#include <QGridLayout>
#include <QRadioButton>
#include <QLabel>
#include <QDoubleSpinBox>
#include <QCheckBox>
#include <QPushButton>
#include <QGroupBox>
#include <QMenuBar>
#include <QSlider>

#include <QT/QDoubleSlider.h>
#include <QT/QExtendedVerticalSlider.h>

    #class QGroupControlWidget

class QControlWidget(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
    
        self.layout = None
        self.row = None
        mb = None 

class QGroupControlWidget(QGroupBox):
    def __init__(self):
        super(QGroupBox, self).__init__()

        self.layout = None #QGroupLayout
        self.row = None #int
'''
**  Common QT Extensions Library
**  Copyright (C) 2013  Paul Rosen
**
**  This program is free software: you can redistribute it and/or modify
**  it under the terms of the GNU General Public License as published by
**  the Free Software Foundation, version 3 of the License, or
**  (at your option) any later version.
**
**  This program is distributed in the hope that it will be useful,
**  but WITHOUT ANY WARRANTY; without even the implied warranty of
**  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
**  GNU General Public License for more details.
**
**  You should have received a copy of the GNU General Public License
**  along with self program.  If not, see <http:#www.gnu.org/licenses/>.
'''

#include <QT/QControlWidget.h>
#include <QMenuBar>

QT.QControlWidget.QControlWidget( QWidget * parent ) : QWidget( parent ){
    layout = QGridLayout( )
    setLayout( layout )
    row = 0

    mb = QMenuBar( self )
    layout.addWidget(mb, row++, 0, 1, 2 )
    layout.setRowStretch( row-1, 0 )
    layout.setRowStretch( row,   1 )
}

QMenuBar * QT.QControlWidget.menuBar(){
    return mb
}

QRadioButton * QT.QControlWidget.addRadioButton( QString title ){
    QRadioButton rb = QRadioButton( title )
    layout.addWidget(rb, row++, 0, 1, 2 )
    layout.setRowStretch( row-1, 0 )
    layout.setRowStretch( row,   1 )
    return rb
}

QSpinBox * QT.QControlWidget.addIntSpinBox ( QString label ){
    QLabel   lbl = QLabel(label)
    QSpinBox spn = QSpinBox( )
    layout.addWidget(lbl,row,   0, 1, 1 )
    layout.addWidget(spn,row++, 1, 1, 1 )
    layout.setRowStretch( row-1, 0 )
    layout.setRowStretch( row,   1 )
    return spn
}

QDoubleSpinBox * QT.QControlWidget.addDblSpinBox( QString label ){
    QLabel         lbl = QLabel(label)
    QDoubleSpinBox spn = QDoubleSpinBox( )
    layout.addWidget(lbl,row,   0, 1, 1 )
    layout.addWidget(spn,row++, 1, 1, 1 )
    layout.setRowStretch( row-1, 0 )
    layout.setRowStretch( row,   1 )
    return spn
}

QSlider * QT.QControlWidget.addHorizontalSlider( QString label ){
    QLabel  lbl = QLabel(label)
    QSlider sld = QSlider( Qt.Horizontal )
    layout.addWidget(lbl,row,   0, 1, 1 )
    layout.addWidget(sld,row++, 1, 1, 1 )
    layout.setRowStretch( row-1, 0 )
    layout.setRowStretch( row,   1 )
    return sld
}

QT.QExtendedVerticalSlider * QT.QControlWidget.addVerticalSlider( QString label ){
    '''
    QLabel  lbl = QLabel(label)
    QLabel  lbl_min = QLabel(tr("min"))
    QLabel  lbl_max = QLabel(tr("max"))
    QSlider sld = QSlider( Qt.Vertical )

    layout.addWidget(lbl,row++, 0, 1, 2 )
    layout.setRowStretch( row-1, 0 )

    layout.addWidget(sld,row, 0, 4, 1, Qt.AlignRight )
    layout.addWidget(lbl_max,row, 1, 1, 1 )
    layout.addWidget(lbl_min,row+3, 1, 1, 1 )
    row+=4
    layout.setRowStretch( row,   1 )
    '''
    QT.QExtendedVerticalSlider sld = QT.QExtendedVerticalSlider( label )
    layout.addWidget    ( sld, row++, 0, 1, 2 )
    layout.setRowStretch( row-1, 0 )
    layout.setRowStretch( row,   1 )

    return sld
}

QT.QDoubleSlider * QT.QControlWidget.addHorizontalDoubleSlider( QString label ){
    QLabel            lbl = QLabel(label)
    QT.QDoubleSlider sld = QT.QDoubleSlider( Qt.Horizontal )
    layout.addWidget(lbl,row,   0, 1, 1 )
    layout.addWidget(sld,row++, 1, 1, 1 )
    layout.setRowStretch( row-1, 0 )
    layout.setRowStretch( row,   1 )
    return sld
}

QT.QDoubleSlider * QT.QControlWidget.addVerticalDoubleSlider( QString label ){
    QLabel            lbl = QLabel(label)
    QT.QDoubleSlider sld = QT.QDoubleSlider( Qt.Vertical )
    layout.addWidget(lbl,row,   0, 1, 1 )
    layout.addWidget(sld,row++, 1, 1, 1 )
    layout.setRowStretch( row-1, 0 )
    layout.setRowStretch( row,   1 )
    return sld
}

QCheckBox * QT.QControlWidget.addCheckbox(  QString label ){
    QCheckBox chk = QCheckBox( label )
    layout.addWidget( chk, row++, 0, 1, 2 )
    layout.setRowStretch( row-1, 0 )
    layout.setRowStretch( row,   1 )
    return chk
}

QPushButton * QT.QControlWidget.addButton(  QString label ){
    QPushButton btn = QPushButton( label )
    layout.addWidget( btn, row++, 0, 1, 2 )
    layout.setRowStretch( row-1, 0 )
    layout.setRowStretch( row,   1 )
    return btn
}

QT.QGroupControlWidget * QT.QControlWidget.addGroupControlWidget( QString title ){
    QT.QGroupControlWidget gcw = QGroupControlWidget( title )
    layout.addWidget( gcw, row++, 0, 1, 2 )
    layout.setRowStretch( row-1, 0 )
    layout.setRowStretch( row,   1 )
    return gcw
}

QT.QGroupControlWidget.QGroupControlWidget( QString title, * parent ) : QGroupBox( title, parent ){
    layout = QGridLayout( )
    setLayout( layout )
    row = 0
}

QRadioButton * QT.QGroupControlWidget.addRadioButton( QString title ){
    QRadioButton rb = QRadioButton( title )
    layout.addWidget(rb, row++, 0, 1, 2 )
    layout.setRowStretch( row-1, 0 )
    layout.setRowStretch( row,   1 )
    return rb
}

QDoubleSpinBox * QT.QGroupControlWidget.addSpinBox( QString label ){
    QLabel         lbl = QLabel(label)
    QDoubleSpinBox spn = QDoubleSpinBox( )
    layout.addWidget(lbl,row,   0, 1, 1 )
    layout.addWidget(spn,row++, 1, 1, 1 )
    layout.setRowStretch( row, 1 )
    return spn
}

QCheckBox * QT.QGroupControlWidget.addCheckbox(  QString label ){
    QCheckBox chk = QCheckBox( label )
    layout.addWidget( chk, row++, 0, 1, 2 )
    layout.setRowStretch( row-1, 0 )
    layout.setRowStretch( row,   1 )
    return chk
}

QPushButton * QT.QGroupControlWidget.addButton(  QString label ){
    QPushButton btn = QPushButton( label )
    layout.addWidget( btn, row++, 0, 1, 2 )
    layout.setRowStretch( row-1, 0 )
    layout.setRowStretch( row,   1 )
    return btn
}

