import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from GradientDescent import Ui_Form

class UI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.predictionOutput = 0
        self.ui.predictButton.clicked.connect(self.prediction)

    def prediction(self, input):
        self.feature = self.ui.featureslineEdit.text();
        self.target = self.ui.targetlineEdit.text();

        self.input_num = int(self.ui.inputlineEdit.text());

        self.ftList = self.feature.split(",")
        for i in range(len(self.ftList)):
            self.ftList[i] = int(self.ftList[i])
        self.tgList = self.target.split(",")
        for i in range(len(self.tgList)):
            self.tgList[i] = int(self.tgList[i])

        tmp_w, tmp_b = self.gradientDescent(0, 0, self.ftList, self.tgList, 0.00001, 1000000)
        tmp_ans = (float(tmp_w) * float(self.input_num)) + tmp_b
        self.ui.resultLabel.setText(str(tmp_ans))

    def computeGradient(self, w, b, x, y):
        m = len(x)
        gradient_w = 0
        gradient_b = 0
    
        for i in range(m):  
            f_wb = w * x[i] + b 
            djdw_tmp = (f_wb - y[i]) * x[i] 
            djdb_tmp = f_wb - y[i] 
            gradient_b += djdb_tmp
            gradient_w += djdw_tmp
        gradient_w = gradient_w / m 
        gradient_b = gradient_b / m 
        
        return gradient_w, gradient_b

    def gradientDescent(self, w, b, x, y, learning_rate, iteration):
    
        w_var = w
        b_var = b
        for i in range(iteration):
            gradient_w, gradient_b = self.computeGradient(w_var, b_var, x, y)     
            w_var = w_var - (learning_rate * gradient_w)
            b_var = b_var - (learning_rate * gradient_b)
            print("w:" + str(w_var))
            print("b: " + str(b_var))
        
    
        return w_var, b_var

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = UI()
    w.show()
    sys.exit(app.exec_())
