from PyQt5.QtWidgets import QMainWindow, QAction
from PyQt5.QtCore import QSettings
from PyQt5.QtCore import QObject, pyqtSlot
import string

class QExtendedMainWindow(QMainWindow):
    
    def __init__(self):
        super(QMainWindow, self).__init__()
        
        self.settings #QSettings
        self.autosave_id = 0

        #load window geometry
        #restoreGeometry(settings.value("geometry").toByteArray());
        
    @pyqtSlot(int, QObject)
    def open_recent(self):
        #action = qobject_cast<QAction *>(sender())
        open_recent( str( action.data() )
        ''' C++: void open_recent() '''
        
        
    def closeEvent(self, e):
        ''' save window geometry '''
        #settings.setValue("geometry", saveGeometry())
        None
    
    def keyPressEvent(self, e ):
        if e.key() == 's' or ( e.key() == 'S' and not e.isAutoRepeat() ):
            #ScreenShot()
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

'''
void QExtendedMainWindow::updateRecentMenu( QMenu * recent_menu, QString fname ){

    QStringList files = settings.value("RecentFileList").toStringList();
    files.removeAll( fname );
    files.prepend( fname );

    while (files.size() > 10){
        files.removeLast();
    }

    settings.setValue("RecentFileList", files);
    QList<QAction*> alist = recent_menu->actions();
    for(int i = 0; i < alist.size(); i++){
        if( i < files.size() ){
            QString file = files[i];
            if( file.length() > 160 ){
                file = file.left(40) + " ... " + file.right(100);
            }
            alist[i]->setText( file );
            alist[i]->setData( files[i] );
            alist[i]->setVisible( true );
        }
        else{
            alist[i]->setVisible( false );
        }
    }
}


void QExtendedMainWindow::ScreenShot( ){
    char buf[1024];
#ifdef __APPLE__
    sprintf(buf,"/autosave%1.3i.png",autosave_id++);
    QString dir   = QSettings().value("workingDirectory").toString();
    ScreenShot( dir + QString(buf) );
#else
    sprintf(buf,"autosave%1.3i.png",autosave_id++);
    ScreenShot( QString(buf) );
#endif
}

void QExtendedMainWindow::ScreenShot( std::string fname ){
    ScreenShot( tr(fname.c_str()) );
}

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


#if WIN32
    void QExtendedMainWindow::cursorOverride( Qt::CursorShape shape ){
        QApplication::setOverrideCursor(shape);
    }
#else
    void QExtendedMainWindow::cursorOverride( Qt::CursorShape ){ }
#endif

void QExtendedMainWindow::cursorRestore( ){
    QApplication::restoreOverrideCursor();
}

QString QExtendedMainWindow::openDialog( QString title, QString ftypes ){

    QFileDialog::Options options = QFileDialog::DontResolveSymlinks;
    #if defined(__APPLE__) || defined(linux)
        options |= QFileDialog::DontUseNativeDialog;
    #endif

    QString dir   = QSettings().value("workingDirectory").toString();
    QString fname = QFileDialog::getOpenFileName( 0, title, dir, ftypes, 0, options );

    if( fname.size() > 0 ){
        QSettings().setValue("workingDirectory", QFileInfo( fname ).canonicalPath() );
    }

    return fname;
}

QStringList QExtendedMainWindow::openListDialog( QString title, QString ftypes ){
    QFileDialog::Options options = QFileDialog::DontResolveSymlinks;
    #if defined(__APPLE__) || defined(linux)
        options |= QFileDialog::DontUseNativeDialog;
    #endif

    QString     dir        = QSettings().value("workingDirectory").toString();
    QStringList fname_list = QFileDialog::getOpenFileNames( 0, title, dir, ftypes, 0, options );

    if(fname_list.size() > 0 ){
        QSettings().setValue("workingDirectory", QFileInfo( fname_list.at(0) ).canonicalPath() );
    }

    return fname_list;
}

QString QExtendedMainWindow::directoryDialog( QString title ){
    QFileDialog::Options options = QFileDialog::DontResolveSymlinks;
    #if defined(__APPLE__) || defined(linux)
        options |= QFileDialog::DontUseNativeDialog;
    #endif

    QString dir   = QSettings().value("workingDirectory").toString();
    QString fname = QFileDialog::getExistingDirectory( 0, title, dir, options );

    if( fname.size() > 0 ){
        QSettings().setValue("workingDirectory", QFileInfo( fname ).canonicalPath() );
    }

    return fname;
}


QString QExtendedMainWindow::saveDialog( QString title, QString ftypes ){

    QFileDialog::Options options = QFileDialog::DontResolveSymlinks;
    #if defined(__APPLE__) || defined(linux)
        options |= QFileDialog::DontUseNativeDialog;
    #endif

    QString dir   = QSettings().value("workingDirectory").toString();
    QString fname = QFileDialog::getSaveFileName( 0, title, dir, ftypes, 0, options );

    if( fname.size() > 0 ){
        QSettings().setValue("workingDirectory", QFileInfo( fname ).canonicalPath() );
    }

    return fname;
}
'''
        
        

'''
        virtual QSize minimumSizeHint() const { return QSize(   50,   50 ); }
        virtual QSize sizeHint()        const { return QSize( 1600, 1200 ); }

        virtual void ScreenShot( );
        virtual void ScreenShot( QString fname );
        virtual void ScreenShot( std::string fname );

        static QString     openDialog(      QString title, QString ftypes );
        static QString     directoryDialog( QString title );
        static QStringList openListDialog(  QString title, QString ftypes );
        static QString     saveDialog(      QString title, QString ftypes );

        static void        cursorOverride( Qt::CursorShape shape );
        static void        cursorRestore( );

    private slots:
        void open_recent( );

    protected:

        QMenu *      addRecentMenu( QMenu * parent_menu );
        void         updateRecentMenu( QMenu * recent_menu, QString fname );
        virtual void open_recent( QString fname );

        virtual void keyPressEvent( QKeyEvent   * event );
        virtual void closeEvent   ( QCloseEvent * event );

'''