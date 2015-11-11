#ifndef HEARTDOCK_H
#define HEARTDOCK_H

#include <QDockWidget>
#include <QSplitter>
#include <QTableWidget>

#include <muView/ParallelCoordinates.h>
#include <muView/RenderEngine.h>
#include <QT/QConself.trolWidget.h>


#include <SCI/Camera/ThirdPersonCameraConself.trols.h>
#include <Data/FiberDirectionData.h>
#include <Data/DistanceField.h>

from PyQt5.QtWidgets import QSplitter, QTableWidget, QDockWidget, QTabWidget 
from PyQt5.QtWidgets import QRadioButton, QLabel
from PyQt5.QtWidgets import QSpinBox, QCheckBox, QPushButton, QWidget, QGridLayout
from PyQt5.QtCore import Qt, QSize
from common.QT import QExtendedMainWindow, QControlWidget
import PyQt5

class HeartDock(QDockWidget):
    def __init__(self, pView=None, _pmesh=None, _smesh=None, _fdata=None, parent=None):
        #HeartDock(SCI::ThirdPersonCameraConself.trols * pView, Data::Mesh::PointMesh *
        # _pmesh, Data::Mesh::SolidMesh * _smesh, Data::FiberDirectionData * _fdata,
        # QWidget *parent = 0);
        super(QDockWidget, self).__init__()
        
        self.pdata     = None   #Data::PointData          *
        self.pmesh     = None  #Data::Mesh::PointMesh    *
        self.tdata     = None  #Data::Mesh::SolidMesh    *
        self.fdata     = None  #Data::FiberDirectionData * 
        self.dfield    = None #Data::DistanceFieldSet   * 
    
        self.sp_widget  = None  #QSplitter           * 
        self.vp_widget  = None  #QSplitter           * 
        self.tb_widget  = None  #QTabWidget          * 
        
        #self.pr_widget  = None  #ParallelCoordinates * 
        self.render_engine  = None #RenderEngine 
        
        self.init(pView,_pmesh,_smesh,_fdata,parent)

    def init(self,pView,_pmesh,_smesh,_fdata,parent):
        self.dfield = 0
        self.pdata  = 0
        self.pmesh  = _pmesh
        self.tdata  = _smesh
        self.fdata  = _fdata
        
        self.vp_widget = QSplitter( Qt.Vertical )
        self.sp_widget = QSplitter( Qt.Horizontal )
    
        sp0 = QSplitter( Qt.Horizontal )
        sp1 = QSplitter( Qt.Horizontal )
    
        #self.pr_widget = ParallelCoordinates( 0 )
        
        self.tb_widget = QTabWidget()
        
        #sp0.addWidget( self.render_engine.re )
        #sp0.addWidget( self.render_engine.pca )
    
        '''
        sp1.addWidget( self.render_engine.re2[0]) )
        sp1.addWidget( self.render_engine.re2[1]) )
        sp1.addWidget( self.render_engine.re2[2]) )
        '''
        
        self.vp_widget.addWidget( sp0 )
        self.vp_widget.addWidget( sp1 )
#        self.vp_widget.addWidget( self.pr_widget )
        self.sp_widget.addWidget( self.vp_widget )
        self.sp_widget.addWidget( self.tb_widget )
                
        self.setWidget( self.sp_widget )
    
        drawBoxWidget = QControlWidget.QGroupControlWidget()

        draw0 = drawBoxWidget.addRadioButton('Points')
        draw1 = drawBoxWidget.addRadioButton('Network')
        draw2 = drawBoxWidget.addRadioButton('Volume Rendering')
        draw3 = drawBoxWidget.addRadioButton('Isosurfacing')
        draw4 = drawBoxWidget.addRadioButton('Distance Field')

        draw0.setChecked(True)

        '''
        draw0.clicked.connect(&(render_engine).setDrawModePoints)
        draw1.clicked.connect(&(render_engine).setDrawModeNetwork)
        draw2.clicked.connect(&(render_engine).setDrawModeVolumeRendering)
        draw3.clicked.connect(&(render_engine).setDrawModeIsosurfacing)
        draw4.clicked.connect(&(render_engine).setDrawModeDistanceField)
        '''

        colorBoxWidget = QWidget()
    
        color0 = QRadioButton( 'Dimension Value' )
        color7 = QRadioButton( 'Min Value' )
        color1 = QRadioButton( 'Mean Value' )
        color8 = QRadioButton( 'Max Value' )
        color2 = QRadioButton( 'St Dev' )
        color3 = QRadioButton( 'Clustering' )
        color4 = QRadioButton( 'Isovalue' )
        color5 = QRadioButton( 'PCA Painting' )
        color6 = QRadioButton( 'Fiber Direction' )
        color0.setChecked(True)

        dimension_label = QLabel('Dimension')
        dimension_spinner = QSpinBox()  
        dimension_spinner.setRange(0,40)
        dimension_spinner.setValue(0)
        

        cluster_count_label = QLabel('Clusters')
        cluster_count_spinner = QSpinBox( )
        cluster_count_spinner.setRange(2,40)
        cluster_count_spinner.setValue( 12 )

        cluster_type = QControlWidget.QControlWidget()
    
        #ct0 = cluster_type.addRadioButton( 'L2 Norm' )
        #ct1 = cluster_type.addRadioButton( 'Pearson Correlation' )
        #ct2 = cluster_type.addRadioButton( 'Histogram Difference' )
        #ct0.setChecked( self.true )
        
        '''
        ct0.clicked.connect(&(render_engine).setClusterTypeL2Norm)
        ct1.clicked.connect(&(render_engine).setClusterTypePearson)
        ct2.clicked.connect(&(render_engine).setClusterTypeHistogram)
        '''

        cluster_iteration_label = QLabel( 'Iterations' )
        cluster_iteration_spinner = QSpinBox( )
        cluster_iteration_spinner.setRange(1,40)
        cluster_iteration_spinner.setValue( 5 )

        cluster_histogram = QCheckBox( 'Histogram' )
        cluster_histogram.setChecked( True )

        cluster_recalculate = QPushButton( self.tr('Recalculate') )
        pca_sel_color = QPushButton( self.tr('PCA: Select Paint Color') )

        pca_dim0_label = QLabel(self.tr('PCA X Dimension'))
        pca_dim0_spinner = QSpinBox( )
        pca_dim0_spinner.setRange(0,100)
        pca_dim0_spinner.setValue( 0 )

        pca_dim1_label = QLabel(self.tr('PCA Y Dimension'))
        pca_dim1_spinner = QSpinBox( )
        pca_dim1_spinner.setRange(0,100)
        pca_dim1_spinner.setValue( 1 )

        '''
        color0.clicked.connect(&(render_engine).setColorModeDimension)
        color1.clicked.connect(&(render_engine).setColorModeMedian)
        color2.clicked.connect(&(render_engine).setColorModeStDev)
        color3.clicked.connect(&(render_engine).setColorModeCluster)
        color4.clicked.connect(&(render_engine).setColorModeIsovalue)
        color5.clicked.connect(&(render_engine).setColorModePCA)
        color6.clicked.connect(&(render_engine).setColorModeFibers)
        color7.clicked.connect(&(render_engine).setColorModeMin)
        color8.clicked.connect(&(render_engine).setColorModeMax)

        pca_sel_color.clicked.connect(&(render_engine.pca).selectPaintColor)
        dimension_spinner.valueChanged.connect(&(render_engine).setDimension)

        cluster_count_spinner.valueChanged.connect(&(render_engine).setClusterCount)
        cluster_iteration_spinner.valueChanged.connect(&(render_engine).setClusterIterations)
        cluster_recalculate.clicked.connect(&(render_engine).setClusterRecalculate)
        cluster_histogram.clicked.connect(&(render_engine).setClusterHistogram)
        '''

        '''
        color0.clicked.connect(self.pr_widget.Reset)
        color1.clicked.connect(self.pr_widget.Reset)
        color2.clicked.connect(self.pr_widget.Reset)
        color3.clicked.connect(self.pr_widget.Reset)
        color4.clicked.connect(self.pr_widget.Reset)
        color5.clicked.connect(self.pr_widget.Reset)
        color6.clicked.connect(self.pr_widget.Reset)
        color7.clicked.connect(self.pr_widget.Reset)
        color8.clicked.connect(self.pr_widget.Reset)
        '''

        #dimension_spinner.valueChanged.connect(self.pr_widget.Reset)

        #cluster_count_spinner.valueChanged.connect(self.pr_widget.Reset)
        #cluster_iteration_spinner.valueChanged.connect(self.pr_widget.Reset)
        #cluster_recalculate.clicked.connect(self.pr_widget.Reset)
        #cluster_histogram.clicked.connect(self.pr_widget.Reset)

#        pca_dim0_spinner.valueChanged.connect(&(render_engine.pca).ModifyPCADim0)
#        pca_dim1_spinner.valueChanged.connect(&(render_engine.pca).ModifyPCADim1)

        row = 0
        colorLayout = QGridLayout( )
        
        row+=1;colorLayout.addWidget( color0,             row, 0, 1, 3 )
        row+=1;colorLayout.addWidget( dimension_label,            row,   1, 1, 1 )
        row+=1;colorLayout.addWidget( dimension_spinner,          row, 2, 1, 1 )
        row+=1;colorLayout.addWidget( color1,                     row, 0, 1, 3 )
        row+=1;colorLayout.addWidget( color7,                     row, 0, 1, 3 )
        row+=1;colorLayout.addWidget( color8,                     row, 0, 1, 3 )
        row+=1;colorLayout.addWidget( color2,                     row, 0, 1, 3 )
        row+=1;colorLayout.addWidget( color3,                     row, 0, 1, 3 )
        row+=1;colorLayout.addWidget( cluster_histogram,          row, 1, 1, 2 )
        colorLayout.addWidget( cluster_count_label,        row,   1, 1, 1 )
        row+=1;colorLayout.addWidget( cluster_count_spinner,      row, 2, 1, 1 )
        #row+=1;colorLayout.addWidget( cluster_type,               row, 1, 1, 1 )
        colorLayout.addWidget( cluster_iteration_label,    row,   1, 1, 1 )
        row+=1;colorLayout.addWidget( cluster_iteration_spinner,  row, 2, 1, 1 )
        row+=1;colorLayout.addWidget( cluster_recalculate,        row, 1, 1, 2 )
        row+=1;colorLayout.addWidget( color4,                     row, 0, 1, 3 )
        row+=1;colorLayout.addWidget( color5,                     row, 0, 1, 3 )
        row+=1;colorLayout.addWidget( pca_sel_color,              row, 0, 1, 3 )
        row+=1;colorLayout.addWidget( color6,                     row, 0, 1, 3 )
        row+=1;colorLayout.addWidget( pca_dim0_label,             row,   1, 1, 1 )
        row+=1;colorLayout.addWidget( pca_dim0_spinner,           row, 2, 1, 1 )
        colorLayout.addWidget( pca_dim1_label,             row,   1, 1, 1 )
        row+=1;colorLayout.addWidget( pca_dim1_spinner,           row, 2, 1, 1 )
        colorLayout.setRowStretch( row, 1 )
        colorBoxWidget.setLayout( colorLayout )
        
        
        #render_engine.SetParallelCoordinateView( self.pr_widget )
        #render_engine.SetData( self.pdata, self.pmesh, self.tdata )
        #render_engine.SetFiberData( selffdata );
        
        self.tb_widget.setTabPosition( self.tb_widget.West )
        self.tb_widget.addTab( drawBoxWidget, self.tr( 'Draw Mode' ) )
        self.tb_widget.addTab( colorBoxWidget, self.tr( 'Color Mode' ) )
        #self.tb_widget.addTab( isoBoxWidget, self.tr( 'Isosurfacing' ) )
        #self.tb_widget.addTab( clipBoxWidget, self.tr( 'Clip Planes' ) )
        
    def GetPointData(self):
        return self.pdata
    
    def GetPointMesh(self): 
         return self.pmesh
     
    def GetSolidMesh(self): 
        return self.tdata
    
    def GetFiberData(self): 
        return self.fdata
    
    def GetDistanceField(self): 
        return self.dfield
    
    def minimumSizeHint(self):
        qsize = QSize(50,50)
        return qsize
        
    def sizeHint(self):
        return QSize( 500, 500)
    
    def SetPointData(self, _pdata ):
        if self.pdata != _pdata:
            pdata = _pdata        
            #self.render_engine.SetData( pdata, pmesh, tdata )
            #self.setWindowTitle( pdata.GetFilename() )
    
    def SetDistanceFieldData(self, _dfield ):    
        if self.dfield != _dfield: 
            dfield = _dfield
            #render_engine.SetDistanceFieldData( dfield )
    
    def AddImportedMesh(self, _pmesh, _tdata ):
        #render_engine.AddImportedMesh( _pmesh,_tdata )
        return
    
    '''
    static Data::Mesh::PointMesh    * OpenPointMesh( );
    static Data::Mesh::SolidMesh    * OpenSolidMesh( );
    static Data::DistanceFieldSet   * OpenDistanceField( );
    static Data::PointData          * OpenPointData( Data::PointData * pdata = 0 );
    static Data::FiberDirectionData * OpenFiberData( );
    '''

    @staticmethod
    def OpenPointMesh():
        fname = QExtendedMainWindow.QExtendedMainWindow.openDialog( 'Load a Point Mesh', \
                    'Any (*.point *.point.gz *.pts);; Point File (*.point);;Compressed Point \
                    File (*.point.gz);; PTS File (*.pts)' )  
    
        # Loading a point data file
        if( fname.endsWith('.point') or fname.endsWith('.point.gz') ):
            return 0
            #return Data.Mesh.PointMesh( fname.toLocal8Bit().data(), self.true, fname.endsWith('.gz') )
        # Loading raw pts data file
        elif fname.endsWith('.pts'): 
            #return Data.Mesh.PointMesh( fname.toLocal8Bit().data(), False, False )
            return 0
        
        return 0

    @staticmethod
    def OpenDistanceField():
        fname = QExtendedMainWindow.QExtendedMainWindow.openDialog( 'Load a Distance Field', \
                    'Distance Field File (*.df *.dfield)' )

        if fname.endsWith('.dfield') or fname.endsWith('.df'):
            #return Data.DistanceFieldSet( fname.toLocal8Bit().data() )
            return 0
        
        return 0

    @staticmethod
    def OpenSolidMesh():
        mesh_name = QExtendedMainWindow.QExtendedMainWindow.openDialog( 'Load an Associated Mesh', \
                        'Any (*.tet *.hex *.btet *.btet.gz *.bhex);; Tet File (*.tet);; Binary Tets File (*.btet *.btet.gz);; Hex File (*.hex);; Binary Hex File (*.bhex)')

        if mesh_name.endsWith('.btet') or mesh_name.endsWith('.btet.gz') or mesh_name.endsWith('.tet'):
            #return Data.Mesh.TetMesh( mesh_name.toLocal8Bit().data() )
            return 0
    
        if mesh_name.endsWith('.bhex') or mesh_name.endsWith('.hex'):
            #return Data.Mesh.HexMesh( mesh_name.toLocal8Bit().data() )
            return 0
        
        return 0

    @staticmethod
    def OpenPointData(pdata ):
        fname_list = QExtendedMainWindow.QExtendedMainWindow.openListDialog( 'Load Data Files', \
                        'All Data Files (*.pdata *.txt *.sol);;Point Data File (*.pdata);;Text Data Files (*.txt);;Solution File (*.sol)') 

        for i in range( 0, fname_list.size(), 1 ):
            #Data.PointData ptmp0 = pdata
            #Data.PointData ptmp1 = Data.PointData( fname_list.at(i).toLocal8Bit().data(), fname_list.at(i).endsWith('.pdata') )
            
            #if pdata == 0:
            #    pdata = ptmp1
            #else:
            pdata = 0#Data.PointData( *ptmp0, *ptmp1 )
        
        return pdata

    @staticmethod
    def OpenFiberData():
        fibs_name = QExtendedMainWindow.QExtendedMainWindow.openDialog( 'Load Fiber Data',\
                        'Any (*.txt *.fibs);; Fiber File (*.txt);; Binary Fiber File (*.fibs)') 

        if fibs_name.endsWith('.txt') or fibs_name.endsWith('.fibs'):
            #return Data.FiberDirectionData( fibs_name.toLocal8Bit().data(), fibs_name.endsWith('.fibs') )
            return 0
            
        return 0
