from PyQt5.QtWidgets import QMainWindow , QApplication
from PyQt5.uic import loadUi
import sys
from classes.predicted_sales_data import Predicted_sales_data
 


class MainPage(QMainWindow):
    """Main page class."""
    def __init__(self):
        """
        Initialize the main page.

        Loads the UI and connects button click event.
        """
        super(MainPage, self).__init__()
        loadUi("Gui/main.ui", self)
        self.daily_predicted_sales_button.clicked.connect(self.predicted_sales_data_button_clickHandler) 
   
    def predicted_sales_data_button_clickHandler(self): 
        self.predicted_sales_data_2 = Predicted_sales_data()
        self.stackedWidget.addWidget(self.predicted_sales_data_2)
        # Initialize back button to return to main stacked widget
        self.predicted_sales_data_2.daily_predicted_sales_back_button.clicked.connect(self.predicted_sales_data_2.goToMainPage)
        self.stackedWidget.setCurrentIndex(1) 

         

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window_login = MainPage()
    window_login.showMaximized()
    sys.exit(app.exec_())
