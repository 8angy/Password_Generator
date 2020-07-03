# michael.bangham3@gmail.com
# Create Random passwords for encryption
import hashlib
from random import randrange, choice
import os, string, hashlib
import sys
import pyperclip
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import english_words

class PasswordGenerator(QWidget):
	def __init__(self, parent=None):
		super(PasswordGenerator, self).__init__(parent=parent)  # these values change where the main window is placed
		self.title = 'Password Generator'
		self.width = 295
		self.height = 140
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setWindowIcon(QIcon('icon.ico'))
		self.setFixedSize(self.width, self.height)

		self.instructions_lbl = QLabel(self)
		self.instructions_lbl.move(10,10)
		self.instructions_lbl.setText("Choose password length and type")

		self.lengths = [i for i in range(8,16)]
		self.password_length_combo = QComboBox(self)
		for i in self.lengths:
			self.password_length_combo.addItem(str(i))
		self.password_length_combo.move(210,10)
		# capture a change in the combobox
		self.password_length_combo.setCurrentIndex(4) # 12
		self.pword_len = str(self.password_length_combo.currentText())
		self.password_length_combo.activated.connect(self.capture_length) 

		self.output_lbl = QLabel(self)
		self.output_lbl.move(10,90)
		self.clipboard_notification_lbl = QLabel(self)
		self.clipboard_notification_lbl.move(10,110)

		self.button1 = QPushButton(self)
		self.button1.setText("Alphanumeric")
		self.button1.move(10,50)
		self.button1.clicked.connect(self.generate_alphanumeric)

		self.button2 = QPushButton(self)
		self.button2.setText("Complex")
		self.button2.move(110,50)
		self.button2.clicked.connect(self.generate_complex)

		self.button2 = QPushButton(self)
		self.button2.setText("Memorable")
		self.button2.move(210,50)
		self.button2.clicked.connect(self.generate_memorable)

		self.show()

	def capture_length(self, Text):
		# save the length to a class variable
		self.pword_len = self.lengths[int(Text)]

	def update_output(self, result):
		self.output_lbl.setText(result)
		self.output_lbl.adjustSize()
		pyperclip.copy(result)
		self.clipboard_notification_lbl.setText('Password now resides in your clipboard!')
		self.clipboard_notification_lbl.adjustSize()

	def generate_alphanumeric(self):
		random_data = os.urandom(128)
		self.update_output(str(hashlib.md5(random_data).hexdigest()[:int(self.pword_len)]))

	def generate_complex(self):
		chars = string.ascii_letters + string.digits + string.punctuation
		self.update_output(str(''.join((choice(chars)) for x in range(int(self.pword_len)))))

	def generate_memorable(self):
		words = english_words.words
		x = len(words)
		self.update_output('{}-{}-{}'.format(words[randrange(x)].strip(),words[randrange(x)].strip(),words[randrange(x)].strip()))

def main():
	app = QApplication(sys.argv)
	ex = PasswordGenerator()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()