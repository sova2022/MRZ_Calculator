# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mrz.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from mrz.generator.td3 import TD3CodeGenerator
from PyQt5 import QtCore, QtGui, QtWidgets
from mrz.generator.td1 import TD1CodeGenerator


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(559, 298)
        MainWindow.setAnimated(True)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.START = QtWidgets.QPushButton(self.centralwidget)
        self.START.setGeometry(QtCore.QRect(10, 240, 111, 41))
        self.START.setAutoDefault(False)
        self.START.setObjectName("START")

        self.male = QtWidgets.QRadioButton(self.centralwidget)
        self.male.setGeometry(QtCore.QRect(440, 100, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.male.setFont(font)
        self.male.setObjectName("male")
        self.male.setChecked(True)

        self.Female = QtWidgets.QRadioButton(self.centralwidget)
        self.Female.setGeometry(QtCore.QRect(440, 120, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Female.setFont(font)
        self.Female.setObjectName("Female")

        self.Unspecified = QtWidgets.QRadioButton(self.centralwidget)
        self.Unspecified.setGeometry(QtCore.QRect(440, 140, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Unspecified.setFont(font)
        self.Unspecified.setObjectName("Unspecified")

        self.ontop = QtWidgets.QCheckBox(self.centralwidget)
        self.ontop.setGeometry(QtCore.QRect(290, 100, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ontop.setFont(font)
        self.ontop.setObjectName("ontop")

        self.chooseid = QtWidgets.QCheckBox(self.centralwidget)
        self.chooseid.setGeometry(QtCore.QRect(290, 120, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.chooseid.setFont(font)
        self.chooseid.setObjectName("chooseid")

        self.Nation = QtWidgets.QLineEdit(self.centralwidget)
        self.Nation.setGeometry(QtCore.QRect(110, 100, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Nation.setFont(font)
        self.Nation.setMaxLength(3)
        self.Nation.setAlignment(QtCore.Qt.AlignCenter)
        self.Nation.setObjectName("Nation")
        rx = QtCore.QRegExp("^[a-z A-Z]{100}")
        val = QtGui.QRegExpValidator(rx)
        self.Nation.setValidator(val)

        self.Issuing = QtWidgets.QLineEdit(self.centralwidget)
        self.Issuing.setGeometry(QtCore.QRect(210, 100, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Issuing.setFont(font)
        self.Issuing.setMaxLength(3)
        self.Issuing.setAlignment(QtCore.Qt.AlignCenter)
        self.Issuing.setObjectName("Issuing")
        self.Issuing.setValidator(val)

        self.Exp = QtWidgets.QLineEdit(self.centralwidget)
        self.Exp.setGeometry(QtCore.QRect(10, 170, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Exp.setFont(font)
        self.Exp.setMaxLength(10)
        self.Exp.setAlignment(QtCore.Qt.AlignCenter)
        self.Exp.setObjectName("Exp")
        rx_3 = QtCore.QRegExp("[0-9./]{100}")
        val_3 = QtGui.QRegExpValidator(rx_3)
        self.Exp.setValidator(val_3)


        self.Numb = QtWidgets.QLineEdit(self.centralwidget)
        self.Numb.setGeometry(QtCore.QRect(110, 170, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Numb.setFont(font)
        self.Numb.setMaxLength(9)
        self.Numb.setAlignment(QtCore.Qt.AlignCenter)
        self.Numb.setObjectName("Numb")
        rx_2 = QtCore.QRegExp("^[a-zA-Z0-9]{100}")
        val_2 = QtGui.QRegExpValidator(rx_2)
        self.Numb.setValidator(val_2)

        self.Extra = QtWidgets.QLineEdit(self.centralwidget)
        self.Extra.setGeometry(QtCore.QRect(290, 170, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Extra.setFont(font)
        self.Extra.setMaxLength(14)
        self.Extra.setAlignment(QtCore.Qt.AlignCenter)
        self.Extra.setObjectName("Extra")
        self.Extra.setValidator(val_2)

        self.Name = QtWidgets.QLineEdit(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(10, 30, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Name.setFont(font)
        self.Name.setMaxLength(24)
        self.Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Name.setObjectName("Name")
        self.Name.setValidator(val)

        self.Surname = QtWidgets.QLineEdit(self.centralwidget)
        self.Surname.setGeometry(QtCore.QRect(290, 30, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Surname.setFont(font)
        self.Surname.setMaxLength(24)
        self.Surname.setAlignment(QtCore.Qt.AlignCenter)
        self.Surname.setObjectName("Surname")
        self.Surname.setValidator(val)

        self.DOB = QtWidgets.QLineEdit(self.centralwidget)
        self.DOB.setGeometry(QtCore.QRect(10, 100, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.DOB.setFont(font)
        self.DOB.setMaxLength(10)
        self.DOB.setAlignment(QtCore.Qt.AlignCenter)
        self.DOB.setObjectName("DOB")
        self.DOB.setValidator(val_3)


        self.label = QtWidgets.QLabel(self.centralwidget) # output window for result
        self.label.setGeometry(QtCore.QRect(130, 230, 401, 61))
        self.label.setFont(QtGui.QFont("OCR-B 10 BT", 11, QtGui.QFont.Light))
        self.label.setWordWrap(True)
        self.label.setLineWidth(2)
        self.label.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.label.setText("     Your MRZ will be here...")
        self.label.setIndent(4)
        self.label.setObjectName("label")

        self.Nationality_lbl = QtWidgets.QLabel(self.centralwidget)
        self.Nationality_lbl.setGeometry(QtCore.QRect(110, 80, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Nationality_lbl.setFont(font)
        self.Nationality_lbl.setObjectName("Nationality_lbl")

        self.Issuing_State = QtWidgets.QLabel(self.centralwidget)
        self.Issuing_State.setGeometry(QtCore.QRect(210, 80, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Issuing_State.setFont(font)
        self.Issuing_State.setObjectName("Issuing_State")

        self.Name_and_Midlename = QtWidgets.QLabel(self.centralwidget)
        self.Name_and_Midlename.setGeometry(QtCore.QRect(10, 10, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Name_and_Midlename.setFont(font)
        self.Name_and_Midlename.setObjectName("Name_and_Midlename")

        self.Surname_lbl = QtWidgets.QLabel(self.centralwidget)
        self.Surname_lbl.setGeometry(QtCore.QRect(290, 10, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Surname_lbl.setFont(font)
        self.Surname_lbl.setObjectName("Surname_lbl")

        self.dob_lbl = QtWidgets.QLabel(self.centralwidget)
        self.dob_lbl.setGeometry(QtCore.QRect(10, 80, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.dob_lbl.setFont(font)
        self.dob_lbl.setObjectName("dob_lbl")

        self.Expire_date_lbl = QtWidgets.QLabel(self.centralwidget)
        self.Expire_date_lbl.setGeometry(QtCore.QRect(10, 150, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Expire_date_lbl.setFont(font)
        self.Expire_date_lbl.setObjectName("Expire_date")

        self.Document_Number = QtWidgets.QLabel(self.centralwidget)
        self.Document_Number.setGeometry(QtCore.QRect(110, 150, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Document_Number.setFont(font)
        self.Document_Number.setObjectName("Document_Number")

        self.Extra_Info = QtWidgets.QLabel(self.centralwidget)
        self.Extra_Info.setGeometry(QtCore.QRect(290, 150, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Extra_Info.setFont(font)
        self.Extra_Info.setObjectName("Extra_Info")

        self.sex = QtWidgets.QLabel(self.centralwidget)
        self.sex.setGeometry(QtCore.QRect(440, 80, 21, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sex.setFont(font)
        self.sex.setObjectName("sex")

        self.Fix = QtWidgets.QLabel(self.centralwidget)
        self.Fix.setGeometry(QtCore.QRect(290, 80, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Fix.setFont(font)
        self.Fix.setObjectName("Fix")

        self.by = QtWidgets.QLabel(self.centralwidget)
        self.by.setGeometry(QtCore.QRect(500, 275, 81, 16))
        # self.label_12.setStyleSheet("border :1px solid blue;")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.by.setFont(font)
        self.by.setStyleSheet('color:grey')
        self.by.setObjectName("by")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MRZ Calculator"))
        self.START.setText(_translate("MainWindow", "Calculate MRZ"))
        self.male.setText(_translate("MainWindow", "Male"))
        self.Female.setText(_translate("MainWindow", "Female"))
        self.Unspecified.setText(_translate("MainWindow", "Unspec."))
        self.ontop.setText(_translate("MainWindow", "always on top"))
        self.chooseid.setText(_translate("MainWindow", "switch type"))
        self.Nationality_lbl.setText(_translate("MainWindow", "Nationality"))
        self.Issuing_State.setText(_translate("MainWindow", "Issuing St"))
        self.Name_and_Midlename.setText(_translate("MainWindow", "Name & Midlename"))
        self.Surname_lbl.setText(_translate("MainWindow", "Surname"))
        self.dob_lbl.setText(_translate("MainWindow", "DB dd.mm.yyyy"))
        self.Expire_date_lbl.setText(_translate("MainWindow", "Exp dd.mm.yyyy"))
        self.Document_Number.setText(_translate("MainWindow", "Document Number"))
        self.Extra_Info.setText(_translate("MainWindow", "Extra Info"))
        self.sex.setText(_translate("MainWindow", "sex"))
        self.Fix.setText(_translate("MainWindow", "Fix"))
        self.by.setText(_translate("MainWindow", "by sova"))



class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ontop.stateChanged.connect(self.on_top)
        self.START.clicked.connect(self.click)

    def on_top(self, state):
        if state:
            self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(QtCore.Qt.Window)
        self.show()
    def click(self):
        iso_3166_1 = ['AFG', 'ALB', 'DZA', 'ASM', 'AND', 'AGO', 'AIA', 'ATA', 'ATG', 'ARG', 'ARM', 'ABW',
                      'AUS', 'AUT', 'AZE', 'BHS', 'BHR', 'BGD', 'BRB', 'BLR', 'BEL', 'BLZ', 'BEN', 'BMU',
                      'BTN', 'BOL', 'BOL', 'BIH', 'BWA', 'BVT', 'BRA', 'IOT', 'BRN', 'BRN', 'BGR', 'BFA',
                      'BDI', 'KHM', 'CMR', 'CAN', 'CPV', 'CYM', 'CAF', 'TCD', 'CHL', 'CHN', 'CXR', 'CCK',
                      'COL', 'COM', 'COG', 'COD', 'COK', 'CRI', 'CIV', 'CIV', 'HRV', 'CUB', 'CYP', 'CZE',
                      'DNK', 'DJI', 'DMA', 'DOM', 'ECU', 'EGY', 'SLV', 'GNQ', 'ERI', 'EST', 'ETH', 'FLK',
                      'FRO', 'FJI', 'FIN', 'FRA', 'GUF', 'PYF', 'ATF', 'GAB', 'GMB', 'GEO', 'DEU', 'GHA',
                      'GIB', 'GRC', 'GRL', 'GRD', 'GLP', 'GUM', 'GTM', 'GGY', 'GIN', 'GNB', 'GUY', 'HTI',
                      'HMD', 'VAT', 'HND', 'HKG', 'HUN', 'ISL', 'IND', 'IDN', 'IRN', 'IRQ', 'IRL', 'IMN',
                      'ISR', 'ITA', 'JAM', 'JPN', 'JEY', 'JOR', 'KAZ', 'KEN', 'KIR', 'PRK', 'KOR', 'KOR',
                      'KWT', 'KGZ', 'LAO', 'LVA', 'LBN', 'LSO', 'LBR', 'LBY', 'LBY', 'LIE', 'LTU', 'LUX',
                      'MAC', 'MKD', 'MDG', 'MWI', 'MYS', 'MDV', 'MLI', 'MLT', 'MHL', 'MTQ', 'MRT', 'MUS',
                      'MYT', 'MEX', 'FSM', 'MDA', 'MCO', 'MNG', 'MNE', 'MSR', 'MAR', 'MOZ', 'MMR', 'MMR',
                      'NAM', 'NRU', 'NPL', 'NLD', 'ANT', 'NCL', 'NZL', 'NIC', 'NER', 'NGA', 'NIU', 'NFK',
                      'MNP', 'NOR', 'OMN', 'PAK', 'PLW', 'PSE', 'PAN', 'PNG', 'PRY', 'PER', 'PHL', 'PCN',
                      'POL', 'PRT', 'PRI', 'QAT', 'REU', 'ROU', 'RUS', 'RUS', 'RWA', 'SHN', 'KNA', 'LCA',
                      'SPM', 'VCT', 'VCT', 'VCT', 'WSM', 'SMR', 'STP', 'SAU', 'SEN', 'SRB', 'SYC', 'SLE',
                      'SGP', 'SVK', 'SVN', 'SLB', 'SOM', 'ZAF', 'SGS', 'SSD', 'ESP', 'LKA', 'SDN', 'SUR',
                      'SJM', 'SWZ', 'SWE', 'CHE', 'SYR', 'TWN', 'TWN', 'TJK', 'TZA', 'THA', 'TLS', 'TGO',
                      'TKL', 'TON', 'TTO', 'TUN', 'TUR', 'TKM', 'TCA', 'TUV', 'UGA', 'UKR', 'ARE', 'GBR',
                      'USA', 'UMI', 'URY', 'UZB', 'VUT', 'VEN', 'VEN', 'VNM', 'VNM', 'VGB', 'VIR', 'WLF',
                      'ESH', 'YEM', 'ZMB', 'ZWE']
        document_type = 'P'
        document_type_id = 'ID'
        optional_data = self.Extra.text()
        given_names = self.Name.text()
        surname = self.Surname.text()
        birth_date = self.DOB.text()
        expiry_date = self.Exp.text()
        import re
        info = '    ERROR: Please enter valid data \n             check all setting and fields!'
        date_pattern = re.compile(r'^(0[1-9]|[12][0-9]|3[01])(\.|/)(0[1-9]|1[0-2])(\2)(19|20)\d{2}$')
        if not date_pattern.match(birth_date):
            return self.label.setText(str(info))


        birth_date = birth_date.replace('.', '')
        birth_date = birth_date.replace('/', '')
        expiry_date = expiry_date.replace('.', '')
        expiry_date = expiry_date.replace('/', '')
        birth_date_dm = birth_date[0:4]
        expiry_date_dm = expiry_date[0:4]
        birth_date_y =  birth_date[4:8]
        expiry_date_y = expiry_date[4:8]

        if (int(birth_date_y) % 4 == 0) and (int(birth_date_y) % 100 != 0) or (int(birth_date_y) % 400 == 0):
            leap_year_b = ['3002', '3102', '3104', '3106', '3109', '3111']
        else:
            leap_year_b = ['2902','3002', '3102', '3104', '3106', '3109', '3111']

        if (int(expiry_date_y) % 4 == 0) and (int(expiry_date_y) % 100 != 0) or (int(expiry_date_y) % 400 == 0):
            leap_year_e = ['3002', '3102', '3104', '3106', '3109', '3111']
        else:
            leap_year_e = ['2902','3002', '3102', '3104', '3106', '3109', '3111']

        if birth_date_dm in leap_year_b:
            return self.label.setText(str(info))
        if expiry_date_dm in leap_year_e:
            return self.label.setText(str(info))


        birth_date = birth_date[6:8] + birth_date [2:4] + birth_date[0:2]
        expiry_date = expiry_date[6:8] + expiry_date[2:4] + expiry_date[0:2]
        document_number = self.Numb.text()
        country_code = self.Issuing.text()
        country_code = country_code.upper()
        nationality = self.Nation.text()
        nationality = nationality.upper()

        if country_code  not in iso_3166_1:
            return self.label.setText(str(info))

        if nationality not in iso_3166_1:
            return self.label.setText(str(info))



        if self.male.isChecked():
            sex = 'M'
        else:
            sex = 'F'

        if self.Unspecified.isChecked():
            sex = 'X'


        if len(country_code) < 3:
            return self.label.setText(str(info))
        elif len(nationality) < 3:
            return self.label.setText(str(info))
        elif len(birth_date) < 6:
            return self.label.setText(str(info))
        elif len(expiry_date) < 6:
            return self.label.setText(str(info))
        elif len(document_number) < 5:
            return self.label.setText(str(info))
        elif len(given_names) < 1:
            return self.label.setText(str(info))
        elif len(surname) < 1:
            return self.label.setText(str(info))

        code = TD3CodeGenerator(
                       document_type,           # Document type   Normally 'P' for passports
                       country_code,            # Country         3 letters code or country name
                       surname,                 # Surname         Special characters will be transliterated
                       given_names,             # Given name(s)   Special characters will be transliterated
                       document_number,         # Document number
                       nationality,             # Nationality
                       birth_date,              # Birth date      YYMMDD
                       sex,                     # Gender          Male: 'M', Female: 'F' or Undefined
                       expiry_date,             # Expiry date     YYMMDD
                       optional_data
        )

        code_id = TD1CodeGenerator(
                       document_type_id,        # Document type   Normally 'I' or 'ID' for id cards
                       country_code,            # Country         3 letters code or country name
                       document_number,         # Document number
                       birth_date,              # Birth date      YYMMDD
                       sex,                     # Gender          Male: 'M', Female: 'F' or Undefined
                       expiry_date,             # Expiry date     YYMMDD
                       nationality,             # Nationality
                       surname,                 # Surname         Special characters will be transliterated
                       given_names,             # Given name(s)   Special characters will be transliterated
                       optional_data
        )


        if self.chooseid.isChecked():

            self.label.setText(str(code_id))
        else:
            self.label.setText(str(code))





if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    sys.exit(app.exec_())



