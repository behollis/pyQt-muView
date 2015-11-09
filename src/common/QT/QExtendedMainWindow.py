from PyQt5.QtWidgets import QMainWindow, QAction, QVariant, QWidget, QFileDialog, QSettings
from PyQt5.QtWidgets import QFileInfo
from PyQt5.QtCore import QSettings
from PyQt5.QtCore import QObject, pyqtSlot

class QExtendedMainWindow(QMainWindow):
    
    def __init__(self):
        super(QMainWindow, self).__init__()
        
        self.settings = QSettings()
        self.autosave_id = 0

        #load window geometry
        QWidget.restoreGeometry(self.settings.value("geometry")) 
        
    @pyqtSlot()
    def open_recent(self):
        action = QWidget.sender()
        self.open_recent( str( action.data() ) )
        ''' C++: void open_recent() '''
        
    def closeEvent(self, e):
        ''' save window geometry '''
        self.settings.setValue('geometry', QWidget.saveGeometry())
    
    def keyPressEvent(self, e):
        '''
        if e.key() == 's' or ( e.key() == 'S' and not e.isAutoRepeat() ):
            self.ScreenShot()
        '''
        return

    def addRecentMenu(self, parent_menu):
        ''' List of recently accessed files '''
        recent_menu = parent_menu.addMenu( 'Recent Files' )
        
        for i in range(0, 10):
            tmp = QAction(self)
            tmp.setVisible(False)
            recent_menu.addAction( tmp )
            tmp.triggered.connect( self.open_recent() )
        
        alist = recent_menu.actions()
        #QSettings settings;
        files = self.settings.value("RecentFileList").toStringList()
        a = alist.size()
        b = files.size()
        limit = b
        if a > b:
            limit = a
            
        for i in range(0, limit):
            file = files[i]
            if file.length() > 160:
                file = file.left(40) + ' ... ' + file.right(100)
            alist[i].setText( file )
            alist[i].setData( files[i] )
            alist[i].setVisible( True )
        
        return recent_menu

    def updateRecentMenu(self, recent_menu, fname ):
        files = self.settings.value( defaultValue='RecentFileList', type=list() )    
        files.removeAll( fname )
        files.prepend( fname )
    
        while files.size() > 10:
            files.removeLast()
    
        self.settings.setValue("RecentFileList", files)
        alist = recent_menu.actions()
        for i in range(0, alist.size(), 1): #int i = 0; i < alist.size(); i++)
            if i < files.size():
                file = files[i];
                if file.length() > 160:
                    file = file.left(40) + " ... " + file.right(100)
                
                alist[i].setText( file )
                alist[i].setData( files[i] )
                alist[i].setVisible( True )
            else:
                alist[i].setVisible( False )
            
    def cursorOverride(self, shape ):
        QWidget.setOverrideCursor(shape)

    def cursorRestore(self):
        QWidget.restoreOverrideCursor()

    def openDialog(self, title, ftypes ):

        options = QFileDialog.DontResolveSymlinks;
        options |= QFileDialog.DontUseNativeDialog;
        
        dir   = QSettings().value("workingDirectory").toString()
        fname = QFileDialog.getOpenFileName( 0, title, dir, ftypes, 0, options )
    
        if fname.size() > 0:
            QSettings.setValue("workingDirectory", QFileInfo( fname ).canonicalPath() )
    
        return fname

    def openListDialog(self, title, ftypes ):
        options = QFileDialog.DontResolveSymlinks
        options |= QFileDialog.DontUseNativeDialog
    
        dir        = QSettings().value("workingDirectory").toString()
        fname_list = QFileDialog.getOpenFileNames( 0, title, dir, ftypes, 0, options )
    
        if fname_list.size() > 0:
            QSettings().setValue("workingDirectory", QFileInfo( fname_list.at(0) ).canonicalPath() )
    
        return fname_list;

    def directoryDialog(self, title ):
        options = QFileDialog.DontResolveSymlinks
        options |= QFileDialog.DontUseNativeDialog
    
        dir   = QSettings().value("workingDirectory").toString()
        fname = QFileDialog.getExistingDirectory( 0, title, dir, options )
    
        if fname.size() > 0 :
            QSettings().setValue("workingDirectory", QFileInfo( fname ).canonicalPath() )
    
        return fname

    def saveDialog(self, title, ftypes ):
        options = QFileDialog.DontResolveSymlinks;
        options |= QFileDialog.DontUseNativeDialog;
    
        dir   = QSettings().value("workingDirectory").toString();
        fname = QFileDialog.getSaveFileName( 0, title, dir, ftypes, 0, options );
    
        if fname.size() > 0 :
            QSettings().setValue("workingDirectory", QFileInfo( fname ).canonicalPath() )

        return fname
'''
    def ScreenShot():
        buf = 'autosave'%1.3i.png",autosave_id++)
        ScreenShot( str(buf) );
    
    def ScreenShot( fname ):
        ScreenShot( str(fname ) )

void QExtendedMainWindow::ScreenShot( QString fname ){
    std::cout << "Grabbing desktop" << std::endl; fflush(stdout);
    QImage capt = QPixmap::grabWindow(QApplication::desktop()->winId()).toImage();

    std::cout << "Cropping window" << std::endl; fflush(stdout);
    QImage save = capt.copy( QRect(QWidget::mapToGlobal(contentsRect().topLeft()), QWidget::mapToGlobal(contentsRect().bottomRight())) );

    if( save.save(fname) ){
        std::cout << "Save OK : " << fname.toLocal8Bit().data() << std::endl; fflush(stdout);
    }
    else{
        std::cout << "Save FAILED" << std::endl; fflush(stdout);
    }
}
'''
