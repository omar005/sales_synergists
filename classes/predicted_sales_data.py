from PyQt5.QtWidgets import QMainWindow , QApplication,QCheckBox,QListWidgetItem,QDialog,QWidget,QVBoxLayout,QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import  QCheckBox
import sys  
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication, QCheckBox
from PyQt5.uic import loadUi
from PyQt5 import  QtWidgets
import subprocess
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtCore import Qt
import pickle
import pandas as pd
from datetime import datetime



class Predicted_sales_data(QMainWindow):
    # Define a custom signal to be emitted when radars are deleted
    #editHappenedSignal = pyqtSignal()
    def __init__(self):
        super(Predicted_sales_data, self).__init__()
        loadUi("Gui/daily_predicted_sales.ui", self)
        self.daily_predicted_sales_back_button.clicked.connect(self.goToMainPage)
        self.displayPredictions()


        ###get the current used database
      
    def goToMainPage(self):
        self.parent().setCurrentIndex(0)  # Set the current page index to go back to the main page
        self.parent().removeWidget(self)
        self.deleteLater()





    def displayPredictions(self):
        #hard coded for the sake of the simplisty
        forecast_start_date='2017-08-15 00:00:00'
        self.unitEditTW.setRowCount(0)

        with open('train_model/trained_prophet_models_favorita.pkl', 'rb') as f:
            trained_models = pickle.load(f)


        forecasted_dfs = []

        for m in trained_models:
            future = m.make_future_dataframe(periods=1)
            fcst_prophet_train = m.predict(future)
            forecasted_df = fcst_prophet_train[fcst_prophet_train['ds'] >= forecast_start_date]
            forecasted_dfs.append(forecasted_df)

        item_names = ['BREAD/BAKERY', 'DAIRY', 'DELI', 'FROZEN FOODS', 'GROCERY I']

        # Update the QTableWidget with predictions
        for i, forecasted_df in enumerate(forecasted_dfs):
            self.unitEditTW.insertRow(i)
            # Get the item name based on index
            self.unitEditTW.setItem(i, 0, QtWidgets.QTableWidgetItem(item_names[i]))  # Item name
            # Populate the cells with data from the DataFrame
            for j, value in enumerate(forecasted_df['yhat']):

                self.unitEditTW.setItem(i, 1+j, QtWidgets.QTableWidgetItem(str(round(value))))  # Total sales

        # Resize the first column to fit its contents
        self.unitEditTW.resizeColumnToContents(0)





    """def displayPredictions(self):
        self.unitEditTW.setRowCount(0)
        # Load the saved model from the file
        with open('prophet_model.pkl', 'rb') as f:
            loaded_model = pickle.load(f)

        # Generate future dates
        future = loaded_model.make_future_dataframe(periods=1)

        # Predict the future values
        forecast = loaded_model.predict(future)

        # Extract relevant columns from forecast DataFrame
        predictions = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(1)

        # Update the QTableWidget with predictions
        i= 0
        for index, row in predictions.iterrows():
            
            self.unitEditTW.insertRow(i)
            try:
                self.unitEditTW.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i)))
                self.unitEditTW.setItem(i, 1, QtWidgets.QTableWidgetItem(str(row['ds'])))
                self.unitEditTW.setItem(i, 2, QtWidgets.QTableWidgetItem(str(row['yhat'])))
                i = i+1
            except Exception as e:
                print("Error:", e)"""


"""    def getPredections(self):
        # Load trained models
        with open('train_model/trained_prophet_models_favorita.pkl', 'rb') as f:
            trained_models = pickle.load(f)

        forecasted_dfs = []

        for m in trained_models:
            future = m.make_future_dataframe(periods=1)
            fcst_prophet_train = m.predict(future)
"""