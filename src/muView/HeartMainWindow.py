from PyQt5.QtWidgets import QAction, QMenu, QApplication
import numpy as np
from PyQt5.QtCore import Qt
from common.QT.QExtendedMainWindow import QExtendedMainWindow
from HeartDock import HeartDock

class MainWindow(QExtendedMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.view               = None#SCI::ThirdPersonCameraControls   
        self.cur_dock           = None#HeartDock()                
        self.file_menu          = QMenu()                 
        self.open_mesh          = None#QAction()               
        self.append_data        = None#QAction()              
        self.open_dfield        = None#QAction()             
        self.import_mesh        = None#QAction()             
        self.save_mesh          = None#QAction()               
        self.save_data          = None#QAction()                
        self.exit               = None#QAction()                    
        self.view_menu          = None#QAction()               
        self.view_reset         = None#QAction()              
        self.view_menu_action   = None#QAction()        
        
        self.init()

    def init(self): 
        self.cur_dock = 0
        
        #self.view.Set( 15.0, 75.0, 5.0, (0,0,0), (0,1,0) )
        #self.view.Load('view.txt')
    
        # Setup File Menu
        self.file_menu =  self.menuBar().addMenu('File')
        
        # Setup Open Menus
        self.open_mesh = QAction('Open Mesh', self )
        self.file_menu.addAction( self.open_mesh )
        self.append_data = QAction('Append Data', self )
        self.file_menu.addAction( self.append_data )
        self.open_dfield = QAction('Open Distance Field' , self )
        self.file_menu.addAction( self.open_dfield )
        self.file_menu.addSeparator()
        self.import_mesh = QAction('Import Additional Mesh' , self )
        self.file_menu.addAction( self.import_mesh )
        self.file_menu.addSeparator()

        # Setup Save Menus
        self.save_mesh = QAction('Save Mesh' , self )
        self.file_menu.addAction( self.save_mesh )
        self.save_data = QAction('Save Data' , self )
        self.file_menu.addAction( self.save_data )
        self.file_menu.addSeparator()

        # Setup Exit Menu
        self.exit = QAction('Exit', self )
        self.file_menu.addAction( self.exit )

        self.exit.setShortcut( 'CTRL+X' )

        self.save_mesh.setEnabled( False )
        self.save_data.setEnabled( False )

        self.open_mesh.triggered.connect( self.open_mesh_file )
        self.append_data.triggered.connect( self.append_data_file )
        self.open_dfield.triggered.connect( self.open_dist_field_file )
        self.import_mesh.triggered.connect( self.import_mesh_file )
        self.save_mesh.triggered.connect( self.save_mesh_file )
        self.save_data.triggered.connect( self.save_data_file )
        #self.exit.triggered.connect( super(MainWindow, self).quit )
    
        self.view_menu = QMenu('View')
        self.view_reset = self.view_menu.addAction( 'Reset' )
        self.view_reset.triggered.connect( self.ResetView )
        self.menuBar().addMenu( self.view_menu )
        
    def ResetView(self):
        #self.view.Set( 15.0f, 75.0f, 5.0f, (0,0,0), (0,1,0) )
        self.Save('view.txt')
        None
        
    def open_mesh_file(self):
        #if defined(WIN32)
        #    QApplication::setOverrideCursor(Qt::WaitCursor)
        #endif

        '''
        Data::Mesh::SolidMesh    * smesh = 0
        Data::Mesh::PointMesh    * pmesh = 0
        Data::PointData          * pdata = 0
        Data::FiberDirectionData * fdata = 0
        '''
        
        pmesh = HeartDock.OpenPointMesh()
        
        if pmesh:
            smesh = HeartDock.OpenSolidMesh()
        
        if smesh:
            fdata = HeartDock.OpenFiberData()
            pdata = HeartDock.OpenPointData()
        
        if pdata:
            self.cur_dock = HeartDock()
            #self.cur_dock = HeartDock(view, pmesh, smesh, fdata, self )
            self.addDockWidget( Qt.RightDockWidgetArea, self.cur_dock )
            self.cur_dock.SetPointData( pdata )
            self.save_mesh.setEnabled(True)
            self.save_data.setEnabled(True)       
        else:
            if pmesh: 
                pmesh = None
            if smesh: 
                smesh = None
            if pdata: 
                pdata = None
            if fdata: 
                fdata = None
        
        QApplication.restoreOverrideCursor()

    def import_mesh_file(self):
        if self.cur_dock == 0:
            return
    
        #if defined(WIN32)
        #    QApplication::setOverrideCursor(Qt::WaitCursor)
        #endif
    
        smesh = 0 #Data::Mesh::SolidMesh
        pmesh = 0 #Data::Mesh::PointMesh
        
        pmesh = HeartDock.OpenPointMesh()
    
        if pmesh:
            smesh = HeartDock.OpenSolidMesh( )
            self.cur_dock.AddImportedMesh( pmesh, smesh )
        else:
            if pmesh: 
                pmesh = 0
            if smesh: 
                smesh = 0
    
        QApplication.restoreOverrideCursor()

    def append_data_file(self):
        #if defined(WIN32)
        #    QApplication::setOverrideCursor(Qt::WaitCursor)
        #endif
    
        if self.cur_dock != 0 :
            pdata = HeartDock.OpenPointData( self.cur_dock.GetPointData() )
            if pdata: self.cur_dock.SetPointData( pdata )
    
        QApplication.restoreOverrideCursor()


    def open_dist_field_file(self):
        dfield = HeartDock.OpenDistanceField()
        if dfield: self.cur_dock.SetDistanceFieldData( dfield )


    def save_mesh_file(self):
        #if defined(WIN32)
        #    QApplication::setOverrideCursor(Qt::WaitCursor)
        #endif
    
        '''
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
        '''
        QApplication.restoreOverrideCursor()

    def save_data_file(self):
        #if defined(WIN32)
        #    QApplication::setOverrideCursor(Qt::WaitCursor)
        #endif
    
        '''
        Data::PointData * pdata = ( cur_dock == 0 ) ? 0 : cur_dock.GetPointData()
    
        if pdata != 0 :
            save_file = saveDialog( tr('Save to Point Data File'), QString('Point Data File (*.pdata)') )
            if save_file.size() > 0 :
                pdata.Save( save_file.toLocal8Bit().data() )
        '''
    
        QApplication.restoreOverrideCursor()
        