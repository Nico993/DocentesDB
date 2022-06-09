from PyQt5.QtWidgets import QTableWidgetItem
class Gestor():

    def InsertTableItems(self,tableWidget,df):
        column = tableWidget.columnCount()
        for i in range(column):
            for j in range(len(df.index)):
                tableWidget.setItem(j,i,QTableWidgetItem(str(df.loc[j].iat[i])))

    def CreateTable(self,df,table):
        table.setColumnCount(len(df.columns)-1)
        columnPosition = table.columnCount()
        table.insertColumn(columnPosition)

        table.setRowCount(len(df)-1)
        rowPosition = table.rowCount()
        table.insertRow(rowPosition)

        ColumnsNames = df.columns.tolist()
        table.setHorizontalHeaderLabels(ColumnsNames)

    def SetComboBox(self,df,comboBox,pos):
        list = []
        for i in range(len(df.index)):
            list.append(str(df.loc[i].iat[pos]))
        comboBox.addItems(list)
        comboBox.setCurrentIndex(-1)