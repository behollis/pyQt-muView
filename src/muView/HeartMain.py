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

    MainWindow( QWidget * parent = 0 );
    ~MainWindow();

public slots:
    virtual void open_mesh_file();
    virtual void import_mesh_file();
    virtual void append_data_file();
    virtual void open_dist_field_file();
    virtual void save_mesh_file();
    virtual void save_data_file();

    void ResetView();

protected:

    SCI::ThirdPersonCameraControls   view;

    HeartDock  * cur_dock;

    QMenu      * file_menu;
    QAction    * open_mesh;
    QAction    * append_data;
    QAction    * open_dfield;
    QAction    * import_mesh;
    QAction    * save_mesh;
    QAction    * save_data;
    QAction    * exit;

    QMenu      * view_menu;
    QAction    * view_reset;
    QAction    * view_menu_action;

};



#endif // MAINWINDOW_H
'''

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


def main() {
    QApplication app(argc, argv);

    QCoreApplication::setOrganizationName( "SCI Institute" );
    QCoreApplication::setOrganizationDomain( "Uncertainty" );
    QCoreApplication::setApplicationName( "muView" );

    SCI::PrintLicense( "muView : Multifield Uncertainty Viewer", "Paul Rosen", "2013" );

    MainWindow w;
    w.setWindowTitle( QString("muView : Multifield Uncertainty Viewer") );
    w.show();

    return app.exec();
}

main()


