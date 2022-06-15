# import pymsteams
# myTeamsMessage = pymsteams.connectorcard("https://ablelabs.webhook.office.com/webhookb2/8034834a-bac8-4429-9de8-bd9e936bae13@0b50e04b-4dc3-4bc5-99f7-09c167ccaba8/IncomingWebhook/1fc71196673e44ee8ba86aa768012d86/fb5ef264-d2d0-45f4-b5f3-3b4962cae1d1")

# myTeamsMessage.title("Sample Title")
# myTeamsMessage.text("Sample text")
# myTeamsMessage.text("Hello from python script! Powered by pysteams.")
# myTeamsMessage.send()

from operator import truediv
from time import sleep
import threading
import RandomChoice
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("./test/ui.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        self.People = ["이종민", "강경민", "안제현", "박상영", "정종윤"]
        #self.Price = RandomChoice.RandomChoice(self.People)
        self.index = 0
        self.PeopleNumber = len(self.People)
        self.NextTime = 0.03
        self.IsStart = False
        
        super().__init__()
        self.setupUi(self)
        self.btn_test.clicked.connect(self.btnClick)
        self.btn_test.pressed.connect(self.btnPressed)
        self.btn_test.released.connect(self.btnReleased)
        
    def btnClick(self):
        print("버튼이 클릭되었습니다.")
        #self.Next()
        
    def btnPressed(self):
        if self.IsStart == False:
            th1 = threading.Thread(target=self.Start)
            th1.start()

    def btnReleased(self):
        th2= threading.Thread(target=self.IncreaseNextTime)
        th2.start()
    
    def Next(self):
        self.index = self.index + 1 if self.index + 1 < self.PeopleNumber else 0
        before_index = self.index + 1 if self.index + 1 != self.PeopleNumber else 0
        pass_index = self.index -1 if self.index != 0 else self.PeopleNumber - 1
        
        self.lb_price_name.setText(self.People[self.index])
        self.lb_pass_name.setText(self.People[pass_index])
        self.lb_before_name.setText(self.People[before_index])
    
    def Start(self):
        self.IsStart = True
        while self.NextTime < 2:
            sleep(self.NextTime)
            self.Next()
        self.IsStart = False
        # End
            
    def IncreaseNextTime(self):
        while self.NextTime < 2:
            sleep(0.1)
            self.NextTime = self.NextTime * 1.05
        sleep(3)
        self.NextTime = 0.03


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()