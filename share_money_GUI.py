# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 22:00:22 2019

@author: Yeally
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QLabel, QWidget, QTextEdit

class AA(QMainWindow):
    def __init__(self):
        super().__init__()
        self.money =[]
        self.name = []
        self.result = []
        self.test = 10
        self.initUI()
        
    def initUI(self):
        self.lab_name = QLabel(self)
        self.lab_name.move(10,10)
        self.lab_name.setText('消费人姓名：')
        self.lab_name.adjustSize()
        
        self.lab_money = QLabel(self)
        self.lab_money.move(250,10)
        self.lab_money.setText('消费数额：')
        self.lab_money.adjustSize()
        
        self.le_row0 = QLineEdit(self)
        self.le_row0.move(10,30)        
        self.le_column0 = QLineEdit(self)
        self.le_column0.move(250,30)
        
        self.le_row1 = QLineEdit(self)
        self.le_row1.move(10,70)   
        self.le_column1 = QLineEdit(self)
        self.le_column1.move(250,70)
        
        self.le_row2 = QLineEdit(self)
        self.le_row2.move(10,110)        
        self.le_column2 = QLineEdit(self)
        self.le_column2.move(250,110)
        
        self.le_row3 = QLineEdit(self)
        self.le_row3.move(10,150)        
        self.le_column3 = QLineEdit(self)
        self.le_column3.move(250,150)
        
        self.le_row4 = QLineEdit(self)
        self.le_row4.move(10,190)        
        self.le_column4 = QLineEdit(self)
        self.le_column4.move(250,190)
        
        self.le_row5 = QLineEdit(self)
        self.le_row5.move(10,230)        
        self.le_column5 = QLineEdit(self)
        self.le_column5.move(250,230)
        
        self.le_row6 = QLineEdit(self)
        self.le_row6.move(10,270)        
        self.le_column6 = QLineEdit(self)
        self.le_column6.move(250,270)
        
        self.le_row7 = QLineEdit(self)
        self.le_row7.move(10,310)        
        self.le_column7 = QLineEdit(self)
        self.le_column7.move(250,310)
        
        self.le_row8 = QLineEdit(self)
        self.le_row8.move(10,350)        
        self.le_column8 = QLineEdit(self)
        self.le_column8.move(250,350)
        
        self.le_row9 = QLineEdit(self)
        self.le_row9.move(10,390)        
        self.le_column9 = QLineEdit(self)
        self.le_column9.move(250,390)
        
        self.le_row10 = QLineEdit(self)
        self.le_row10.move(10,430)        
        self.le_column10 = QLineEdit(self)
        self.le_column10.move(250,430)
        
        self.le_row11 = QLineEdit(self)
        self.le_row11.move(10,470)        
        self.le_column11 = QLineEdit(self)
        self.le_column11.move(250,470)
        
        self.le_row12 = QLineEdit(self)
        self.le_row12.move(10,510)        
        self.le_column12 = QLineEdit(self)
        self.le_column12.move(250,510)
        
        self.le_row13 = QLineEdit(self)
        self.le_row13.move(10,550)        
        self.le_column13 = QLineEdit(self)
        self.le_column13.move(250,550)
        
        self.le_row14 = QLineEdit(self)
        self.le_row14.move(10,590)        
        self.le_column14 = QLineEdit(self)
        self.le_column14.move(250,590)
        
        self.le_row15 = QLineEdit(self)
        self.le_row15.move(10,630)        
        self.le_column15 = QLineEdit(self)
        self.le_column15.move(250,630)
        
        self.le_row16 = QLineEdit(self)
        self.le_row16.move(10,670)        
        self.le_column16 = QLineEdit(self)
        self.le_column16.move(250,670)
        
        self.le_row17 = QLineEdit(self)
        self.le_row17.move(10,710)        
        self.le_column17 = QLineEdit(self)
        self.le_column17.move(250,710)
        
        self.le_row18 = QLineEdit(self)
        self.le_row18.move(10,750)        
        self.le_column18 = QLineEdit(self)
        self.le_column18.move(250,750)
        
        self.le_row19 = QLineEdit(self)
        self.le_row19.move(10,790)        
        self.le_column19 = QLineEdit(self)
        self.le_column19.move(250,790)
        
        self.le_row0.editingFinished.connect(self.Changed_row0)
        self.le_column0.editingFinished.connect(self.Changed_column0)
        self.le_row1.editingFinished.connect(self.Changed_row1)
        self.le_column1.editingFinished.connect(self.Changed_column1)
        self.le_row2.editingFinished.connect(self.Changed_row2)
        self.le_column2.editingFinished.connect(self.Changed_column2)
        self.le_row3.editingFinished.connect(self.Changed_row3)
        self.le_column3.editingFinished.connect(self.Changed_column3)
        self.le_row4.editingFinished.connect(self.Changed_row4)
        self.le_column4.editingFinished.connect(self.Changed_column4)
        self.le_row5.editingFinished.connect(self.Changed_row5)
        self.le_column5.editingFinished.connect(self.Changed_column5)
        self.le_row6.editingFinished.connect(self.Changed_row6)
        self.le_column6.editingFinished.connect(self.Changed_column6)
        self.le_row7.editingFinished.connect(self.Changed_row7)
        self.le_column7.editingFinished.connect(self.Changed_column7)
        self.le_row8.editingFinished.connect(self.Changed_row8)
        self.le_column8.editingFinished.connect(self.Changed_column8)
        self.le_row9.editingFinished.connect(self.Changed_row9)
        self.le_column9.editingFinished.connect(self.Changed_column9)
        self.le_row10.editingFinished.connect(self.Changed_row10)
        self.le_column10.editingFinished.connect(self.Changed_column10)
        self.le_row11.editingFinished.connect(self.Changed_row11)
        self.le_column11.editingFinished.connect(self.Changed_column11)
        self.le_row12.editingFinished.connect(self.Changed_row12)
        self.le_column12.editingFinished.connect(self.Changed_column12)
        self.le_row13.editingFinished.connect(self.Changed_row13)
        self.le_column13.editingFinished.connect(self.Changed_column13)
        self.le_row14.editingFinished.connect(self.Changed_row14)
        self.le_column14.editingFinished.connect(self.Changed_column14)
        self.le_row15.editingFinished.connect(self.Changed_row15)
        self.le_column15.editingFinished.connect(self.Changed_column15)
        self.le_row16.editingFinished.connect(self.Changed_row16)
        self.le_column16.editingFinished.connect(self.Changed_column16)
        self.le_row17.editingFinished.connect(self.Changed_row17)
        self.le_column17.editingFinished.connect(self.Changed_column17)
        self.le_row18.editingFinished.connect(self.Changed_row18)
        self.le_column18.editingFinished.connect(self.Changed_column18)
        self.le_row19.editingFinished.connect(self.Changed_row19)
        self.le_column19.editingFinished.connect(self.Changed_column19)
        
        self.btn = QPushButton('结算', self)
        self.btn.move(400,10)
        self.btn.clicked.connect(self.calculate)
        
        self.te = QTextEdit(self)
        self.te.move(400,50)
        
        self.lab = QLabel(self)
        self.lab.move(800,800)
    
        self.setGeometry(50,50,1000,1000)
        self.setWindowTitle('欢迎使用AA制计算软件， author:Yeally ')
        self.show()
        
    
    def Changed_row0(self):
        self.name.append(self.le_row0.text())
    def Changed_column0(self):
        self.money.append(eval(self.le_column0.text()))
    def Changed_row1(self):
        self.name.append(self.le_row1.text())
    def Changed_column1(self):
        self.money.append(eval(self.le_column1.text())) 
    def Changed_row2(self):
        self.name.append(self.le_row2.text())
    def Changed_column2(self):
        self.money.append(eval(self.le_column2.text())) 
    def Changed_row3(self):
        self.name.append(self.le_row3.text())
    def Changed_column3(self):
        self.money.append(eval(self.le_column3.text()))
    def Changed_row4(self):
        self.name.append(self.le_row4.text())
    def Changed_column4(self):
        self.money.append(eval(self.le_column4.text())) 
    def Changed_row5(self):
        self.name.append(self.le_row5.text())
    def Changed_column5(self):
        self.money.append(eval(self.le_column5.text()))
    def Changed_row6(self):
        self.name.append(self.le_row6.text())
    def Changed_column6(self):
        self.money.append(eval(self.le_column6.text()))
    def Changed_row7(self):
        self.name.append(self.le_row7.text())
    def Changed_column7(self):
        self.money.append(eval(self.le_column7.text()))
    def Changed_row8(self):
        self.name.append(self.le_row8.text())
    def Changed_column8(self):
        self.money.append(eval(self.le_column8.text()))
    def Changed_row9(self):
        self.name.append(self.le_row9.text())
    def Changed_column9(self):
        self.money.append(eval(self.le_column9.text()))
    def Changed_row10(self):
        self.name.append(self.le_row10.text())
    def Changed_column10(self):
        self.money.append(eval(self.le_column10.text()))
    def Changed_row11(self):
        self.name.append(self.le_row11.text())
    def Changed_column11(self):
        self.money.append(eval(self.le_column11.text()))
    def Changed_row12(self):
        self.name.append(self.le_row12.text())
    def Changed_column12(self):
        self.money.append(eval(self.le_column12.text()))
    def Changed_row13(self):
        self.name.append(self.le_row13.text())
    def Changed_column13(self):
        self.money.append(eval(self.le_column13.text()))
    def Changed_row14(self):
        self.name.append(self.le_row14.text())
    def Changed_column14(self):
        self.money.append(eval(self.le_column14.text()))
    def Changed_row15(self):
        self.name.append(self.le_row15.text())
    def Changed_column15(self):
        self.money.append(eval(self.le_column15.text()))
    def Changed_row16(self):
        self.name.append(self.le_row16.text())
    def Changed_column16(self):
        self.money.append(eval(self.le_column16.text()))
    def Changed_row17(self):
        self.name.append(self.le_row17.text())
    def Changed_column17(self):
        self.money.append(eval(self.le_column17.text()))
    def Changed_row18(self):
        self.name.append(self.le_row18.text())
    def Changed_column18(self):
        self.money.append(eval(self.le_column18.text()))
    def Changed_row19(self):
        self.name.append(self.le_row19.text())
    def Changed_column19(self):
        self.money.append(eval(self.le_column19.text()))
    
    def calculate(self):    
        print(self.name, self.money)
        
        get = {}
        get_sort2 = [] 
        give_number = 0
        
        sum_money = sum(self.money)
        average_money = sum_money / len(self.name)
        
        for _ in self.money:
            if _ < average_money:
                give_number += 1
        for n,m in zip(self.name,self.money):
            gt = round(m - average_money,3)
            get[n] = gt
            
        get_sort = sorted(get.items(),key = lambda x:x[1])
        
        for (a,b) in get_sort:
            get_sort2.append(list((a,b)))      #将列表里的元组元素转变为列表元素
            
        i = 0
        own = 0           #当前面的人（孙等)所给的钱不足时所欠的数
        enough = 0        #当前面的人（孙等)所给的钱还有多余的钱的多余数
        k = len(self.money)
        
        
        for i in range(give_number):
        
        
            if own != 0:
                gap = abs(get_sort2[i][1]) -own
    
                if gap > 0:
                    if k > give_number:
                        self.result.append('{}给{}{}元'.format(get_sort2[i][0], get_sort2[k-1][0], abs(own)))
                    get_sort2[i][1] += own
                    k -= 1
                    own = 0
                elif gap < 0:
                    if k > give_number:
                        self.result.append('{}给{}{}元'.format(get_sort2[i][0], get_sort2[k-1][0], abs(get_sort2[i][1])))
                    own = own - abs(get_sort2[i][1])
                    get_sort2[i][1] += own
                    continue
                else:
                    if k > give_number:
                        self.result.append('{}给{}{}元'.format(get_sort2[i][0], get_sort2[k-1][0], abs(get_sort2[i][1])))
                    own = own - abs(get_sort2[i][1])
                    get_sort2[i][1] += own
                    continue
            
                    
                
            if (own == 0) and (enough == 0):
                
                decrease =  abs(get_sort2[i][1]) - abs(get_sort2[k-1][1])
    
                if decrease > 0:
                    if k > give_number:
                        self.result.append('{}给{}{}元'.format(get_sort2[i][0], get_sort2[k-1][0], abs(get_sort2[k-1][1])))
                    enough = decrease
                    k -= 1
                elif decrease < 0:
    
                    if k > give_number:
                        self.result.append('{}给{}{}元'.format(get_sort2[i][0], get_sort2[k-1][0], abs(get_sort2[i][1])))
                    own = abs(decrease)
                    if own == 0:
                        k -= 1
                else:
                    if k > give_number:
                        self.result.append('{}给{}{}元'.format(get_sort2[i][0], get_sort2[k-1][0], abs(get_sort2[i][1])))
                    own = 0
                    k -= 1
    
        
            if enough != 0:
                gap2 = abs(get_sort2[k-1][1]) - enough
                while abs(get_sort2[k-1][1]) - enough < 0:
                    if k > give_number:
                        self.result.append('{}给{}{}元'.format(get_sort2[i][0], get_sort2[k-1][0], abs(get_sort2[k-1][1])))
                    enough -= abs(get_sort2[k-1][1])
                    get_sort2[i][1] += abs(get_sort2[k-1][1])
                    k -= 1
                if gap2 > 0:
                    if k > give_number:
                        self.result.append('{}给{}{}元'.format(get_sort2[i][0], get_sort2[k-1][0], abs(enough)))
                    get_sort2[k-1][1] -= enough
                    enough = 0
                    continue
                if gap2 == 0:
                    if k > give_number:
                        self.result.append('{}给{}{}元'.format(get_sort2[i][0], get_sort2[k-1][0], abs(enough)))
                    get_sort2[k-1][1] -= enough
                    enough = 0
                    k -= 1
                    continue
        
        
        
        
        
        
        
        print(self.result)
        self.te.setPlainText(str(self.result))
        self.te.adjustSize()
#        self.lab.setText(str(self.result))    
#        self.lab.adjustSize()

        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = AA()
    sys.exit(app.exec_())