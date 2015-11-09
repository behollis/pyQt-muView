#ifndef HEARTDOCK_H
#define HEARTDOCK_H

#include <QDockWidget>
#include <QSplitter>
#include <QTableWidget>

#include <muView/ParallelCoordinates.h>
#include <muView/RenderEngine.h>
#include <QT/QControlWidget.h>


#include <SCI/Camera/ThirdPersonCameraControls.h>
#include <Data/FiberDirectionData.h>
#include <Data/DistanceField.h>

from PyQt5.QtWidgets import QSplitter, QTableWidget, QDockWidget, QTabWidget, QControlWidget, QRadioButton, QLabel
from PyQt5.QtWidgets import QSpinBox, QCheckBox, QPushButton, QWidget, QGridLayout
#from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class HeartDock(QDockWidget):
    def __init__(self):
        #HeartDock(SCI::ThirdPersonCameraControls * pView, Data::Mesh::PointMesh *
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
        
        self.pr_widget  = None  #ParallelCoordinates * 
        self.render_engine  = None #RenderEngine 
    
        self.init()

    def init(self):
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
        self.vp_widget.addWidget( self.pr_widget )
        self.sp_widget.addWidget( self.vp_widget )
        self.sp_widget.addWidget( self.tb_widget )
                
        self.setWidget( self.sp_widget )
    
        drawBoxWidget = QControlWidget()

        draw0 = drawBoxWidget.addRadioButton( tr('Points')           )
        draw1 = drawBoxWidget.addRadioButton( tr('Network')          )
        draw2 = drawBoxWidget.addRadioButton( tr('Volume Rendering') )
        draw3 = drawBoxWidget.addRadioButton( tr('Isosurfacing')     )
        draw4 = drawBoxWidget.addRadioButton( tr('Distance Field')   )

        draw0.setChecked(True)

        '''
        draw0.clicked.connect(&(render_engine).setDrawModePoints)
        draw1.clicked.connect(&(render_engine).setDrawModeNetwork)
        draw2.clicked.connect(&(render_engine).setDrawModeVolumeRendering)
        draw3.clicked.connect(&(render_engine).setDrawModeIsosurfacing)
        draw4.clicked.connect(&(render_engine).setDrawModeDistanceField)
        '''

        colorBoxWidget = QWidget()
    
        color0 = QRadioButton( tr('Dimension Value') )
        color7 = QRadioButton( tr('Min Value') )
        color1 = QRadioButton( tr('Mean Value') )
        color8 = QRadioButton( tr('Max Value') )
        color2 = QRadioButton( tr('St Dev') )
        color3 = QRadioButton( tr('Clustering') )
        color4 = QRadioButton( tr('Isovalue') )
        color5 = QRadioButton( tr('PCA Painting') )
        color6 = QRadioButton( tr('Fiber Direction') )
        color0.setChecked(True)

        dimension_label = QLabel(tr('Dimension'))
        dimension_spinner = QSpinBox()  
        dimension_spinner.setRange(0,40)
        dimension_spinner.setValue(0)

        cluster_count_label = QLabel(tr('Clusters'))
        cluster_count_spinner = QSpinBox( )
        cluster_count_spinner.setRange(2,40)
        cluster_count_spinner.setValue( 12 )

        cluster_type = QControlWidget()
    
        ct0 = cluster_type.addRadioButton( tr('L2 Norm') )
        ct1 = cluster_type.addRadioButton( tr('Pearson Correlation') )
        ct2 = cluster_type.addRadioButton( tr('Histogram Difference') )
        ct0.setChecked( True )
        
        '''
        ct0.clicked.connect(&(render_engine).setClusterTypeL2Norm)
        ct1.clicked.connect(&(render_engine).setClusterTypePearson)
        ct2.clicked.connect(&(render_engine).setClusterTypeHistogram)
        '''

        cluster_iteration_label = QLabel(tr('Iterations'))
        cluster_iteration_spinner = QSpinBox( )
        cluster_iteration_spinner.setRange(1,40)
        cluster_iteration_spinner.setValue( 5 )

        cluster_histogram = QCheckBox( tr('Histogram') )
        cluster_histogram.setChecked( True )

        cluster_recalculate = QPushButton( tr('Recalculate') )
        pca_sel_color = QPushButton( tr('PCA: Select Paint Color') )

        pca_dim0_label = QLabel(tr('PCA X Dimension'))
        pca_dim0_spinner = QSpinBox( )
        pca_dim0_spinner.setRange(0,100)
        pca_dim0_spinner.setValue( 0 )

        pca_dim1_label = QLabel(tr('PCA Y Dimension'))
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

        color0.clicked.connect(self.pr_widget.Reset)
        color1.clicked.connect(self.pr_widget.Reset)
        color2.clicked.connect(self.pr_widget.Reset)
        color3.clicked.connect(self.pr_widget.Reset)
        color4.clicked.connect(self.pr_widget.Reset)
        color5.clicked.connect(self.pr_widget.Reset)
        color6.clicked.connect(self.pr_widget.Reset)
        color7.clicked.connect(self.pr_widget.Reset)
        color8.clicked.connect(self.pr_widget.Reset)

        dimension_spinner.valueChanged.connect(self.pr_widget.Reset)

        cluster_count_spinner.valueChanged.connect(self.pr_widget.Reset)
        cluster_iteration_spinner.valueChanged.connect(self.pr_widget.Reset)
        cluster_recalculate.clicked.connect(self.pr_widget.Reset)
        cluster_histogram.clicked.connect(self.pr_widget.Reset)

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
        row+=1;colorLayout.addWidget( cluster_type,               row, 1, 1, 1 )
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
     
        tb_widget->setTabPosition( tb_widget->West );
        tb_widget->addTab(  drawBoxWidget, tr( 'Draw Mode' ) );
        tb_widget->addTab( colorBoxWidget, tr( 'Color Mode' ) );
        tb_widget->addTab(   isoBoxWidget, tr( 'Isosurfacing' ) );
        tb_widget->addTab(  clipBoxWidget, tr( 'Clip Planes' ) );

        dfield = 0;
        pdata  = 0;
        pmesh  = _pmesh;
        tdata  = _smesh;
        fdata  = _fdata;
    
        render_engine.SetParallelCoordinateView( pr_widget );
        render_engine.SetData( pdata, pmesh, tdata );
        render_engine.SetFiberData( fdata );

    def minimumSizeHint():
        return QSize(  50,  50); }
        
    def sizeHint():
        return QSize( 500, 500)
    
    def GetPointData():
        return pdata
    
     def GetPointMesh(): 
         return pmesh
     
    def GetSolidMesh(): 
        return tdata
    
    def GetFiberData(): 
        return fdata
    
    def GetDistanceField(): 
        return dfield

    def SetPointData( _pdata ):
        if pdata != _pdata:
            if pdata: 
                delete pdata
            pdata = _pdata
            self.render_engine.SetData( pdata, pmesh, tdata )
            self.setWindowTitle( pdata.GetFilename() )
    
    def SetDistanceFieldData( _dfield ):
        
        if( dfield != _dfield )
    
            if(dfield) delete dfield
            dfield = _dfield
            render_engine.SetDistanceFieldData( dfield )
    
    def AddImportedMesh( _pmesh, _tdata ):
        render_engine.AddImportedMesh( _pmesh,_tdata )

    def OpenPointMesh():
        fname = QT.QExtendedMainWindow.openDialog( tr('Load a Point Mesh'), QString('Any (*.point *.point.gz *.pts);; Point File (*.point);;Compressed Point File (*.point.gz);; PTS File (*.pts)') )
    
        # Loading a point data file
        if( fname.endsWith('.point') or fname.endsWith('.point.gz') ):
            return Data.Mesh.PointMesh( fname.toLocal8Bit().data(), True, fname.endsWith('.gz') )
        # Loading raw pts data file
        elif( fname.endsWith('.pts'): 
            return Data.Mesh.PointMesh( fname.toLocal8Bit().data(), False, False )
    
        return 0

    def OpenDistanceField( ):
        fname = QT.QExtendedMainWindow.openDialog( tr('Load a Distance Field'), QString('Distance Field File (*.df *.dfield)') )

        if( fname.endsWith('.dfield') or fname.endsWith('.df') )
            return Data.DistanceFieldSet( fname.toLocal8Bit().data() )

        return 0


    def OpenSolidMesh():
        mesh_name = QT.QExtendedMainWindow.openDialog( tr('Load an Associated Mesh'), QString('Any (*.tet *.hex *.btet *.btet.gz *.bhex);; Tet File (*.tet);; Binary Tets File (*.btet *.btet.gz);; Hex File (*.hex);; Binary Hex File (*.bhex)') )

        if( mesh_name.endsWith('.btet') or mesh_name.endsWith('.btet.gz') or mesh_name.endsWith('.tet') ):
            return Data.Mesh.TetMesh( mesh_name.toLocal8Bit().data() )
        
    
        if( mesh_name.endsWith('.bhex') or mesh_name.endsWith('.hex') ):
            return Data.Mesh.HexMesh( mesh_name.toLocal8Bit().data() )
    
        return 0

    def OpenPointData( pdata )
        fname_list = QT.QExtendedMainWindow.openListDialog( tr('Load Data Files'), QString('All Data Files (*.pdata *.txt *.sol);;Point Data File (*.pdata);;Text Data Files (*.txt);;Solution File (*.sol)') )

        for(i = 0; i < fname_list.size(); i++)

            Data.PointData ptmp0 = pdata
            Data.PointData ptmp1 = Data.PointData( fname_list.at(i).toLocal8Bit().data(), fname_list.at(i).endsWith('.pdata') )
    
            if pdata == 0:
                pdata = ptmp1
            else:
                pdata = Data.PointData( *ptmp0, *ptmp1 )
                delete ptmp0
                delete ptmp1
        
        return pdata

    def OpenFiberData():
        fibs_name = QT.QExtendedMainWindow.openDialog( tr('Load Fiber Data'), QString('Any (*.txt *.fibs);; Fiber File (*.txt);; Binary Fiber File (*.fibs)') )

        if( fibs_name.endsWith('.txt') or fibs_name.endsWith('.fibs') )
            return Data.FiberDirectionData( fibs_name.toLocal8Bit().data(), fibs_name.endsWith('.fibs') )

        return 0
