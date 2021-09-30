class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.duckduckgo.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()


    def navigateHome(self):
        self.browser.setUrl(QUrl('https://www.duckduckgo.com'))


    def navigateToUrl(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))


    def updateUrl(self, q):
        self.url_bar.setText(q.toString())


    #Navbar setup
    navbar = QToolBar()
    self.addToolBAr(navbar)

    # Back button
    back_btn = QAction('Back', self)
    back_btn.triggered.connect(self.browser.back)
    navbar.addAction(back_btn)

    # Forward button
    forward_btn = QAction('Forward', self)
    forward_btn.triggered.connect(self.browser.forward)
    navbar.addAction(forward_btn)

    # Reload button
    reload_btn = QAction('Reload', self)
    reload_btn.triggered.connect(self.browser.reload)
    navbar.addAction(reload_btn)

    # home button
    home_btn = QAction('Home', self)
    home_btn.triggered.connect(self.naviagteHome)
    navbar.addAction(home_btn)

    # url bar text box
    self.url_bar = QLineEdit()
    self.url_bar.returnPressed.connect(self.navigateToUrl)
    navbar.addWidget(self.url_bar)
    self.browser.urlChanged.connect(self.updateUrl)
