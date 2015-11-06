#from PyQt5.QtWidgets import QWidget
from common.QT.QExtendedMainWindow import QExtendedMainWindow
from PyQt5.QtCore import import QAction, QMenu, tr
import PyQt5.QtCore
import numpy as np
from gtk._gtk import MenuBar

'''
#include <QApplication>
#include <muView/HeartMainWindow.h>
#include <time.h>
#include <QApplication>
#include <QT/QExtendedMainWindow.h>
#include <muView/ParallelCoordinates.h>
#include <muView/HeartDock.h>
#include <muView/HeartMainWindow.h>
#include <QMenuBar>
#include <QDesktopWidget>
#include <iostream>
'''

class MainWindow(QExtendedMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # SCI::ThirdPersonCameraControls   view
        self.cur_dock           = HeartDock()                
        self.file_menu          = QMenu()                 
        self.open_mesh          = QAction()               
        self.append_data        = QAction()              
        self.open_dfield        = QAction()             
        self.import_mesh        = QAction()             
        self.save_mesh          = QAction()               
        self.save_data          = QAction()                
        self.exit               = QAction()                    
        self.view_menu          = QAction()               
        self.view_reset         = QAction()              
        self.view_menu_action   = QAction()        
        
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

        self.save_mesh.setEnabled( False )
        self.save_data.setEnabled( False )

        self.open_mesh.triggered().connect( open_mesh_file() )
        self.append_data.triggered().connect( append_data_file() )
        self.open_dfield.triggered().connect( open_dist_field_file() )
        self.import_mesh.triggered().connect( import_mesh_file() )
        self.save_mesh.triggered().connect( save_mesh_file() )
        self.save_data.triggered().connect( save_data_file() )
        self.exit.triggered().connect( quit() )
    
        view_menu = QMenu('View')
        view_reset = view_menu.addAction( tr('Reset') )
        self.view_reset.triggered().connect( self.ResetView() )
        self.menuBar().addMenu( view_menu )
        
    def open_mesh_file():
        #if defined(WIN32)
        #    QApplication::setOverrideCursor(Qt::WaitCursor)
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

        
'''    
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