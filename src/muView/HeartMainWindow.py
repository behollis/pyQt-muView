#from PyQt5.QtWidgets import QWidget
from common.QT.QExtendedMainWindow import QExtendedMainWindow
from PyQt5.QtCore import import QAction, QMenu, tr
import PyQt5.QtCore
import numpy as np
from gtk._gtk import MenuBar

class MainWindow(QExtendedMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # SCI::ThirdPersonCameraControls   view
        self.cur_dock = HeartDock()                # HeartDock* 
        self.file_menu = QMenu()               # QMenu* 
        self.open_mesh = QAction()               # QAction* 
        self.append_data = QAction()             # QAction* 
        self.open_dfield = QAction()             # QAction* 
        self.import_mesh = QAction()             # QAction* 
        self.save_mesh = QAction()               # QAction* 
        self.save_data = QAction()               # QAction* 
        self.exit = QAction()                    # QAction* 
        self.view_menu = QAction()               # QMenu* 
        self.view_reset = QAction()              # QAction* 
        self.view_menu_action = QAction()        # QAction* 
        
        self.init()

    def ResetView(self):
        #self.view.Set( 15.0f, 75.0f, 5.0f, (0,0,0), (0,1,0) )
        self.Save('view.txt')
        None

    def init(self): 
        self.cur_dock = 0
        
        #self.view.Set( 15.0f, 75.0f, 5.0f, (0,0,0), (0,1,0) )
        self.view.Load('view.txt')
    
        # Setup File Menu
        file_menu =  self.menuBar().addMenu('&File')
        
        # Setup Open Menus
        open_mesh = QAction('Open Mesh')
        file_menu.addAction( open_mesh )
        file_menu.addAction( append_data = QAction('Append Data' ) )
        file_menu.addAction( open_dfield = QAction('Open Distance Field') )
        file_menu.addSeparator()

        file_menu.addAction( import_mesh = QAction('Import Additional Mesh') )
        file_menu.addSeparator()

        # Setup Save Menus
        file_menu.addAction( save_mesh = QAction('Save Mesh') )
        file_menu.addAction( save_data = QAction('Save Data') )
        file_menu.addSeparator()

        # Setup Exit Menu
        file_menu.addAction( exit = QAction('E&xit') )

        exit.setShortcut(tr('CTRL+X'))

        self.save_mesh.setEnabled(False)
        self.save_data.setEnabled(False)

        self.open_mesh.triggered().connect( open_mesh_file() )
        self.append_data.triggered().connect( append_data_file() )
        self.open_dfield.triggered().connect( open_dist_field_file() )
        self.import_mesh.triggered().connect( import_mesh_file() )
        self.save_mesh.triggered().connect( save_mesh_file() )
        self.save_data.triggered().connect(save_data_file() )

        self.exit.triggered().connect(quit())
    
    
        view_menu = QMenu('View')
        view_reset = view_menu.addAction(tr('Reset'))
        self.view_reset.triggered().connect( self.ResetView() )
        self.menuBar().addMenu( view_menu )
        
        '''
        
'''
#include <QApplication>
#include <muView/HeartMainWindow.h>
#include <time.h>


#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QApplication>

#include <QT/QExtendedMainWindow.h>

#include <muView/ParallelCoordinates.h>
#include <muView/HeartDock.h>

'''
class MainWindow : public QT::QExtendedMainWindow {

    Q_OBJECT
    
public:

    MainWindow( QWidget * parent = 0 )
    ~MainWindow()

public slots:
    virtual void open_mesh_file()
    virtual void import_mesh_file()
    virtual void append_data_file()
    virtual void open_dist_field_file()
    virtual void save_mesh_file()
    virtual void save_data_file()

    void ResetView()

protected:

    SCI::ThirdPersonCameraControls   view

    HeartDock  * cur_dock

    QMenu      * file_menu
    QAction    * open_mesh
    QAction    * append_data
    QAction    * open_dfield
    QAction    * import_mesh
    QAction    * save_mesh
    QAction    * save_data
    QAction    * exit

    QMenu      * view_menu
    QAction    * view_reset
    QAction    * view_menu_action

}



#endif # MAINWINDOW_H

#include <muView/HeartMainWindow.h>

#include <QMenuBar>
#include <QDesktopWidget>
#include <iostream>

MainWindow::MainWindow(QWidget *parent) : QT::QExtendedMainWindow(parent){

    cur_dock   = 0

    view.Set( 15.0f, 75.0f, 5.0f, SCI::Vex3(0,0,0), SCI::Vex3(0,1,0) )
    view.Load('view.txt')


    # Setup File Menu
    file_menu = menuBar().addMenu('&File')
    {
        # Setup Open Menus
        file_menu.addAction( open_mesh   = new QAction('Open Mesh',   this ) )
        file_menu.addAction( append_data = new QAction('Append Data', this ) )
        file_menu.addAction( open_dfield = new QAction('Open Distance Field',  this ) )
        file_menu.addSeparator()

        file_menu.addAction( import_mesh = new QAction('Import Additional Mesh',   this ) )
        file_menu.addSeparator()

        # Setup Save Menus
        file_menu.addAction( save_mesh   = new QAction('Save Mesh',   this ) )
        file_menu.addAction( save_data   = new QAction('Save Data',   this ) )
        file_menu.addSeparator()

        # Setup Exit Menu
        file_menu.addAction( exit        = new QAction('E&xit',       this ) )

        exit.setShortcut(tr('CTRL+X'))

        save_mesh.setEnabled(False)
        save_data.setEnabled(False)

        connect(  open_mesh, SIGNAL(triggered()), this, SLOT(open_mesh_file())      )
        connect(append_data, SIGNAL(triggered()), this, SLOT(append_data_file())    )
        connect(open_dfield, SIGNAL(triggered()), this, SLOT(open_dist_field_file()))

        connect(import_mesh, SIGNAL(triggered()), this, SLOT(import_mesh_file()) )

        connect(  save_mesh, SIGNAL(triggered()), this, SLOT(save_mesh_file())  )
        connect(  save_data, SIGNAL(triggered()), this, SLOT(save_data_file())  )

        connect(       exit, SIGNAL(triggered()), qApp, SLOT(quit())            )
    }


    view_menu = new QMenu('View')
        view_reset = view_menu.addAction(tr('Reset'))
        connect( view_reset, SIGNAL(triggered()), this, SLOT(ResetView()) )
    menuBar().addMenu( view_menu )

}

MainWindow::~MainWindow(){ }




void MainWindow::open_mesh_file(){
    #if defined(WIN32)
        QApplication::setOverrideCursor(Qt::WaitCursor)
    #endif

    Data::Mesh::SolidMesh    * smesh = 0
    Data::Mesh::PointMesh    * pmesh = 0
    Data::PointData          * pdata = 0
    Data::FiberDirectionData * fdata = 0

    pmesh = HeartDock::OpenPointMesh( )

    if( pmesh ){
        smesh = HeartDock::OpenSolidMesh( )
    }


    if( smesh ){
        fdata = HeartDock::OpenFiberData( )
        pdata = HeartDock::OpenPointData( )
    }

    if( pdata ){
        addDockWidget( Qt::RightDockWidgetArea, cur_dock = new HeartDock(&view, pmesh, smesh, fdata, this ) )
        cur_dock.SetPointData( pdata )
        save_mesh.setEnabled(True)
        save_data.setEnabled(True)
    }

    else{
        if(pmesh) delete pmesh
        if(smesh) delete smesh
        if(pdata) delete pdata
        if(fdata) delete fdata
    }

    QApplication::restoreOverrideCursor()

}


void MainWindow::import_mesh_file(){
    if( cur_dock == 0 ) return

    #if defined(WIN32)
        QApplication::setOverrideCursor(Qt::WaitCursor)
    #endif

    Data::Mesh::SolidMesh    * smesh = 0
    Data::Mesh::PointMesh    * pmesh = 0

    pmesh = HeartDock::OpenPointMesh( )

    if( pmesh ){
        smesh = HeartDock::OpenSolidMesh( )
        ((HeartDock*)cur_dock).AddImportedMesh( pmesh, smesh )
    }
    else{
        if(pmesh) delete pmesh
        if(smesh) delete smesh
    }

    QApplication::restoreOverrideCursor()

}

void MainWindow::append_data_file(){
    #if defined(WIN32)
        QApplication::setOverrideCursor(Qt::WaitCursor)
    #endif

    if( cur_dock != 0 ){
        Data::PointData * pdata = HeartDock::OpenPointData( cur_dock.GetPointData() )
        if( pdata ){
            cur_dock.SetPointData( pdata )
        }
    }

    QApplication::restoreOverrideCursor()
}


void MainWindow::open_dist_field_file(){

    Data::DistanceFieldSet * dfield = HeartDock::OpenDistanceField()

    if(dfield){
        cur_dock.SetDistanceFieldData( dfield )
    }

}


void MainWindow::save_mesh_file(){
    #if defined(WIN32)
        QApplication::setOverrideCursor(Qt::WaitCursor)
    #endif

    Data::Mesh::PointMesh    * pmesh = ( cur_dock == 0 ) ? 0 : cur_dock.GetPointMesh()
    Data::Mesh::SolidMesh    * smesh = ( cur_dock == 0 ) ? 0 : cur_dock.GetSolidMesh()
    Data::FiberDirectionData * fdata = ( cur_dock == 0 ) ? 0 : cur_dock.GetFiberData()

    if( pmesh ){
        QString save_file = saveDialog( tr('Save to Point File'), QString('Point File (*.point *.point.gz)') )
        if(save_file.size() > 0 ){
            pmesh.Save( save_file.toLocal8Bit().data(), save_file.endsWith( tr('.gz') ) )
        }
    }

    if( dynamic_cast<Data::Mesh::TetMesh*>(smesh) != 0 ){
        QString save_file = saveDialog( tr('Save to Tets File'), QString('Binary Tets File (*.btet *.btet.gz)') )
        if(save_file.size() > 0){
            smesh.Save( save_file.toLocal8Bit().data() )
        }
    }

    if( dynamic_cast<Data::Mesh::HexMesh*>(smesh) != 0 ){
        QString save_file = saveDialog( tr('Save Hex File'), QString('Binary Hex File (*.bhex)') )
        if(save_file.size() > 0){
            smesh.Save( save_file.toLocal8Bit().data() )
        }
    }

    if( fdata ){
        QString save_file = saveDialog( tr('Save to Fiber File'), QString('Fiber File (*.fibs)') )
        if(save_file.size() > 0 ){
            fdata.Save( save_file.toLocal8Bit().data() )
        }
    }


    QApplication::restoreOverrideCursor()
}

void MainWindow::save_data_file(){
    #if defined(WIN32)
        QApplication::setOverrideCursor(Qt::WaitCursor)
    #endif

    Data::PointData * pdata = ( cur_dock == 0 ) ? 0 : cur_dock.GetPointData()

    if( pdata != 0 ){
        QString save_file = saveDialog( tr('Save to Point Data File'), QString('Point Data File (*.pdata)') )
        if(save_file.size() > 0){
            pdata.Save( save_file.toLocal8Bit().data() )
        }
    }

    QApplication::restoreOverrideCursor()
}

'''