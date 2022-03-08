from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem


def setData(table: QTableWidget, data: dict):
    keys = []
    count_row = 0
    for key in data.keys():
        keys.append(key)
        if len(data[key]) > count_row:
            count_row = len(data[key])
    table.setColumnCount(len(keys))
    table.setRowCount(count_row)

    horHeaders = []
    for n, key in enumerate(data.keys()):
        horHeaders.append(key)
        for m, item in enumerate(data[key]):
            newitem = QTableWidgetItem(item)
            table.setItem(m, n, newitem)
    table.setHorizontalHeaderLabels(horHeaders)
    table.resizeColumnsToContents()
    table.resizeRowsToContents()
