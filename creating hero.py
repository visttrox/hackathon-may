from PyQt5 import QtCore, QtGui, QtWidgets
import sys, json, random
from Double_Slyder import *
from pathlib import Path
from os import path


def read_file(filename):
    with open(filename, encoding='utf8') as file_:
        return file_.read()


def write_to_file(filename, content):
    with open(filename, 'w', encoding='utf8') as file_:
        return file_.write(content)


def render_template(template_path, output_path, context):
    content = read_file(template_path)

    for key, value in context.items():
        content = content.replace('{%s}' % key, str(value))

    write_to_file(output_path, content)


def new_image(person, classes, race, feature, spell, weapon, strength, dexterity, physique, intelligence, wisdom, charisma, points):
    counter = 1
    while True:
        if not path.exists("result_image/image "+str(counter)+'.svg'):
            break
        counter += 1
    context = {
        "person" : person,
        "classes" : classes,
        "race" : race,
        "feature" : feature,
        "spell" : spell,
        "weapon" : weapon,
        "strength" : strength,
        "dexterity" : dexterity,
        "physique" : physique,
        "intelligence" : intelligence,
        "wisdom": wisdom,
        "charisma": charisma,
        "points" : points,
    }
    render_template("kart.svg", "result_image/image "+str(counter)+".svg", context)


class Okno(object):
    def setupUi(self, Window):
        Window.resize(1400, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Window.setWindowIcon(icon)

        self.okno = QtWidgets.QWidget(Window)
        self.okno.setGeometry(QtCore.QRect(0, 10, 1390, 790))
        self.main_layout = QtWidgets.QHBoxLayout(self.okno)
        self.window_1 = QtWidgets.QVBoxLayout()
        self.window_2 = QtWidgets.QVBoxLayout()
        self.line = QtWidgets.QFrame(self.okno)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.main_layout.addLayout(self.window_1)
        self.main_layout.addWidget(self.line)
        self.main_layout.addLayout(self.window_2)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/colors/red.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/colors/green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image/colors/blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("image/colors/yellow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("image/colors/purple.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("image/icons/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("image/icons/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("image/icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icons = [icon1, icon2, icon3, icon4, icon5]

        self._translate = QtCore.QCoreApplication.translate
        with open('names.json', 'r', encoding="utf-8") as file:
            self.data = json.load(file)

        self.classes_box = QtWidgets.QGroupBox(self.okno)
        self.classes_group = QtWidgets.QButtonGroup(self.okno)
        self.classes_group.setExclusive(False)
        self.classes_box.setMaximumSize(QtCore.QSize(700, 90))
        self.classes_layout = QtWidgets.QHBoxLayout(self.classes_box)
        for name in self.data['Классы']:
            self.classes_button = QtWidgets.QCheckBox(self.classes_box)
            self.classes_button.setChecked(True)
            self.classes_button.setText(self._translate("Window", name))
            self.classes_layout.addWidget(self.classes_button)
            self.classes_group.addButton(self.classes_button)
        self.window_1.addWidget(self.classes_box)

        self.race_box = QtWidgets.QGroupBox(self.okno)
        self.race_group = QtWidgets.QButtonGroup(self.okno)
        self.race_group.setExclusive(False)
        self.race_box.setMaximumSize(QtCore.QSize(700, 90))
        self.race_layout = QtWidgets.QHBoxLayout(self.race_box)
        for name in self.data['Расы']:
            self.race_button = QtWidgets.QCheckBox(self.race_box)
            self.race_button.setChecked(True)
            self.race_button.setText(self._translate("Window", name))
            self.race_layout.addWidget(self.race_button)
            self.race_group.addButton(self.race_button)
        self.window_1.addWidget(self.race_box)

        self.feature_box = QtWidgets.QGroupBox(self.okno)
        self.feature_group = QtWidgets.QButtonGroup(self.okno)
        self.feature_group.setExclusive(False)
        self.feature_box.setMaximumSize(QtCore.QSize(700, 90))
        self.feature_layout = QtWidgets.QHBoxLayout(self.feature_box)
        for name in self.data['Черты']:
            self.feature_button = QtWidgets.QCheckBox(self.feature_box)
            self.feature_button.setChecked(True)
            self.feature_button.setText(self._translate("Window", name))
            self.feature_layout.addWidget(self.feature_button)
            self.feature_group.addButton(self.feature_button)
        self.window_1.addWidget(self.feature_box)

        self.spells_box = QtWidgets.QGroupBox(self.okno)
        self.spells_group = QtWidgets.QButtonGroup(self.okno)
        self.spells_group.setExclusive(False)
        self.spells_box.setMaximumSize(QtCore.QSize(700, 90))
        self.spells_layout = QtWidgets.QHBoxLayout(self.spells_box)
        for name in self.data['Заклинания']:
            self.spells_button = QtWidgets.QCheckBox(self.spells_box)
            self.spells_button.setChecked(True)
            self.spells_button.setText(self._translate("Window", name))
            self.spells_layout.addWidget(self.spells_button)
            self.spells_group.addButton(self.spells_button)
        self.window_1.addWidget(self.spells_box)

        self.weapon_box = QtWidgets.QGroupBox(self.okno)
        self.weapon_box.setMaximumSize(QtCore.QSize(700, 90))
        self.weapon_group = QtWidgets.QButtonGroup(self.okno)
        self.weapon_group.setExclusive(False)
        self.weapon_layout = QtWidgets.QHBoxLayout(self.weapon_box)
        for name in self.data['Оружия']:
            self.weapon_button = QtWidgets.QCheckBox(self.weapon_box)
            self.weapon_button.setChecked(True)
            self.weapon_button.setText(self._translate("Window", name))
            self.weapon_layout.addWidget(self.weapon_button)
            self.weapon_group.addButton(self.weapon_button)
        self.window_1.addWidget(self.weapon_box)

        self.points_layout = QtWidgets.QHBoxLayout()
        self.instructions = QtWidgets.QPushButton(self.okno)
        self.instructions.setMaximumWidth(100)
        self.instructions.clicked.connect(self.instruction)
        self.points_layout.addWidget(self.instructions)
        self.min_points = QtWidgets.QLabel(self.okno)
        self.min_points.setMaximumSize(QtCore.QSize(180, 30))
        self.min_points.setFrameShape(QtWidgets.QFrame.Panel)
        self.min_points.setAlignment(QtCore.Qt.AlignCenter)
        self.points_layout.addWidget(self.min_points)
        self.max_points = QtWidgets.QLabel(self.okno)
        self.max_points.setMaximumSize(QtCore.QSize(180, 30))
        self.max_points.setFrameShape(QtWidgets.QFrame.Panel)
        self.max_points.setAlignment(QtCore.Qt.AlignCenter)
        self.points_layout.addWidget(self.max_points)
        self.window_1.addLayout(self.points_layout)
        
        self.strength_layout = QtWidgets.QHBoxLayout()
        self.strength_layout.setContentsMargins(10, -1, -1, -1)
        self.text_strength = QtWidgets.QLabel(self.okno)
        self.text_strength.setMinimumSize(QtCore.QSize(100, 0))
        self.strength_layout.addWidget(self.text_strength)
        self.spinbox_number_strength_min = QtWidgets.QSpinBox(self.okno)
        self.spinbox_number_strength_min.setAlignment(QtCore.Qt.AlignCenter)
        self.spinbox_number_strength_min.setRange(1, 15)
        self.spinbox_number_strength_min.setValue(1)
        self.spinbox_number_strength_min.setMinimumWidth(50)
        self.spinbox_number_strength_max = QtWidgets.QSpinBox(self.okno)
        self.spinbox_number_strength_max.setAlignment(QtCore.Qt.AlignCenter)
        self.spinbox_number_strength_max.setRange(1, 15)
        self.spinbox_number_strength_max.setValue(15)
        self.spinbox_number_strength_max.setMinimumWidth(50)
        self.strength_slider = RangeSlider(self.spinbox_number_strength_min, self.spinbox_number_strength_max)
        self.strength_slider.setRangeLimit(0, 14)
        self.strength_slider.setRange(0, 14)
        self.strength_slider.setTickPosition(3)
        self.spinbox_number_strength_min.valueChanged.connect(lambda : (self.new_points(), self.strength_slider.new())) 
        self.spinbox_number_strength_max.valueChanged.connect(lambda : (self.new_points(), self.strength_slider.new()))
        self.strength_layout.addWidget(self.strength_slider)
        self.strength_layout.addWidget(self.spinbox_number_strength_min)
        self.strength_layout.addWidget(self.spinbox_number_strength_max)
        self.list_strength = QtWidgets.QComboBox(self.okno)
        self.list_strength.setMinimumSize(QtCore.QSize(170, 0))
        self.list_strength.addItem("Нет группы сравнения")
        counter = 0
        for color in self.data['Группы']:
            self.list_strength.addItem(self.icons[counter], color)
            counter += 1
        self.strength_layout.addWidget(self.list_strength)
        self.window_1.addLayout(self.strength_layout)

        self.dexterity_layout = QtWidgets.QHBoxLayout()
        self.dexterity_layout.setContentsMargins(10, -1, -1, -1)
        self.text_dexterity = QtWidgets.QLabel(self.okno)
        self.text_dexterity.setMinimumSize(QtCore.QSize(100, 0))
        self.dexterity_layout.addWidget(self.text_dexterity)
        self.spinbox_number_dexterity_min = QtWidgets.QSpinBox(self.okno)
        self.spinbox_number_dexterity_min.setAlignment(QtCore.Qt.AlignCenter)
        self.spinbox_number_dexterity_min.setRange(1, 15)
        self.spinbox_number_dexterity_min.setValue(1)
        self.spinbox_number_dexterity_min.setMinimumWidth(50)
        self.spinbox_number_dexterity_max = QtWidgets.QSpinBox(self.okno)
        self.spinbox_number_dexterity_max.setAlignment(QtCore.Qt.AlignCenter)
        self.spinbox_number_dexterity_max.setRange(1, 15)
        self.spinbox_number_dexterity_max.setValue(15)
        self.spinbox_number_dexterity_max.setMinimumWidth(50)
        self.dexterity_slider = RangeSlider(self.spinbox_number_dexterity_min, self.spinbox_number_dexterity_max)
        self.dexterity_slider.setRangeLimit(0, 14)
        self.dexterity_slider.setRange(0, 14)
        self.dexterity_slider.setTickPosition(3)
        self.spinbox_number_dexterity_min.valueChanged.connect(lambda : (self.new_points(), self.dexterity_slider.new()))
        self.spinbox_number_dexterity_max.valueChanged.connect(lambda : (self.new_points(), self.dexterity_slider.new()))
        self.dexterity_layout.addWidget(self.dexterity_slider)
        self.dexterity_layout.addWidget(self.spinbox_number_dexterity_min)
        self.dexterity_layout.addWidget(self.spinbox_number_dexterity_max)
        self.list_dexterity = QtWidgets.QComboBox(self.okno)
        self.list_dexterity.setMinimumSize(QtCore.QSize(170, 0))
        self.list_dexterity.addItem("Нет группы сравнения")
        counter = 0
        for color in self.data['Группы']:
            self.list_dexterity.addItem(self.icons[counter], color)
            counter += 1
        self.dexterity_layout.addWidget(self.list_dexterity)
        self.window_1.addLayout(self.dexterity_layout)

        self.physique_layout = QtWidgets.QHBoxLayout()
        self.physique_layout.setContentsMargins(10, -1, -1, -1)
        self.text_physique = QtWidgets.QLabel(self.okno)
        self.text_physique.setMinimumSize(QtCore.QSize(100, 0))
        self.physique_layout.addWidget(self.text_physique)
        self.spinbox_number_physique_min = QtWidgets.QSpinBox(self.okno)
        self.spinbox_number_physique_min.setAlignment(QtCore.Qt.AlignCenter)
        self.spinbox_number_physique_min.setRange(1, 15)
        self.spinbox_number_physique_min.setValue(1)
        self.spinbox_number_physique_min.setMinimumWidth(50)
        self.spinbox_number_physique_max = QtWidgets.QSpinBox(self.okno)
        self.spinbox_number_physique_max.setAlignment(QtCore.Qt.AlignCenter)
        self.spinbox_number_physique_max.setRange(1, 15)
        self.spinbox_number_physique_max.setValue(15)
        self.spinbox_number_physique_max.setMinimumWidth(50)
        self.physique_slider = RangeSlider(self.spinbox_number_physique_min, self.spinbox_number_physique_max)
        self.physique_slider.setRangeLimit(0, 14)
        self.physique_slider.setRange(0, 14)
        self.physique_slider.setTickPosition(3)
        self.spinbox_number_physique_min.valueChanged.connect(lambda : (self.new_points(), self.physique_slider.new())) 
        self.spinbox_number_physique_max.valueChanged.connect(lambda : (self.new_points(), self.physique_slider.new()))
        self.physique_layout.addWidget(self.physique_slider)
        self.physique_layout.addWidget(self.spinbox_number_physique_min)
        self.physique_layout.addWidget(self.spinbox_number_physique_max)
        self.list_physique = QtWidgets.QComboBox(self.okno)
        self.list_physique.setMinimumSize(QtCore.QSize(170, 0))
        self.list_physique.addItem("Нет группы сравнения")
        counter = 0
        for color in self.data['Группы']:
            self.list_physique.addItem(self.icons[counter], color)
            counter += 1
        self.physique_layout.addWidget(self.list_physique)
        self.window_1.addLayout(self.physique_layout)

        self.intelligence_layout = QtWidgets.QHBoxLayout()
        self.intelligence_layout.setContentsMargins(10, -1, -1, -1)
        self.text_intelligence = QtWidgets.QLabel(self.okno)
        self.text_intelligence.setMinimumSize(QtCore.QSize(100, 0))
        self.intelligence_layout.addWidget(self.text_intelligence)
        self.spinbox_number_intelligence_min = QtWidgets.QSpinBox(self.okno)
        self.spinbox_number_intelligence_min.setAlignment(QtCore.Qt.AlignCenter)
        self.spinbox_number_intelligence_min.setRange(1, 15)
        self.spinbox_number_intelligence_min.setValue(1)
        self.spinbox_number_intelligence_min.setMinimumWidth(50)
        self.spinbox_number_intelligence_max = QtWidgets.QSpinBox(self.okno)
        self.spinbox_number_intelligence_max.setAlignment(QtCore.Qt.AlignCenter)
        self.spinbox_number_intelligence_max.setRange(1, 15)
        self.spinbox_number_intelligence_max.setValue(15)
        self.spinbox_number_intelligence_max.setMinimumWidth(50)
        self.intelligence_slider = RangeSlider(self.spinbox_number_intelligence_min, self.spinbox_number_intelligence_max)
        self.intelligence_slider.setRangeLimit(0, 14)
        self.intelligence_slider.setRange(0, 14)
        self.intelligence_slider.setTickPosition(3)
        self.spinbox_number_intelligence_min.valueChanged.connect(lambda : (self.new_points(), self.intelligence_slider.new()))
        self.spinbox_number_intelligence_max.valueChanged.connect(lambda : (self.new_points(), self.intelligence_slider.new()))
        self.intelligence_layout.addWidget(self.intelligence_slider)
        self.intelligence_layout.addWidget(self.spinbox_number_intelligence_min)
        self.intelligence_layout.addWidget(self.spinbox_number_intelligence_max)
        self.list_intelligence = QtWidgets.QComboBox(self.okno)
        self.list_intelligence.setMinimumSize(QtCore.QSize(170, 0))
        self.list_intelligence.addItem("Нет группы сравнения")
        counter = 0
        for color in self.data['Группы']:
            self.list_intelligence.addItem(self.icons[counter], color)
            counter += 1
        self.intelligence_layout.addWidget(self.list_intelligence)
        self.window_1.addLayout(self.intelligence_layout)

        self.wisdom_layout = QtWidgets.QHBoxLayout()
        self.wisdom_layout.setContentsMargins(10, -1, -1, -1)
        self.text_wisdom = QtWidgets.QLabel(self.okno)
        self.text_wisdom.setMinimumSize(QtCore.QSize(100, 0))
        self.wisdom_layout.addWidget(self.text_wisdom)
        self.spinbox_number_wisdom_min = QtWidgets.QSpinBox(self.okno)
        self.spinbox_number_wisdom_min.setAlignment(QtCore.Qt.AlignCenter)
        self.spinbox_number_wisdom_min.setRange(1, 15)
        self.spinbox_number_wisdom_min.setValue(1)
        self.spinbox_number_wisdom_min.setMinimumWidth(50)
        self.spinbox_number_wisdom_max = QtWidgets.QSpinBox(self.okno)
        self.spinbox_number_wisdom_max.setAlignment(QtCore.Qt.AlignCenter)
        self.spinbox_number_wisdom_max.setRange(1, 15)
        self.spinbox_number_wisdom_max.setValue(15)
        self.spinbox_number_wisdom_max.setMinimumWidth(50)
        self.wisdom_slider = RangeSlider(self.spinbox_number_wisdom_min, self.spinbox_number_wisdom_max)
        self.wisdom_slider.setRangeLimit(0, 14)
        self.wisdom_slider.setRange(0, 14)
        self.wisdom_slider.setTickPosition(3)
        self.spinbox_number_wisdom_min.valueChanged.connect(lambda : (self.new_points(), self.wisdom_slider.new()))
        self.spinbox_number_wisdom_max.valueChanged.connect(lambda : (self.new_points(), self.wisdom_slider.new()))
        self.wisdom_layout.addWidget(self.wisdom_slider)
        self.wisdom_layout.addWidget(self.spinbox_number_wisdom_min)
        self.wisdom_layout.addWidget(self.spinbox_number_wisdom_max)
        self.list_wisdom = QtWidgets.QComboBox(self.okno)
        self.list_wisdom.setMinimumSize(QtCore.QSize(170, 0))
        self.list_wisdom.addItem("Нет группы сравнения")
        counter = 0
        for color in self.data['Группы']:
            self.list_wisdom.addItem(self.icons[counter], color)
            counter += 1
        self.wisdom_layout.addWidget(self.list_wisdom)
        self.window_1.addLayout(self.wisdom_layout)

        self.charisma_layout = QtWidgets.QHBoxLayout()
        self.charisma_layout.setContentsMargins(10, -1, -1, -1)
        self.text_charisma = QtWidgets.QLabel(self.okno)
        self.text_charisma.setMinimumSize(QtCore.QSize(100, 0))
        self.charisma_layout.addWidget(self.text_charisma)
        self.spinbox_number_charisma_min = QtWidgets.QSpinBox(self.okno)
        self.spinbox_number_charisma_min.setAlignment(QtCore.Qt.AlignCenter)
        self.spinbox_number_charisma_min.setRange(1, 15)
        self.spinbox_number_charisma_min.setValue(1)
        self.spinbox_number_charisma_min.setMinimumWidth(50)
        self.spinbox_number_charisma_max = QtWidgets.QSpinBox(self.okno)
        self.spinbox_number_charisma_max.setAlignment(QtCore.Qt.AlignCenter)
        self.spinbox_number_charisma_max.setRange(1, 15)
        self.spinbox_number_charisma_max.setValue(15)
        self.spinbox_number_charisma_max.setMinimumWidth(50)
        self.charisma_slider = RangeSlider(self.spinbox_number_charisma_min, self.spinbox_number_charisma_max)
        self.charisma_slider.setRangeLimit(0, 14)
        self.charisma_slider.setRange(0, 14)
        self.charisma_slider.setTickPosition(3)
        self.spinbox_number_charisma_min.valueChanged.connect(lambda : (self.new_points(), self.charisma_slider.new()))
        self.spinbox_number_charisma_max.valueChanged.connect(lambda : (self.new_points(), self.charisma_slider.new()))
        self.charisma_layout.addWidget(self.charisma_slider)
        self.charisma_layout.addWidget(self.spinbox_number_charisma_min)
        self.charisma_layout.addWidget(self.spinbox_number_charisma_max)
        self.list_charisma = QtWidgets.QComboBox(self.okno)
        self.list_charisma.setMinimumSize(QtCore.QSize(170, 0))
        self.list_charisma.addItem("Нет группы сравнения")
        counter = 0
        for color in self.data['Группы']:
            self.list_charisma.addItem(self.icons[counter], color)
            counter += 1
        self.charisma_layout.addWidget(self.list_charisma)
        self.window_1.addLayout(self.charisma_layout)

        self.list_sliders = [self.strength_slider, self.dexterity_slider, self.physique_slider, self.intelligence_slider, self.wisdom_slider, self.charisma_slider]

        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.setContentsMargins(-1, -1, -1, 10)
        self.number_characters_layout = QtWidgets.QHBoxLayout()
        self.text_number_characters = QtWidgets.QLabel(self.okno)
        self.text_number_characters.setMaximumWidth(150)
        self.text_number_characters.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.number_characters_layout.addWidget(self.text_number_characters)
        self.spinbox_number_characters = QtWidgets.QSpinBox(self.okno)
        self.spinbox_number_characters.setMaximumWidth(100)
        self.spinbox_number_characters.setAlignment(QtCore.Qt.AlignCenter)
        self.spinbox_number_characters.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinbox_number_characters.setMinimum(1)
        self.spinbox_number_characters.setValue(5)
        self.number_characters_layout.addWidget(self.spinbox_number_characters)
        self.button_layout.addLayout(self.number_characters_layout)
        self.generate_button = QtWidgets.QPushButton(self.okno)
        self.generate_button.setMaximumWidth(100)
        self.generate_button.clicked.connect(self.generate)
        self.button_layout.addWidget(self.generate_button)
        self.reset_button = QtWidgets.QPushButton(self.okno)
        self.reset_button.setMaximumWidth(80)
        self.reset_button.clicked.connect(self.reset)
        self.button_layout.addWidget(self.reset_button)
        self.window_1.addLayout(self.button_layout)

        self.division_window_layout = QtWidgets.QHBoxLayout()
        self.features_layout = QtWidgets.QVBoxLayout()
        self.features_layout.setContentsMargins(10, -1, -1, -1)

        self.person_layout = QtWidgets.QHBoxLayout()
        self.text_person = QtWidgets.QLabel(self.okno)
        self.text_person.setMinimumWidth(250)
        self.person_layout.addWidget(self.text_person)
        self.features_layout.addLayout(self.person_layout)
        self.text_person.setMaximumHeight(35)

        self.class_layout = QtWidgets.QHBoxLayout()
        self.class_layout.setSpacing(100)
        self.text_class = QtWidgets.QLabel(self.okno)
        self.text_class.setMinimumWidth(250)
        self.class_layout.addWidget(self.text_class)
        self.reset_class_button = QtWidgets.QPushButton(self.okno)
        self.reset_class_button.setMaximumSize(QtCore.QSize(35, 35))
        self.reset_class_button.setIcon(icon6)
        self.reset_class_button.setIconSize(QtCore.QSize(30, 30))
        self.reset_class_button.clicked.connect(lambda : self.reset_characters(self.classes_group, self.text_class, "Класс"))
        self.reset_class_button.setDisabled(True)
        self.class_layout.addWidget(self.reset_class_button)
        self.features_layout.addLayout(self.class_layout)

        self.race_layout = QtWidgets.QHBoxLayout()
        self.race_layout.setSpacing(100)
        self.text_race = QtWidgets.QLabel(self.okno)
        self.text_race.setMinimumWidth(250)
        self.race_layout.addWidget(self.text_race)
        self.reset_race_button = QtWidgets.QPushButton(self.okno)
        self.reset_race_button.setMaximumSize(QtCore.QSize(35, 35))
        self.reset_race_button.setIcon(icon6)
        self.reset_race_button.setIconSize(QtCore.QSize(30, 30))
        self.reset_race_button.clicked.connect(lambda : self.reset_characters(self.race_group, self.text_race, "Раса"))
        self.reset_race_button.setDisabled(True)
        self.race_layout.addWidget(self.reset_race_button)
        self.features_layout.addLayout(self.race_layout)

        self.feature_layout = QtWidgets.QHBoxLayout()
        self.feature_layout.setSpacing(100)
        self.text_feature = QtWidgets.QLabel(self.okno)
        self.text_feature.setMinimumWidth(250)
        self.feature_layout.addWidget(self.text_feature)
        self.reset_feature_button = QtWidgets.QPushButton(self.okno)
        self.reset_feature_button.setMaximumSize(QtCore.QSize(35, 35))
        self.reset_feature_button.setIcon(icon6)
        self.reset_feature_button.setIconSize(QtCore.QSize(30, 30))
        self.reset_feature_button.clicked.connect(lambda : self.reset_characters(self.feature_group, self.text_feature, "Черта"))
        self.reset_feature_button.setDisabled(True)
        self.feature_layout.addWidget(self.reset_feature_button)
        self.features_layout.addLayout(self.feature_layout)

        self.spells_layout = QtWidgets.QHBoxLayout()
        self.spells_layout.setSpacing(100)
        self.text_spells = QtWidgets.QLabel(self.okno)
        self.text_spells.setMinimumWidth(250)
        self.spells_layout.addWidget(self.text_spells)
        self.reset_spells_button = QtWidgets.QPushButton(self.okno)
        self.reset_spells_button.setMaximumSize(QtCore.QSize(35, 35))
        self.reset_spells_button.setIcon(icon6)
        self.reset_spells_button.setIconSize(QtCore.QSize(30, 30))
        self.reset_spells_button.clicked.connect(lambda : self.reset_characters(self.spells_group, self.text_spells, "Заклинание"))
        self.reset_spells_button.setDisabled(True)
        self.spells_layout.addWidget(self.reset_spells_button)
        self.features_layout.addLayout(self.spells_layout)

        self.weapon_layout = QtWidgets.QHBoxLayout()
        self.weapon_layout.setSpacing(100)
        self.text_weapon = QtWidgets.QLabel(self.okno)
        self.text_weapon.setMaximumWidth(250)
        self.weapon_layout.addWidget(self.text_weapon)
        self.reset_weapon_button = QtWidgets.QPushButton(self.okno)
        self.reset_weapon_button.setMaximumSize(QtCore.QSize(35, 35))
        self.reset_weapon_button.setIcon(icon6)
        self.reset_weapon_button.setIconSize(QtCore.QSize(30, 30))
        self.reset_weapon_button.clicked.connect(lambda : self.reset_characters(self.weapon_group, self.text_weapon, "Оружие"))
        self.reset_weapon_button.setDisabled(True)
        self.weapon_layout.addWidget(self.reset_weapon_button)
        self.features_layout.addLayout(self.weapon_layout)

        self.strength_layout_2 = QtWidgets.QHBoxLayout()
        self.text_strength_2 = QtWidgets.QLabel(self.okno)
        self.strength_layout_2.addWidget(self.text_strength_2)
        self.minus_strength_button = QtWidgets.QPushButton(self.okno)
        self.minus_strength_button.setMaximumSize(QtCore.QSize(35, 35))
        self.minus_strength_button.setIcon(icon7)
        self.minus_strength_button.setIconSize(QtCore.QSize(30, 30))
        self.minus_strength_button.setDisabled(True)
        self.minus_strength_button.clicked.connect(lambda : self.minus_and_plus(self.minus_strength_button, self.plus_strength_button, -1, self.text_strength_2, "Сила"))
        self.strength_layout_2.addWidget(self.minus_strength_button)
        self.plus_strength_button = QtWidgets.QPushButton(self.okno)
        self.plus_strength_button.setMaximumSize(QtCore.QSize(35, 35))
        self.plus_strength_button.setIcon(icon8)
        self.plus_strength_button.setIconSize(QtCore.QSize(30, 30))
        self.plus_strength_button.setDisabled(True)
        self.plus_strength_button.clicked.connect(lambda : self.minus_and_plus(self.minus_strength_button, self.plus_strength_button, 1, self.text_strength_2, "Сила"))
        self.strength_layout_2.addWidget(self.plus_strength_button)
        self.features_layout.addLayout(self.strength_layout_2)

        self.dexterity_layout_2 = QtWidgets.QHBoxLayout()
        self.text_dexterity_2 = QtWidgets.QLabel(self.okno)
        self.dexterity_layout_2.addWidget(self.text_dexterity_2)
        self.minus_dexterity_button = QtWidgets.QPushButton(self.okno)
        self.minus_dexterity_button.setMaximumSize(QtCore.QSize(35, 35))
        self.minus_dexterity_button.setIcon(icon7)
        self.minus_dexterity_button.setIconSize(QtCore.QSize(30, 30))
        self.minus_dexterity_button.setDisabled(True)
        self.minus_dexterity_button.clicked.connect(lambda : self.minus_and_plus(self.minus_dexterity_button, self.plus_dexterity_button, -1, self.text_dexterity_2, "Ловкость"))
        self.dexterity_layout_2.addWidget(self.minus_dexterity_button)
        self.plus_dexterity_button = QtWidgets.QPushButton(self.okno)
        self.plus_dexterity_button.setMaximumSize(QtCore.QSize(35, 35))
        self.plus_dexterity_button.setIcon(icon8)
        self.plus_dexterity_button.setIconSize(QtCore.QSize(30, 30))
        self.plus_dexterity_button.setDisabled(True)
        self.plus_dexterity_button.clicked.connect(lambda : self.minus_and_plus(self.minus_dexterity_button, self.plus_dexterity_button, 1, self.text_dexterity_2, "Ловкость"))
        self.dexterity_layout_2.addWidget(self.plus_dexterity_button)
        self.features_layout.addLayout(self.dexterity_layout_2)

        self.physique_layout_2 = QtWidgets.QHBoxLayout()
        self.text_physique_2 = QtWidgets.QLabel(self.okno)
        self.physique_layout_2.addWidget(self.text_physique_2)
        self.minus_physique_button = QtWidgets.QPushButton(self.okno)
        self.minus_physique_button.setMaximumSize(QtCore.QSize(35, 35))
        self.minus_physique_button.setIcon(icon7)
        self.minus_physique_button.setIconSize(QtCore.QSize(30, 30))
        self.minus_physique_button.setDisabled(True)
        self.minus_physique_button.clicked.connect(lambda : self.minus_and_plus(self.minus_physique_button, self.plus_physique_button, -1, self.text_physique_2, "Телосложение"))
        self.physique_layout_2.addWidget(self.minus_physique_button)
        self.plus_physique_button = QtWidgets.QPushButton(self.okno)
        self.plus_physique_button.setMaximumSize(QtCore.QSize(35, 35))
        self.plus_physique_button.setIcon(icon8)
        self.plus_physique_button.setIconSize(QtCore.QSize(30, 30))
        self.plus_physique_button.setDisabled(True)
        self.plus_physique_button.clicked.connect(lambda : self.minus_and_plus(self.minus_physique_button, self.plus_physique_button, 1, self.text_physique_2, "Телосложение"))
        self.physique_layout_2.addWidget(self.plus_physique_button)
        self.features_layout.addLayout(self.physique_layout_2)

        self.intelligence_layout_2 = QtWidgets.QHBoxLayout()
        self.text_intelligence_2 = QtWidgets.QLabel(self.okno)
        self.intelligence_layout_2.addWidget(self.text_intelligence_2)
        self.minus_intelligence_button = QtWidgets.QPushButton(self.okno)
        self.minus_intelligence_button.setMaximumSize(QtCore.QSize(35, 35))
        self.minus_intelligence_button.setIcon(icon7)
        self.minus_intelligence_button.setIconSize(QtCore.QSize(30, 30))
        self.minus_intelligence_button.setDisabled(True)
        self.minus_intelligence_button.clicked.connect(lambda : self.minus_and_plus(self.minus_intelligence_button, self.plus_intelligence_button, -1, self.text_intelligence_2, "Интеллект"))
        self.intelligence_layout_2.addWidget(self.minus_intelligence_button)
        self.plus_intelligence_button = QtWidgets.QPushButton(self.okno)
        self.plus_intelligence_button.setMaximumSize(QtCore.QSize(35, 35))
        self.plus_intelligence_button.setIcon(icon8)
        self.plus_intelligence_button.setIconSize(QtCore.QSize(30, 30))
        self.plus_intelligence_button.setDisabled(True)
        self.plus_intelligence_button.clicked.connect(lambda : self.minus_and_plus(self.minus_intelligence_button, self.plus_intelligence_button, 1, self.text_intelligence_2, "Интеллект"))
        self.intelligence_layout_2.addWidget(self.plus_intelligence_button)
        self.features_layout.addLayout(self.intelligence_layout_2)

        self.wisdom_layout_2 = QtWidgets.QHBoxLayout()
        self.text_wisdom_2 = QtWidgets.QLabel(self.okno)
        self.wisdom_layout_2.addWidget(self.text_wisdom_2)
        self.minus_wisdom_button = QtWidgets.QPushButton(self.okno)
        self.minus_wisdom_button.setMaximumSize(QtCore.QSize(35, 35))
        self.minus_wisdom_button.setIcon(icon7)
        self.minus_wisdom_button.setIconSize(QtCore.QSize(30, 30))
        self.minus_wisdom_button.setDisabled(True)
        self.minus_wisdom_button.clicked.connect(lambda : self.minus_and_plus(self.minus_wisdom_button, self.plus_wisdom_button, -1, self.text_wisdom_2, "Мудрость"))
        self.wisdom_layout_2.addWidget(self.minus_wisdom_button)
        self.plus_wisdom_button = QtWidgets.QPushButton(self.okno)
        self.plus_wisdom_button.setMaximumSize(QtCore.QSize(35, 35))
        self.plus_wisdom_button.setIcon(icon8)
        self.plus_wisdom_button.setIconSize(QtCore.QSize(30, 30))
        self.plus_wisdom_button.setDisabled(True)
        self.plus_wisdom_button.clicked.connect(lambda : self.minus_and_plus(self.minus_wisdom_button, self.plus_wisdom_button, 1, self.text_wisdom_2, "Мудрость"))
        self.wisdom_layout_2.addWidget(self.plus_wisdom_button)
        self.features_layout.addLayout(self.wisdom_layout_2)

        self.charisma_layout_2 = QtWidgets.QHBoxLayout()
        self.text_charisma_2 = QtWidgets.QLabel(self.okno)
        self.charisma_layout_2.addWidget(self.text_charisma_2)
        self.minus_charisma_button = QtWidgets.QPushButton(self.okno)
        self.minus_charisma_button.setMaximumSize(QtCore.QSize(35, 35))
        self.minus_charisma_button.setIcon(icon7)
        self.minus_charisma_button.setIconSize(QtCore.QSize(30, 30))
        self.minus_charisma_button.setDisabled(True)
        self.minus_charisma_button.clicked.connect(lambda : self.minus_and_plus(self.minus_charisma_button, self.plus_charisma_button, -1, self.text_charisma_2, "Харизма"))
        self.charisma_layout_2.addWidget(self.minus_charisma_button)
        self.plus_charisma_button = QtWidgets.QPushButton(self.okno)
        self.plus_charisma_button.setMaximumSize(QtCore.QSize(35, 35))
        self.plus_charisma_button.setIcon(icon8)
        self.plus_charisma_button.setIconSize(QtCore.QSize(30, 30))
        self.plus_charisma_button.setDisabled(True)
        self.plus_charisma_button.clicked.connect(lambda : self.minus_and_plus(self.minus_charisma_button, self.plus_charisma_button, 1, self.text_charisma_2, "Харизма"))
        self.charisma_layout_2.addWidget(self.plus_charisma_button)
        self.features_layout.addLayout(self.charisma_layout_2)

        self.points_layout_2 = QtWidgets.QHBoxLayout()
        self.text_points = QtWidgets.QLabel(self.okno)
        self.text_points.setMaximumHeight(30)
        self.points_layout_2.addWidget(self.text_points)
        self.features_layout.addLayout(self.points_layout_2)

        self.dowload_image_layout = QtWidgets.QHBoxLayout()
        self.dowload_image_button = QtWidgets.QPushButton(self.okno)
        self.dowload_image_button.setMaximumWidth(150)
        self.dowload_image_button.setDisabled(True)
        self.dowload_image_button.clicked.connect(lambda : new_image(
        "Персонаж "+str(self.person), 
        self.list_characters["Персонаж "+str(self.person)]["Класс"], 
        self.list_characters["Персонаж "+str(self.person)]["Раса"], 
        self.list_characters["Персонаж "+str(self.person)]["Черта"], 
        self.list_characters["Персонаж "+str(self.person)]["Заклинание"], 
        self.list_characters["Персонаж "+str(self.person)]["Оружие"], 
        self.list_characters["Персонаж "+str(self.person)]["Сила"], 
        self.list_characters["Персонаж "+str(self.person)]["Ловкость"], 
        self.list_characters["Персонаж "+str(self.person)]["Телосложение"], 
        self.list_characters["Персонаж "+str(self.person)]["Интеллект"], 
        self.list_characters["Персонаж "+str(self.person)]["Мудрость"], 
        self.list_characters["Персонаж "+str(self.person)]["Харизма"], 
        self.list_characters["Персонаж "+str(self.person)]["Очков"]))
        self.dowload_image_layout.addWidget(self.dowload_image_button)
        self.features_layout.addLayout(self.dowload_image_layout)

        self.division_window_layout.addLayout(self.features_layout)

        self.image_layout = QtWidgets.QVBoxLayout()

        self.image_race = QtWidgets.QLabel(self.okno)
        self.image_race.setMaximumSize(QtCore.QSize(200, 200))
        self.image_layout.addWidget(self.image_race)

        self.image_weapon = QtWidgets.QLabel(self.okno)
        self.image_weapon.setMaximumSize(QtCore.QSize(200, 200))
        self.image_layout.addWidget(self.image_weapon)

        self.image_spells = QtWidgets.QLabel(self.okno)
        self.image_spells.setMaximumSize(QtCore.QSize(200, 200))
        self.image_layout.addWidget(self.image_spells)

        self.switch_layout = QtWidgets.QHBoxLayout()
        self.switch_layout.setContentsMargins(0, 0, 10, 10)
        self.previous_button = QtWidgets.QPushButton(self.okno)
        self.previous_button.setDisabled(True)
        self.previous_button.clicked.connect(self.back)
        self.switch_layout.addWidget(self.previous_button)
        self.next_button = QtWidgets.QPushButton(self.okno)
        self.next_button.setDisabled(True)
        self.next_button.clicked.connect(self.forth)
        self.switch_layout.addWidget(self.next_button)
        self.image_layout.addLayout(self.switch_layout)

        self.division_window_layout.addLayout(self.image_layout)
        self.window_2.addLayout(self.division_window_layout)
        self.retranslateUi(Window)


    def instruction(self):
        self.messege_box = QtWidgets.QMessageBox()
        self.messege_box.setWindowTitle('Инструкция!!!')
        self.messege_box.setText("Это инструкция по создателю персонажа. Для начала выберете нужные показатели своего героя, еще выберите в каком диапазоне вы бы хотели иметь характеристики, над ними показываеться сколько минимум потратиться очков на создание персонажа, всего распределиться 75 очков, минимум не должен превышать 75 очков. Правее написано количество максимальных очков, желательно чтобы оно было не меньше 75, а то остануться свободные очки. Также можно выбрать сравнение условий характеристик, в этом случае выполниться как минимум одно условие с одинаковыми группами, если же групп нет, то значения будут всегда по условиям. Можно выбрать сколько карточек персонажей будет сгенирировано. Есть кнопка 'Сбросить' чтобы поставить все обратно на стартовые значения. При нажатии кнопки 'Сгенерировать', справа будут сгенерированы карточки персонажей. Кнопками 'Предыдущий'и 'Следующий' можно перелистывать карточки. Есть кнопка 'Сохранить картинку', в этом случае картинка персонажа будет сохранена. Есть кнопки 'Сбросить', 'Убавить', 'Прибавить', они нужны если надо как-то подредактировать персонажа, кнопка 'Прибавить' работает с очками, и если оставшийся очков нет, она не будет работать. Удачи в использовании!!")
        self.messege_box.setStyleSheet("font-size: 16px; color: white; font-family: Arial; font-style: normal; background-color: black; QPushButton {background-color: #E0FFFF; color: white; border-radius: 10px;} QPushButton:hover {background-color: #5A8896;}")
        self.messege_box.exec_()


    def new_points(self):
        minimum = 0
        maximum = 0
        for i in self.list_sliders:
            minimum += i.first_position+1
            maximum += i.second_position+1
        self.min_points.setText(self._translate("Window", "Минимальные очки: "+str(minimum)))
        self.max_points.setText(self._translate("Window", "Максимально очков: "+str(maximum)))
        return (minimum, maximum)


    def generate(self):
        try:
            self.random_class = random.choice([button.text() for button in self.classes_group.buttons() if button.isChecked()])
            self.random_race = random.choice([button.text() for button in self.race_group.buttons() if button.isChecked()])
            self.random_feature = random.choice([button.text() for button in self.feature_group.buttons() if button.isChecked()])
            self.random_spells = random.choice([button.text() for button in self.spells_group.buttons() if button.isChecked()])
            self.random_weapon = random.choice([button.text() for button in self.weapon_group.buttons() if button.isChecked()])
            if self.new_points()[0] > 75:
                self.messege_box = QtWidgets.QMessageBox()
                self.messege_box.setWindowTitle('Предупреждение!!!')
                self.messege_box.setText("Слишком большое количество минимальных очков!")
                self.messege_box.setStyleSheet("font-size: 16px; color: white; font-family: Arial; font-style: normal; background-color: black; QPushButton {background-color: #E0FFFF; color: white; border-radius: 10px;} QPushButton:hover {background-color: #5A8896;}")
                self.messege_box.exec_()
            else:
                self.list_characters = {}
                self.person = 1
                self.text_person.setText(self._translate("Window", "Персонаж " + str(self.person)))
                self.previous_button.setDisabled(True)
                for button in [self.reset_class_button, self.reset_race_button, self.reset_feature_button, self.reset_spells_button, self.reset_weapon_button, self.minus_strength_button, self.plus_strength_button, self.minus_dexterity_button, self.plus_dexterity_button, self.minus_physique_button, self.plus_physique_button, self.minus_intelligence_button, self.plus_intelligence_button, self.minus_wisdom_button, self.plus_wisdom_button, self.minus_charisma_button, self.plus_charisma_button, self.dowload_image_button, self.next_button]:
                    button.setEnabled(True)
                for i in range(self.spinbox_number_characters.value()):
                    self.text_class.setText(self._translate("Window", "Класс:     "+self.random_class))
                    self.text_race.setText(self._translate("Window", "Раса:     "+self.random_race))
                    self.text_feature.setText(self._translate("Window", "Черта:     "+self.random_feature))
                    self.text_spells.setText(self._translate("Window", "Заклинание:     "+self.random_spells))
                    self.text_weapon.setText(self._translate("Window", "Оружие:     "+self.random_weapon))
                    self.points = 75
                    
                    if self.list_strength.currentText() == 'Нет группы сравнения':
                        self.strength = self.spinbox_number_strength_min.value()
                    else:
                        self.strength = 1
                    self.text_strength_2.setText(self._translate("Window", "Сила:"+str(self.strength)))
                    self.points -= self.strength
                    
                    if self.list_dexterity.currentText() == 'Нет группы сравнения':
                        self.dexterity = self.spinbox_number_dexterity_min.value()
                    else:
                        self.dexterity = 1
                    self.text_dexterity_2.setText(self._translate("Window", "Ловкость:"+str(self.dexterity)))
                    self.points -= self.dexterity
                    
                    if self.list_physique.currentText() == 'Нет группы сравнения':
                        self.physique = self.spinbox_number_physique_min.value()
                    else:
                        self.physique = 1
                    self.text_physique_2.setText(self._translate("Window", "Телосложение:"+str(self.physique)))
                    self.points -= self.physique
                    
                    if self.list_intelligence.currentText() == 'Нет группы сравнения':
                        self.intelligence = self.spinbox_number_intelligence_min.value()
                    else:
                        self.intelligence = 1
                    self.text_intelligence_2.setText(self._translate("Window", "Интеллект:"+str(self.intelligence)))
                    self.points -= self.intelligence
                    
                    if self.list_wisdom.currentText() == 'Нет группы сравнения':
                        self.wisdom = self.spinbox_number_wisdom_min.value()
                    else:
                        self.wisdom = 1
                    self.text_wisdom_2.setText(self._translate("Window", "Мудрость:"+str(self.wisdom)))
                    self.points -= self.wisdom
                    
                    if self.list_charisma.currentText() == 'Нет группы сравнения':
                        self.charisma = self.spinbox_number_charisma_min.value()
                    else:
                        self.charisma = 1
                    self.text_charisma_2.setText(self._translate("Window", "Харизма:"+str(self.charisma)))
                    self.points -= self.charisma
                    
                    self.text_points.setText(self._translate("Window", "Осталось очков: "+str(self.points)))
                    self.list_characters['Персонаж '+str(i+1)] = {
                    "Класс" : self.random_class, 
                    "Раса" : self.random_race,
                    "Черта" : self.random_feature,
                    "Заклинание" : self.random_spells,
                    "Оружие" : self.random_weapon,
                    "Сила" : self.strength,
                    "Ловкость" : self.dexterity,
                    "Телосложение" : self.physique,
                    "Интеллект" : self.intelligence,
                    "Мудрость" : self.wisdom,
                    "Харизма" : self.charisma,
                    "Очков" : self.points,
                    "Изображение расы" : str(Path('/'.join(self.data["Расы"][self.random_race]))),
                    "Изображение оружия" : str(Path('/'.join(self.data["Оружия"][self.random_weapon]))),
                    "Изображение заклинания" : str(Path('/'.join(self.data["Заклинания"][self.random_spells]))),
                    }
                    self.image_race.setPixmap(QtGui.QPixmap(self.list_characters["Персонаж "+str(self.person)]["Изображение расы"]))
                    self.image_weapon.setPixmap(QtGui.QPixmap(self.list_characters["Персонаж "+str(self.person)]["Изображение оружия"]))
                    self.image_spells.setPixmap(QtGui.QPixmap(self.list_characters["Персонаж "+str(self.person)]["Изображение заклинания"]))
                    self.random_class = random.choice([button.text() for button in self.classes_group.buttons() if button.isChecked()])
                    self.random_race = random.choice([button.text() for button in self.race_group.buttons() if button.isChecked()])
                    self.random_feature = random.choice([button.text() for button in self.feature_group.buttons() if button.isChecked()])
                    self.random_spells = random.choice([button.text() for button in self.spells_group.buttons() if button.isChecked()])
                    self.random_weapon = random.choice([button.text() for button in self.weapon_group.buttons() if button.isChecked()])
        except:
            self.messege_box = QtWidgets.QMessageBox()
            self.messege_box.setWindowTitle('Предупреждение!!!')
            self.messege_box.setText("Установите хотя бы один флажок!")
            self.messege_box.setStyleSheet("font-size: 16px; color: white; font-family: Arial; font-style: normal; background-color: black; QPushButton {background-color: #E0FFFF; color: white; border-radius: 10px;} QPushButton:hover {background-color: #5A8896;}")
            self.messege_box.exec_()


    def reset(self):
        for group in [self.classes_group.buttons(), self.race_group.buttons(), self.feature_group.buttons(), self.spells_group.buttons(), self.weapon_group.buttons()]:
            for button in group:
                button.setChecked(True)
        for i in [self.list_strength, self.list_dexterity, self.list_physique, self.list_intelligence, self.list_wisdom, self.list_charisma]:
            i.setCurrentIndex(0)
        for i in self.list_sliders:
            i.reset(1, 15)
        self.new_points()
        self.spinbox_number_characters.setValue(5)
    

    def reset_characters(self, group, text_field, name):
        self.i = random.choice([button.text() for button in group.buttons() if button.isChecked()])
        while self.i == self.list_characters["Персонаж "+str(self.person)][name]:
            self.i = random.choice([button.text() for button in group.buttons() if button.isChecked()])
        text_field.setText(self._translate("Window", name+":     "+self.i))
        self.list_characters["Персонаж "+str(self.person)][name] = self.i


    def minus_and_plus(self, button_minus, button_plus, number, text_field, name):
        if number > 0:
            if self.list_characters["Персонаж "+str(self.person)][name] < 15 and self.list_characters["Персонаж "+str(self.person)]["Очков"] >= number:
                text_field.setText(self._translate("Window", name+": "+str(self.list_characters["Персонаж "+str(self.person)][name]+number)))
                self.list_characters["Персонаж "+str(self.person)]["Очков"] -= number
                self.list_characters["Персонаж "+str(self.person)][name] += number
                self.text_points.setText(self._translate("Window", "Осталось очков: "+str(self.list_characters["Персонаж "+str(self.person)]["Очков"])))
        elif self.list_characters["Персонаж "+str(self.person)][name] > 1:
            text_field.setText(self._translate("Window", name+": "+str(self.list_characters["Персонаж "+str(self.person)][name]+number)))
            self.list_characters["Персонаж "+str(self.person)]["Очков"] -= number
            self.list_characters["Персонаж "+str(self.person)][name] += number
            self.text_points.setText(self._translate("Window", "Осталось очков: "+str(self.list_characters["Персонаж "+str(self.person)]["Очков"])))


    def forth(self):
        self.person += 1
        self.previous_button.setEnabled(True)
        self.text_class.setText(self._translate("Window", "Класс:     "+self.list_characters["Персонаж "+str(self.person)]["Класс"]))
        self.text_race.setText(self._translate("Window", "Раса:     "+self.list_characters["Персонаж "+str(self.person)]["Раса"]))
        self.text_feature.setText(self._translate("Window", "Черта:     "+self.list_characters["Персонаж "+str(self.person)]["Черта"]))
        self.text_spells.setText(self._translate("Window", "Заклинание:     "+self.list_characters["Персонаж "+str(self.person)]["Заклинание"]))
        self.text_weapon.setText(self._translate("Window", "Оружие:     "+self.list_characters["Персонаж "+str(self.person)]["Оружие"]))
        self.text_strength_2.setText(self._translate("Window", "Сила: "+str(self.list_characters["Персонаж "+str(self.person)]["Сила"])))
        self.text_dexterity_2.setText(self._translate("Window", "Ловкость:"+str(self.list_characters["Персонаж "+str(self.person)]["Ловкость"])))
        self.text_physique_2.setText(self._translate("Window", "Телосложение:"+str(self.list_characters["Персонаж "+str(self.person)]["Телосложение"])))
        self.text_intelligence_2.setText(self._translate("Window", "Интеллект:"+str(self.list_characters["Персонаж "+str(self.person)]["Интеллект"])))
        self.text_wisdom_2.setText(self._translate("Window", "Мудрость:"+str(self.list_characters["Персонаж "+str(self.person)]["Мудрость"])))
        self.text_charisma_2.setText(self._translate("Window", "Харизма:" +str(self.list_characters["Персонаж "+str(self.person)]["Харизма"])))
        self.text_points.setText(self._translate("Window", "Осталось очков: " +str(self.list_characters["Персонаж "+str(self.person)]["Очков"])))
        self.text_person.setText(self._translate("Window", "Персонаж " + str(self.person)))
        self.image_race.setPixmap(QtGui.QPixmap(self.list_characters["Персонаж "+str(self.person)]["Изображение расы"]))
        self.image_weapon.setPixmap(QtGui.QPixmap(self.list_characters["Персонаж "+str(self.person)]["Изображение оружия"]))
        self.image_spells.setPixmap(QtGui.QPixmap(self.list_characters["Персонаж "+str(self.person)]["Изображение заклинания"]))
        if len(self.list_characters) <= self.person:
            self.next_button.setDisabled(True)


    def back(self):
        self.person -= 1
        self.next_button.setEnabled(True)
        self.text_class.setText(self._translate("Window", "Класс:     "+self.list_characters["Персонаж "+str(self.person)]["Класс"]))
        self.text_race.setText(self._translate("Window", "Раса:     "+self.list_characters["Персонаж "+str(self.person)]["Раса"]))
        self.text_feature.setText(self._translate("Window", "Черта:     "+self.list_characters["Персонаж "+str(self.person)]["Черта"]))
        self.text_spells.setText(self._translate("Window", "Заклинание:     "+self.list_characters["Персонаж "+str(self.person)]["Заклинание"]))
        self.text_weapon.setText(self._translate("Window", "Оружие:     "+self.list_characters["Персонаж "+str(self.person)]["Оружие"]))
        self.text_strength_2.setText(self._translate("Window", "Сила: "+str(self.list_characters["Персонаж "+str(self.person)]["Сила"])))
        self.text_dexterity_2.setText(self._translate("Window", "Ловкость:"+str(self.list_characters["Персонаж "+str(self.person)]["Ловкость"])))
        self.text_physique_2.setText(self._translate("Window", "Телосложение:"+str(self.list_characters["Персонаж "+str(self.person)]["Телосложение"])))
        self.text_intelligence_2.setText(self._translate("Window", "Интеллект:"+str(self.list_characters["Персонаж "+str(self.person)]["Интеллект"])))
        self.text_wisdom_2.setText(self._translate("Window", "Мудрость:"+str(self.list_characters["Персонаж "+str(self.person)]["Мудрость"])))
        self.text_charisma_2.setText(self._translate("Window", "Харизма:" +str(self.list_characters["Персонаж "+str(self.person)]["Харизма"])))
        self.text_points.setText(self._translate("Window", "Осталось очков: " +str(self.list_characters["Персонаж "+str(self.person)]["Очков"])))
        self.text_person.setText(self._translate("Window", "Персонаж " + str(self.person)))
        self.image_race.setPixmap(QtGui.QPixmap(self.list_characters["Персонаж "+str(self.person)]["Изображение расы"]))
        self.image_weapon.setPixmap(QtGui.QPixmap(self.list_characters["Персонаж "+str(self.person)]["Изображение оружия"]))
        self.image_spells.setPixmap(QtGui.QPixmap(self.list_characters["Персонаж "+str(self.person)]["Изображение заклинания"]))
        if self.person <= 1:
            self.previous_button.setDisabled(True)


    def retranslateUi(self, Window):
        Window.setWindowTitle(self._translate("Window", "Создатель Героя"))
        self.classes_box.setTitle(self._translate("Window", "Классы"))
        self.race_box.setTitle(self._translate("Window", "Расы"))
        self.feature_box.setTitle(self._translate("Window", "Черты"))
        self.spells_box.setTitle(self._translate("Window", "Заклинания"))
        self.weapon_box.setTitle(self._translate("Window", "Оружие"))
        self.instructions.setText(self._translate("Window", "Инструкция!"))
        self.new_points()
        self.text_strength.setText(self._translate("Window", "Сила:"))
        self.text_dexterity.setText(self._translate("Window", "Ловкость:"))
        self.text_physique.setText(self._translate("Window", "Телосложение:"))
        self.text_intelligence.setText(self._translate("Window", "Интеллект:"))
        self.text_wisdom.setText(self._translate("Window", "Мудрость:"))
        self.text_charisma.setText(self._translate("Window", "Харизма:"))
        self.text_number_characters.setText(self._translate("Window", "Количество персонажей:"))
        self.generate_button.setText(self._translate("Window", "Сгенерировать"))
        self.reset_button.setText(self._translate("Window", "Сбросить"))
        self.text_person.setText(self._translate("Window", "Персонаж"))
        self.text_class.setText(self._translate("Window", "Класс:"))
        self.text_race.setText(self._translate("Window", "Раса:"))
        self.text_feature.setText(self._translate("Window", "Черта"))
        self.text_spells.setText(self._translate("Window", "Заклинание:"))
        self.text_weapon.setText(self._translate("Window", "Оружие:"))
        self.text_strength_2.setText(self._translate("Window", "Сила:"))
        self.text_dexterity_2.setText(self._translate("Window", "Ловкость:"))
        self.text_physique_2.setText(self._translate("Window", "Телосложение:"))
        self.text_intelligence_2.setText(self._translate("Window", "Интеллект:"))
        self.text_wisdom_2.setText(self._translate("Window", "Мудрость:"))
        self.text_charisma_2.setText(self._translate("Window", "Харизма:"))
        self.text_points.setText(self._translate("Window", "Осталось очков:"))
        self.dowload_image_button.setText(self._translate("Window", "Сохранить картинку"))
        self.previous_button.setText(self._translate("Window", "предыдущий"))
        self.next_button.setText(self._translate("Window", "Следующий"))


def main():
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    okno = Okno()
    okno.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()