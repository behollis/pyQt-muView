import sys
from PyQt5.QtWidgets import QApplication
from HeartMainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setOrganizationName( 'SCI Institute' )
    app.setOrganizationDomain( 'Uncertainty' )
    app.setApplicationName( 'muView' )

    #SCI::PrintLicense( "muView : Multifield Uncertainty Viewer", "Paul Rosen", "2013" );

    w = MainWindow()

    w.setWindowTitle( 'muView : Multifield Uncertainty Viewer' )
    w.show()

    sys.exit(app.exec_())



