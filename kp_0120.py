# -*- coding: utf-8 -*-
import sys

#http://dorafop.my.coocan.jp/Qt/Qt107.html

from PyQt5.QtWidgets import *
#from PyQr5.QtGui import*
import PyQt5.QtCore as QtCore
#import PyQt5.QtGui as QtGui
#import PyQt4.QtCore as QtCore
#import PyQt4.QtGui as QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon

pt_list = ["オンバーン", "ユキノオー", "ブルンゲル", "エンテイ", "ドリュウズ", "バルジーナ"]


class ShowPoke(QWidget):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent=parent)
		self.interval = 10
		self.count = 0
		self.setup_ui()


	def setup_ui(self):
		#self.start_button = QPushButton("START", parent=self)
		#self.stop_button = QPushButton("STOP", parent=self)

		# ラベルオブジェクト作成
		#自分PT
		self.lbl_my1 = QLabel(self)
		self.lbl_my2 = QLabel(self)
		self.lbl_my3 = QLabel(self)
		self.lbl_my4 = QLabel(self)
		self.lbl_my5 = QLabel(self)
		self.lbl_my6 = QLabel(self)
		#相手PT
		self.lbl_opponent1 = QLabel(self)
		self.lbl_opponent2 = QLabel(self)
		self.lbl_opponent3 = QLabel(self)
		self.lbl_opponent4 = QLabel(self)
		self.lbl_opponent5 = QLabel(self)
		self.lbl_opponent6 = QLabel(self)

		# QLineEditオブジェクト作成
		#qle = QLineEdit(self)

		#qle.move(60, 100)
		self.lbl_my1.move(60, 40)
		self.lbl_my2.move(160, 40)
		self.lbl_my3.move(60, 80)
		self.lbl_my4.move(160, 80)
		self.lbl_my5.move(60, 120)
		self.lbl_my6.move(160, 120)

		self.lbl_opponent1.move(460, 40)
		self.lbl_opponent2.move(560, 40)
		self.lbl_opponent3.move(460, 80)
		self.lbl_opponent4.move(560, 80)
		self.lbl_opponent5.move(460, 120)
		self.lbl_opponent6.move(560, 120)

		# qleに文字が入力されたら、onChanged関数の呼び出し
		#qle.textChanged[str].connect(self.onChanged)

		self.setGeometry(300, 300, 280, 170)
		self.setWindowTitle('QLineEdit')
		self.show()



	def onChanged(self, text): #今使ってない

		# ラベルに入力されたテキストを挿入
		self.lbl_opponent2.setText(text)
		# 入力されたテキストによって、ラベルの長さを調整
		self.lbl_opponent2.adjustSize()

	def show_pt(self, pt_list):
		self.lbl_my1.setText(pt_list[0])
		self.lbl_my1.adjustSize()
		self.lbl_my2.setText(pt_list[1])
		self.lbl_my2.adjustSize()
		self.lbl_my3.setText(pt_list[2])
		self.lbl_my3.adjustSize()
		self.lbl_my4.setText(pt_list[3])
		self.lbl_my4.adjustSize()
		self.lbl_my5.setText(pt_list[4])
		self.lbl_my5.adjustSize()
		self.lbl_my6.setText(pt_list[5])
		self.lbl_my6.adjustSize()

	#def add_button(self, opponent_name): #ボタンを押すとボタンを生成できないかなと思って
		#self.choose_button2 = QPushButton(opponent_name, parent=self)
		#self.choose_button2.setIcon(QIcon("715.png"))


	def add_opponent(self, opponent_name): #相手のPTを表示する
		if self.count==0:
			# ラベルに入力されたテキストを挿入
			self.lbl_opponent1.setText(opponent_name)
			# 入力されたテキストによって、ラベルの長さを調整
			self.lbl_opponent1.adjustSize()
		elif self.count==1:
			self.lbl_opponent2.setText(opponent_name)
			self.lbl_opponent2.adjustSize()
		elif self.count==2:
			self.lbl_opponent3.setText(opponent_name)
			self.lbl_opponent3.adjustSize()
		elif self.count==3:
			self.lbl_opponent4.setText(opponent_name)
			self.lbl_opponent4.adjustSize()
		elif self.count==4:
			self.lbl_opponent5.setText(opponent_name)
			self.lbl_opponent5.adjustSize()
		elif self.count==5:
			self.lbl_opponent6.setText(opponent_name)
			self.lbl_opponent6.adjustSize()

		self.count += 1

		"""
		layout = QGridLayout()
		layout.addWidget(self.start_button, 0, 0)
		layout.addWidget(self.stop_button, 0, 1)

		self.setLayout(layout)"""



class ButtonBoxWidget(QWidget):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent=parent)
		self.count = 0
		self.setup_ui()
		self.my_chosen_list = []
		self.opponent_chosen_list = []



	def setup_ui(self):
		#自分の選出のボタン
		#self.choose_button1 = QPushButton(pt_list[0], parent=self)
		self.choose_button1 = QPushButton("", parent=self)
		self.choose_button1.setCheckable(True)
		self.choose_button1.setIcon(QIcon("715.png"))
		self.choose_button2 = QPushButton(pt_list[1], parent=self)
		self.choose_button2.setCheckable(True)
		self.choose_button3 = QPushButton(pt_list[2], parent=self)
		self.choose_button3.setCheckable(True)
		self.choose_button4 = QPushButton(pt_list[3], parent=self)
		self.choose_button4.setCheckable(True)
		self.choose_button5 = QPushButton(pt_list[4], parent=self)
		self.choose_button5.setCheckable(True)
		self.choose_button6 = QPushButton(pt_list[5], parent=self)
		self.choose_button6.setCheckable(True)

		#相手のPTのボタン
		self.opponent_pt1 = QPushButton(parent=self)
		self.opponent_pt1.setCheckable(True)
		self.opponent_pt2 = QPushButton(parent=self)
		self.opponent_pt2.setCheckable(True)
		self.opponent_pt3 = QPushButton(parent=self)
		self.opponent_pt3.setCheckable(True)
		self.opponent_pt4 = QPushButton(parent=self)
		self.opponent_pt4.setCheckable(True)
		self.opponent_pt5 = QPushButton(parent=self)
		self.opponent_pt5.setCheckable(True)
		self.opponent_pt6 = QPushButton(parent=self)
		self.opponent_pt6.setCheckable(True)

		#相手のPT入力のためのボタン
		self.opponent_button1 = QPushButton("ミミッキュ", parent=self)
		self.opponent_button2 = QPushButton("ランドロス霊獣", parent=self)
		self.opponent_button3 = QPushButton("リザードン", parent=self)
		self.opponent_button4 = QPushButton("ギャラドス", parent=self)
		self.opponent_button5 = QPushButton("カプ・コケコ", parent=self)
		self.opponent_button6 = QPushButton("バシャーモ", parent=self)
		self.opponent_button7 = QPushButton("カバルドン", parent=self)
		self.opponent_button8 = QPushButton("カプ・テテフ", parent=self)
		self.opponent_button9 = QPushButton("メタグロス", parent=self)
		self.opponent_button10 = QPushButton("アーゴヨン", parent=self)
		self.opponent_button11 = QPushButton("ゲッコウガ", parent=self)
		self.opponent_button12 = QPushButton("ポリゴン２", parent=self)
		self.opponent_button13 = QPushButton("カプ・レヒレ", parent=self)
		self.opponent_button14 = QPushButton("ボルトロス霊獣", parent=self)
		self.opponent_button15 = QPushButton("テッカグヤ", parent=self)
		self.opponent_button16 = QPushButton("ボーマンダ", parent=self)
		self.opponent_button17 = QPushButton("ギルガルド", parent=self)
		self.opponent_button18 = QPushButton("ナットレイ", parent=self)
		self.opponent_button19 = QPushButton("ヒードラン", parent=self)
		self.opponent_button20 = QPushButton("ゲンガー", parent=self)
		self.opponent_button21 = QPushButton("ルカリオ", parent=self)
		self.opponent_button22 = QPushButton("キノガッサ", parent=self)
		self.opponent_button23 = QPushButton("ガブリアス", parent=self)
		self.opponent_button24 = QPushButton("ドリュウズ", parent=self)
		self.opponent_button25 = QPushButton("クチート", parent=self)
		self.opponent_button26 = QPushButton("バンギラス", parent=self)
		self.opponent_button27 = QPushButton("マンムー", parent=self)
		self.opponent_button28 = QPushButton("マリルリ", parent=self)
		self.opponent_button29 = QPushButton("ガルーラ", parent=self)
		self.opponent_button30 = QPushButton("カミツルギ", parent=self)

		#self.stop_button = QPushButton("STOP", parent=self)
		self.new_button = QPushButton("記録せず新規作成", parent=self)
		self.record_button = QPushButton("記録して新規作成", parent=self)
		self.quit_button = QPushButton("QUIT", parent=self)

		layout = QGridLayout()
		#自分側ボタン
		layout.addWidget(self.choose_button1, 0, 0)
		layout.addWidget(self.choose_button2, 0, 1)
		layout.addWidget(self.choose_button3, 1, 0)
		layout.addWidget(self.choose_button4, 1, 1)
		layout.addWidget(self.choose_button5, 2, 0)
		layout.addWidget(self.choose_button6, 2, 1)

		#相手側
		layout.addWidget(self.opponent_pt1, 0, 3)
		layout.addWidget(self.opponent_pt2, 0, 4)
		layout.addWidget(self.opponent_pt3, 1, 3)
		layout.addWidget(self.opponent_pt4, 1, 4)
		layout.addWidget(self.opponent_pt5, 2, 3)
		layout.addWidget(self.opponent_pt6, 2, 4)

		#ポケモン一覧
		layout.addWidget(self.opponent_button1, 3, 0)
		layout.addWidget(self.opponent_button2, 3, 1)
		layout.addWidget(self.opponent_button3, 3, 2)
		layout.addWidget(self.opponent_button4, 3, 3)
		layout.addWidget(self.opponent_button5, 3, 4)
		layout.addWidget(self.opponent_button6, 4, 0)
		layout.addWidget(self.opponent_button7, 4, 1)
		layout.addWidget(self.opponent_button8, 4, 2)
		layout.addWidget(self.opponent_button9, 4, 3)
		layout.addWidget(self.opponent_button10, 4, 4)
		layout.addWidget(self.opponent_button11, 5, 0)
		layout.addWidget(self.opponent_button12, 5, 1)
		layout.addWidget(self.opponent_button13, 5, 2)
		layout.addWidget(self.opponent_button14, 5, 3)
		layout.addWidget(self.opponent_button15, 5, 4)
		layout.addWidget(self.opponent_button16, 6, 0)
		layout.addWidget(self.opponent_button17, 6, 1)
		layout.addWidget(self.opponent_button18, 6, 2)
		layout.addWidget(self.opponent_button19, 6, 3)
		layout.addWidget(self.opponent_button20, 6, 4)
		layout.addWidget(self.opponent_button21, 7, 0)
		layout.addWidget(self.opponent_button22, 7, 1)
		layout.addWidget(self.opponent_button23, 7, 2)
		layout.addWidget(self.opponent_button24, 7, 3)
		layout.addWidget(self.opponent_button25, 7, 4)
		layout.addWidget(self.opponent_button26, 8, 0)
		layout.addWidget(self.opponent_button27, 8, 1)
		layout.addWidget(self.opponent_button28, 8, 2)
		layout.addWidget(self.opponent_button29, 8, 3)
		layout.addWidget(self.opponent_button30, 8, 4)

		layout.addWidget(self.new_button, 9, 2)
		layout.addWidget(self.record_button, 9, 3)
		layout.addWidget(self.quit_button, 9, 4)
		self.setLayout(layout)

	def add_name_opponent_pt(self, opponent_name):
		if self.count==0:
			#選択したボタンの名前を入れる
			self.opponent_pt1.setText(opponent_name)
			#更新
			#self.opponent_pt1.update()
		elif self.count==1:
			self.opponent_pt2.setText(opponent_name)
			#self.opponent_pt2.update()
		elif self.count==2:
			self.opponent_pt3.setText(opponent_name)
			#self.opponent_pt3.update()
		elif self.count==3:
			self.opponent_pt4.setText(opponent_name)
			#self.opponent_pt4.update()
		elif self.count==4:
			self.opponent_pt5.setText(opponent_name)
			#self.opponent_pt5.update()
		elif self.count==5:
			self.opponent_pt6.setText(opponent_name)
			#self.opponent_pt6.update()

		self.count += 1


	def make_my_chosen_list(self, chosen_name): #味方の選んだポケモンをリストに入れる
		if QAbstractButton.toggled(checked):
			self.my_chosen_list.append(chosen_name)
			print (self.my_chosen_list)

	def make_opponent_chosen_list(self, opponent_name):
		self.opponent_chosen_list.append(opponent_name)
		print (self.opponent_chosen_list)


def main():
  app = QApplication( sys.argv )

  # Control outside looking
  panel = QWidget()

  #show_widget = ShowPoke(parent=panel)
  button_box_widget = ButtonBoxWidget(parent=panel)

  panel_layout = QVBoxLayout()
  #panel_layout.addWidget(show_widget)
  panel_layout.addWidget(button_box_widget)
  panel.setLayout(panel_layout)
  panel.setFixedSize(1000, 600)


  main_window = QMainWindow()
  main_window.setWindowTitle( "kp" )
  main_window.setCentralWidget( panel )

  #自分のパーティ
  #pt_list = ["オンバーン", "ユキノオー", "ブルンゲル", "エンテイ", "ドリュウズ", "バルジーナ"]

  #show_widget.show_pt(pt_list)

  #トグルされたときに選出リストに追加する
  """
  button_box_widget.choose_button1.toggled.connect(lambda:
		button_box_widget.make_my_chosen_list(pt_list[0]))
  button_box_widget.choose_button2.clicked.connect(lambda:
		button_box_widget.make_my_chosen_list(pt_list[1]))
  button_box_widget.choose_button3.clicked.connect(lambda:
		button_box_widget.make_my_chosen_list(pt_list[2]))
  button_box_widget.choose_button4.clicked.connect(lambda:
		button_box_widget.make_my_chosen_list(pt_list[3]))
  button_box_widget.choose_button5.clicked.connect(lambda:
		button_box_widget.make_my_chosen_list(pt_list[4]))
  button_box_widget.choose_button6.clicked.connect(lambda:
		button_box_widget.make_my_chosen_list(pt_list[5]))"""



  #テキスト表示するだけの奴↓使わなそう
  #button_box_widget.opponent_button1.clicked.connect(lambda:
  #      show_widget.add_opponent("ミミッキュ"))

  button_box_widget.opponent_button1.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("ミミッキュ"))
  button_box_widget.opponent_button2.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("ランドロス"))
  button_box_widget.opponent_button3.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("リザードン"))
  button_box_widget.opponent_button4.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("ギャラドス"))
  button_box_widget.opponent_button5.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("カプ・コケコ"))
  button_box_widget.opponent_button6.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("バシャーモ"))
  button_box_widget.opponent_button7.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("カバルドン"))
  button_box_widget.opponent_button8.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("カプ・テテフ"))
  button_box_widget.opponent_button9.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("メタグロス"))
  button_box_widget.opponent_button10.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("アーゴヨン"))
  button_box_widget.opponent_button11.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("ゲッコウガ"))
  button_box_widget.opponent_button12.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("ポリゴン２"))
  button_box_widget.opponent_button13.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("レヒレ"))
  button_box_widget.opponent_button14.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("レボルト"))
  button_box_widget.opponent_button15.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("テッカグヤ"))
  button_box_widget.opponent_button16.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("ボーマンダ"))
  button_box_widget.opponent_button17.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("ギルガルド"))
  button_box_widget.opponent_button18.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("ナットレイ"))
  button_box_widget.opponent_button19.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("ヒードラン"))
  button_box_widget.opponent_button20.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("ゲンガー"))
  button_box_widget.opponent_button21.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("ルカリオ"))
  button_box_widget.opponent_button22.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("キノガッサ"))
  button_box_widget.opponent_button23.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("ガブリアス"))
  button_box_widget.opponent_button24.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("ドリュウズ"))
  button_box_widget.opponent_button25.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("クチート"))
  button_box_widget.opponent_button26.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("バンギラス"))
  button_box_widget.opponent_button27.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("マンムー"))
  button_box_widget.opponent_button28.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("マリルリ"))
  button_box_widget.opponent_button29.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("ガルーラ"))
  button_box_widget.opponent_button30.clicked.connect(lambda:
        button_box_widget.add_name_opponent_pt("カミツルギ"))

  button_box_widget.quit_button.clicked.connect(
        app.quit)


  main_window.show()
  app.exec_()

if __name__ == "__main__":
  main()
