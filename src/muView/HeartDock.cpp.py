#include <muView/HeartDock.h>

#include <QFileDialog>
#include <QT/QExtendedMainWindow.h>

HeartDock.HeartDock(SCI.ThirdPersonCameraControls * pView, * _pmesh, * _smesh, *_fdata, *parent) : QDockWidget(parent), render_engine( pView )
{

    vp_widget = QSplitter( Qt.Vertical )
    sp_widget = QSplitter( Qt.Horizontal )

    QSplitter sp0 = QSplitter( Qt.Horizontal )
    QSplitter sp1 = QSplitter( Qt.Horizontal )

    pr_widget = ParallelCoordinates( 0 )
    tb_widget = QTabWidget( )

    sp0.addWidget( &(render_engine.re) )
#    sp0.addWidget( &(render_engine.pca) )

    sp1.addWidget( &(render_engine.re2[0]) )
    sp1.addWidget( &(render_engine.re2[1]) )
    sp1.addWidget( &(render_engine.re2[2]) )

    vp_widget.addWidget( sp0 )
    vp_widget.addWidget( sp1 )
    vp_widget.addWidget( pr_widget )

    sp_widget.addWidget( vp_widget )
    sp_widget.addWidget( tb_widget )

    setWidget( sp_widget )

    QT.QControlWidget drawBoxWidget = QT.QControlWidget( )
    {
        QRadioButton draw0 = drawBoxWidget.addRadioButton( tr("Points")           )
        QRadioButton draw1 = drawBoxWidget.addRadioButton( tr("Network")          )
        QRadioButton draw2 = drawBoxWidget.addRadioButton( tr("Volume Rendering") )
        QRadioButton draw3 = drawBoxWidget.addRadioButton( tr("Isosurfacing")     )
        QRadioButton draw4 = drawBoxWidget.addRadioButton( tr("Distance Field")   )

        draw0.setChecked(True)

        draw0.clicked.connect(&(render_engine).setDrawModePoints)
        draw1.clicked.connect(&(render_engine).setDrawModeNetwork)
        draw2.clicked.connect(&(render_engine).setDrawModeVolumeRendering)
        draw3.clicked.connect(&(render_engine).setDrawModeIsosurfacing)
        draw4.clicked.connect(&(render_engine).setDrawModeDistanceField)
    }

    QWidget   colorBoxWidget = QWidget( )
    {
        QRadioButton color0 = QRadioButton( tr("Dimension Value") )
        QRadioButton color7 = QRadioButton( tr("Min Value") )
        QRadioButton color1 = QRadioButton( tr("Mean Value") )
        QRadioButton color8 = QRadioButton( tr("Max Value") )
        QRadioButton color2 = QRadioButton( tr("St Dev") )
        QRadioButton color3 = QRadioButton( tr("Clustering") )
        QRadioButton color4 = QRadioButton( tr("Isovalue") )
        QRadioButton color5 = QRadioButton( tr("PCA Painting") )
        QRadioButton color6 = QRadioButton( tr("Fiber Direction") )
        color0.setChecked(True)

        QLabel dimension_label = QLabel(tr("Dimension"))
        QSpinBox dimension_spinner = QSpinBox( )
        dimension_spinner.setRange(0,40)
        dimension_spinner.setValue(0)

        QLabel cluster_count_label = QLabel(tr("Clusters"))
        QSpinBox cluster_count_spinner = QSpinBox( )
        cluster_count_spinner.setRange(2,40)
        cluster_count_spinner.setValue( 12 )

        QT.QControlWidget cluster_type = QT.QControlWidget( )
        {
            QRadioButton ct0 = cluster_type.addRadioButton( tr("L2 Norm") )
            QRadioButton ct1 = cluster_type.addRadioButton( tr("Pearson Correlation") )
            QRadioButton ct2 = cluster_type.addRadioButton( tr("Histogram Difference") )
            ct0.setChecked( True )
            ct0.clicked.connect(&(render_engine).setClusterTypeL2Norm)
            ct1.clicked.connect(&(render_engine).setClusterTypePearson)
            ct2.clicked.connect(&(render_engine).setClusterTypeHistogram)
        }

        QLabel cluster_iteration_label = QLabel(tr("Iterations"))
        QSpinBox cluster_iteration_spinner = QSpinBox( )
        cluster_iteration_spinner.setRange(1,40)
        cluster_iteration_spinner.setValue( 5 )

        QCheckBox cluster_histogram = QCheckBox( tr("Histogram") )
        cluster_histogram.setChecked( True )

        QPushButton cluster_recalculate = QPushButton( tr("Recalculate") )

        QPushButton pca_sel_color = QPushButton( tr("PCA: Select Paint Color") )

        QLabel   pca_dim0_label = QLabel(tr("PCA X Dimension"))
        QSpinBox pca_dim0_spinner = QSpinBox( )
        pca_dim0_spinner.setRange(0,100)
        pca_dim0_spinner.setValue( 0 )

        QLabel   pca_dim1_label = QLabel(tr("PCA Y Dimension"))
        QSpinBox pca_dim1_spinner = QSpinBox( )
        pca_dim1_spinner.setRange(0,100)
        pca_dim1_spinner.setValue( 1 )

        color0.clicked.connect(&(render_engine).setColorModeDimension)
        color1.clicked.connect(&(render_engine).setColorModeMedian)
        color2.clicked.connect(&(render_engine).setColorModeStDev)
        color3.clicked.connect(&(render_engine).setColorModeCluster)
        color4.clicked.connect(&(render_engine).setColorModeIsovalue)
        color5.clicked.connect(&(render_engine).setColorModePCA)
        color6.clicked.connect(&(render_engine).setColorModeFibers)
        color7.clicked.connect(&(render_engine).setColorModeMin)
        color8.clicked.connect(&(render_engine).setColorModeMax)

#        pca_sel_color.clicked.connect(&(render_engine.pca).selectPaintColor)

        dimension_spinner.valueChanged.connect(&(render_engine).setDimension)

        cluster_count_spinner.valueChanged.connect(&(render_engine).setClusterCount)
        cluster_iteration_spinner.valueChanged.connect(&(render_engine).setClusterIterations)
        cluster_recalculate.clicked.connect(&(render_engine).setClusterRecalculate)
        cluster_histogram.clicked.connect(&(render_engine).setClusterHistogram)

        color0.clicked.connect(pr_widget.Reset)
        color1.clicked.connect(pr_widget.Reset)
        color2.clicked.connect(pr_widget.Reset)
        color3.clicked.connect(pr_widget.Reset)
        color4.clicked.connect(pr_widget.Reset)
        color5.clicked.connect(pr_widget.Reset)
        color6.clicked.connect(pr_widget.Reset)
        color7.clicked.connect(pr_widget.Reset)
        color8.clicked.connect(pr_widget.Reset)

        dimension_spinner.valueChanged.connect(pr_widget.Reset)

        cluster_count_spinner.valueChanged.connect(pr_widget.Reset)
        cluster_iteration_spinner.valueChanged.connect(pr_widget.Reset)
        cluster_recalculate.clicked.connect(pr_widget.Reset)
        cluster_histogram.clicked.connect(pr_widget.Reset)

#        pca_dim0_spinner.valueChanged.connect(&(render_engine.pca).ModifyPCADim0)
#        pca_dim1_spinner.valueChanged.connect(&(render_engine.pca).ModifyPCADim1)

        row = 0
        QGridLayout colorLayout = QGridLayout( )
        colorLayout.addWidget( color0,                     row++, 0, 1, 3 )
        colorLayout.addWidget( dimension_label,            row,   1, 1, 1 )
        colorLayout.addWidget( dimension_spinner,          row++, 2, 1, 1 )
        colorLayout.addWidget( color1,                     row++, 0, 1, 3 )
        colorLayout.addWidget( color7,                     row++, 0, 1, 3 )
        colorLayout.addWidget( color8,                     row++, 0, 1, 3 )
        colorLayout.addWidget( color2,                     row++, 0, 1, 3 )
        colorLayout.addWidget( color3,                     row++, 0, 1, 3 )
        colorLayout.addWidget( cluster_histogram,          row++, 1, 1, 2 )
        colorLayout.addWidget( cluster_count_label,        row,   1, 1, 1 )
        colorLayout.addWidget( cluster_count_spinner,      row++, 2, 1, 1 )
        colorLayout.addWidget( cluster_type,               row++, 1, 1, 1 )
        colorLayout.addWidget( cluster_iteration_label,    row,   1, 1, 1 )
        colorLayout.addWidget( cluster_iteration_spinner,  row++, 2, 1, 1 )
        colorLayout.addWidget( cluster_recalculate,        row++, 1, 1, 2 )
        colorLayout.addWidget( color4,                     row++, 0, 1, 3 )
        colorLayout.addWidget( color5,                     row++, 0, 1, 3 )
        colorLayout.addWidget( pca_sel_color,              row++, 0, 1, 3 )
        colorLayout.addWidget( color6,                     row++, 0, 1, 3 )
        colorLayout.addWidget( pca_dim0_label,             row,   1, 1, 1 )
        colorLayout.addWidget( pca_dim0_spinner,           row++, 2, 1, 1 )
        colorLayout.addWidget( pca_dim1_label,             row,   1, 1, 1 )
        colorLayout.addWidget( pca_dim1_spinner,           row++, 2, 1, 1 )

        colorLayout.setRowStretch( row, 1 )

        colorBoxWidget.setLayout( colorLayout )
    }



    QWidget   isoBoxWidget = QWidget( )
    {

        QCheckBox show_d_iso = QCheckBox( tr("Dimension Isosurface") )
        QCheckBox show_min_iso = QCheckBox( tr("Minimum Isosurface") )
        QCheckBox show_mean_iso = QCheckBox( tr("Mean Isosurface") )
        QCheckBox show_max_iso = QCheckBox( tr("Maximum Isosurface") )
        QLabel iso_label = QLabel(tr("Iso value"))
        QDoubleSpinBox iso_spinner = QDoubleSpinBox( )
        iso_spinner.setRange(-15,15)
        iso_spinner.setValue(0)
        QPushButton volume = QPushButton( tr("Volume") )

        show_d_iso.clicked.connect(&(render_engine).setDimIsosurface)
        show_min_iso.clicked.connect(&(render_engine).setMinIsosurface)
        show_mean_iso.clicked.connect(&(render_engine).setMeanIsosurface)
        show_max_iso.clicked.connect(&(render_engine).setMaxIsosurface)
        iso_spinner.valueChanged.connect(&(render_engine).setIsovalue)
        iso_spinner.valueChanged.connect(pr_widget.Reset)
        volume.clicked.connect(&(render_engine).calculateSubVolume)


        row = 0
        QGridLayout isoLayout = QGridLayout( )
        isoLayout.addWidget( show_d_iso,                 row++, 1, 1, 3 )
        isoLayout.addWidget( show_min_iso,               row++, 1, 1, 3 )
        isoLayout.addWidget( show_mean_iso,              row++, 1, 1, 3 )
        isoLayout.addWidget( show_max_iso,               row++, 1, 1, 3 )
        isoLayout.addWidget( iso_label,                  row,   1, 1, 1 )
        isoLayout.addWidget( iso_spinner,                row++, 2, 1, 1 )
        isoLayout.addWidget( volume,                     row++, 1, 1, 3 )
        isoLayout.setRowStretch( row, 1 )

        isoBoxWidget.setLayout( isoLayout )
    }


    QWidget   clipBoxWidget = QWidget( )
    {
        QCheckBox e_clipX = QCheckBox( tr("Clip X") )
        QCheckBox e_clipY = QCheckBox( tr("Clip Y") )
        QCheckBox e_clipZ = QCheckBox( tr("Clip Z") )
        QCheckBox f_clipX = QCheckBox( tr("flip") )
        QCheckBox f_clipY = QCheckBox( tr("flip") )
        QCheckBox f_clipZ = QCheckBox( tr("flip") )
        QDoubleSpinBox v_clipX = QDoubleSpinBox( )
        QDoubleSpinBox v_clipY = QDoubleSpinBox( )
        QDoubleSpinBox v_clipZ = QDoubleSpinBox( )
        v_clipX.setRange(-15,15)
        v_clipX.setSingleStep(0.05f)
        v_clipX.setValue(0)
        v_clipY.setRange(-15,15)
        v_clipY.setSingleStep(0.05f)
        v_clipY.setValue(0)
        v_clipZ.setRange(-15,15)
        v_clipZ.setValue(0)
        v_clipZ.setSingleStep(0.05f)

        e_clipX.clicked.connect(&(render_engine).setClipXEnable)
        e_clipY.clicked.connect(&(render_engine).setClipYEnable)
        e_clipZ.clicked.connect(&(render_engine).setClipZEnable)

        v_clipX.valueChanged.connect(&(render_engine).setClipXVal)
        v_clipY.valueChanged.connect(&(render_engine).setClipYVal)
        v_clipZ.valueChanged.connect(&(render_engine).setClipZVal)

        f_clipX.clicked.connect(&(render_engine).setClipXFlip)
        f_clipY.clicked.connect(&(render_engine).setClipYFlip)
        f_clipZ.clicked.connect(&(render_engine).setClipZFlip)

        row = 0
        QGridLayout clipLayout = QGridLayout( )
        clipLayout.addWidget( e_clipX, row,   0, 1, 1 )
        clipLayout.addWidget( v_clipX, row,   1, 1, 1 )
        clipLayout.addWidget( f_clipX, row++, 2, 1, 1 )
        clipLayout.addWidget( e_clipY, row,   0, 1, 1 )
        clipLayout.addWidget( v_clipY, row,   1, 1, 1 )
        clipLayout.addWidget( f_clipY, row++, 2, 1, 1 )
        clipLayout.addWidget( e_clipZ, row,   0, 1, 1 )
        clipLayout.addWidget( v_clipZ, row,   1, 1, 1 )
        clipLayout.addWidget( f_clipZ, row++, 2, 1, 1 )
        clipLayout.setRowStretch( row, 1 )

        clipBoxWidget.setLayout( clipLayout )
    }


    tb_widget.setTabPosition( tb_widget.West )
    tb_widget.addTab(  drawBoxWidget, tr( "Draw Mode" ) )
    tb_widget.addTab( colorBoxWidget, tr( "Color Mode" ) )
    tb_widget.addTab(   isoBoxWidget, tr( "Isosurfacing" ) )
    tb_widget.addTab(  clipBoxWidget, tr( "Clip Planes" ) )


    dfield = 0
    pdata  = 0
    pmesh  = _pmesh
    tdata  = _smesh
    fdata  = _fdata

    render_engine.SetParallelCoordinateView( pr_widget )
    render_engine.SetData( pdata, pmesh, tdata )
    render_engine.SetFiberData( fdata )

}

void HeartDock.SetPointData( Data.PointData * _pdata )
{
    if( pdata != _pdata )
    {
        if(pdata) delete pdata
        pdata = _pdata
        render_engine.SetData( pdata, pmesh, tdata )
        setWindowTitle( tr(pdata.GetFilename().c_str()) )
    }
}

void HeartDock.SetDistanceFieldData( Data.DistanceFieldSet * _dfield )
{
    if( dfield != _dfield )
    {
        if(dfield) delete dfield
        dfield = _dfield
        render_engine.SetDistanceFieldData( dfield )
    }
}

void HeartDock.AddImportedMesh( Data.Mesh.PointMesh * _pmesh, * _tdata )
{
    render_engine.AddImportedMesh( _pmesh,_tdata )
}



Data.Mesh.PointMesh * HeartDock.OpenPointMesh( )
{

    fname = QT.QExtendedMainWindow.openDialog( tr("Load a Point Mesh"), QString("Any (*.point *.point.gz *.pts);; Point File (*.point);;Compressed Point File (*.point.gz);; PTS File (*.pts)") )

    # Loading a point data file
    if( fname.endsWith(".point") or fname.endsWith(".point.gz") )
    {
        return Data.Mesh.PointMesh( fname.toLocal8Bit().data(), True, fname.endsWith(".gz") )
    }
    # Loading raw pts data file
    elif( fname.endsWith(".pts") )
    {
        return Data.Mesh.PointMesh( fname.toLocal8Bit().data(), False, False )
    }

    return 0

}

Data.DistanceFieldSet * HeartDock.OpenDistanceField( )
{

    fname = QT.QExtendedMainWindow.openDialog( tr("Load a Distance Field"), QString("Distance Field File (*.df *.dfield)") )

    if( fname.endsWith(".dfield") or fname.endsWith(".df") )
    {
        return Data.DistanceFieldSet( fname.toLocal8Bit().data() )
    }

    return 0

}


Data.Mesh.SolidMesh * HeartDock.OpenSolidMesh( )
{

    mesh_name = QT.QExtendedMainWindow.openDialog( tr("Load an Associated Mesh"), QString("Any (*.tet *.hex *.btet *.btet.gz *.bhex);; Tet File (*.tet);; Binary Tets File (*.btet *.btet.gz);; Hex File (*.hex);; Binary Hex File (*.bhex)") )

    if( mesh_name.endsWith(".btet") or mesh_name.endsWith(".btet.gz") or mesh_name.endsWith(".tet") )
    {
        return Data.Mesh.TetMesh( mesh_name.toLocal8Bit().data() )
    }

    if( mesh_name.endsWith(".bhex") or mesh_name.endsWith(".hex") )
    {
        return Data.Mesh.HexMesh( mesh_name.toLocal8Bit().data() )
    }

    return 0

}

Data.PointData * HeartDock.OpenPointData( Data.PointData * pdata )
{

    fname_list = QT.QExtendedMainWindow.openListDialog( tr("Load Data Files"), QString("All Data Files (*.pdata *.txt *.sol);;Point Data File (*.pdata);;Text Data Files (*.txt);;Solution File (*.sol)") )

    for(i = 0; i < fname_list.size(); i++)
    {

        Data.PointData ptmp0 = pdata
        Data.PointData ptmp1 = Data.PointData( fname_list.at(i).toLocal8Bit().data(), fname_list.at(i).endsWith(".pdata") )

        if(pdata == 0)
        {
            pdata = ptmp1
        }
        else:
        {
            pdata = Data.PointData( *ptmp0, *ptmp1 )
            delete ptmp0
            delete ptmp1
        }
    }

    return pdata

}

Data.FiberDirectionData * HeartDock.OpenFiberData( )
{
    fibs_name = QT.QExtendedMainWindow.openDialog( tr("Load Fiber Data"), QString("Any (*.txt *.fibs);; Fiber File (*.txt);; Binary Fiber File (*.fibs)") )

    if( fibs_name.endsWith(".txt") or fibs_name.endsWith(".fibs") )
    {
        return Data.FiberDirectionData( fibs_name.toLocal8Bit().data(), fibs_name.endsWith(".fibs") )
    }

    return 0
}


