import os, sys
from kivy.resources import resource_add_path, resource_find
import math
import pandas as pd
import requests
import json
from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog

screen_menu = """
ScreenManager:
    id: screen_manager
    Start:
    Choice:
    Manual_1:
    Manual_2:
    Manual_3:
    Manual_4:
    Manual_5:
    Manual_6:
    Manual_7:
    Manual_8:
    Manual_9:
    Manual_10:    
    Manual_end_1:
    Manual_end_2:
    Manual_end_3:
    Manual_end_4:
    Manual_end_5:
    Manual_end_6:
    Manual_end_7:
    Manual_end_8:
    Manual_end_9:
    Manual_end_10:
    Manual_reb_1:
    Manual_reb_2:
    Auto:
    Auto_end_1:
    Auto_end_2:
    Auto_end_3:
    Auto_end_4:
    Auto_end_5:
    Auto_end_6:
    Auto_end_7:
    Auto_end_8:
    Auto_end_9:
    Auto_end_10:
    Auto_reb_1:
    Auto_reb_2:
<Start>:
    name: 'start'
    MDTopAppBar:
        title: 'TradeBot v2.0'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Начать формирование портфеля'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        on_release: 
            root.manager.transition.direction = 'down'
            root.manager.current = 'choice'
    MDRectangleFlatButton:
        text: 'Выйти'
        pos_hint: {'center_x':0.5,'center_y':0.7}
        on_release: app.stop()
<Choice>:
    name: 'choice'
    MDTopAppBar:
        title: 'Как будем формировать портфель?'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Ввести данные вручню'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'manual_1'
    MDRectangleFlatButton:
        text: 'Внести данные автоматически'
        pos_hint: {'center_x':0.5,'center_y':0.7}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'auto'
    MDRectangleFlatButton:
        text: 'Вернуться в главное меню'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_release: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'start'
<Manual_1>:
    name: 'manual_1'
    MDTopAppBar:
        title: 'Акция 1: введите количество активов акции и её стоимость в различные дни'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDTextField:
        id: field_num
        hint_text: "Количество акций"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.8}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_1
        hint_text: "День 1"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_2
        hint_text: "День 2"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_3
        hint_text: "День 3"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_4
        hint_text: "День 4"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.4}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_5
        hint_text: "День 5"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.3}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_6
        hint_text: "День 6"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_7
        hint_text: "День 7"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_8
        hint_text: "День 8"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_9
        hint_text: "День 9"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.4}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_10
        hint_text: "День 10"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.3}
        size_hint_x:None
        width:300
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release:
            root.manager.screens[2].input()
            root.manager.transition.direction = 'left'
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release:
            root.manager.screens[2].clear()
            root.manager.transition.direction = 'right'
            root.manager.current = 'choice'
<Manual_2>:
    name: 'manual_2'
    MDTopAppBar:
        title: 'Акция 2: введите количество активов акции и её стоимость в различные дни'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDTextField:
        id: field_num
        hint_text: "Количество акций"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.8}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_1
        hint_text: "День 1"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_2
        hint_text: "День 2"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_3
        hint_text: "День 3"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_4
        hint_text: "День 4"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.4}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_5
        hint_text: "День 5"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.3}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_6
        hint_text: "День 6"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_7
        hint_text: "День 7"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_8
        hint_text: "День 8"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_9
        hint_text: "День 9"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.4}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_10
        hint_text: "День 10"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.3}
        size_hint_x:None
        width:300
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release:
            root.manager.screens[3].input()
            root.manager.transition.direction = 'left'
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release:
            root.manager.screens[3].clear()
            root.manager.transition.direction = 'right'
            root.manager.current = 'manual_1'
<Manual_3>:
    name: 'manual_3'
    MDTopAppBar:
        title: 'Акция 3: введите количество активов акции и её стоимость в различные дни'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDTextField:
        id: field_num
        hint_text: "Количество акций"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.8}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_1
        hint_text: "День 1"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_2
        hint_text: "День 2"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_3
        hint_text: "День 3"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_4
        hint_text: "День 4"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.4}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_5
        hint_text: "День 5"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.3}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_6
        hint_text: "День 6"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_7
        hint_text: "День 7"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_8
        hint_text: "День 8"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_9
        hint_text: "День 9"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.4}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_10
        hint_text: "День 10"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.3}
        size_hint_x:None
        width:300
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release:
            root.manager.screens[4].input()
            root.manager.transition.direction = 'left'
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release:
            root.manager.screens[4].clear()
            root.manager.transition.direction = 'right'
            root.manager.current = 'manual_2'
<Manual_4>:
    name: 'manual_4'
    MDTopAppBar:
        title: 'Акция 4: введите количество активов акции и её стоимость в различные дни'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDTextField:
        id: field_num
        hint_text: "Количество акций"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.8}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_1
        hint_text: "День 1"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_2
        hint_text: "День 2"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_3
        hint_text: "День 3"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_4
        hint_text: "День 4"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.4}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_5
        hint_text: "День 5"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.3}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_6
        hint_text: "День 6"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_7
        hint_text: "День 7"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_8
        hint_text: "День 8"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_9
        hint_text: "День 9"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.4}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_10
        hint_text: "День 10"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.3}
        size_hint_x:None
        width:300
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release:
            root.manager.screens[5].input()
            root.manager.transition.direction = 'left'
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release:
            root.manager.screens[5].clear()
            root.manager.transition.direction = 'right'
            root.manager.current = 'manual_3'
<Manual_5>:
    name: 'manual_5'
    MDTopAppBar:
        title: 'Акция 5: введите количество активов акции и её стоимость в различные дни'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDTextField:
        id: field_num
        hint_text: "Количество акций"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.8}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_1
        hint_text: "День 1"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_2
        hint_text: "День 2"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_3
        hint_text: "День 3"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_4
        hint_text: "День 4"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.4}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_5
        hint_text: "День 5"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.3}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_6
        hint_text: "День 6"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_7
        hint_text: "День 7"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_8
        hint_text: "День 8"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_9
        hint_text: "День 9"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.4}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_10
        hint_text: "День 10"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.3}
        size_hint_x:None
        width:300
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release:
            root.manager.screens[6].input()
            root.manager.transition.direction = 'left'
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release:
            root.manager.screens[6].clear()
            root.manager.transition.direction = 'right'
            root.manager.current = 'manual_4'
<Manual_6>:
    name: 'manual_6'
    MDTopAppBar:
        title: 'Акция 6: введите количество активов акции и её стоимость в различные дни'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDTextField:
        id: field_num
        hint_text: "Количество акций"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.8}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_1
        hint_text: "День 1"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_2
        hint_text: "День 2"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_3
        hint_text: "День 3"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_4
        hint_text: "День 4"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.4}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_5
        hint_text: "День 5"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.3}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_6
        hint_text: "День 6"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_7
        hint_text: "День 7"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_8
        hint_text: "День 8"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_9
        hint_text: "День 9"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.4}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_10
        hint_text: "День 10"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.3}
        size_hint_x:None
        width:300
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release:
            root.manager.screens[7].input()
            root.manager.transition.direction = 'left'
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release:
            root.manager.screens[7].clear()
            root.manager.transition.direction = 'right'
            root.manager.current = 'manual_5'
<Manual_7>:
    name: 'manual_7'
    MDTopAppBar:
        title: 'Акция 7: введите количество активов акции и её стоимость в различные дни'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDTextField:
        id: field_num
        hint_text: "Количество акций"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.8}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_1
        hint_text: "День 1"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_2
        hint_text: "День 2"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_3
        hint_text: "День 3"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_4
        hint_text: "День 4"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.4}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_5
        hint_text: "День 5"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.3}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_6
        hint_text: "День 6"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_7
        hint_text: "День 7"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_8
        hint_text: "День 8"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_9
        hint_text: "День 9"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.4}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_10
        hint_text: "День 10"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.3}
        size_hint_x:None
        width:300
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release:
            root.manager.screens[8].input()
            root.manager.transition.direction = 'left'
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release:
            root.manager.screens[8].clear()
            root.manager.transition.direction = 'right'
            root.manager.current = 'manual_6'
<Manual_8>:
    name: 'manual_8'
    MDTopAppBar:
        title: 'Акция 8: введите количество активов акции и её стоимость в различные дни'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDTextField:
        id: field_num
        hint_text: "Количество акций"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.8}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_1
        hint_text: "День 1"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_2
        hint_text: "День 2"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_3
        hint_text: "День 3"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_4
        hint_text: "День 4"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.4}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_5
        hint_text: "День 5"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.3}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_6
        hint_text: "День 6"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_7
        hint_text: "День 7"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_8
        hint_text: "День 8"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_9
        hint_text: "День 9"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.4}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_10
        hint_text: "День 10"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.3}
        size_hint_x:None
        width:300
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release:
            root.manager.screens[9].input()
            root.manager.transition.direction = 'left'
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release:
            root.manager.screens[9].clear()
            root.manager.transition.direction = 'right'
            root.manager.current = 'manual_7'
<Manual_9>:
    name: 'manual_9'
    MDTopAppBar:
        title: 'Акция 9: введите количество активов акции и её стоимость в различные дни'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDTextField:
        id: field_num
        hint_text: "Количество акций"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.8}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_1
        hint_text: "День 1"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_2
        hint_text: "День 2"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_3
        hint_text: "День 3"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_4
        hint_text: "День 4"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.4}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_5
        hint_text: "День 5"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.3}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_6
        hint_text: "День 6"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_7
        hint_text: "День 7"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_8
        hint_text: "День 8"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_9
        hint_text: "День 9"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.4}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_10
        hint_text: "День 10"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.3}
        size_hint_x:None
        width:300
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release:
            root.manager.screens[10].input()
            root.manager.transition.direction = 'left'
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release:
            root.manager.screens[10].clear()
            root.manager.transition.direction = 'right'
            root.manager.current = 'manual_8'
<Manual_10>:
    name: 'manual_10'
    MDTopAppBar:
        title: 'Акция 10: введите количество активов акции и её стоимость в различные дни'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDTextField:
        id: field_num
        hint_text: "Количество акций"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.8}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_1
        hint_text: "День 1"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_2
        hint_text: "День 2"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_3
        hint_text: "День 3"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_4
        hint_text: "День 4"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.4}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_5
        hint_text: "День 5"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.3}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_6
        hint_text: "День 6"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_7
        hint_text: "День 7"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_8
        hint_text: "День 8"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_9
        hint_text: "День 9"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.4}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_10
        hint_text: "День 10"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.3}
        size_hint_x:None
        width:300
    MDRectangleFlatButton:
        text: 'Готово'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release:
            root.manager.screens[11].input()
            root.manager.transition.direction = 'left'
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release:
            root.manager.screens[11].clear()
            root.manager.transition.direction = 'right'
            root.manager.current = 'manual_9'
<Manual_end_1>:
    name: 'manual_end_1'
    MDTopAppBar:
        title: 'Информация об акции 1'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'manual_end_2'
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_release: 
            root.manager.screens[12].load_manual_end_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'choice'
<Manual_end_2>:
    name: 'manual_end_2'
    MDTopAppBar:
        title: 'Информация об акции 2'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'manual_end_3'
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_release: 
            root.manager.screens[13].load_manual_end_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'manual_end_1'
<Manual_end_3>:
    name: 'manual_end_3'
    MDTopAppBar:
        title: 'Информация об акции 3'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'manual_end_4'
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_release: 
            root.manager.screens[14].load_manual_end_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'manual_end_2'
<Manual_end_4>:
    name: 'manual_end_4'
    MDTopAppBar:
        title: 'Информация об акции 4'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'manual_end_5'
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_release: 
            root.manager.screens[15].load_manual_end_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'manual_end_3'
<Manual_end_5>:
    name: 'manual_end_5'
    MDTopAppBar:
        title: 'Информация об акции 5'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'manual_end_6'
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_release: 
            root.manager.screens[16].load_manual_end_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'manual_end_4'
<Manual_end_6>:
    name: 'manual_end_6'
    MDTopAppBar:
        title: 'Информация об акции 6'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'manual_end_7'
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_release: 
            root.manager.screens[17].load_manual_end_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'manual_end_5'
<Manual_end_7>:
    name: 'manual_end_7'
    MDTopAppBar:
        title: 'Информация об акции 7'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'manual_end_8'
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_release: 
            root.manager.screens[18].load_manual_end_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'manual_end_6'
<Manual_end_8>:
    name: 'manual_end_8'
    MDTopAppBar:
        title: 'Информация об акции 8'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'manual_end_9'
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_release: 
            root.manager.screens[19].load_manual_end_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'manual_end_7'
<Manual_end_9>:
    name: 'manual_end_9'
    MDTopAppBar:
        title: 'Информация об акции 9'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'manual_end_10'
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_release: 
            root.manager.screens[20].load_manual_end_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'manual_end_8'
<Manual_end_10>:
    name: 'manual_end_10'
    MDTopAppBar:
        title: 'Информация об акции 10'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'manual_reb_1'
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_release: 
            root.manager.screens[21].load_manual_end_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'manual_end_9'
<Manual_reb_1>:
    name: 'manual_reb_1'
    MDTopAppBar:
        title: 'Ваш портфель готов!'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'manual_reb_2'
    MDRectangleFlatButton:
        text: 'Меню'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'manual_end_10'
<Manual_reb_2>:
    name: 'manual_reb_2'
    MDTopAppBar:
        title: 'Ребалансированный портфель'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_release: 
            root.manager.screens[23].load_manual_reb_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'manual_reb_1'
    MDRectangleFlatButton:
        text: 'Выйти'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.screens[23].leave()
<Auto>:
    name: 'auto'
    MDTopAppBar:
        title: 'Введите количество активов для каждой акции'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDTextField:
        id: field_1
        hint_text: "Акция 1"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.8}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_2
        hint_text: "Акция 2"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_3
        hint_text: "Акция 3"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_4
        hint_text: "Акция 4"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_5
        hint_text: "Акция 5"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.4}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_6
        hint_text: "Акция 6"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.8}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_7
        hint_text: "Акция 7"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_8
        hint_text: "Акция 8"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_9
        hint_text: "Акция 9"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_10
        hint_text: "Акция 10"
        helper_text: "в рублях"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.4}
        size_hint_x:None
        width:300
    MDRectangleFlatButton:
        text: 'Готово'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release:
            root.manager.screens[24].input()
            root.manager.transition.direction = 'right'
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release:
            root.manager.screens[24].clear()
            root.manager.transition.direction = 'left'
            root.manager.current = 'choice'
<Auto_end_1>:
    name: 'auto_end_1'
    MDTopAppBar:
        title: 'Информация об акции 1'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'auto_end_2'
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_release: 
            root.manager.screens[25].load_auto_end_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'choice'
<Auto_end_2>:
    name: 'auto_end_2'
    MDTopAppBar:
        title: 'Информация об акции 2'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'auto_end_3'
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_release: 
            root.manager.screens[26].load_auto_end_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'auto_end_1'
<Auto_end_3>:
    name: 'auto_end_3'
    MDTopAppBar:
        title: 'Информация об акции 3'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'auto_end_4'
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_release: 
            root.manager.screens[27].load_auto_end_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'auto_end_2'
<Auto_end_4>:
    name: 'auto_end_4'
    MDTopAppBar:
        title: 'Информация об акции 4'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'auto_end_5'
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_release: 
            root.manager.screens[28].load_auto_end_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'auto_end_3'
<Auto_end_5>:
    name: 'auto_end_5'
    MDTopAppBar:
        title: 'Информация об акции 5'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'auto_end_6'
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_release: 
            root.manager.screens[29].load_auto_end_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'auto_end_4'
<Auto_end_6>:
    name: 'auto_end_6'
    MDTopAppBar:
        title: 'Информация об акции 6'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'auto_end_7'
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_release: 
            root.manager.screens[30].load_auto_end_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'auto_end_5'
<Auto_end_7>:
    name: 'auto_end_7'
    MDTopAppBar:
        title: 'Информация об акции 7'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'auto_end_8'
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_release: 
            root.manager.screens[31].load_auto_end_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'auto_end_6'
<Auto_end_8>:
    name: 'auto_end_8'
    MDTopAppBar:
        title: 'Информация об акции 8'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'auto_end_9'
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_release: 
            root.manager.screens[32].load_auto_end_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'auto_end_7'
<Auto_end_9>:
    name: 'auto_end_9'
    MDTopAppBar:
        title: 'Информация об акции 9'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'auto_end_10'
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_release: 
            root.manager.screens[33].load_auto_end_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'auto_end_8'
<Auto_end_10>:
    name: 'auto_end_10'
    MDTopAppBar:
        title: 'Информация об акции 10'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'auto_reb_1'
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_release: 
            root.manager.screens[34].load_auto_end_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'auto_end_9'
<Auto_reb_1>:
    name: 'auto_reb_1'
    MDTopAppBar:
        title: 'Ваш портфель готов!'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Далее'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'auto_reb_2'
    MDRectangleFlatButton:
        text: 'Меню'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'auto_end_10'
<Auto_reb_2>:
    name: 'auto_reb_2'
    MDTopAppBar:
        title: 'Ребалансированный портфель'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_release: 
            root.manager.screens[36].load_manual_reb_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'auto_reb_1'
    MDRectangleFlatButton:
        text: 'Выйти'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.screens[36].leave()
"""

class Start(Screen):
    pass

class Choice(Screen):
    pass

class Manual_1(Screen):
    num = []
    days = []
    stocks_prices = []
    divs_dif = []
    prices_dif = []
    dif = []
    divs_dif_2 = []
    prices_dif_2 = []
    reb = []
    reb_stocks_prices = []
    def input(self):
        if ((self.ids.field_1.text != '') and (self.ids.field_2.text != '') and (self.ids.field_3.text != '') and (self.ids.field_4.text != '') and (self.ids.field_5.text != '') and (self.ids.field_6.text != '') and (self.ids.field_7.text != '') and (self.ids.field_8.text != '') and (self.ids.field_9.text != '') and (self.ids.field_10.text != '') and (self.ids.field_num.text != '')):
            i = int(0)
            for i in range(10):
                self.days.append(float(i + 1))
            self.stocks_prices.append(float(self.ids.field_1.text))
            self.stocks_prices.append(float(self.ids.field_2.text))
            self.stocks_prices.append(float(self.ids.field_3.text))
            self.stocks_prices.append(float(self.ids.field_4.text))
            self.stocks_prices.append(float(self.ids.field_5.text))
            self.stocks_prices.append(float(self.ids.field_6.text))
            self.stocks_prices.append(float(self.ids.field_7.text))
            self.stocks_prices.append(float(self.ids.field_8.text))
            self.stocks_prices.append(float(self.ids.field_9.text))
            self.stocks_prices.append(float(self.ids.field_10.text))
            self.num.append(float(self.ids.field_num.text))
            average_day = float(0.0)
            average_stocks_price = float(0.0)
            for i in range(10):
                average_day = average_day + self.days[i]
                average_stocks_price = average_stocks_price + self.stocks_prices[i]
            average_stocks_price = average_stocks_price / 10
            average_day = average_day / 10
            i = 0
            for i in range(10):
                self.divs_dif.append(float(self.days[i] - average_day))
                self.prices_dif.append(float(self.stocks_prices[i] - average_stocks_price))
                self.dif.append(float(self.divs_dif[i] * self.prices_dif[i]))
                self.divs_dif_2.append(float(self.divs_dif[i] * self.divs_dif[i]))
                self.prices_dif_2.append(float(self.prices_dif[i] * self.prices_dif[i]))
            max_price = 0
            for i in range(10):
                self.reb.append(0)
                if (self.stocks_prices[i] > max_price):
                    max_price = self.stocks_prices[i]
            i = 0
            for i in range(10):
                self.reb_stocks_prices.append(self.stocks_prices[i])
                while (self.reb_stocks_prices[i] < max_price):
                    self.reb_stocks_prices[i] = self.reb_stocks_prices[i] + self.stocks_prices[i]
                    self.reb[i] = self.reb[i] + 1
            self.manager.current = 'manual_2'
        else:
            self.dialog = MDDialog(title="Ошибка",
                               text="Данные введены некорректно или отсутствуют",
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
            self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()
    def clear(self, *args):
        self.num = []
        self.days = []
        self.stocks_prices = []
        self.divs_dif = []
        self.prices_dif = []
        self.dif = []
        self.divs_dif_2 = []
        self.prices_dif_2 = []
        self.reb = []
        self.reb_stocks_prices = []

class Manual_2(Screen):
    num = []
    days = []
    stocks_prices = []
    divs_dif = []
    prices_dif = []
    dif = []
    divs_dif_2 = []
    prices_dif_2 = []
    reb = []
    reb_stocks_prices = []
    def input(self):
        if ((self.ids.field_1.text != '') and (self.ids.field_2.text != '') and (self.ids.field_3.text != '') and (self.ids.field_4.text != '') and (self.ids.field_5.text != '') and (self.ids.field_6.text != '') and (self.ids.field_7.text != '') and (self.ids.field_8.text != '') and (self.ids.field_9.text != '') and (self.ids.field_10.text != '') and (self.ids.field_num.text != '')):
            i = int(0)
            for i in range(10):
                self.days.append(float(i + 1))
            self.stocks_prices.append(float(self.ids.field_1.text))
            self.stocks_prices.append(float(self.ids.field_2.text))
            self.stocks_prices.append(float(self.ids.field_3.text))
            self.stocks_prices.append(float(self.ids.field_4.text))
            self.stocks_prices.append(float(self.ids.field_5.text))
            self.stocks_prices.append(float(self.ids.field_6.text))
            self.stocks_prices.append(float(self.ids.field_7.text))
            self.stocks_prices.append(float(self.ids.field_8.text))
            self.stocks_prices.append(float(self.ids.field_9.text))
            self.stocks_prices.append(float(self.ids.field_10.text))
            self.num.append(float(self.ids.field_num.text))
            average_day = float(0.0)
            average_stocks_price = float(0.0)
            for i in range(10):
                average_day = average_day + self.days[i]
                average_stocks_price = average_stocks_price + self.stocks_prices[i]
            average_stocks_price = average_stocks_price / 10
            average_day = average_day / 10
            i = 0
            for i in range(10):
                self.divs_dif.append(float(self.days[i] - average_day))
                self.prices_dif.append(float(self.stocks_prices[i] - average_stocks_price))
                self.dif.append(float(self.divs_dif[i] * self.prices_dif[i]))
                self.divs_dif_2.append(float(self.divs_dif[i] * self.divs_dif[i]))
                self.prices_dif_2.append(float(self.prices_dif[i] * self.prices_dif[i]))
            max_price = 0
            for i in range(10):
                self.reb.append(0)
                if (self.stocks_prices[i] > max_price):
                    max_price = self.stocks_prices[i]
            i = 0
            for i in range(10):
                self.reb_stocks_prices.append(self.stocks_prices[i])
                while (self.reb_stocks_prices[i] < max_price):
                    self.reb_stocks_prices[i] = self.reb_stocks_prices[i] + self.stocks_prices[i]
                    self.reb[i] = self.reb[i] + 1
            self.manager.current = 'manual_3'
        else:
            self.dialog = MDDialog(title="Ошибка",
                               text="Данные введены некорректно или отсутствуют",
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
            self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()
    def clear(self, *args):
        self.num = []
        self.days = []
        self.stocks_prices = []
        self.divs_dif = []
        self.prices_dif = []
        self.dif = []
        self.divs_dif_2 = []
        self.prices_dif_2 = []
        self.reb = []
        self.reb_stocks_prices = []

class Manual_3(Screen):
    num = []
    days = []
    stocks_prices = []
    divs_dif = []
    prices_dif = []
    dif = []
    divs_dif_2 = []
    prices_dif_2 = []
    reb = []
    reb_stocks_prices = []
    def input(self):
        if ((self.ids.field_1.text != '') and (self.ids.field_2.text != '') and (self.ids.field_3.text != '') and (self.ids.field_4.text != '') and (self.ids.field_5.text != '') and (self.ids.field_6.text != '') and (self.ids.field_7.text != '') and (self.ids.field_8.text != '') and (self.ids.field_9.text != '') and (self.ids.field_10.text != '') and (self.ids.field_num.text != '')):
            i = int(0)
            for i in range(10):
                self.days.append(float(i + 1))
            self.stocks_prices.append(float(self.ids.field_1.text))
            self.stocks_prices.append(float(self.ids.field_2.text))
            self.stocks_prices.append(float(self.ids.field_3.text))
            self.stocks_prices.append(float(self.ids.field_4.text))
            self.stocks_prices.append(float(self.ids.field_5.text))
            self.stocks_prices.append(float(self.ids.field_6.text))
            self.stocks_prices.append(float(self.ids.field_7.text))
            self.stocks_prices.append(float(self.ids.field_8.text))
            self.stocks_prices.append(float(self.ids.field_9.text))
            self.stocks_prices.append(float(self.ids.field_10.text))
            self.num.append(float(self.ids.field_num.text))
            average_day = float(0.0)
            average_stocks_price = float(0.0)
            for i in range(10):
                average_day = average_day + self.days[i]
                average_stocks_price = average_stocks_price + self.stocks_prices[i]
            average_stocks_price = average_stocks_price / 10
            average_day = average_day / 10
            i = 0
            for i in range(10):
                self.divs_dif.append(float(self.days[i] - average_day))
                self.prices_dif.append(float(self.stocks_prices[i] - average_stocks_price))
                self.dif.append(float(self.divs_dif[i] * self.prices_dif[i]))
                self.divs_dif_2.append(float(self.divs_dif[i] * self.divs_dif[i]))
                self.prices_dif_2.append(float(self.prices_dif[i] * self.prices_dif[i]))
            max_price = 0
            for i in range(10):
                self.reb.append(0)
                if (self.stocks_prices[i] > max_price):
                    max_price = self.stocks_prices[i]
            i = 0
            for i in range(10):
                self.reb_stocks_prices.append(self.stocks_prices[i])
                while (self.reb_stocks_prices[i] < max_price):
                    self.reb_stocks_prices[i] = self.reb_stocks_prices[i] + self.stocks_prices[i]
                    self.reb[i] = self.reb[i] + 1
            self.manager.current = 'manual_4'
        else:
            self.dialog = MDDialog(title="Ошибка",
                               text="Данные введены некорректно или отсутствуют",
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
            self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()
    def clear(self, *args):
        self.num = []
        self.days = []
        self.stocks_prices = []
        self.divs_dif = []
        self.prices_dif = []
        self.dif = []
        self.divs_dif_2 = []
        self.prices_dif_2 = []
        self.reb = []
        self.reb_stocks_prices = []

class Manual_4(Screen):
    num = []
    days = []
    stocks_prices = []
    divs_dif = []
    prices_dif = []
    dif = []
    divs_dif_2 = []
    prices_dif_2 = []
    reb = []
    reb_stocks_prices = []
    def input(self):
        if ((self.ids.field_1.text != '') and (self.ids.field_2.text != '') and (self.ids.field_3.text != '') and (self.ids.field_4.text != '') and (self.ids.field_5.text != '') and (self.ids.field_6.text != '') and (self.ids.field_7.text != '') and (self.ids.field_8.text != '') and (self.ids.field_9.text != '') and (self.ids.field_10.text != '') and (self.ids.field_num.text != '')):
            i = int(0)
            for i in range(10):
                self.days.append(float(i + 1))
            self.stocks_prices.append(float(self.ids.field_1.text))
            self.stocks_prices.append(float(self.ids.field_2.text))
            self.stocks_prices.append(float(self.ids.field_3.text))
            self.stocks_prices.append(float(self.ids.field_4.text))
            self.stocks_prices.append(float(self.ids.field_5.text))
            self.stocks_prices.append(float(self.ids.field_6.text))
            self.stocks_prices.append(float(self.ids.field_7.text))
            self.stocks_prices.append(float(self.ids.field_8.text))
            self.stocks_prices.append(float(self.ids.field_9.text))
            self.stocks_prices.append(float(self.ids.field_10.text))
            self.num.append(float(self.ids.field_num.text))
            average_day = float(0.0)
            average_stocks_price = float(0.0)
            for i in range(10):
                average_day = average_day + self.days[i]
                average_stocks_price = average_stocks_price + self.stocks_prices[i]
            average_stocks_price = average_stocks_price / 10
            average_day = average_day / 10
            i = 0
            for i in range(10):
                self.divs_dif.append(float(self.days[i] - average_day))
                self.prices_dif.append(float(self.stocks_prices[i] - average_stocks_price))
                self.dif.append(float(self.divs_dif[i] * self.prices_dif[i]))
                self.divs_dif_2.append(float(self.divs_dif[i] * self.divs_dif[i]))
                self.prices_dif_2.append(float(self.prices_dif[i] * self.prices_dif[i]))
            max_price = 0
            for i in range(10):
                self.reb.append(0)
                if (self.stocks_prices[i] > max_price):
                    max_price = self.stocks_prices[i]
            i = 0
            for i in range(10):
                self.reb_stocks_prices.append(self.stocks_prices[i])
                while (self.reb_stocks_prices[i] < max_price):
                    self.reb_stocks_prices[i] = self.reb_stocks_prices[i] + self.stocks_prices[i]
                    self.reb[i] = self.reb[i] + 1
            self.manager.current = 'manual_5'
        else:
            self.dialog = MDDialog(title="Ошибка",
                               text="Данные введены некорректно или отсутствуют",
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
            self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()
    def clear(self, *args):
        self.num = []
        self.days = []
        self.stocks_prices = []
        self.divs_dif = []
        self.prices_dif = []
        self.dif = []
        self.divs_dif_2 = []
        self.prices_dif_2 = []
        self.reb = []
        self.reb_stocks_prices = []

class Manual_5(Screen):
    num = []
    days = []
    stocks_prices = []
    divs_dif = []
    prices_dif = []
    dif = []
    divs_dif_2 = []
    prices_dif_2 = []
    reb = []
    reb_stocks_prices = []
    def input(self):
        if ((self.ids.field_1.text != '') and (self.ids.field_2.text != '') and (self.ids.field_3.text != '') and (self.ids.field_4.text != '') and (self.ids.field_5.text != '') and (self.ids.field_6.text != '') and (self.ids.field_7.text != '') and (self.ids.field_8.text != '') and (self.ids.field_9.text != '') and (self.ids.field_10.text != '') and (self.ids.field_num.text != '')):
            i = int(0)
            for i in range(10):
                self.days.append(float(i + 1))
            self.stocks_prices.append(float(self.ids.field_1.text))
            self.stocks_prices.append(float(self.ids.field_2.text))
            self.stocks_prices.append(float(self.ids.field_3.text))
            self.stocks_prices.append(float(self.ids.field_4.text))
            self.stocks_prices.append(float(self.ids.field_5.text))
            self.stocks_prices.append(float(self.ids.field_6.text))
            self.stocks_prices.append(float(self.ids.field_7.text))
            self.stocks_prices.append(float(self.ids.field_8.text))
            self.stocks_prices.append(float(self.ids.field_9.text))
            self.stocks_prices.append(float(self.ids.field_10.text))
            self.num.append(float(self.ids.field_num.text))
            average_day = float(0.0)
            average_stocks_price = float(0.0)
            for i in range(10):
                average_day = average_day + self.days[i]
                average_stocks_price = average_stocks_price + self.stocks_prices[i]
            average_stocks_price = average_stocks_price / 10
            average_day = average_day / 10
            i = 0
            for i in range(10):
                self.divs_dif.append(float(self.days[i] - average_day))
                self.prices_dif.append(float(self.stocks_prices[i] - average_stocks_price))
                self.dif.append(float(self.divs_dif[i] * self.prices_dif[i]))
                self.divs_dif_2.append(float(self.divs_dif[i] * self.divs_dif[i]))
                self.prices_dif_2.append(float(self.prices_dif[i] * self.prices_dif[i]))
            max_price = 0
            for i in range(10):
                self.reb.append(0)
                if (self.stocks_prices[i] > max_price):
                    max_price = self.stocks_prices[i]
            i = 0
            for i in range(10):
                self.reb_stocks_prices.append(self.stocks_prices[i])
                while (self.reb_stocks_prices[i] < max_price):
                    self.reb_stocks_prices[i] = self.reb_stocks_prices[i] + self.stocks_prices[i]
                    self.reb[i] = self.reb[i] + 1
            self.manager.current = 'manual_6'
        else:
            self.dialog = MDDialog(title="Ошибка",
                               text="Данные введены некорректно или отсутствуют",
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
            self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()
    def clear(self, *args):
        self.num = []
        self.days = []
        self.stocks_prices = []
        self.divs_dif = []
        self.prices_dif = []
        self.dif = []
        self.divs_dif_2 = []
        self.prices_dif_2 = []
        self.reb = []
        self.reb_stocks_prices = []

class Manual_6(Screen):
    num = []
    days = []
    stocks_prices = []
    divs_dif = []
    prices_dif = []
    dif = []
    divs_dif_2 = []
    prices_dif_2 = []
    reb = []
    reb_stocks_prices = []
    def input(self):
        if ((self.ids.field_1.text != '') and (self.ids.field_2.text != '') and (self.ids.field_3.text != '') and (self.ids.field_4.text != '') and (self.ids.field_5.text != '') and (self.ids.field_6.text != '') and (self.ids.field_7.text != '') and (self.ids.field_8.text != '') and (self.ids.field_9.text != '') and (self.ids.field_10.text != '') and (self.ids.field_num.text != '')):
            i = int(0)
            for i in range(10):
                self.days.append(float(i + 1))
            self.stocks_prices.append(float(self.ids.field_1.text))
            self.stocks_prices.append(float(self.ids.field_2.text))
            self.stocks_prices.append(float(self.ids.field_3.text))
            self.stocks_prices.append(float(self.ids.field_4.text))
            self.stocks_prices.append(float(self.ids.field_5.text))
            self.stocks_prices.append(float(self.ids.field_6.text))
            self.stocks_prices.append(float(self.ids.field_7.text))
            self.stocks_prices.append(float(self.ids.field_8.text))
            self.stocks_prices.append(float(self.ids.field_9.text))
            self.stocks_prices.append(float(self.ids.field_10.text))
            self.num.append(float(self.ids.field_num.text))
            average_day = float(0.0)
            average_stocks_price = float(0.0)
            for i in range(10):
                average_day = average_day + self.days[i]
                average_stocks_price = average_stocks_price + self.stocks_prices[i]
            average_stocks_price = average_stocks_price / 10
            average_day = average_day / 10
            i = 0
            for i in range(10):
                self.divs_dif.append(float(self.days[i] - average_day))
                self.prices_dif.append(float(self.stocks_prices[i] - average_stocks_price))
                self.dif.append(float(self.divs_dif[i] * self.prices_dif[i]))
                self.divs_dif_2.append(float(self.divs_dif[i] * self.divs_dif[i]))
                self.prices_dif_2.append(float(self.prices_dif[i] * self.prices_dif[i]))
            max_price = 0
            for i in range(10):
                self.reb.append(0)
                if (self.stocks_prices[i] > max_price):
                    max_price = self.stocks_prices[i]
            i = 0
            for i in range(10):
                self.reb_stocks_prices.append(self.stocks_prices[i])
                while (self.reb_stocks_prices[i] < max_price):
                    self.reb_stocks_prices[i] = self.reb_stocks_prices[i] + self.stocks_prices[i]
                    self.reb[i] = self.reb[i] + 1
            self.manager.current = 'manual_7'
        else:
            self.dialog = MDDialog(title="Ошибка",
                               text="Данные введены некорректно или отсутствуют",
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
            self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()
    def clear(self, *args):
        self.num = []
        self.days = []
        self.stocks_prices = []
        self.divs_dif = []
        self.prices_dif = []
        self.dif = []
        self.divs_dif_2 = []
        self.prices_dif_2 = []
        self.reb = []
        self.reb_stocks_prices = []

class Manual_7(Screen):
    num = []
    days = []
    stocks_prices = []
    divs_dif = []
    prices_dif = []
    dif = []
    divs_dif_2 = []
    prices_dif_2 = []
    reb = []
    reb_stocks_prices = []
    def input(self):
        if ((self.ids.field_1.text != '') and (self.ids.field_2.text != '') and (self.ids.field_3.text != '') and (self.ids.field_4.text != '') and (self.ids.field_5.text != '') and (self.ids.field_6.text != '') and (self.ids.field_7.text != '') and (self.ids.field_8.text != '') and (self.ids.field_9.text != '') and (self.ids.field_10.text != '') and (self.ids.field_num.text != '')):
            i = int(0)
            for i in range(10):
                self.days.append(float(i + 1))
            self.stocks_prices.append(float(self.ids.field_1.text))
            self.stocks_prices.append(float(self.ids.field_2.text))
            self.stocks_prices.append(float(self.ids.field_3.text))
            self.stocks_prices.append(float(self.ids.field_4.text))
            self.stocks_prices.append(float(self.ids.field_5.text))
            self.stocks_prices.append(float(self.ids.field_6.text))
            self.stocks_prices.append(float(self.ids.field_7.text))
            self.stocks_prices.append(float(self.ids.field_8.text))
            self.stocks_prices.append(float(self.ids.field_9.text))
            self.stocks_prices.append(float(self.ids.field_10.text))
            self.num.append(float(self.ids.field_num.text))
            average_day = float(0.0)
            average_stocks_price = float(0.0)
            for i in range(10):
                average_day = average_day + self.days[i]
                average_stocks_price = average_stocks_price + self.stocks_prices[i]
            average_stocks_price = average_stocks_price / 10
            average_day = average_day / 10
            i = 0
            for i in range(10):
                self.divs_dif.append(float(self.days[i] - average_day))
                self.prices_dif.append(float(self.stocks_prices[i] - average_stocks_price))
                self.dif.append(float(self.divs_dif[i] * self.prices_dif[i]))
                self.divs_dif_2.append(float(self.divs_dif[i] * self.divs_dif[i]))
                self.prices_dif_2.append(float(self.prices_dif[i] * self.prices_dif[i]))
            max_price = 0
            for i in range(10):
                self.reb.append(0)
                if (self.stocks_prices[i] > max_price):
                    max_price = self.stocks_prices[i]
            i = 0
            for i in range(10):
                self.reb_stocks_prices.append(self.stocks_prices[i])
                while (self.reb_stocks_prices[i] < max_price):
                    self.reb_stocks_prices[i] = self.reb_stocks_prices[i] + self.stocks_prices[i]
                    self.reb[i] = self.reb[i] + 1
            self.manager.current = 'manual_8'
        else:
            self.dialog = MDDialog(title="Ошибка",
                               text="Данные введены некорректно или отсутствуют",
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
            self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()
    def clear(self, *args):
        self.num = []
        self.days = []
        self.stocks_prices = []
        self.divs_dif = []
        self.prices_dif = []
        self.dif = []
        self.divs_dif_2 = []
        self.prices_dif_2 = []
        self.reb = []
        self.reb_stocks_prices = []

class Manual_8(Screen):
    num = []
    days = []
    stocks_prices = []
    divs_dif = []
    prices_dif = []
    dif = []
    divs_dif_2 = []
    prices_dif_2 = []
    reb = []
    reb_stocks_prices = []
    def input(self):
        if ((self.ids.field_1.text != '') and (self.ids.field_2.text != '') and (self.ids.field_3.text != '') and (self.ids.field_4.text != '') and (self.ids.field_5.text != '') and (self.ids.field_6.text != '') and (self.ids.field_7.text != '') and (self.ids.field_8.text != '') and (self.ids.field_9.text != '') and (self.ids.field_10.text != '') and (self.ids.field_num.text != '')):
            i = int(0)
            for i in range(10):
                self.days.append(float(i + 1))
            self.stocks_prices.append(float(self.ids.field_1.text))
            self.stocks_prices.append(float(self.ids.field_2.text))
            self.stocks_prices.append(float(self.ids.field_3.text))
            self.stocks_prices.append(float(self.ids.field_4.text))
            self.stocks_prices.append(float(self.ids.field_5.text))
            self.stocks_prices.append(float(self.ids.field_6.text))
            self.stocks_prices.append(float(self.ids.field_7.text))
            self.stocks_prices.append(float(self.ids.field_8.text))
            self.stocks_prices.append(float(self.ids.field_9.text))
            self.stocks_prices.append(float(self.ids.field_10.text))
            self.num.append(float(self.ids.field_num.text))
            average_day = float(0.0)
            average_stocks_price = float(0.0)
            for i in range(10):
                average_day = average_day + self.days[i]
                average_stocks_price = average_stocks_price + self.stocks_prices[i]
            average_stocks_price = average_stocks_price / 10
            average_day = average_day / 10
            i = 0
            for i in range(10):
                self.divs_dif.append(float(self.days[i] - average_day))
                self.prices_dif.append(float(self.stocks_prices[i] - average_stocks_price))
                self.dif.append(float(self.divs_dif[i] * self.prices_dif[i]))
                self.divs_dif_2.append(float(self.divs_dif[i] * self.divs_dif[i]))
                self.prices_dif_2.append(float(self.prices_dif[i] * self.prices_dif[i]))
            max_price = 0
            for i in range(10):
                self.reb.append(0)
                if (self.stocks_prices[i] > max_price):
                    max_price = self.stocks_prices[i]
            i = 0
            for i in range(10):
                self.reb_stocks_prices.append(self.stocks_prices[i])
                while (self.reb_stocks_prices[i] < max_price):
                    self.reb_stocks_prices[i] = self.reb_stocks_prices[i] + self.stocks_prices[i]
                    self.reb[i] = self.reb[i] + 1
            self.manager.current = 'manual_9'
        else:
            self.dialog = MDDialog(title="Ошибка",
                               text="Данные введены некорректно или отсутствуют",
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
            self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()
    def clear(self, *args):
        self.num = []
        self.days = []
        self.stocks_prices = []
        self.divs_dif = []
        self.prices_dif = []
        self.dif = []
        self.divs_dif_2 = []
        self.prices_dif_2 = []
        self.reb = []
        self.reb_stocks_prices = []

class Manual_9(Screen):
    num = []
    days = []
    stocks_prices = []
    divs_dif = []
    prices_dif = []
    dif = []
    divs_dif_2 = []
    prices_dif_2 = []
    reb = []
    reb_stocks_prices = []
    def input(self):
        if ((self.ids.field_1.text != '') and (self.ids.field_2.text != '') and (self.ids.field_3.text != '') and (self.ids.field_4.text != '') and (self.ids.field_5.text != '') and (self.ids.field_6.text != '') and (self.ids.field_7.text != '') and (self.ids.field_8.text != '') and (self.ids.field_9.text != '') and (self.ids.field_10.text != '') and (self.ids.field_num.text != '')):
            i = int(0)
            for i in range(10):
                self.days.append(float(i + 1))
            self.stocks_prices.append(float(self.ids.field_1.text))
            self.stocks_prices.append(float(self.ids.field_2.text))
            self.stocks_prices.append(float(self.ids.field_3.text))
            self.stocks_prices.append(float(self.ids.field_4.text))
            self.stocks_prices.append(float(self.ids.field_5.text))
            self.stocks_prices.append(float(self.ids.field_6.text))
            self.stocks_prices.append(float(self.ids.field_7.text))
            self.stocks_prices.append(float(self.ids.field_8.text))
            self.stocks_prices.append(float(self.ids.field_9.text))
            self.stocks_prices.append(float(self.ids.field_10.text))
            self.num.append(float(self.ids.field_num.text))
            average_day = float(0.0)
            average_stocks_price = float(0.0)
            for i in range(10):
                average_day = average_day + self.days[i]
                average_stocks_price = average_stocks_price + self.stocks_prices[i]
            average_stocks_price = average_stocks_price / 10
            average_day = average_day / 10
            i = 0
            for i in range(10):
                self.divs_dif.append(float(self.days[i] - average_day))
                self.prices_dif.append(float(self.stocks_prices[i] - average_stocks_price))
                self.dif.append(float(self.divs_dif[i] * self.prices_dif[i]))
                self.divs_dif_2.append(float(self.divs_dif[i] * self.divs_dif[i]))
                self.prices_dif_2.append(float(self.prices_dif[i] * self.prices_dif[i]))
            max_price = 0
            for i in range(10):
                self.reb.append(0)
                if (self.stocks_prices[i] > max_price):
                    max_price = self.stocks_prices[i]
            i = 0
            for i in range(10):
                self.reb_stocks_prices.append(self.stocks_prices[i])
                while (self.reb_stocks_prices[i] < max_price):
                    self.reb_stocks_prices[i] = self.reb_stocks_prices[i] + self.stocks_prices[i]
                    self.reb[i] = self.reb[i] + 1
            self.manager.current = 'manual_10'
        else:
            self.dialog = MDDialog(title="Ошибка",
                               text="Данные введены некорректно или отсутствуют",
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
            self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()
    def clear(self, *args):
        self.num = []
        self.days = []
        self.stocks_prices = []
        self.divs_dif = []
        self.prices_dif = []
        self.dif = []
        self.divs_dif_2 = []
        self.prices_dif_2 = []
        self.reb = []
        self.reb_stocks_prices = []

class Manual_10(Screen):
    num = []
    days = []
    stocks_prices = []
    divs_dif = []
    prices_dif = []
    dif = []
    divs_dif_2 = []
    prices_dif_2 = []
    reb = []
    reb_stocks_prices = []
    def input(self):
        if ((self.ids.field_1.text != '') and (self.ids.field_2.text != '') and (self.ids.field_3.text != '') and (self.ids.field_4.text != '') and (self.ids.field_5.text != '') and (self.ids.field_6.text != '') and (self.ids.field_7.text != '') and (self.ids.field_8.text != '') and (self.ids.field_9.text != '') and (self.ids.field_10.text != '') and (self.ids.field_num.text != '')):
            i = int(0)
            for i in range(10):
                self.days.append(float(i + 1))
            self.stocks_prices.append(float(self.ids.field_1.text))
            self.stocks_prices.append(float(self.ids.field_2.text))
            self.stocks_prices.append(float(self.ids.field_3.text))
            self.stocks_prices.append(float(self.ids.field_4.text))
            self.stocks_prices.append(float(self.ids.field_5.text))
            self.stocks_prices.append(float(self.ids.field_6.text))
            self.stocks_prices.append(float(self.ids.field_7.text))
            self.stocks_prices.append(float(self.ids.field_8.text))
            self.stocks_prices.append(float(self.ids.field_9.text))
            self.stocks_prices.append(float(self.ids.field_10.text))
            self.num.append(float(self.ids.field_num.text))
            average_day = float(0.0)
            average_stocks_price = float(0.0)
            for i in range(10):
                average_day = average_day + self.days[i]
                average_stocks_price = average_stocks_price + self.stocks_prices[i]
            average_stocks_price = average_stocks_price / 10
            average_day = average_day / 10
            i = 0
            for i in range(10):
                self.divs_dif.append(float(self.days[i] - average_day))
                self.prices_dif.append(float(self.stocks_prices[i] - average_stocks_price))
                self.dif.append(float(self.divs_dif[i] * self.prices_dif[i]))
                self.divs_dif_2.append(float(self.divs_dif[i] * self.divs_dif[i]))
                self.prices_dif_2.append(float(self.prices_dif[i] * self.prices_dif[i]))
            max_price = 0
            for i in range(10):
                self.reb.append(0)
                if (self.stocks_prices[i] > max_price):
                    max_price = self.stocks_prices[i]
            i = 0
            for i in range(10):
                self.reb_stocks_prices.append(self.stocks_prices[i])
                while (self.reb_stocks_prices[i] < max_price):
                    self.reb_stocks_prices[i] = self.reb_stocks_prices[i] + self.stocks_prices[i]
                    self.reb[i] = self.reb[i] + 1
            self.manager.current = 'manual_end_1'
        else:
            self.dialog = MDDialog(title="Ошибка",
                               text="Данные введены некорректно или отсутствуют",
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
            self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()
    def clear(self, *args):
        self.num = []
        self.days = []
        self.stocks_prices = []
        self.divs_dif = []
        self.prices_dif = []
        self.dif = []
        self.divs_dif_2 = []
        self.prices_dif_2 = []
        self.reb = []
        self.reb_stocks_prices = []

class Manual_end_1(Screen):
    dispersion_x = float(0)
    dispersion_y = float(0)
    standard_dev_x = float(0)
    standard_dev_y = float(0)
    cov_ratio = float(0)
    cor_ratio = float(0)
    b = float(0)
    a = float(0)
    x = 0
    y = 0
    def load_manual_end(self):
        average_day = float(0.0)
        average_stocks_price = float(0.0)
        for i in range(10):
            average_day = average_day + Manual_1.days[i]
            average_stocks_price = average_stocks_price + Manual_1.stocks_prices[i]
        average_stocks_price = average_stocks_price / 10
        average_day = average_day / 10
        i = 0
        for i in range(10):
            self.dispersion_x = self.dispersion_x + Manual_1.divs_dif_2[i]
            self.dispersion_y = self.dispersion_y + Manual_1.prices_dif_2[i]
        self.dispersion_x = self.dispersion_x / 10
        self.dispersion_y = self.dispersion_y / 10
        self.standard_dev_x = float(math.sqrt(self.dispersion_x / 10))
        self.standard_dev_y = float(math.sqrt(self.dispersion_y / 10))
        i = 0
        for i in range(10):
            self.cov_ratio = self.cov_ratio + Manual_1.dif[i]
        self.cov_ratio = self.cov_ratio / 10
        self.cor_ratio = self.cov_ratio / (math.sqrt(self.dispersion_x) * math.sqrt(self.dispersion_y))
        self.b = float((self.cor_ratio * self.standard_dev_y) / self.standard_dev_x)
        self.a = float(average_stocks_price - (self.b * average_day))
        if (self.b > 0):
            self.lab_1 = "Сигнал тренда: ПОКУПАТЬ"
        elif (self.b < 0):
            self.x = 1
            self.lab_1 = "Сигнал тренда: ПРОДАВАТЬ"
        else:
            self.x = 2
            lab_1 = "Сигнал тренда: СТОЯТЬ"
        if (self.cor_ratio > 0.7):
            self.lab_2 = "Сигнал доверия: ПОКУПАТЬ"
        elif (self.cor_ratio < (-0.7)):
            self.y = 1
            self.lab_2 = "Сигнал доверия: ПРОДАВАТЬ"
        else:
            self.y = 2
            self.lab_2 = "Сигнал доверия: СТОЯТЬ"
        if (self.x == self.y):
            self.lab_3 = "Итоговая рекомендация робота: ПОКУПАТЬ"
        else:
            self.lab_3 = "Итоговая рекомендация робота: СТОЯТЬ"
        layout = MDBoxLayout
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.575},
                                 size_hint=(0.9, 0.6),
                                 rows_num=10,
                                 column_data=[
                                     ("Номер акции (x)", dp(15)),
                                     ("Стоимость акции (y)", dp(15)),
                                     ("x-x(ср)", dp(15)),
                                     ("y-y(ср)", dp(20)),
                                     ("(x-x(ср))(y-y(ср))", dp(30)),
                                     ("x-x(ср)^2", dp(30)),
                                     ("y-y(ср)^2", dp(30))
                                 ],
                                 row_data=[
                                     ("{0:.0f}".format(Manual_1.days[i]), "{0:.2f}".format(Manual_1.stocks_prices[i]), Manual_1.divs_dif[i], Manual_1.prices_dif[i], Manual_1.dif[i], Manual_1.divs_dif_2[i], Manual_1.prices_dif_2[i])
                                     for i in range(10)]
                                 )
        self.add_widget(self.data_table)
        return layout
    def load_manual_end_dialog(self):
        self.dialog = MDDialog(title="Информация о портфеле",
                               text="Дисперсии: s(x)^2 = {0:.4f}, ".format(self.dispersion_x) + "s(y)^2 = {0:.4f}".format(self.dispersion_y) + "\nСтандартные отклонения: s(x) = {0:.4f} млн. руб., ".format(self.standard_dev_x) + "s(y) = {0:.4f} млн. руб.".format(self.standard_dev_y) + "\nКоэффициент ковариации: K(xy) = {0:.4f}".format(self.cov_ratio) + "\nКоэффициент корреляции: r(xy) = {0:.2f}".format(self.cor_ratio) + "\nУравнение парной регрессии: y = {0:.4f}x + ".format(self.b) +  "{0:.3f}".format(self.a),
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()
    def load_manual_end_ready(self):
        self.dialog = MDDialog(title="Ваш портфель готов!",
                               text=self.lab_3,
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()
    def on_enter(self):
        self.load_manual_end()
        self.load_manual_end_ready()
    def on_leave(self, *args):
        self.data_table.clear_widgets()

class Manual_end_2(Screen):
    dispersion_x = float(0)
    dispersion_y = float(0)
    standard_dev_x = float(0)
    standard_dev_y = float(0)
    cov_ratio = float(0)
    cor_ratio = float(0)
    b = float(0)
    a = float(0)
    x = 0
    y = 0
    def load_manual_end(self):
        average_day = float(0.0)
        average_stocks_price = float(0.0)
        for i in range(10):
            average_day = average_day + Manual_2.days[i]
            average_stocks_price = average_stocks_price + Manual_2.stocks_prices[i]
        average_stocks_price = average_stocks_price / 10
        average_day = average_day / 10
        i = 0
        for i in range(10):
            self.dispersion_x = self.dispersion_x + Manual_2.divs_dif_2[i]
            self.dispersion_y = self.dispersion_y + Manual_2.prices_dif_2[i]
        self.dispersion_x = self.dispersion_x / 10
        self.dispersion_y = self.dispersion_y / 10
        self.standard_dev_x = float(math.sqrt(self.dispersion_x / 10))
        self.standard_dev_y = float(math.sqrt(self.dispersion_y / 10))
        i = 0
        for i in range(10):
            self.cov_ratio = self.cov_ratio + Manual_2.dif[i]
        self.cov_ratio = self.cov_ratio / 10
        self.cor_ratio = self.cov_ratio / (math.sqrt(self.dispersion_x) * math.sqrt(self.dispersion_y))
        self.b = float((self.cor_ratio * self.standard_dev_y) / self.standard_dev_x)
        self.a = float(average_stocks_price - (self.b * average_day))
        if (self.b > 0):
            self.lab_1 = "Сигнал тренда: ПОКУПАТЬ"
        elif (self.b < 0):
            self.x = 1
            self.lab_1 = "Сигнал тренда: ПРОДАВАТЬ"
        else:
            self.x = 2
            lab_1 = "Сигнал тренда: СТОЯТЬ"
        if (self.cor_ratio > 0.7):
            self.lab_2 = "Сигнал доверия: ПОКУПАТЬ"
        elif (self.cor_ratio < (-0.7)):
            self.y = 1
            self.lab_2 = "Сигнал доверия: ПРОДАВАТЬ"
        else:
            self.y = 2
            self.lab_2 = "Сигнал доверия: СТОЯТЬ"
        if (self.x == self.y):
            self.lab_3 = "Итоговая рекомендация робота: ПОКУПАТЬ"
        else:
            self.lab_3 = "Итоговая рекомендация робота: СТОЯТЬ"
        layout = MDBoxLayout
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.575},
                                 size_hint=(0.9, 0.6),
                                 rows_num=10,
                                 column_data=[
                                     ("Номер акции (x)", dp(15)),
                                     ("Стоимость акции (y)", dp(15)),
                                     ("x-x(ср)", dp(15)),
                                     ("y-y(ср)", dp(20)),
                                     ("(x-x(ср))(y-y(ср))", dp(30)),
                                     ("x-x(ср)^2", dp(30)),
                                     ("y-y(ср)^2", dp(30))
                                 ],
                                 row_data=[
                                     ("{0:.0f}".format(Manual_2.days[i]), "{0:.2f}".format(Manual_2.stocks_prices[i]), Manual_2.divs_dif[i], Manual_2.prices_dif[i], Manual_2.dif[i], Manual_2.divs_dif_2[i], Manual_2.prices_dif_2[i])
                                     for i in range(10)]
                                 )
        self.add_widget(self.data_table)
        return layout
    def load_manual_end_dialog(self):
        self.dialog = MDDialog(title="Информация о портфеле",
                               text="Дисперсии: s(x)^2 = {0:.4f}, ".format(self.dispersion_x) + "s(y)^2 = {0:.4f}".format(self.dispersion_y) + "\nСтандартные отклонения: s(x) = {0:.4f} млн. руб., ".format(self.standard_dev_x) + "s(y) = {0:.4f} млн. руб.".format(self.standard_dev_y) + "\nКоэффициент ковариации: K(xy) = {0:.4f}".format(self.cov_ratio) + "\nКоэффициент корреляции: r(xy) = {0:.2f}".format(self.cor_ratio) + "\nУравнение парной регрессии: y = {0:.4f}x + ".format(self.b) +  "{0:.3f}".format(self.a),
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()
    def load_manual_end_ready(self):
        self.dialog = MDDialog(title="Ваш портфель готов!",
                               text=self.lab_3,
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()
    def on_enter(self):
        self.load_manual_end()
        self.load_manual_end_ready()
    def on_leave(self, *args):
        self.data_table.clear_widgets()

class Manual_end_3(Screen):
    dispersion_x = float(0)
    dispersion_y = float(0)
    standard_dev_x = float(0)
    standard_dev_y = float(0)
    cov_ratio = float(0)
    cor_ratio = float(0)
    b = float(0)
    a = float(0)
    x = 0
    y = 0
    def load_manual_end(self):
        average_day = float(0.0)
        average_stocks_price = float(0.0)
        for i in range(10):
            average_day = average_day + Manual_3.days[i]
            average_stocks_price = average_stocks_price + Manual_3.stocks_prices[i]
        average_stocks_price = average_stocks_price / 10
        average_day = average_day / 10
        i = 0
        for i in range(10):
            self.dispersion_x = self.dispersion_x + Manual_3.divs_dif_2[i]
            self.dispersion_y = self.dispersion_y + Manual_3.prices_dif_2[i]
        self.dispersion_x = self.dispersion_x / 10
        self.dispersion_y = self.dispersion_y / 10
        self.standard_dev_x = float(math.sqrt(self.dispersion_x / 10))
        self.standard_dev_y = float(math.sqrt(self.dispersion_y / 10))
        i = 0
        for i in range(10):
            self.cov_ratio = self.cov_ratio + Manual_3.dif[i]
        self.cov_ratio = self.cov_ratio / 10
        self.cor_ratio = self.cov_ratio / (math.sqrt(self.dispersion_x) * math.sqrt(self.dispersion_y))
        self.b = float((self.cor_ratio * self.standard_dev_y) / self.standard_dev_x)
        self.a = float(average_stocks_price - (self.b * average_day))
        if (self.b > 0):
            self.lab_1 = "Сигнал тренда: ПОКУПАТЬ"
        elif (self.b < 0):
            self.x = 1
            self.lab_1 = "Сигнал тренда: ПРОДАВАТЬ"
        else:
            self.x = 2
            lab_1 = "Сигнал тренда: СТОЯТЬ"
        if (self.cor_ratio > 0.7):
            self.lab_2 = "Сигнал доверия: ПОКУПАТЬ"
        elif (self.cor_ratio < (-0.7)):
            self.y = 1
            self.lab_2 = "Сигнал доверия: ПРОДАВАТЬ"
        else:
            self.y = 2
            self.lab_2 = "Сигнал доверия: СТОЯТЬ"
        if (self.x == self.y):
            self.lab_3 = "Итоговая рекомендация робота: ПОКУПАТЬ"
        else:
            self.lab_3 = "Итоговая рекомендация робота: СТОЯТЬ"
        layout = MDBoxLayout
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.575},
                                 size_hint=(0.9, 0.6),
                                 rows_num=10,
                                 column_data=[
                                     ("Номер акции (x)", dp(15)),
                                     ("Стоимость акции (y)", dp(15)),
                                     ("x-x(ср)", dp(15)),
                                     ("y-y(ср)", dp(20)),
                                     ("(x-x(ср))(y-y(ср))", dp(30)),
                                     ("x-x(ср)^2", dp(30)),
                                     ("y-y(ср)^2", dp(30))
                                 ],
                                 row_data=[
                                     ("{0:.0f}".format(Manual_3.days[i]), "{0:.2f}".format(Manual_3.stocks_prices[i]), Manual_3.divs_dif[i], Manual_3.prices_dif[i], Manual_3.dif[i], Manual_3.divs_dif_2[i], Manual_3.prices_dif_2[i])
                                     for i in range(10)]
                                 )
        self.add_widget(self.data_table)
        return layout
    def load_manual_end_dialog(self):
        self.dialog = MDDialog(title="Информация о портфеле",
                               text="Дисперсии: s(x)^2 = {0:.4f}, ".format(self.dispersion_x) + "s(y)^2 = {0:.4f}".format(self.dispersion_y) + "\nСтандартные отклонения: s(x) = {0:.4f} млн. руб., ".format(self.standard_dev_x) + "s(y) = {0:.4f} млн. руб.".format(self.standard_dev_y) + "\nКоэффициент ковариации: K(xy) = {0:.4f}".format(self.cov_ratio) + "\nКоэффициент корреляции: r(xy) = {0:.2f}".format(self.cor_ratio) + "\nУравнение парной регрессии: y = {0:.4f}x + ".format(self.b) +  "{0:.3f}".format(self.a),
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()
    def load_manual_end_ready(self):
        self.dialog = MDDialog(title="Ваш портфель готов!",
                               text=self.lab_3,
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()
    def on_enter(self):
        self.load_manual_end()
        self.load_manual_end_ready()
    def on_leave(self, *args):
        self.data_table.clear_widgets()

class Manual_end_4(Screen):
    dispersion_x = float(0)
    dispersion_y = float(0)
    standard_dev_x = float(0)
    standard_dev_y = float(0)
    cov_ratio = float(0)
    cor_ratio = float(0)
    b = float(0)
    a = float(0)
    x = 0
    y = 0
    def load_manual_end(self):
        average_day = float(0.0)
        average_stocks_price = float(0.0)
        for i in range(10):
            average_day = average_day + Manual_4.days[i]
            average_stocks_price = average_stocks_price + Manual_4.stocks_prices[i]
        average_stocks_price = average_stocks_price / 10
        average_day = average_day / 10
        i = 0
        for i in range(10):
            self.dispersion_x = self.dispersion_x + Manual_4.divs_dif_2[i]
            self.dispersion_y = self.dispersion_y + Manual_4.prices_dif_2[i]
        self.dispersion_x = self.dispersion_x / 10
        self.dispersion_y = self.dispersion_y / 10
        self.standard_dev_x = float(math.sqrt(self.dispersion_x / 10))
        self.standard_dev_y = float(math.sqrt(self.dispersion_y / 10))
        i = 0
        for i in range(10):
            self.cov_ratio = self.cov_ratio + Manual_4.dif[i]
        self.cov_ratio = self.cov_ratio / 10
        self.cor_ratio = self.cov_ratio / (math.sqrt(self.dispersion_x) * math.sqrt(self.dispersion_y))
        self.b = float((self.cor_ratio * self.standard_dev_y) / self.standard_dev_x)
        self.a = float(average_stocks_price - (self.b * average_day))
        if (self.b > 0):
            self.lab_1 = "Сигнал тренда: ПОКУПАТЬ"
        elif (self.b < 0):
            self.x = 1
            self.lab_1 = "Сигнал тренда: ПРОДАВАТЬ"
        else:
            self.x = 2
            lab_1 = "Сигнал тренда: СТОЯТЬ"
        if (self.cor_ratio > 0.7):
            self.lab_2 = "Сигнал доверия: ПОКУПАТЬ"
        elif (self.cor_ratio < (-0.7)):
            self.y = 1
            self.lab_2 = "Сигнал доверия: ПРОДАВАТЬ"
        else:
            self.y = 2
            self.lab_2 = "Сигнал доверия: СТОЯТЬ"
        if (self.x == self.y):
            self.lab_3 = "Итоговая рекомендация робота: ПОКУПАТЬ"
        else:
            self.lab_3 = "Итоговая рекомендация робота: СТОЯТЬ"
        layout = MDBoxLayout
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.575},
                                 size_hint=(0.9, 0.6),
                                 rows_num=10,
                                 column_data=[
                                     ("Номер акции (x)", dp(15)),
                                     ("Стоимость акции (y)", dp(15)),
                                     ("x-x(ср)", dp(15)),
                                     ("y-y(ср)", dp(20)),
                                     ("(x-x(ср))(y-y(ср))", dp(30)),
                                     ("x-x(ср)^2", dp(30)),
                                     ("y-y(ср)^2", dp(30))
                                 ],
                                 row_data=[
                                     ("{0:.0f}".format(Manual_4.days[i]), "{0:.2f}".format(Manual_4.stocks_prices[i]), Manual_4.divs_dif[i], Manual_4.prices_dif[i], Manual_4.dif[i], Manual_4.divs_dif_2[i], Manual_4.prices_dif_2[i])
                                     for i in range(10)]
                                 )
        self.add_widget(self.data_table)
        return layout
    def load_manual_end_dialog(self):
        self.dialog = MDDialog(title="Информация о портфеле",
                               text="Дисперсии: s(x)^2 = {0:.4f}, ".format(self.dispersion_x) + "s(y)^2 = {0:.4f}".format(self.dispersion_y) + "\nСтандартные отклонения: s(x) = {0:.4f} млн. руб., ".format(self.standard_dev_x) + "s(y) = {0:.4f} млн. руб.".format(self.standard_dev_y) + "\nКоэффициент ковариации: K(xy) = {0:.4f}".format(self.cov_ratio) + "\nКоэффициент корреляции: r(xy) = {0:.2f}".format(self.cor_ratio) + "\nУравнение парной регрессии: y = {0:.4f}x + ".format(self.b) +  "{0:.3f}".format(self.a),
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()
    def load_manual_end_ready(self):
        self.dialog = MDDialog(title="Ваш портфель готов!",
                               text=self.lab_3,
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()
    def on_enter(self):
        self.load_manual_end()
        self.load_manual_end_ready()
    def on_leave(self, *args):
        self.data_table.clear_widgets()

class Manual_end_5(Screen):
    dispersion_x = float(0)
    dispersion_y = float(0)
    standard_dev_x = float(0)
    standard_dev_y = float(0)
    cov_ratio = float(0)
    cor_ratio = float(0)
    b = float(0)
    a = float(0)
    x = 0
    y = 0
    def load_manual_end(self):
        average_day = float(0.0)
        average_stocks_price = float(0.0)
        for i in range(10):
            average_day = average_day + Manual_5.days[i]
            average_stocks_price = average_stocks_price + Manual_5.stocks_prices[i]
        average_stocks_price = average_stocks_price / 10
        average_day = average_day / 10
        i = 0
        for i in range(10):
            self.dispersion_x = self.dispersion_x + Manual_5.divs_dif_2[i]
            self.dispersion_y = self.dispersion_y + Manual_5.prices_dif_2[i]
        self.dispersion_x = self.dispersion_x / 10
        self.dispersion_y = self.dispersion_y / 10
        self.standard_dev_x = float(math.sqrt(self.dispersion_x / 10))
        self.standard_dev_y = float(math.sqrt(self.dispersion_y / 10))
        i = 0
        for i in range(10):
            self.cov_ratio = self.cov_ratio + Manual_5.dif[i]
        self.cov_ratio = self.cov_ratio / 10
        self.cor_ratio = self.cov_ratio / (math.sqrt(self.dispersion_x) * math.sqrt(self.dispersion_y))
        self.b = float((self.cor_ratio * self.standard_dev_y) / self.standard_dev_x)
        self.a = float(average_stocks_price - (self.b * average_day))
        if (self.b > 0):
            self.lab_1 = "Сигнал тренда: ПОКУПАТЬ"
        elif (self.b < 0):
            self.x = 1
            self.lab_1 = "Сигнал тренда: ПРОДАВАТЬ"
        else:
            self.x = 2
            lab_1 = "Сигнал тренда: СТОЯТЬ"
        if (self.cor_ratio > 0.7):
            self.lab_2 = "Сигнал доверия: ПОКУПАТЬ"
        elif (self.cor_ratio < (-0.7)):
            self.y = 1
            self.lab_2 = "Сигнал доверия: ПРОДАВАТЬ"
        else:
            self.y = 2
            self.lab_2 = "Сигнал доверия: СТОЯТЬ"
        if (self.x == self.y):
            self.lab_3 = "Итоговая рекомендация робота: ПОКУПАТЬ"
        else:
            self.lab_3 = "Итоговая рекомендация робота: СТОЯТЬ"
        layout = MDBoxLayout
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.575},
                                 size_hint=(0.9, 0.6),
                                 rows_num=10,
                                 column_data=[
                                     ("Номер акции (x)", dp(15)),
                                     ("Стоимость акции (y)", dp(15)),
                                     ("x-x(ср)", dp(15)),
                                     ("y-y(ср)", dp(20)),
                                     ("(x-x(ср))(y-y(ср))", dp(30)),
                                     ("x-x(ср)^2", dp(30)),
                                     ("y-y(ср)^2", dp(30))
                                 ],
                                 row_data=[
                                     ("{0:.0f}".format(Manual_5.days[i]), "{0:.2f}".format(Manual_5.stocks_prices[i]), Manual_5.divs_dif[i], Manual_5.prices_dif[i], Manual_5.dif[i], Manual_5.divs_dif_2[i], Manual_5.prices_dif_2[i])
                                     for i in range(10)]
                                 )
        self.add_widget(self.data_table)
        return layout
    def load_manual_end_dialog(self):
        self.dialog = MDDialog(title="Информация о портфеле",
                               text="Дисперсии: s(x)^2 = {0:.4f}, ".format(self.dispersion_x) + "s(y)^2 = {0:.4f}".format(self.dispersion_y) + "\nСтандартные отклонения: s(x) = {0:.4f} млн. руб., ".format(self.standard_dev_x) + "s(y) = {0:.4f} млн. руб.".format(self.standard_dev_y) + "\nКоэффициент ковариации: K(xy) = {0:.4f}".format(self.cov_ratio) + "\nКоэффициент корреляции: r(xy) = {0:.2f}".format(self.cor_ratio) + "\nУравнение парной регрессии: y = {0:.4f}x + ".format(self.b) +  "{0:.3f}".format(self.a),
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()
    def load_manual_end_ready(self):
        self.dialog = MDDialog(title="Ваш портфель готов!",
                               text=self.lab_3,
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()
    def on_enter(self):
        self.load_manual_end()
        self.load_manual_end_ready()
    def on_leave(self, *args):
        self.data_table.clear_widgets()

class Manual_end_6(Screen):
    dispersion_x = float(0)
    dispersion_y = float(0)
    standard_dev_x = float(0)
    standard_dev_y = float(0)
    cov_ratio = float(0)
    cor_ratio = float(0)
    b = float(0)
    a = float(0)
    x = 0
    y = 0
    def load_manual_end(self):
        average_day = float(0.0)
        average_stocks_price = float(0.0)
        for i in range(10):
            average_day = average_day + Manual_6.days[i]
            average_stocks_price = average_stocks_price + Manual_6.stocks_prices[i]
        average_stocks_price = average_stocks_price / 10
        average_day = average_day / 10
        i = 0
        for i in range(10):
            self.dispersion_x = self.dispersion_x + Manual_6.divs_dif_2[i]
            self.dispersion_y = self.dispersion_y + Manual_6.prices_dif_2[i]
        self.dispersion_x = self.dispersion_x / 10
        self.dispersion_y = self.dispersion_y / 10
        self.standard_dev_x = float(math.sqrt(self.dispersion_x / 10))
        self.standard_dev_y = float(math.sqrt(self.dispersion_y / 10))
        i = 0
        for i in range(10):
            self.cov_ratio = self.cov_ratio + Manual_6.dif[i]
        self.cov_ratio = self.cov_ratio / 10
        self.cor_ratio = self.cov_ratio / (math.sqrt(self.dispersion_x) * math.sqrt(self.dispersion_y))
        self.b = float((self.cor_ratio * self.standard_dev_y) / self.standard_dev_x)
        self.a = float(average_stocks_price - (self.b * average_day))
        if (self.b > 0):
            self.lab_1 = "Сигнал тренда: ПОКУПАТЬ"
        elif (self.b < 0):
            self.x = 1
            self.lab_1 = "Сигнал тренда: ПРОДАВАТЬ"
        else:
            self.x = 2
            lab_1 = "Сигнал тренда: СТОЯТЬ"
        if (self.cor_ratio > 0.7):
            self.lab_2 = "Сигнал доверия: ПОКУПАТЬ"
        elif (self.cor_ratio < (-0.7)):
            self.y = 1
            self.lab_2 = "Сигнал доверия: ПРОДАВАТЬ"
        else:
            self.y = 2
            self.lab_2 = "Сигнал доверия: СТОЯТЬ"
        if (self.x == self.y):
            self.lab_3 = "Итоговая рекомендация робота: ПОКУПАТЬ"
        else:
            self.lab_3 = "Итоговая рекомендация робота: СТОЯТЬ"
        layout = MDBoxLayout
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.575},
                                 size_hint=(0.9, 0.6),
                                 rows_num=10,
                                 column_data=[
                                     ("Номер акции (x)", dp(15)),
                                     ("Стоимость акции (y)", dp(15)),
                                     ("x-x(ср)", dp(15)),
                                     ("y-y(ср)", dp(20)),
                                     ("(x-x(ср))(y-y(ср))", dp(30)),
                                     ("x-x(ср)^2", dp(30)),
                                     ("y-y(ср)^2", dp(30))
                                 ],
                                 row_data=[
                                     ("{0:.0f}".format(Manual_6.days[i]), "{0:.2f}".format(Manual_6.stocks_prices[i]), Manual_6.divs_dif[i], Manual_6.prices_dif[i], Manual_6.dif[i], Manual_6.divs_dif_2[i], Manual_6.prices_dif_2[i])
                                     for i in range(10)]
                                 )
        self.add_widget(self.data_table)
        return layout
    def load_manual_end_dialog(self):
        self.dialog = MDDialog(title="Информация о портфеле",
                               text="Дисперсии: s(x)^2 = {0:.4f}, ".format(self.dispersion_x) + "s(y)^2 = {0:.4f}".format(self.dispersion_y) + "\nСтандартные отклонения: s(x) = {0:.4f} млн. руб., ".format(self.standard_dev_x) + "s(y) = {0:.4f} млн. руб.".format(self.standard_dev_y) + "\nКоэффициент ковариации: K(xy) = {0:.4f}".format(self.cov_ratio) + "\nКоэффициент корреляции: r(xy) = {0:.2f}".format(self.cor_ratio) + "\nУравнение парной регрессии: y = {0:.4f}x + ".format(self.b) +  "{0:.3f}".format(self.a),
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()
    def load_manual_end_ready(self):
        self.dialog = MDDialog(title="Ваш портфель готов!",
                               text=self.lab_3,
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()
    def on_enter(self):
        self.load_manual_end()
        self.load_manual_end_ready()
    def on_leave(self, *args):
        self.data_table.clear_widgets()

class Manual_end_7(Screen):
    dispersion_x = float(0)
    dispersion_y = float(0)
    standard_dev_x = float(0)
    standard_dev_y = float(0)
    cov_ratio = float(0)
    cor_ratio = float(0)
    b = float(0)
    a = float(0)
    x = 0
    y = 0
    def load_manual_end(self):
        average_day = float(0.0)
        average_stocks_price = float(0.0)
        for i in range(10):
            average_day = average_day + Manual_7.days[i]
            average_stocks_price = average_stocks_price + Manual_7.stocks_prices[i]
        average_stocks_price = average_stocks_price / 10
        average_day = average_day / 10
        i = 0
        for i in range(10):
            self.dispersion_x = self.dispersion_x + Manual_7.divs_dif_2[i]
            self.dispersion_y = self.dispersion_y + Manual_7.prices_dif_2[i]
        self.dispersion_x = self.dispersion_x / 10
        self.dispersion_y = self.dispersion_y / 10
        self.standard_dev_x = float(math.sqrt(self.dispersion_x / 10))
        self.standard_dev_y = float(math.sqrt(self.dispersion_y / 10))
        i = 0
        for i in range(10):
            self.cov_ratio = self.cov_ratio + Manual_7.dif[i]
        self.cov_ratio = self.cov_ratio / 10
        self.cor_ratio = self.cov_ratio / (math.sqrt(self.dispersion_x) * math.sqrt(self.dispersion_y))
        self.b = float((self.cor_ratio * self.standard_dev_y) / self.standard_dev_x)
        self.a = float(average_stocks_price - (self.b * average_day))
        if (self.b > 0):
            self.lab_1 = "Сигнал тренда: ПОКУПАТЬ"
        elif (self.b < 0):
            self.x = 1
            self.lab_1 = "Сигнал тренда: ПРОДАВАТЬ"
        else:
            self.x = 2
            lab_1 = "Сигнал тренда: СТОЯТЬ"
        if (self.cor_ratio > 0.7):
            self.lab_2 = "Сигнал доверия: ПОКУПАТЬ"
        elif (self.cor_ratio < (-0.7)):
            self.y = 1
            self.lab_2 = "Сигнал доверия: ПРОДАВАТЬ"
        else:
            self.y = 2
            self.lab_2 = "Сигнал доверия: СТОЯТЬ"
        if (self.x == self.y):
            self.lab_3 = "Итоговая рекомендация робота: ПОКУПАТЬ"
        else:
            self.lab_3 = "Итоговая рекомендация робота: СТОЯТЬ"
        layout = MDBoxLayout
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.575},
                                 size_hint=(0.9, 0.6),
                                 rows_num=10,
                                 column_data=[
                                     ("Номер акции (x)", dp(15)),
                                     ("Стоимость акции (y)", dp(15)),
                                     ("x-x(ср)", dp(15)),
                                     ("y-y(ср)", dp(20)),
                                     ("(x-x(ср))(y-y(ср))", dp(30)),
                                     ("x-x(ср)^2", dp(30)),
                                     ("y-y(ср)^2", dp(30))
                                 ],
                                 row_data=[
                                     ("{0:.0f}".format(Manual_7.days[i]), "{0:.2f}".format(Manual_7.stocks_prices[i]), Manual_7.divs_dif[i], Manual_7.prices_dif[i], Manual_7.dif[i], Manual_7.divs_dif_2[i], Manual_7.prices_dif_2[i])
                                     for i in range(10)]
                                 )
        self.add_widget(self.data_table)
        return layout
    def load_manual_end_dialog(self):
        self.dialog = MDDialog(title="Информация о портфеле",
                               text="Дисперсии: s(x)^2 = {0:.4f}, ".format(self.dispersion_x) + "s(y)^2 = {0:.4f}".format(self.dispersion_y) + "\nСтандартные отклонения: s(x) = {0:.4f} млн. руб., ".format(self.standard_dev_x) + "s(y) = {0:.4f} млн. руб.".format(self.standard_dev_y) + "\nКоэффициент ковариации: K(xy) = {0:.4f}".format(self.cov_ratio) + "\nКоэффициент корреляции: r(xy) = {0:.2f}".format(self.cor_ratio) + "\nУравнение парной регрессии: y = {0:.4f}x + ".format(self.b) +  "{0:.3f}".format(self.a),
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()
    def load_manual_end_ready(self):
        self.dialog = MDDialog(title="Ваш портфель готов!",
                               text=self.lab_3,
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()
    def on_enter(self):
        self.load_manual_end()
        self.load_manual_end_ready()
    def on_leave(self, *args):
        self.data_table.clear_widgets()

class Manual_end_8(Screen):
    dispersion_x = float(0)
    dispersion_y = float(0)
    standard_dev_x = float(0)
    standard_dev_y = float(0)
    cov_ratio = float(0)
    cor_ratio = float(0)
    b = float(0)
    a = float(0)
    x = 0
    y = 0
    def load_manual_end(self):
        average_day = float(0.0)
        average_stocks_price = float(0.0)
        for i in range(10):
            average_day = average_day + Manual_8.days[i]
            average_stocks_price = average_stocks_price + Manual_8.stocks_prices[i]
        average_stocks_price = average_stocks_price / 10
        average_day = average_day / 10
        i = 0
        for i in range(10):
            self.dispersion_x = self.dispersion_x + Manual_8.divs_dif_2[i]
            self.dispersion_y = self.dispersion_y + Manual_8.prices_dif_2[i]
        self.dispersion_x = self.dispersion_x / 10
        self.dispersion_y = self.dispersion_y / 10
        self.standard_dev_x = float(math.sqrt(self.dispersion_x / 10))
        self.standard_dev_y = float(math.sqrt(self.dispersion_y / 10))
        i = 0
        for i in range(10):
            self.cov_ratio = self.cov_ratio + Manual_8.dif[i]
        self.cov_ratio = self.cov_ratio / 10
        self.cor_ratio = self.cov_ratio / (math.sqrt(self.dispersion_x) * math.sqrt(self.dispersion_y))
        self.b = float((self.cor_ratio * self.standard_dev_y) / self.standard_dev_x)
        self.a = float(average_stocks_price - (self.b * average_day))
        if (self.b > 0):
            self.lab_1 = "Сигнал тренда: ПОКУПАТЬ"
        elif (self.b < 0):
            self.x = 1
            self.lab_1 = "Сигнал тренда: ПРОДАВАТЬ"
        else:
            self.x = 2
            lab_1 = "Сигнал тренда: СТОЯТЬ"
        if (self.cor_ratio > 0.7):
            self.lab_2 = "Сигнал доверия: ПОКУПАТЬ"
        elif (self.cor_ratio < (-0.7)):
            self.y = 1
            self.lab_2 = "Сигнал доверия: ПРОДАВАТЬ"
        else:
            self.y = 2
            self.lab_2 = "Сигнал доверия: СТОЯТЬ"
        if (self.x == self.y):
            self.lab_3 = "Итоговая рекомендация робота: ПОКУПАТЬ"
        else:
            self.lab_3 = "Итоговая рекомендация робота: СТОЯТЬ"
        layout = MDBoxLayout
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.575},
                                 size_hint=(0.9, 0.6),
                                 rows_num=10,
                                 column_data=[
                                     ("Номер акции (x)", dp(15)),
                                     ("Стоимость акции (y)", dp(15)),
                                     ("x-x(ср)", dp(15)),
                                     ("y-y(ср)", dp(20)),
                                     ("(x-x(ср))(y-y(ср))", dp(30)),
                                     ("x-x(ср)^2", dp(30)),
                                     ("y-y(ср)^2", dp(30))
                                 ],
                                 row_data=[
                                     ("{0:.0f}".format(Manual_8.days[i]), "{0:.2f}".format(Manual_8.stocks_prices[i]), Manual_8.divs_dif[i], Manual_8.prices_dif[i], Manual_8.dif[i], Manual_8.divs_dif_2[i], Manual_8.prices_dif_2[i])
                                     for i in range(10)]
                                 )
        self.add_widget(self.data_table)
        return layout
    def load_manual_end_dialog(self):
        self.dialog = MDDialog(title="Информация о портфеле",
                               text="Дисперсии: s(x)^2 = {0:.4f}, ".format(self.dispersion_x) + "s(y)^2 = {0:.4f}".format(self.dispersion_y) + "\nСтандартные отклонения: s(x) = {0:.4f} млн. руб., ".format(self.standard_dev_x) + "s(y) = {0:.4f} млн. руб.".format(self.standard_dev_y) + "\nКоэффициент ковариации: K(xy) = {0:.4f}".format(self.cov_ratio) + "\nКоэффициент корреляции: r(xy) = {0:.2f}".format(self.cor_ratio) + "\nУравнение парной регрессии: y = {0:.4f}x + ".format(self.b) +  "{0:.3f}".format(self.a),
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()
    def load_manual_end_ready(self):
        self.dialog = MDDialog(title="Ваш портфель готов!",
                               text=self.lab_3,
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()
    def on_enter(self):
        self.load_manual_end()
        self.load_manual_end_ready()
    def on_leave(self, *args):
        self.data_table.clear_widgets()

class Manual_end_9(Screen):
    dispersion_x = float(0)
    dispersion_y = float(0)
    standard_dev_x = float(0)
    standard_dev_y = float(0)
    cov_ratio = float(0)
    cor_ratio = float(0)
    b = float(0)
    a = float(0)
    x = 0
    y = 0
    def load_manual_end(self):
        average_day = float(0.0)
        average_stocks_price = float(0.0)
        for i in range(10):
            average_day = average_day + Manual_9.days[i]
            average_stocks_price = average_stocks_price + Manual_9.stocks_prices[i]
        average_stocks_price = average_stocks_price / 10
        average_day = average_day / 10
        i = 0
        for i in range(10):
            self.dispersion_x = self.dispersion_x + Manual_9.divs_dif_2[i]
            self.dispersion_y = self.dispersion_y + Manual_9.prices_dif_2[i]
        self.dispersion_x = self.dispersion_x / 10
        self.dispersion_y = self.dispersion_y / 10
        self.standard_dev_x = float(math.sqrt(self.dispersion_x / 10))
        self.standard_dev_y = float(math.sqrt(self.dispersion_y / 10))
        i = 0
        for i in range(10):
            self.cov_ratio = self.cov_ratio + Manual_9.dif[i]
        self.cov_ratio = self.cov_ratio / 10
        self.cor_ratio = self.cov_ratio / (math.sqrt(self.dispersion_x) * math.sqrt(self.dispersion_y))
        self.b = float((self.cor_ratio * self.standard_dev_y) / self.standard_dev_x)
        self.a = float(average_stocks_price - (self.b * average_day))
        if (self.b > 0):
            self.lab_1 = "Сигнал тренда: ПОКУПАТЬ"
        elif (self.b < 0):
            self.x = 1
            self.lab_1 = "Сигнал тренда: ПРОДАВАТЬ"
        else:
            self.x = 2
            lab_1 = "Сигнал тренда: СТОЯТЬ"
        if (self.cor_ratio > 0.7):
            self.lab_2 = "Сигнал доверия: ПОКУПАТЬ"
        elif (self.cor_ratio < (-0.7)):
            self.y = 1
            self.lab_2 = "Сигнал доверия: ПРОДАВАТЬ"
        else:
            self.y = 2
            self.lab_2 = "Сигнал доверия: СТОЯТЬ"
        if (self.x == self.y):
            self.lab_3 = "Итоговая рекомендация робота: ПОКУПАТЬ"
        else:
            self.lab_3 = "Итоговая рекомендация робота: СТОЯТЬ"
        layout = MDBoxLayout
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.575},
                                 size_hint=(0.9, 0.6),
                                 rows_num=10,
                                 column_data=[
                                     ("Номер акции (x)", dp(15)),
                                     ("Стоимость акции (y)", dp(15)),
                                     ("x-x(ср)", dp(15)),
                                     ("y-y(ср)", dp(20)),
                                     ("(x-x(ср))(y-y(ср))", dp(30)),
                                     ("x-x(ср)^2", dp(30)),
                                     ("y-y(ср)^2", dp(30))
                                 ],
                                 row_data=[
                                     ("{0:.0f}".format(Manual_9.days[i]), "{0:.2f}".format(Manual_9.stocks_prices[i]), Manual_9.divs_dif[i], Manual_9.prices_dif[i], Manual_9.dif[i], Manual_9.divs_dif_2[i], Manual_9.prices_dif_2[i])
                                     for i in range(10)]
                                 )
        self.add_widget(self.data_table)
        return layout
    def load_manual_end_dialog(self):
        self.dialog = MDDialog(title="Информация о портфеле",
                               text="Дисперсии: s(x)^2 = {0:.4f}, ".format(self.dispersion_x) + "s(y)^2 = {0:.4f}".format(self.dispersion_y) + "\nСтандартные отклонения: s(x) = {0:.4f} млн. руб., ".format(self.standard_dev_x) + "s(y) = {0:.4f} млн. руб.".format(self.standard_dev_y) + "\nКоэффициент ковариации: K(xy) = {0:.4f}".format(self.cov_ratio) + "\nКоэффициент корреляции: r(xy) = {0:.2f}".format(self.cor_ratio) + "\nУравнение парной регрессии: y = {0:.4f}x + ".format(self.b) +  "{0:.3f}".format(self.a),
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()
    def load_manual_end_ready(self):
        self.dialog = MDDialog(title="Ваш портфель готов!",
                               text=self.lab_3,
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()
    def on_enter(self):
        self.load_manual_end()
        self.load_manual_end_ready()
    def on_leave(self, *args):
        self.data_table.clear_widgets()

class Manual_end_10(Screen):
    dispersion_x = float(0)
    dispersion_y = float(0)
    standard_dev_x = float(0)
    standard_dev_y = float(0)
    cov_ratio = float(0)
    cor_ratio = float(0)
    b = float(0)
    a = float(0)
    x = 0
    y = 0
    def load_manual_end(self):
        average_day = float(0.0)
        average_stocks_price = float(0.0)
        for i in range(10):
            average_day = average_day + Manual_10.days[i]
            average_stocks_price = average_stocks_price + Manual_10.stocks_prices[i]
        average_stocks_price = average_stocks_price / 10
        average_day = average_day / 10
        i = 0
        for i in range(10):
            self.dispersion_x = self.dispersion_x + Manual_10.divs_dif_2[i]
            self.dispersion_y = self.dispersion_y + Manual_10.prices_dif_2[i]
        self.dispersion_x = self.dispersion_x / 10
        self.dispersion_y = self.dispersion_y / 10
        self.standard_dev_x = float(math.sqrt(self.dispersion_x / 10))
        self.standard_dev_y = float(math.sqrt(self.dispersion_y / 10))
        i = 0
        for i in range(10):
            self.cov_ratio = self.cov_ratio + Manual_10.dif[i]
        self.cov_ratio = self.cov_ratio / 10
        self.cor_ratio = self.cov_ratio / (math.sqrt(self.dispersion_x) * math.sqrt(self.dispersion_y))
        self.b = float((self.cor_ratio * self.standard_dev_y) / self.standard_dev_x)
        self.a = float(average_stocks_price - (self.b * average_day))
        if (self.b > 0):
            self.lab_1 = "Сигнал тренда: ПОКУПАТЬ"
        elif (self.b < 0):
            self.x = 1
            self.lab_1 = "Сигнал тренда: ПРОДАВАТЬ"
        else:
            self.x = 2
            lab_1 = "Сигнал тренда: СТОЯТЬ"
        if (self.cor_ratio > 0.7):
            self.lab_2 = "Сигнал доверия: ПОКУПАТЬ"
        elif (self.cor_ratio < (-0.7)):
            self.y = 1
            self.lab_2 = "Сигнал доверия: ПРОДАВАТЬ"
        else:
            self.y = 2
            self.lab_2 = "Сигнал доверия: СТОЯТЬ"
        if (self.x == self.y):
            self.lab_3 = "Итоговая рекомендация робота: ПОКУПАТЬ"
        else:
            self.lab_3 = "Итоговая рекомендация робота: СТОЯТЬ"
        layout = MDBoxLayout
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.575},
                                 size_hint=(0.9, 0.6),
                                 rows_num=10,
                                 column_data=[
                                     ("Номер акции (x)", dp(15)),
                                     ("Стоимость акции (y)", dp(20)),
                                     ("x-x(ср)", dp(15)),
                                     ("y-y(ср)", dp(20)),
                                     ("(x-x(ср))(y-y(ср))", dp(30)),
                                     ("x-x(ср)^2", dp(30)),
                                     ("y-y(ср)^2", dp(30))
                                 ],
                                 row_data=[
                                     ("{0:.0f}".format(Manual_10.days[i]), "{0:.2f}".format(Manual_10.stocks_prices[i]), Manual_10.divs_dif[i], Manual_10.prices_dif[i], Manual_10.dif[i], Manual_10.divs_dif_2[i], Manual_10.prices_dif_2[i])
                                     for i in range(10)]
                                 )
        self.add_widget(self.data_table)
        return layout
    def load_manual_end_dialog(self):
        self.dialog = MDDialog(title="Информация о портфеле",
                               text="Дисперсии: s(x)^2 = {0:.4f}, ".format(self.dispersion_x) + "s(y)^2 = {0:.4f}".format(self.dispersion_y) + "\nСтандартные отклонения: s(x) = {0:.4f} млн. руб., ".format(self.standard_dev_x) + "s(y) = {0:.4f} млн. руб.".format(self.standard_dev_y) + "\nКоэффициент ковариации: K(xy) = {0:.4f}".format(self.cov_ratio) + "\nКоэффициент корреляции: r(xy) = {0:.2f}".format(self.cor_ratio) + "\nУравнение парной регрессии: y = {0:.4f}x + ".format(self.b) +  "{0:.3f}".format(self.a),
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()
    def load_manual_end_ready(self):
        self.dialog = MDDialog(title="Ваш портфель готов!",
                               text=self.lab_3,
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()
    def on_enter(self):
        self.load_manual_end()
        self.load_manual_end_ready()
    def on_leave(self, *args):
        self.data_table.clear_widgets()

class Manual_reb_1(Screen):
    sum = float(0)
    reb = []
    reb_stocks_prices = []
    lab = "Для ребалансировки портфеля понадобилось:\n"
    def load_manual_reb(self):
        self.sum = self.sum + (Manual_1.stocks_prices[0] * Manual_1.num[0])
        self.sum = self.sum + (Manual_2.stocks_prices[0] * Manual_2.num[0])
        self.sum = self.sum + (Manual_3.stocks_prices[0] * Manual_3.num[0])
        self.sum = self.sum + (Manual_4.stocks_prices[0] * Manual_4.num[0])
        self.sum = self.sum + (Manual_5.stocks_prices[0] * Manual_5.num[0])
        self.sum = self.sum + (Manual_6.stocks_prices[0] * Manual_6.num[0])
        self.sum = self.sum + (Manual_7.stocks_prices[0] * Manual_7.num[0])
        self.sum = self.sum + (Manual_8.stocks_prices[0] * Manual_8.num[0])
        self.sum = self.sum + (Manual_9.stocks_prices[0] * Manual_9.num[0])
        self.sum = self.sum + (Manual_10.stocks_prices[0] * Manual_10.num[0])
        layout = MDBoxLayout
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.575},
                                      size_hint=(0.9, 0.6),
                                      rows_num=10,
                                      column_data=[
                                          ("Номер акции", dp(40)),
                                          ("Стоимость акции", dp(40)),
                                          ("Количество активов", dp(40)),
                                          ("Доля из портфеля", dp(40)),
                                      ],
                                      row_data=[
                                          ('1', Manual_1.stocks_prices[0], "{0:.0f}".format(Manual_1.num[0]), "{0:.2f}".format(((Manual_1.stocks_prices[0]*Manual_1.num[0])/self.sum)*100) + "%",
                                           '2', Manual_2.stocks_prices[0], "{0:.0f}".format(Manual_2.num[0]), "{0:.2f}".format(((Manual_2.stocks_prices[0]*Manual_2.num[0])/self.sum)*100) + "%",
                                           '3', Manual_3.stocks_prices[0], "{0:.0f}".format(Manual_3.num[0]), "{0:.2f}".format(((Manual_3.stocks_prices[0]*Manual_3.num[0])/self.sum)*100) + "%",
                                           '4', Manual_4.stocks_prices[0], "{0:.0f}".format(Manual_4.num[0]), "{0:.2f}".format(((Manual_4.stocks_prices[0]*Manual_4.num[0])/self.sum)*100) + "%",
                                           '5', Manual_5.stocks_prices[0], "{0:.0f}".format(Manual_5.num[0]),
                                           "{0:.2f}".format(((Manual_5.stocks_prices[0]*Manual_5.num[0])/self.sum)*100) + "%",
                                           '6', Manual_6.stocks_prices[0], "{0:.0f}".format(Manual_6.num[0]),
                                           "{0:.2f}".format(((Manual_6.stocks_prices[0]*Manual_6.num[0])/self.sum)*100) + "%",
                                           '7', Manual_7.stocks_prices[0], "{0:.0f}".format(Manual_7.num[0]),
                                           "{0:.2f}".format(((Manual_7.stocks_prices[0]*Manual_7.num[0])/self.sum)*100) + "%",
                                           '8', Manual_8.stocks_prices[0], "{0:.0f}".format(Manual_8.num[0]),
                                           "{0:.2f}".format(((Manual_8.stocks_prices[0]*Manual_8.num[0])/self.sum)*100) + "%",
                                           '9', Manual_9.stocks_prices[0], "{0:.0f}".format(Manual_9.num[0]),
                                           "{0:.2f}".format(((Manual_9.stocks_prices[0]*Manual_9.num[0])/self.sum)*100) + "%",
                                           '10', Manual_10.stocks_prices[0], "{0:.0f}".format(Manual_10.num[0]),
                                           "{0:.2f}".format(((Manual_10.stocks_prices[0]*Manual_10.num[0])/self.sum)*100) + "%")
                                      ]
                                      )
        self.add_widget(self.data_table)
        return layout
    def on_enter(self):
        self.load_manual_reb()
    def on_leave(self, *args):
        self.data_table.clear_widgets()

class Manual_reb_2(Screen):
    reb = []
    reb_stocks_prices = []
    lab = "Для ребалансировки портфеля понадобилось:\n"
    def load_manual_reb(self):
        i = 0
        max_price = float(0)
        for i in range(10):
            self.reb.append(0)
        if ((Manual_1.stocks_prices[0]*Manual_1.num[0]) > max_price):
            max_price = Manual_1.stocks_prices[0]*Manual_1.num[0]
        if ((Manual_2.stocks_prices[0]*Manual_2.num[0]) > max_price):
            max_price = Manual_2.stocks_prices[0]*Manual_2.num[0]
        if ((Manual_3.stocks_prices[0]*Manual_3.num[0]) > max_price):
            max_price = Manual_3.stocks_prices[0]*Manual_3.num[0]
        if ((Manual_4.stocks_prices[0]*Manual_4.num[0]) > max_price):
            max_price = Manual_4.stocks_prices[0]*Manual_4.num[0]
        if ((Manual_5.stocks_prices[0]*Manual_5.num[0]) > max_price):
            max_price = Manual_5.stocks_prices[0]*Manual_5.num[0]
        if ((Manual_6.stocks_prices[0]*Manual_6.num[0]) > max_price):
            max_price = Manual_6.stocks_prices[0]*Manual_6.num[0]
        if ((Manual_7.stocks_prices[0]*Manual_7.num[0]) > max_price):
            max_price = Manual_7.stocks_prices[0]*Manual_7.num[0]
        if ((Manual_8.stocks_prices[0]*Manual_8.num[0]) > max_price):
            max_price = Manual_8.stocks_prices[0]*Manual_8.num[0]
        if ((Manual_9.stocks_prices[0]*Manual_9.num[0]) > max_price):
            max_price = Manual_9.stocks_prices[0]*Manual_9.num[0]
        if ((Manual_10.stocks_prices[0]*Manual_10.num[0]) > max_price):
            max_price = Manual_10.stocks_prices[0]*Manual_10.num[0]
        self.reb_stocks_prices.append(Manual_1.stocks_prices[0])
        self.reb_stocks_prices.append(Manual_2.stocks_prices[0])
        self.reb_stocks_prices.append(Manual_3.stocks_prices[0])
        self.reb_stocks_prices.append(Manual_4.stocks_prices[0])
        self.reb_stocks_prices.append(Manual_5.stocks_prices[0])
        self.reb_stocks_prices.append(Manual_6.stocks_prices[0])
        self.reb_stocks_prices.append(Manual_7.stocks_prices[0])
        self.reb_stocks_prices.append(Manual_8.stocks_prices[0])
        self.reb_stocks_prices.append(Manual_9.stocks_prices[0])
        self.reb_stocks_prices.append(Manual_10.stocks_prices[0])
        while (self.reb_stocks_prices[0] < max_price):
            self.reb_stocks_prices[0] = self.reb_stocks_prices[0] + Manual_1.stocks_prices[0]
            self.reb[0] = self.reb[0] + 1
        while (self.reb_stocks_prices[1] < max_price):
            self.reb_stocks_prices[1] = self.reb_stocks_prices[1] + Manual_2.stocks_prices[0]
            self.reb[1] = self.reb[1] + 1
        while (self.reb_stocks_prices[2] < max_price):
            self.reb_stocks_prices[2] = self.reb_stocks_prices[2] + Manual_3.stocks_prices[0]
            self.reb[2] = self.reb[2] + 1
        while (self.reb_stocks_prices[3] < max_price):
            self.reb_stocks_prices[3] = self.reb_stocks_prices[3] + Manual_4.stocks_prices[0]
            self.reb[3] = self.reb[3] + 1
        while (self.reb_stocks_prices[4] < max_price):
            self.reb_stocks_prices[4] = self.reb_stocks_prices[4] + Manual_5.stocks_prices[0]
            self.reb[4] = self.reb[4] + 1
        while (self.reb_stocks_prices[5] < max_price):
            self.reb_stocks_prices[5] = self.reb_stocks_prices[5] + Manual_6.stocks_prices[0]
            self.reb[5] = self.reb[5] + 1
        while (self.reb_stocks_prices[6] < max_price):
            self.reb_stocks_prices[6] = self.reb_stocks_prices[6] + Manual_7.stocks_prices[0]
            self.reb[6] = self.reb[6] + 1
        while (self.reb_stocks_prices[7] < max_price):
            self.reb_stocks_prices[7] = self.reb_stocks_prices[7] + Manual_8.stocks_prices[0]
            self.reb[7] = self.reb[7] + 1
        while (self.reb_stocks_prices[8] < max_price):
            self.reb_stocks_prices[8] = self.reb_stocks_prices[8] + Manual_9.stocks_prices[0]
            self.reb[8] = self.reb[8] + 1
        while (self.reb_stocks_prices[9] < max_price):
            self.reb_stocks_prices[9] = self.reb_stocks_prices[9] + Manual_10.stocks_prices[0]
            self.reb[9] = self.reb[9] + 1
        i = 0
        for i in range(10):
            if (self.reb[i] > 0):
                self.lab = self.lab + "- докупить акцию №" + str(i + 1) + " ещё " + str(self.reb[i]) + " раз(а)"
                if (i == 9):
                    self.lab = self.lab + "."
                else:
                    self.lab = self.lab + ";\n"
        layout = MDBoxLayout
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.575},
                                      size_hint=(0.9, 0.6),
                                      rows_num=10,
                                      column_data=[
                                          ("Номер акции", dp(30)),
                                          ("Исходная стоимость акции", dp(30)),
                                          ("Количество активов", dp(30)),
                                          ("Общая стоимость", dp(30)),
                                          ("Ребалансировання стоимость акции", dp(30)),
                                      ],
                                      row_data=[
                                          ('1', Manual_1.stocks_prices[0], "{0:.0f}".format(Manual_1.num[0]), "{0:.0f}".format(Manual_1.stocks_prices[0]*Manual_1.num[0]), self.reb_stocks_prices[0],
                                           '2', Manual_2.stocks_prices[0], "{0:.0f}".format(Manual_2.num[0]), "{0:.0f}".format(Manual_2.stocks_prices[0]*Manual_2.num[0]), self.reb_stocks_prices[1],
                                           '3', Manual_3.stocks_prices[0], "{0:.0f}".format(Manual_3.num[0]), "{0:.0f}".format(Manual_3.stocks_prices[0]*Manual_3.num[0]), self.reb_stocks_prices[2],
                                           '4', Manual_4.stocks_prices[0], "{0:.0f}".format(Manual_4.num[0]), "{0:.0f}".format(Manual_4.stocks_prices[0]*Manual_4.num[0]), self.reb_stocks_prices[3],
                                           '5', Manual_5.stocks_prices[0], "{0:.0f}".format(Manual_5.num[0]), "{0:.0f}".format(Manual_5.stocks_prices[0]*Manual_5.num[0]), self.reb_stocks_prices[4],
                                           '6', Manual_6.stocks_prices[0], "{0:.0f}".format(Manual_6.num[0]), "{0:.0f}".format(Manual_6.stocks_prices[0]*Manual_6.num[0]), self.reb_stocks_prices[5],
                                           '7', Manual_7.stocks_prices[0], "{0:.0f}".format(Manual_7.num[0]), "{0:.0f}".format(Manual_7.stocks_prices[0]*Manual_7.num[0]), self.reb_stocks_prices[6],
                                           '8', Manual_8.stocks_prices[0], "{0:.0f}".format(Manual_8.num[0]), "{0:.0f}".format(Manual_8.stocks_prices[0]*Manual_8.num[0]), self.reb_stocks_prices[7],
                                           '9', Manual_9.stocks_prices[0], "{0:.0f}".format(Manual_9.num[0]), "{0:.0f}".format(Manual_9.stocks_prices[0]*Manual_9.num[0]), self.reb_stocks_prices[8],
                                           '10', Manual_10.stocks_prices[0], "{0:.0f}".format(Manual_10.num[0]), "{0:.0f}".format(Manual_10.stocks_prices[0]*Manual_10.num[0]),self.reb_stocks_prices[9])
                                      ]
                                      )
        self.add_widget(self.data_table)
        return layout
    def load_manual_reb_dialog(self):
        self.dialog = MDDialog(title="Информация о ребалансировке",
                               text=self.lab,
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()
    def on_enter(self):
        self.load_manual_reb()
    def leave(self, *args):
        self.data_table.clear_widgets()
        Manual_1.days = []
        Manual_2.days = []
        Manual_3.days = []
        Manual_4.days = []
        Manual_5.days = []
        Manual_6.days = []
        Manual_7.days = []
        Manual_8.days = []
        Manual_9.days = []
        Manual_10.days = []
        Manual_1.stocks_prices = []
        Manual_2.stocks_prices = []
        Manual_3.stocks_prices = []
        Manual_4.stocks_prices = []
        Manual_5.stocks_prices = []
        Manual_6.stocks_prices = []
        Manual_7.stocks_prices = []
        Manual_8.stocks_prices = []
        Manual_9.stocks_prices = []
        Manual_10.stocks_prices = []
        Manual_1.divs_dif = []
        Manual_2.divs_dif = []
        Manual_3.divs_dif = []
        Manual_4.divs_dif = []
        Manual_5.divs_dif = []
        Manual_6.divs_dif = []
        Manual_7.divs_dif = []
        Manual_8.divs_dif = []
        Manual_9.divs_dif = []
        Manual_10.divs_dif = []
        Manual_1.prices_dif = []
        Manual_2.prices_dif = []
        Manual_3.prices_dif = []
        Manual_4.prices_dif = []
        Manual_5.prices_dif = []
        Manual_6.prices_dif = []
        Manual_7.prices_dif = []
        Manual_8.prices_dif = []
        Manual_9.prices_dif = []
        Manual_10.prices_dif = []
        Manual_1.dif = []
        Manual_2.dif = []
        Manual_3.dif = []
        Manual_4.dif = []
        Manual_5.dif = []
        Manual_6.dif = []
        Manual_7.dif = []
        Manual_8.dif = []
        Manual_9.dif = []
        Manual_10.dif = []
        Manual_1.divs_dif_2 = []
        Manual_2.divs_dif_2 = []
        Manual_3.divs_dif_2 = []
        Manual_4.divs_dif_2 = []
        Manual_5.divs_dif_2 = []
        Manual_6.divs_dif_2 = []
        Manual_7.divs_dif_2 = []
        Manual_8.divs_dif_2 = []
        Manual_9.divs_dif_2 = []
        Manual_10.divs_dif_2 = []
        Manual_1.prices_dif_2 = []
        Manual_2.prices_dif_2 = []
        Manual_3.prices_dif_2 = []
        Manual_4.prices_dif_2 = []
        Manual_5.prices_dif_2 = []
        Manual_6.prices_dif_2 = []
        Manual_7.prices_dif_2 = []
        Manual_8.prices_dif_2 = []
        Manual_9.prices_dif_2 = []
        Manual_10.prices_dif_2 = []
        Manual_1.reb = []
        Manual_2.reb = []
        Manual_3.reb = []
        Manual_4.reb = []
        Manual_5.reb = []
        Manual_6.reb = []
        Manual_7.reb = []
        Manual_8.reb = []
        Manual_9.reb = []
        Manual_10.reb = []
        Manual_1.reb_stocks_prices = []
        Manual_2.reb_stocks_prices = []
        Manual_3.reb_stocks_prices = []
        Manual_4.reb_stocks_prices = []
        Manual_5.reb_stocks_prices = []
        Manual_6.reb_stocks_prices = []
        Manual_7.reb_stocks_prices = []
        Manual_8.reb_stocks_prices = []
        Manual_9.reb_stocks_prices = []
        Manual_10.reb_stocks_prices = []
        Manual_1.num = []
        Manual_2.num = []
        Manual_3.num = []
        Manual_4.num = []
        Manual_5.num = []
        Manual_6.num = []
        Manual_7.num = []
        Manual_8.num = []
        Manual_9.num = []
        Manual_10.num = []
        self.dispersion_x = float(0)
        self.dispersion_y = float(0)
        self.standard_dev_x = float(0)
        self.standard_dev_y = float(0)
        self.cov_ratio = float(0)
        self.cor_ratio = float(0)
        self.b = float(0)
        self.a = float(0)
        self.x = 0
        self.y = 0
        self.lab_1 = ""
        self.lab_2 = ""
        self.lab_3 = ""
        self.reb = []
        self.reb_stocks_prices = []
        self.lab = "Для ребалансировки портфеля понадобилось:\n"
        self.manager.current = 'choice'

class Auto(Screen):
    num = []
    def input(self):
        if ((self.ids.field_1.text != '') and (self.ids.field_2.text != '') and (self.ids.field_3.text != '') and (self.ids.field_4.text != '') and (self.ids.field_5.text != '') and (self.ids.field_6.text != '') and (self.ids.field_7.text != '') and (self.ids.field_8.text != '') and (self.ids.field_9.text != '') and (self.ids.field_10.text != '')):
            self.num.append(float(self.ids.field_1.text))
            self.num.append(float(self.ids.field_2.text))
            self.num.append(float(self.ids.field_3.text))
            self.num.append(float(self.ids.field_4.text))
            self.num.append(float(self.ids.field_5.text))
            self.num.append(float(self.ids.field_6.text))
            self.num.append(float(self.ids.field_7.text))
            self.num.append(float(self.ids.field_8.text))
            self.num.append(float(self.ids.field_9.text))
            self.num.append(float(self.ids.field_10.text))
            self.manager.current = 'auto_end_1'
        else:
            self.dialog = MDDialog(title="Ошибка",
                               text="Данные введены некорректно или отсутствуют",
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
            self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()
    def clear(self, *args):
        self.num = []

class Auto_end_1(Screen):
    days = []
    stocks_prices = []
    divs_dif = []
    prices_dif = []
    dif = []
    divs_dif_2 = []
    prices_dif_2 = []
    dispersion_x = float(0)
    dispersion_y = float(0)
    standard_dev_x = float(0)
    standard_dev_y = float(0)
    cov_ratio = float(0)
    cor_ratio = float(0)
    b = float(0)
    a = float(0)
    x = 0
    y = 0
    def load_auto_end(self):
        base_url = "http://iss.moex.com/iss/history/engines/stock/markets/index/boards/SNDX/securities.json"
        response = requests.get(base_url)
        result = json.loads(response.text)
        col_name = result['history']['columns']
        data_index = pd.DataFrame(columns=col_name)
        url_index = 'http://iss.moex.com/iss/history/engines/stock/markets/index/boards/SNDX/securities/imoex.json'
        response = requests.get(url_index)
        result = json.loads(response.text)
        resp_date = result['history']['data']
        data_index = pd.DataFrame(resp_date, columns=col_name)
        z1 = len(resp_date)
        z2 = 100
        while z1 == 100:
            url_opt = '?start=' + str(z2)
            url_next_page = (url_index + url_opt)
            response = requests.get(url_next_page)
            result = json.loads(response.text)
            resp_date = result['history']['data']
            data_next_page = pd.DataFrame(resp_date, columns=col_name)
            data_index = pd.concat([data_index, data_next_page], ignore_index=True)
            z1 = len(resp_date)
            z2 = z2 + 100
        i = int(0)
        for i in range(10):
            self.days.append(float(i + 1))
        for i in range(0,10):
            self.stocks_prices.append(float(resp_date[len(resp_date) - (i+1)][6]))
        average_day = float(0.0)
        average_stocks_price = float(0.0)
        for i in range(10):
            average_day = average_day + self.days[i]
            average_stocks_price = average_stocks_price + self.stocks_prices[i]
        average_stocks_price = average_stocks_price / 10
        average_day = average_day / 10
        i = 0
        for i in range(10):
            self.divs_dif.append(float(self.days[i] - average_day))
            self.prices_dif.append(float(self.stocks_prices[i] - average_stocks_price))
            self.dif.append(float(self.divs_dif[i] * self.prices_dif[i]))
            self.divs_dif_2.append(float(self.divs_dif[i] * self.divs_dif[i]))
            self.prices_dif_2.append(float(self.prices_dif[i] * self.prices_dif[i]))
        i = 0
        for i in range(10):
            self.dispersion_x = self.dispersion_x + self.divs_dif_2[i]
            self.dispersion_y = self.dispersion_y + self.prices_dif_2[i]
        self.dispersion_x = self.dispersion_x / 10
        self.dispersion_y = self.dispersion_y / 10
        self.standard_dev_x = float(math.sqrt(self.dispersion_x / 10))
        self.standard_dev_y = float(math.sqrt(self.dispersion_y / 10))
        i = 0
        for i in range(10):
            self.cov_ratio = self.cov_ratio + self.dif[i]
        self.cov_ratio = self.cov_ratio / 10
        self.cor_ratio = self.cov_ratio / (math.sqrt(self.dispersion_x) * math.sqrt(self.dispersion_y))
        self.b = float((self.cor_ratio * self.standard_dev_y) / self.standard_dev_x)
        self.a = float(average_stocks_price - (self.b * average_day))
        if (self.b > 0):
            self.lab_1 = "Сигнал тренда: ПОКУПАТЬ"
        elif (self.b < 0):
            self.x = 1
            self.lab_1 = "Сигнал тренда: ПРОДАВАТЬ"
        else:
            self.x = 2
            self.lab_1 = "Сигнал тренда: СТОЯТЬ"
        if (self.cor_ratio > 0.7):
            self.lab_2 = "Сигнал доверия: ПОКУПАТЬ"
        elif (self.cor_ratio < (-0.7)):
            self.y = 1
            self.lab_2 = "Сигнал доверия: ПРОДАВАТЬ"
        else:
            self.y = 2
            self.lab_2 = "Сигнал доверия: СТОЯТЬ"
        if (self.x == self.y):
            self.lab_3 = "Итоговая рекомендация робота: ПОКУПАТЬ"
        else:
            self.lab_3 = "Итоговая рекомендация робота: СТОЯТЬ"
        layout = MDBoxLayout
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.575},
                                      size_hint=(0.9, 0.6),
                                      rows_num=10,
                                      column_data=[
                                          ("День (x)", dp(15)),
                                          ("Стоимость акции (y)", dp(20)),
                                          ("x-x(ср)", dp(15)),
                                          ("y-y(ср)", dp(20)),
                                          ("(x-x(ср))(y-y(ср))", dp(30)),
                                          ("x-x(ср)^2", dp(30)),
                                          ("y-y(ср)^2", dp(30))
                                      ],
                                      row_data=[
                                          ("{0:.0f}".format(self.days[i]),
                                           "{0:.2f}".format(self.stocks_prices[i]), self.divs_dif[i],
                                           self.prices_dif[i], self.dif[i], self.divs_dif_2[i],
                                           self.prices_dif_2[i])
                                          for i in range(10)]
                                      )
        self.add_widget(self.data_table)
        return layout

    def load_auto_end_dialog(self):
        self.dialog = MDDialog(title="Информация об акции",
                               text="Дисперсии: s(x)^2 = {0:.4f}, ".format(
                                   self.dispersion_x) + "s(y)^2 = {0:.4f}".format(
                                   self.dispersion_y) + "\nСтандартные отклонения: s(x) = {0:.4f} млн. руб., ".format(
                                   self.standard_dev_x) + "s(y) = {0:.4f} млн. руб.".format(
                                   self.standard_dev_y) + "\nКоэффициент ковариации: K(xy) = {0:.4f}".format(
                                   self.cov_ratio) + "\nКоэффициент корреляции: r(xy) = {0:.2f}".format(
                                   self.cor_ratio) + "\nУравнение парной регрессии: y = {0:.4f}x + ".format(
                                   self.b) + "{0:.3f}".format(self.a),
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()

    def load_auto_end_ready(self):
        self.dialog = MDDialog(title=" ",
                               text=self.lab_3,
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def on_enter(self):
        self.load_auto_end()
        self.load_auto_end_ready()

    def on_leave(self, *args):
        self.data_table.clear_widgets()

class Auto_end_2(Screen):
    days = []
    stocks_prices = []
    divs_dif = []
    prices_dif = []
    dif = []
    divs_dif_2 = []
    prices_dif_2 = []
    dispersion_x = float(0)
    dispersion_y = float(0)
    standard_dev_x = float(0)
    standard_dev_y = float(0)
    cov_ratio = float(0)
    cor_ratio = float(0)
    b = float(0)
    a = float(0)
    x = 0
    y = 0
    def load_auto_end(self):
        base_url = "http://iss.moex.com/iss/history/engines/stock/markets/index/boards/SNDX/securities.json"
        response = requests.get(base_url)
        result = json.loads(response.text)
        col_name = result['history']['columns']
        data_index = pd.DataFrame(columns=col_name)
        url_index = 'http://iss.moex.com/iss/history/engines/stock/markets/index/boards/SNDX/securities/imoex.json'
        response = requests.get(url_index)
        result = json.loads(response.text)
        resp_date = result['history']['data']
        data_index = pd.DataFrame(resp_date, columns=col_name)
        z1 = len(resp_date)
        z2 = 100
        while z1 == 100:
            url_opt = '?start=' + str(z2)
            url_next_page = (url_index + url_opt)
            response = requests.get(url_next_page)
            result = json.loads(response.text)
            resp_date = result['history']['data']
            data_next_page = pd.DataFrame(resp_date, columns=col_name)
            data_index = pd.concat([data_index, data_next_page], ignore_index=True)
            z1 = len(resp_date)
            z2 = z2 + 100
        i = int(0)
        for i in range(10):
            self.days.append(float(i + 1))
        for i in range(10,20):
            self.stocks_prices.append(float(resp_date[len(resp_date) - (i+1)][6]))
        average_day = float(0.0)
        average_stocks_price = float(0.0)
        for i in range(10):
            average_day = average_day + self.days[i]
            average_stocks_price = average_stocks_price + self.stocks_prices[i]
        average_stocks_price = average_stocks_price / 10
        average_day = average_day / 10
        i = 0
        for i in range(10):
            self.divs_dif.append(float(self.days[i] - average_day))
            self.prices_dif.append(float(self.stocks_prices[i] - average_stocks_price))
            self.dif.append(float(self.divs_dif[i] * self.prices_dif[i]))
            self.divs_dif_2.append(float(self.divs_dif[i] * self.divs_dif[i]))
            self.prices_dif_2.append(float(self.prices_dif[i] * self.prices_dif[i]))
        i = 0
        for i in range(10):
            self.dispersion_x = self.dispersion_x + self.divs_dif_2[i]
            self.dispersion_y = self.dispersion_y + self.prices_dif_2[i]
        self.dispersion_x = self.dispersion_x / 10
        self.dispersion_y = self.dispersion_y / 10
        self.standard_dev_x = float(math.sqrt(self.dispersion_x / 10))
        self.standard_dev_y = float(math.sqrt(self.dispersion_y / 10))
        i = 0
        for i in range(10):
            self.cov_ratio = self.cov_ratio + self.dif[i]
        self.cov_ratio = self.cov_ratio / 10
        self.cor_ratio = self.cov_ratio / (math.sqrt(self.dispersion_x) * math.sqrt(self.dispersion_y))
        self.b = float((self.cor_ratio * self.standard_dev_y) / self.standard_dev_x)
        self.a = float(average_stocks_price - (self.b * average_day))
        if (self.b > 0):
            self.lab_1 = "Сигнал тренда: ПОКУПАТЬ"
        elif (self.b < 0):
            self.x = 1
            self.lab_1 = "Сигнал тренда: ПРОДАВАТЬ"
        else:
            self.x = 2
            self.lab_1 = "Сигнал тренда: СТОЯТЬ"
        if (self.cor_ratio > 0.7):
            self.lab_2 = "Сигнал доверия: ПОКУПАТЬ"
        elif (self.cor_ratio < (-0.7)):
            self.y = 1
            self.lab_2 = "Сигнал доверия: ПРОДАВАТЬ"
        else:
            self.y = 2
            self.lab_2 = "Сигнал доверия: СТОЯТЬ"
        if (self.x == self.y):
            self.lab_3 = "Итоговая рекомендация робота: ПОКУПАТЬ"
        else:
            self.lab_3 = "Итоговая рекомендация робота: СТОЯТЬ"
        layout = MDBoxLayout
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.575},
                                      size_hint=(0.9, 0.6),
                                      rows_num=10,
                                      column_data=[
                                          ("День (x)", dp(15)),
                                          ("Стоимость акции (y)", dp(20)),
                                          ("x-x(ср)", dp(15)),
                                          ("y-y(ср)", dp(20)),
                                          ("(x-x(ср))(y-y(ср))", dp(30)),
                                          ("x-x(ср)^2", dp(30)),
                                          ("y-y(ср)^2", dp(30))
                                      ],
                                      row_data=[
                                          ("{0:.0f}".format(self.days[i]),
                                           "{0:.2f}".format(self.stocks_prices[i]), self.divs_dif[i],
                                           self.prices_dif[i], self.dif[i], self.divs_dif_2[i],
                                           self.prices_dif_2[i])
                                          for i in range(10)]
                                      )
        self.add_widget(self.data_table)
        return layout

    def load_auto_end_dialog(self):
        self.dialog = MDDialog(title="Информация об акции",
                               text="Дисперсии: s(x)^2 = {0:.4f}, ".format(
                                   self.dispersion_x) + "s(y)^2 = {0:.4f}".format(
                                   self.dispersion_y) + "\nСтандартные отклонения: s(x) = {0:.4f} млн. руб., ".format(
                                   self.standard_dev_x) + "s(y) = {0:.4f} млн. руб.".format(
                                   self.standard_dev_y) + "\nКоэффициент ковариации: K(xy) = {0:.4f}".format(
                                   self.cov_ratio) + "\nКоэффициент корреляции: r(xy) = {0:.2f}".format(
                                   self.cor_ratio) + "\nУравнение парной регрессии: y = {0:.4f}x + ".format(
                                   self.b) + "{0:.3f}".format(self.a),
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()

    def load_auto_end_ready(self):
        self.dialog = MDDialog(title=" ",
                               text=self.lab_3,
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def on_enter(self):
        self.load_auto_end()
        self.load_auto_end_ready()

    def on_leave(self, *args):
        self.data_table.clear_widgets()

class Auto_end_3(Screen):
    days = []
    stocks_prices = []
    divs_dif = []
    prices_dif = []
    dif = []
    divs_dif_2 = []
    prices_dif_2 = []
    dispersion_x = float(0)
    dispersion_y = float(0)
    standard_dev_x = float(0)
    standard_dev_y = float(0)
    cov_ratio = float(0)
    cor_ratio = float(0)
    b = float(0)
    a = float(0)
    x = 0
    y = 0
    def load_auto_end(self):
        base_url = "http://iss.moex.com/iss/history/engines/stock/markets/index/boards/SNDX/securities.json"
        response = requests.get(base_url)
        result = json.loads(response.text)
        col_name = result['history']['columns']
        data_index = pd.DataFrame(columns=col_name)
        url_index = 'http://iss.moex.com/iss/history/engines/stock/markets/index/boards/SNDX/securities/imoex.json'
        response = requests.get(url_index)
        result = json.loads(response.text)
        resp_date = result['history']['data']
        data_index = pd.DataFrame(resp_date, columns=col_name)
        z1 = len(resp_date)
        z2 = 100
        while z1 == 100:
            url_opt = '?start=' + str(z2)
            url_next_page = (url_index + url_opt)
            response = requests.get(url_next_page)
            result = json.loads(response.text)
            resp_date = result['history']['data']
            data_next_page = pd.DataFrame(resp_date, columns=col_name)
            data_index = pd.concat([data_index, data_next_page], ignore_index=True)
            z1 = len(resp_date)
            z2 = z2 + 100
        i = int(0)
        for i in range(10):
            self.days.append(float(i + 1))
        for i in range(20,30):
            self.stocks_prices.append(float(resp_date[len(resp_date) - (i+1)][6]))
        average_day = float(0.0)
        average_stocks_price = float(0.0)
        for i in range(10):
            average_day = average_day + self.days[i]
            average_stocks_price = average_stocks_price + self.stocks_prices[i]
        average_stocks_price = average_stocks_price / 10
        average_day = average_day / 10
        i = 0
        for i in range(10):
            self.divs_dif.append(float(self.days[i] - average_day))
            self.prices_dif.append(float(self.stocks_prices[i] - average_stocks_price))
            self.dif.append(float(self.divs_dif[i] * self.prices_dif[i]))
            self.divs_dif_2.append(float(self.divs_dif[i] * self.divs_dif[i]))
            self.prices_dif_2.append(float(self.prices_dif[i] * self.prices_dif[i]))
        i = 0
        for i in range(10):
            self.dispersion_x = self.dispersion_x + self.divs_dif_2[i]
            self.dispersion_y = self.dispersion_y + self.prices_dif_2[i]
        self.dispersion_x = self.dispersion_x / 10
        self.dispersion_y = self.dispersion_y / 10
        self.standard_dev_x = float(math.sqrt(self.dispersion_x / 10))
        self.standard_dev_y = float(math.sqrt(self.dispersion_y / 10))
        i = 0
        for i in range(10):
            self.cov_ratio = self.cov_ratio + self.dif[i]
        self.cov_ratio = self.cov_ratio / 10
        self.cor_ratio = self.cov_ratio / (math.sqrt(self.dispersion_x) * math.sqrt(self.dispersion_y))
        self.b = float((self.cor_ratio * self.standard_dev_y) / self.standard_dev_x)
        self.a = float(average_stocks_price - (self.b * average_day))
        if (self.b > 0):
            self.lab_1 = "Сигнал тренда: ПОКУПАТЬ"
        elif (self.b < 0):
            self.x = 1
            self.lab_1 = "Сигнал тренда: ПРОДАВАТЬ"
        else:
            self.x = 2
            self.lab_1 = "Сигнал тренда: СТОЯТЬ"
        if (self.cor_ratio > 0.7):
            self.lab_2 = "Сигнал доверия: ПОКУПАТЬ"
        elif (self.cor_ratio < (-0.7)):
            self.y = 1
            self.lab_2 = "Сигнал доверия: ПРОДАВАТЬ"
        else:
            self.y = 2
            self.lab_2 = "Сигнал доверия: СТОЯТЬ"
        if (self.x == self.y):
            self.lab_3 = "Итоговая рекомендация робота: ПОКУПАТЬ"
        else:
            self.lab_3 = "Итоговая рекомендация робота: СТОЯТЬ"
        layout = MDBoxLayout
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.575},
                                      size_hint=(0.9, 0.6),
                                      rows_num=10,
                                      column_data=[
                                          ("День (x)", dp(15)),
                                          ("Стоимость акции (y)", dp(20)),
                                          ("x-x(ср)", dp(15)),
                                          ("y-y(ср)", dp(20)),
                                          ("(x-x(ср))(y-y(ср))", dp(30)),
                                          ("x-x(ср)^2", dp(30)),
                                          ("y-y(ср)^2", dp(30))
                                      ],
                                      row_data=[
                                          ("{0:.0f}".format(self.days[i]),
                                           "{0:.2f}".format(self.stocks_prices[i]), self.divs_dif[i],
                                           self.prices_dif[i], self.dif[i], self.divs_dif_2[i],
                                           self.prices_dif_2[i])
                                          for i in range(10)]
                                      )
        self.add_widget(self.data_table)
        return layout

    def load_auto_end_dialog(self):
        self.dialog = MDDialog(title="Информация об акции",
                               text="Дисперсии: s(x)^2 = {0:.4f}, ".format(
                                   self.dispersion_x) + "s(y)^2 = {0:.4f}".format(
                                   self.dispersion_y) + "\nСтандартные отклонения: s(x) = {0:.4f} млн. руб., ".format(
                                   self.standard_dev_x) + "s(y) = {0:.4f} млн. руб.".format(
                                   self.standard_dev_y) + "\nКоэффициент ковариации: K(xy) = {0:.4f}".format(
                                   self.cov_ratio) + "\nКоэффициент корреляции: r(xy) = {0:.2f}".format(
                                   self.cor_ratio) + "\nУравнение парной регрессии: y = {0:.4f}x + ".format(
                                   self.b) + "{0:.3f}".format(self.a),
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()

    def load_auto_end_ready(self):
        self.dialog = MDDialog(title=" ",
                               text=self.lab_3,
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def on_enter(self):
        self.load_auto_end()
        self.load_auto_end_ready()

    def on_leave(self, *args):
        self.data_table.clear_widgets()

class Auto_end_4(Screen):
    days = []
    stocks_prices = []
    divs_dif = []
    prices_dif = []
    dif = []
    divs_dif_2 = []
    prices_dif_2 = []
    dispersion_x = float(0)
    dispersion_y = float(0)
    standard_dev_x = float(0)
    standard_dev_y = float(0)
    cov_ratio = float(0)
    cor_ratio = float(0)
    b = float(0)
    a = float(0)
    x = 0
    y = 0
    def load_auto_end(self):
        base_url = "http://iss.moex.com/iss/history/engines/stock/markets/index/boards/SNDX/securities.json"
        response = requests.get(base_url)
        result = json.loads(response.text)
        col_name = result['history']['columns']
        data_index = pd.DataFrame(columns=col_name)
        url_index = 'http://iss.moex.com/iss/history/engines/stock/markets/index/boards/SNDX/securities/imoex.json'
        response = requests.get(url_index)
        result = json.loads(response.text)
        resp_date = result['history']['data']
        data_index = pd.DataFrame(resp_date, columns=col_name)
        z1 = len(resp_date)
        z2 = 100
        while z1 == 100:
            url_opt = '?start=' + str(z2)
            url_next_page = (url_index + url_opt)
            response = requests.get(url_next_page)
            result = json.loads(response.text)
            resp_date = result['history']['data']
            data_next_page = pd.DataFrame(resp_date, columns=col_name)
            data_index = pd.concat([data_index, data_next_page], ignore_index=True)
            z1 = len(resp_date)
            z2 = z2 + 100
        i = int(0)
        for i in range(10):
            self.days.append(float(i + 1))
        for i in range(30,40):
            self.stocks_prices.append(float(resp_date[len(resp_date) - (i+1)][6]))
        average_day = float(0.0)
        average_stocks_price = float(0.0)
        for i in range(10):
            average_day = average_day + self.days[i]
            average_stocks_price = average_stocks_price + self.stocks_prices[i]
        average_stocks_price = average_stocks_price / 10
        average_day = average_day / 10
        i = 0
        for i in range(10):
            self.divs_dif.append(float(self.days[i] - average_day))
            self.prices_dif.append(float(self.stocks_prices[i] - average_stocks_price))
            self.dif.append(float(self.divs_dif[i] * self.prices_dif[i]))
            self.divs_dif_2.append(float(self.divs_dif[i] * self.divs_dif[i]))
            self.prices_dif_2.append(float(self.prices_dif[i] * self.prices_dif[i]))
        i = 0
        for i in range(10):
            self.dispersion_x = self.dispersion_x + self.divs_dif_2[i]
            self.dispersion_y = self.dispersion_y + self.prices_dif_2[i]
        self.dispersion_x = self.dispersion_x / 10
        self.dispersion_y = self.dispersion_y / 10
        self.standard_dev_x = float(math.sqrt(self.dispersion_x / 10))
        self.standard_dev_y = float(math.sqrt(self.dispersion_y / 10))
        i = 0
        for i in range(10):
            self.cov_ratio = self.cov_ratio + self.dif[i]
        self.cov_ratio = self.cov_ratio / 10
        self.cor_ratio = self.cov_ratio / (math.sqrt(self.dispersion_x) * math.sqrt(self.dispersion_y))
        self.b = float((self.cor_ratio * self.standard_dev_y) / self.standard_dev_x)
        self.a = float(average_stocks_price - (self.b * average_day))
        if (self.b > 0):
            self.lab_1 = "Сигнал тренда: ПОКУПАТЬ"
        elif (self.b < 0):
            self.x = 1
            self.lab_1 = "Сигнал тренда: ПРОДАВАТЬ"
        else:
            self.x = 2
            self.lab_1 = "Сигнал тренда: СТОЯТЬ"
        if (self.cor_ratio > 0.7):
            self.lab_2 = "Сигнал доверия: ПОКУПАТЬ"
        elif (self.cor_ratio < (-0.7)):
            self.y = 1
            self.lab_2 = "Сигнал доверия: ПРОДАВАТЬ"
        else:
            self.y = 2
            self.lab_2 = "Сигнал доверия: СТОЯТЬ"
        if (self.x == self.y):
            self.lab_3 = "Итоговая рекомендация робота: ПОКУПАТЬ"
        else:
            self.lab_3 = "Итоговая рекомендация робота: СТОЯТЬ"
        layout = MDBoxLayout
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.575},
                                      size_hint=(0.9, 0.6),
                                      rows_num=10,
                                      column_data=[
                                          ("День (x)", dp(15)),
                                          ("Стоимость акции (y)", dp(20)),
                                          ("x-x(ср)", dp(15)),
                                          ("y-y(ср)", dp(20)),
                                          ("(x-x(ср))(y-y(ср))", dp(30)),
                                          ("x-x(ср)^2", dp(30)),
                                          ("y-y(ср)^2", dp(30))
                                      ],
                                      row_data=[
                                          ("{0:.0f}".format(self.days[i]),
                                           "{0:.2f}".format(self.stocks_prices[i]), self.divs_dif[i],
                                           self.prices_dif[i], self.dif[i], self.divs_dif_2[i],
                                           self.prices_dif_2[i])
                                          for i in range(10)]
                                      )
        self.add_widget(self.data_table)
        return layout

    def load_auto_end_dialog(self):
        self.dialog = MDDialog(title="Информация об акции",
                               text="Дисперсии: s(x)^2 = {0:.4f}, ".format(
                                   self.dispersion_x) + "s(y)^2 = {0:.4f}".format(
                                   self.dispersion_y) + "\nСтандартные отклонения: s(x) = {0:.4f} млн. руб., ".format(
                                   self.standard_dev_x) + "s(y) = {0:.4f} млн. руб.".format(
                                   self.standard_dev_y) + "\nКоэффициент ковариации: K(xy) = {0:.4f}".format(
                                   self.cov_ratio) + "\nКоэффициент корреляции: r(xy) = {0:.2f}".format(
                                   self.cor_ratio) + "\nУравнение парной регрессии: y = {0:.4f}x + ".format(
                                   self.b) + "{0:.3f}".format(self.a),
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()

    def load_auto_end_ready(self):
        self.dialog = MDDialog(title=" ",
                               text=self.lab_3,
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def on_enter(self):
        self.load_auto_end()
        self.load_auto_end_ready()

    def on_leave(self, *args):
        self.data_table.clear_widgets()

class Auto_end_5(Screen):
    days = []
    stocks_prices = []
    divs_dif = []
    prices_dif = []
    dif = []
    divs_dif_2 = []
    prices_dif_2 = []
    dispersion_x = float(0)
    dispersion_y = float(0)
    standard_dev_x = float(0)
    standard_dev_y = float(0)
    cov_ratio = float(0)
    cor_ratio = float(0)
    b = float(0)
    a = float(0)
    x = 0
    y = 0
    def load_auto_end(self):
        base_url = "http://iss.moex.com/iss/history/engines/stock/markets/index/boards/SNDX/securities.json"
        response = requests.get(base_url)
        result = json.loads(response.text)
        col_name = result['history']['columns']
        data_index = pd.DataFrame(columns=col_name)
        url_index = 'http://iss.moex.com/iss/history/engines/stock/markets/index/boards/SNDX/securities/imoex.json'
        response = requests.get(url_index)
        result = json.loads(response.text)
        resp_date = result['history']['data']
        data_index = pd.DataFrame(resp_date, columns=col_name)
        z1 = len(resp_date)
        z2 = 100
        while z1 == 100:
            url_opt = '?start=' + str(z2)
            url_next_page = (url_index + url_opt)
            response = requests.get(url_next_page)
            result = json.loads(response.text)
            resp_date = result['history']['data']
            data_next_page = pd.DataFrame(resp_date, columns=col_name)
            data_index = pd.concat([data_index, data_next_page], ignore_index=True)
            z1 = len(resp_date)
            z2 = z2 + 100
        i = int(0)
        for i in range(10):
            self.days.append(float(i + 1))
        for i in range(40,50):
            self.stocks_prices.append(float(resp_date[len(resp_date) - (i+1)][6]))
        average_day = float(0.0)
        average_stocks_price = float(0.0)
        for i in range(10):
            average_day = average_day + self.days[i]
            average_stocks_price = average_stocks_price + self.stocks_prices[i]
        average_stocks_price = average_stocks_price / 10
        average_day = average_day / 10
        i = 0
        for i in range(10):
            self.divs_dif.append(float(self.days[i] - average_day))
            self.prices_dif.append(float(self.stocks_prices[i] - average_stocks_price))
            self.dif.append(float(self.divs_dif[i] * self.prices_dif[i]))
            self.divs_dif_2.append(float(self.divs_dif[i] * self.divs_dif[i]))
            self.prices_dif_2.append(float(self.prices_dif[i] * self.prices_dif[i]))
        i = 0
        for i in range(10):
            self.dispersion_x = self.dispersion_x + self.divs_dif_2[i]
            self.dispersion_y = self.dispersion_y + self.prices_dif_2[i]
        self.dispersion_x = self.dispersion_x / 10
        self.dispersion_y = self.dispersion_y / 10
        self.standard_dev_x = float(math.sqrt(self.dispersion_x / 10))
        self.standard_dev_y = float(math.sqrt(self.dispersion_y / 10))
        i = 0
        for i in range(10):
            self.cov_ratio = self.cov_ratio + self.dif[i]
        self.cov_ratio = self.cov_ratio / 10
        self.cor_ratio = self.cov_ratio / (math.sqrt(self.dispersion_x) * math.sqrt(self.dispersion_y))
        self.b = float((self.cor_ratio * self.standard_dev_y) / self.standard_dev_x)
        self.a = float(average_stocks_price - (self.b * average_day))
        if (self.b > 0):
            self.lab_1 = "Сигнал тренда: ПОКУПАТЬ"
        elif (self.b < 0):
            self.x = 1
            self.lab_1 = "Сигнал тренда: ПРОДАВАТЬ"
        else:
            self.x = 2
            self.lab_1 = "Сигнал тренда: СТОЯТЬ"
        if (self.cor_ratio > 0.7):
            self.lab_2 = "Сигнал доверия: ПОКУПАТЬ"
        elif (self.cor_ratio < (-0.7)):
            self.y = 1
            self.lab_2 = "Сигнал доверия: ПРОДАВАТЬ"
        else:
            self.y = 2
            self.lab_2 = "Сигнал доверия: СТОЯТЬ"
        if (self.x == self.y):
            self.lab_3 = "Итоговая рекомендация робота: ПОКУПАТЬ"
        else:
            self.lab_3 = "Итоговая рекомендация робота: СТОЯТЬ"
        layout = MDBoxLayout
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.575},
                                      size_hint=(0.9, 0.6),
                                      rows_num=10,
                                      column_data=[
                                          ("День (x)", dp(15)),
                                          ("Стоимость акции (y)", dp(20)),
                                          ("x-x(ср)", dp(15)),
                                          ("y-y(ср)", dp(20)),
                                          ("(x-x(ср))(y-y(ср))", dp(30)),
                                          ("x-x(ср)^2", dp(30)),
                                          ("y-y(ср)^2", dp(30))
                                      ],
                                      row_data=[
                                          ("{0:.0f}".format(self.days[i]),
                                           "{0:.2f}".format(self.stocks_prices[i]), self.divs_dif[i],
                                           self.prices_dif[i], self.dif[i], self.divs_dif_2[i],
                                           self.prices_dif_2[i])
                                          for i in range(10)]
                                      )
        self.add_widget(self.data_table)
        return layout

    def load_auto_end_dialog(self):
        self.dialog = MDDialog(title="Информация об акции",
                               text="Дисперсии: s(x)^2 = {0:.4f}, ".format(
                                   self.dispersion_x) + "s(y)^2 = {0:.4f}".format(
                                   self.dispersion_y) + "\nСтандартные отклонения: s(x) = {0:.4f} млн. руб., ".format(
                                   self.standard_dev_x) + "s(y) = {0:.4f} млн. руб.".format(
                                   self.standard_dev_y) + "\nКоэффициент ковариации: K(xy) = {0:.4f}".format(
                                   self.cov_ratio) + "\nКоэффициент корреляции: r(xy) = {0:.2f}".format(
                                   self.cor_ratio) + "\nУравнение парной регрессии: y = {0:.4f}x + ".format(
                                   self.b) + "{0:.3f}".format(self.a),
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()

    def load_auto_end_ready(self):
        self.dialog = MDDialog(title=" ",
                               text=self.lab_3,
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def on_enter(self):
        self.load_auto_end()
        self.load_auto_end_ready()

    def on_leave(self, *args):
        self.data_table.clear_widgets()

class Auto_end_6(Screen):
    days = []
    stocks_prices = []
    divs_dif = []
    prices_dif = []
    dif = []
    divs_dif_2 = []
    prices_dif_2 = []
    dispersion_x = float(0)
    dispersion_y = float(0)
    standard_dev_x = float(0)
    standard_dev_y = float(0)
    cov_ratio = float(0)
    cor_ratio = float(0)
    b = float(0)
    a = float(0)
    x = 0
    y = 0
    def load_auto_end(self):
        base_url = "http://iss.moex.com/iss/history/engines/stock/markets/index/boards/SNDX/securities.json"
        response = requests.get(base_url)
        result = json.loads(response.text)
        col_name = result['history']['columns']
        data_index = pd.DataFrame(columns=col_name)
        url_index = 'http://iss.moex.com/iss/history/engines/stock/markets/index/boards/SNDX/securities/imoex.json'
        response = requests.get(url_index)
        result = json.loads(response.text)
        resp_date = result['history']['data']
        data_index = pd.DataFrame(resp_date, columns=col_name)
        z1 = len(resp_date)
        z2 = 100
        while z1 == 100:
            url_opt = '?start=' + str(z2)
            url_next_page = (url_index + url_opt)
            response = requests.get(url_next_page)
            result = json.loads(response.text)
            resp_date = result['history']['data']
            data_next_page = pd.DataFrame(resp_date, columns=col_name)
            data_index = pd.concat([data_index, data_next_page], ignore_index=True)
            z1 = len(resp_date)
            z2 = z2 + 100
        i = int(0)
        for i in range(10):
            self.days.append(float(i + 1))
        for i in range(50,60):
            self.stocks_prices.append(float(resp_date[len(resp_date) - (i+1)][6]))
        average_day = float(0.0)
        average_stocks_price = float(0.0)
        for i in range(10):
            average_day = average_day + self.days[i]
            average_stocks_price = average_stocks_price + self.stocks_prices[i]
        average_stocks_price = average_stocks_price / 10
        average_day = average_day / 10
        i = 0
        for i in range(10):
            self.divs_dif.append(float(self.days[i] - average_day))
            self.prices_dif.append(float(self.stocks_prices[i] - average_stocks_price))
            self.dif.append(float(self.divs_dif[i] * self.prices_dif[i]))
            self.divs_dif_2.append(float(self.divs_dif[i] * self.divs_dif[i]))
            self.prices_dif_2.append(float(self.prices_dif[i] * self.prices_dif[i]))
        i = 0
        for i in range(10):
            self.dispersion_x = self.dispersion_x + self.divs_dif_2[i]
            self.dispersion_y = self.dispersion_y + self.prices_dif_2[i]
        self.dispersion_x = self.dispersion_x / 10
        self.dispersion_y = self.dispersion_y / 10
        self.standard_dev_x = float(math.sqrt(self.dispersion_x / 10))
        self.standard_dev_y = float(math.sqrt(self.dispersion_y / 10))
        i = 0
        for i in range(10):
            self.cov_ratio = self.cov_ratio + self.dif[i]
        self.cov_ratio = self.cov_ratio / 10
        self.cor_ratio = self.cov_ratio / (math.sqrt(self.dispersion_x) * math.sqrt(self.dispersion_y))
        self.b = float((self.cor_ratio * self.standard_dev_y) / self.standard_dev_x)
        self.a = float(average_stocks_price - (self.b * average_day))
        if (self.b > 0):
            self.lab_1 = "Сигнал тренда: ПОКУПАТЬ"
        elif (self.b < 0):
            self.x = 1
            self.lab_1 = "Сигнал тренда: ПРОДАВАТЬ"
        else:
            self.x = 2
            self.lab_1 = "Сигнал тренда: СТОЯТЬ"
        if (self.cor_ratio > 0.7):
            self.lab_2 = "Сигнал доверия: ПОКУПАТЬ"
        elif (self.cor_ratio < (-0.7)):
            self.y = 1
            self.lab_2 = "Сигнал доверия: ПРОДАВАТЬ"
        else:
            self.y = 2
            self.lab_2 = "Сигнал доверия: СТОЯТЬ"
        if (self.x == self.y):
            self.lab_3 = "Итоговая рекомендация робота: ПОКУПАТЬ"
        else:
            self.lab_3 = "Итоговая рекомендация робота: СТОЯТЬ"
        layout = MDBoxLayout
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.575},
                                      size_hint=(0.9, 0.6),
                                      rows_num=10,
                                      column_data=[
                                          ("День (x)", dp(15)),
                                          ("Стоимость акции (y)", dp(20)),
                                          ("x-x(ср)", dp(15)),
                                          ("y-y(ср)", dp(20)),
                                          ("(x-x(ср))(y-y(ср))", dp(30)),
                                          ("x-x(ср)^2", dp(30)),
                                          ("y-y(ср)^2", dp(30))
                                      ],
                                      row_data=[
                                          ("{0:.0f}".format(self.days[i]),
                                           "{0:.2f}".format(self.stocks_prices[i]), self.divs_dif[i],
                                           self.prices_dif[i], self.dif[i], self.divs_dif_2[i],
                                           self.prices_dif_2[i])
                                          for i in range(10)]
                                      )
        self.add_widget(self.data_table)
        return layout

    def load_auto_end_dialog(self):
        self.dialog = MDDialog(title="Информация об акции",
                               text="Дисперсии: s(x)^2 = {0:.4f}, ".format(
                                   self.dispersion_x) + "s(y)^2 = {0:.4f}".format(
                                   self.dispersion_y) + "\nСтандартные отклонения: s(x) = {0:.4f} млн. руб., ".format(
                                   self.standard_dev_x) + "s(y) = {0:.4f} млн. руб.".format(
                                   self.standard_dev_y) + "\nКоэффициент ковариации: K(xy) = {0:.4f}".format(
                                   self.cov_ratio) + "\nКоэффициент корреляции: r(xy) = {0:.2f}".format(
                                   self.cor_ratio) + "\nУравнение парной регрессии: y = {0:.4f}x + ".format(
                                   self.b) + "{0:.3f}".format(self.a),
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()

    def load_auto_end_ready(self):
        self.dialog = MDDialog(title=" ",
                               text=self.lab_3,
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def on_enter(self):
        self.load_auto_end()
        self.load_auto_end_ready()

    def on_leave(self, *args):
        self.data_table.clear_widgets()

class Auto_end_7(Screen):
    days = []
    stocks_prices = []
    divs_dif = []
    prices_dif = []
    dif = []
    divs_dif_2 = []
    prices_dif_2 = []
    dispersion_x = float(0)
    dispersion_y = float(0)
    standard_dev_x = float(0)
    standard_dev_y = float(0)
    cov_ratio = float(0)
    cor_ratio = float(0)
    b = float(0)
    a = float(0)
    x = 0
    y = 0
    def load_auto_end(self):
        base_url = "http://iss.moex.com/iss/history/engines/stock/markets/index/boards/SNDX/securities.json"
        response = requests.get(base_url)
        result = json.loads(response.text)
        col_name = result['history']['columns']
        data_index = pd.DataFrame(columns=col_name)
        url_index = 'http://iss.moex.com/iss/history/engines/stock/markets/index/boards/SNDX/securities/imoex.json'
        response = requests.get(url_index)
        result = json.loads(response.text)
        resp_date = result['history']['data']
        data_index = pd.DataFrame(resp_date, columns=col_name)
        z1 = len(resp_date)
        z2 = 100
        while z1 == 100:
            url_opt = '?start=' + str(z2)
            url_next_page = (url_index + url_opt)
            response = requests.get(url_next_page)
            result = json.loads(response.text)
            resp_date = result['history']['data']
            data_next_page = pd.DataFrame(resp_date, columns=col_name)
            data_index = pd.concat([data_index, data_next_page], ignore_index=True)
            z1 = len(resp_date)
            z2 = z2 + 100
        i = int(0)
        for i in range(10):
            self.days.append(float(i + 1))
        for i in range(60,70):
            self.stocks_prices.append(float(resp_date[len(resp_date) - (i+1)][6]))
        average_day = float(0.0)
        average_stocks_price = float(0.0)
        for i in range(10):
            average_day = average_day + self.days[i]
            average_stocks_price = average_stocks_price + self.stocks_prices[i]
        average_stocks_price = average_stocks_price / 10
        average_day = average_day / 10
        i = 0
        for i in range(10):
            self.divs_dif.append(float(self.days[i] - average_day))
            self.prices_dif.append(float(self.stocks_prices[i] - average_stocks_price))
            self.dif.append(float(self.divs_dif[i] * self.prices_dif[i]))
            self.divs_dif_2.append(float(self.divs_dif[i] * self.divs_dif[i]))
            self.prices_dif_2.append(float(self.prices_dif[i] * self.prices_dif[i]))
        i = 0
        for i in range(10):
            self.dispersion_x = self.dispersion_x + self.divs_dif_2[i]
            self.dispersion_y = self.dispersion_y + self.prices_dif_2[i]
        self.dispersion_x = self.dispersion_x / 10
        self.dispersion_y = self.dispersion_y / 10
        self.standard_dev_x = float(math.sqrt(self.dispersion_x / 10))
        self.standard_dev_y = float(math.sqrt(self.dispersion_y / 10))
        i = 0
        for i in range(10):
            self.cov_ratio = self.cov_ratio + self.dif[i]
        self.cov_ratio = self.cov_ratio / 10
        self.cor_ratio = self.cov_ratio / (math.sqrt(self.dispersion_x) * math.sqrt(self.dispersion_y))
        self.b = float((self.cor_ratio * self.standard_dev_y) / self.standard_dev_x)
        self.a = float(average_stocks_price - (self.b * average_day))
        if (self.b > 0):
            self.lab_1 = "Сигнал тренда: ПОКУПАТЬ"
        elif (self.b < 0):
            self.x = 1
            self.lab_1 = "Сигнал тренда: ПРОДАВАТЬ"
        else:
            self.x = 2
            self.lab_1 = "Сигнал тренда: СТОЯТЬ"
        if (self.cor_ratio > 0.7):
            self.lab_2 = "Сигнал доверия: ПОКУПАТЬ"
        elif (self.cor_ratio < (-0.7)):
            self.y = 1
            self.lab_2 = "Сигнал доверия: ПРОДАВАТЬ"
        else:
            self.y = 2
            self.lab_2 = "Сигнал доверия: СТОЯТЬ"
        if (self.x == self.y):
            self.lab_3 = "Итоговая рекомендация робота: ПОКУПАТЬ"
        else:
            self.lab_3 = "Итоговая рекомендация робота: СТОЯТЬ"
        layout = MDBoxLayout
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.575},
                                      size_hint=(0.9, 0.6),
                                      rows_num=10,
                                      column_data=[
                                          ("День (x)", dp(15)),
                                          ("Стоимость акции (y)", dp(20)),
                                          ("x-x(ср)", dp(15)),
                                          ("y-y(ср)", dp(20)),
                                          ("(x-x(ср))(y-y(ср))", dp(30)),
                                          ("x-x(ср)^2", dp(30)),
                                          ("y-y(ср)^2", dp(30))
                                      ],
                                      row_data=[
                                          ("{0:.0f}".format(self.days[i]),
                                           "{0:.2f}".format(self.stocks_prices[i]), self.divs_dif[i],
                                           self.prices_dif[i], self.dif[i], self.divs_dif_2[i],
                                           self.prices_dif_2[i])
                                          for i in range(10)]
                                      )
        self.add_widget(self.data_table)
        return layout

    def load_auto_end_dialog(self):
        self.dialog = MDDialog(title="Информация об акции",
                               text="Дисперсии: s(x)^2 = {0:.4f}, ".format(
                                   self.dispersion_x) + "s(y)^2 = {0:.4f}".format(
                                   self.dispersion_y) + "\nСтандартные отклонения: s(x) = {0:.4f} млн. руб., ".format(
                                   self.standard_dev_x) + "s(y) = {0:.4f} млн. руб.".format(
                                   self.standard_dev_y) + "\nКоэффициент ковариации: K(xy) = {0:.4f}".format(
                                   self.cov_ratio) + "\nКоэффициент корреляции: r(xy) = {0:.2f}".format(
                                   self.cor_ratio) + "\nУравнение парной регрессии: y = {0:.4f}x + ".format(
                                   self.b) + "{0:.3f}".format(self.a),
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()

    def load_auto_end_ready(self):
        self.dialog = MDDialog(title=" ",
                               text=self.lab_3,
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def on_enter(self):
        self.load_auto_end()
        self.load_auto_end_ready()

    def on_leave(self, *args):
        self.data_table.clear_widgets()

class Auto_end_8(Screen):
    days = []
    stocks_prices = []
    divs_dif = []
    prices_dif = []
    dif = []
    divs_dif_2 = []
    prices_dif_2 = []
    dispersion_x = float(0)
    dispersion_y = float(0)
    standard_dev_x = float(0)
    standard_dev_y = float(0)
    cov_ratio = float(0)
    cor_ratio = float(0)
    b = float(0)
    a = float(0)
    x = 0
    y = 0
    def load_auto_end(self):
        base_url = "http://iss.moex.com/iss/history/engines/stock/markets/index/boards/SNDX/securities.json"
        response = requests.get(base_url)
        result = json.loads(response.text)
        col_name = result['history']['columns']
        data_index = pd.DataFrame(columns=col_name)
        url_index = 'http://iss.moex.com/iss/history/engines/stock/markets/index/boards/SNDX/securities/imoex.json'
        response = requests.get(url_index)
        result = json.loads(response.text)
        resp_date = result['history']['data']
        data_index = pd.DataFrame(resp_date, columns=col_name)
        z1 = len(resp_date)
        z2 = 100
        while z1 == 100:
            url_opt = '?start=' + str(z2)
            url_next_page = (url_index + url_opt)
            response = requests.get(url_next_page)
            result = json.loads(response.text)
            resp_date = result['history']['data']
            data_next_page = pd.DataFrame(resp_date, columns=col_name)
            data_index = pd.concat([data_index, data_next_page], ignore_index=True)
            z1 = len(resp_date)
            z2 = z2 + 100
        i = int(0)
        for i in range(10):
            self.days.append(float(i + 1))
        for i in range(70,80):
            self.stocks_prices.append(float(resp_date[len(resp_date) - (i+1)][6]))
        average_day = float(0.0)
        average_stocks_price = float(0.0)
        for i in range(10):
            average_day = average_day + self.days[i]
            average_stocks_price = average_stocks_price + self.stocks_prices[i]
        average_stocks_price = average_stocks_price / 10
        average_day = average_day / 10
        i = 0
        for i in range(10):
            self.divs_dif.append(float(self.days[i] - average_day))
            self.prices_dif.append(float(self.stocks_prices[i] - average_stocks_price))
            self.dif.append(float(self.divs_dif[i] * self.prices_dif[i]))
            self.divs_dif_2.append(float(self.divs_dif[i] * self.divs_dif[i]))
            self.prices_dif_2.append(float(self.prices_dif[i] * self.prices_dif[i]))
        i = 0
        for i in range(10):
            self.dispersion_x = self.dispersion_x + self.divs_dif_2[i]
            self.dispersion_y = self.dispersion_y + self.prices_dif_2[i]
        self.dispersion_x = self.dispersion_x / 10
        self.dispersion_y = self.dispersion_y / 10
        self.standard_dev_x = float(math.sqrt(self.dispersion_x / 10))
        self.standard_dev_y = float(math.sqrt(self.dispersion_y / 10))
        i = 0
        for i in range(10):
            self.cov_ratio = self.cov_ratio + self.dif[i]
        self.cov_ratio = self.cov_ratio / 10
        self.cor_ratio = self.cov_ratio / (math.sqrt(self.dispersion_x) * math.sqrt(self.dispersion_y))
        self.b = float((self.cor_ratio * self.standard_dev_y) / self.standard_dev_x)
        self.a = float(average_stocks_price - (self.b * average_day))
        if (self.b > 0):
            self.lab_1 = "Сигнал тренда: ПОКУПАТЬ"
        elif (self.b < 0):
            self.x = 1
            self.lab_1 = "Сигнал тренда: ПРОДАВАТЬ"
        else:
            self.x = 2
            self.lab_1 = "Сигнал тренда: СТОЯТЬ"
        if (self.cor_ratio > 0.7):
            self.lab_2 = "Сигнал доверия: ПОКУПАТЬ"
        elif (self.cor_ratio < (-0.7)):
            self.y = 1
            self.lab_2 = "Сигнал доверия: ПРОДАВАТЬ"
        else:
            self.y = 2
            self.lab_2 = "Сигнал доверия: СТОЯТЬ"
        if (self.x == self.y):
            self.lab_3 = "Итоговая рекомендация робота: ПОКУПАТЬ"
        else:
            self.lab_3 = "Итоговая рекомендация робота: СТОЯТЬ"
        layout = MDBoxLayout
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.575},
                                      size_hint=(0.9, 0.6),
                                      rows_num=10,
                                      column_data=[
                                          ("День (x)", dp(15)),
                                          ("Стоимость акции (y)", dp(20)),
                                          ("x-x(ср)", dp(15)),
                                          ("y-y(ср)", dp(20)),
                                          ("(x-x(ср))(y-y(ср))", dp(30)),
                                          ("x-x(ср)^2", dp(30)),
                                          ("y-y(ср)^2", dp(30))
                                      ],
                                      row_data=[
                                          ("{0:.0f}".format(self.days[i]),
                                           "{0:.2f}".format(self.stocks_prices[i]), self.divs_dif[i],
                                           self.prices_dif[i], self.dif[i], self.divs_dif_2[i],
                                           self.prices_dif_2[i])
                                          for i in range(10)]
                                      )
        self.add_widget(self.data_table)
        return layout

    def load_auto_end_dialog(self):
        self.dialog = MDDialog(title="Информация об акции",
                               text="Дисперсии: s(x)^2 = {0:.4f}, ".format(
                                   self.dispersion_x) + "s(y)^2 = {0:.4f}".format(
                                   self.dispersion_y) + "\nСтандартные отклонения: s(x) = {0:.4f} млн. руб., ".format(
                                   self.standard_dev_x) + "s(y) = {0:.4f} млн. руб.".format(
                                   self.standard_dev_y) + "\nКоэффициент ковариации: K(xy) = {0:.4f}".format(
                                   self.cov_ratio) + "\nКоэффициент корреляции: r(xy) = {0:.2f}".format(
                                   self.cor_ratio) + "\nУравнение парной регрессии: y = {0:.4f}x + ".format(
                                   self.b) + "{0:.3f}".format(self.a),
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()

    def load_auto_end_ready(self):
        self.dialog = MDDialog(title=" ",
                               text=self.lab_3,
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def on_enter(self):
        self.load_auto_end()
        self.load_auto_end_ready()

    def on_leave(self, *args):
        self.data_table.clear_widgets()

class Auto_end_9(Screen):
    days = []
    stocks_prices = []
    divs_dif = []
    prices_dif = []
    dif = []
    divs_dif_2 = []
    prices_dif_2 = []
    dispersion_x = float(0)
    dispersion_y = float(0)
    standard_dev_x = float(0)
    standard_dev_y = float(0)
    cov_ratio = float(0)
    cor_ratio = float(0)
    b = float(0)
    a = float(0)
    x = 0
    y = 0
    def load_auto_end(self):
        base_url = "http://iss.moex.com/iss/history/engines/stock/markets/index/boards/SNDX/securities.json"
        response = requests.get(base_url)
        result = json.loads(response.text)
        col_name = result['history']['columns']
        data_index = pd.DataFrame(columns=col_name)
        url_index = 'http://iss.moex.com/iss/history/engines/stock/markets/index/boards/SNDX/securities/imoex.json'
        response = requests.get(url_index)
        result = json.loads(response.text)
        resp_date = result['history']['data']
        data_index = pd.DataFrame(resp_date, columns=col_name)
        z1 = len(resp_date)
        z2 = 100
        while z1 == 100:
            url_opt = '?start=' + str(z2)
            url_next_page = (url_index + url_opt)
            response = requests.get(url_next_page)
            result = json.loads(response.text)
            resp_date = result['history']['data']
            data_next_page = pd.DataFrame(resp_date, columns=col_name)
            data_index = pd.concat([data_index, data_next_page], ignore_index=True)
            z1 = len(resp_date)
            z2 = z2 + 100
        i = int(0)
        for i in range(10):
            self.days.append(float(i + 1))
        for i in range(80,90):
            self.stocks_prices.append(float(resp_date[len(resp_date) - (i+1)][6]))
        average_day = float(0.0)
        average_stocks_price = float(0.0)
        for i in range(10):
            average_day = average_day + self.days[i]
            average_stocks_price = average_stocks_price + self.stocks_prices[i]
        average_stocks_price = average_stocks_price / 10
        average_day = average_day / 10
        i = 0
        for i in range(10):
            self.divs_dif.append(float(self.days[i] - average_day))
            self.prices_dif.append(float(self.stocks_prices[i] - average_stocks_price))
            self.dif.append(float(self.divs_dif[i] * self.prices_dif[i]))
            self.divs_dif_2.append(float(self.divs_dif[i] * self.divs_dif[i]))
            self.prices_dif_2.append(float(self.prices_dif[i] * self.prices_dif[i]))
        i = 0
        for i in range(10):
            self.dispersion_x = self.dispersion_x + self.divs_dif_2[i]
            self.dispersion_y = self.dispersion_y + self.prices_dif_2[i]
        self.dispersion_x = self.dispersion_x / 10
        self.dispersion_y = self.dispersion_y / 10
        self.standard_dev_x = float(math.sqrt(self.dispersion_x / 10))
        self.standard_dev_y = float(math.sqrt(self.dispersion_y / 10))
        i = 0
        for i in range(10):
            self.cov_ratio = self.cov_ratio + self.dif[i]
        self.cov_ratio = self.cov_ratio / 10
        self.cor_ratio = self.cov_ratio / (math.sqrt(self.dispersion_x) * math.sqrt(self.dispersion_y))
        self.b = float((self.cor_ratio * self.standard_dev_y) / self.standard_dev_x)
        self.a = float(average_stocks_price - (self.b * average_day))
        if (self.b > 0):
            self.lab_1 = "Сигнал тренда: ПОКУПАТЬ"
        elif (self.b < 0):
            self.x = 1
            self.lab_1 = "Сигнал тренда: ПРОДАВАТЬ"
        else:
            self.x = 2
            self.lab_1 = "Сигнал тренда: СТОЯТЬ"
        if (self.cor_ratio > 0.7):
            self.lab_2 = "Сигнал доверия: ПОКУПАТЬ"
        elif (self.cor_ratio < (-0.7)):
            self.y = 1
            self.lab_2 = "Сигнал доверия: ПРОДАВАТЬ"
        else:
            self.y = 2
            self.lab_2 = "Сигнал доверия: СТОЯТЬ"
        if (self.x == self.y):
            self.lab_3 = "Итоговая рекомендация робота: ПОКУПАТЬ"
        else:
            self.lab_3 = "Итоговая рекомендация робота: СТОЯТЬ"
        layout = MDBoxLayout
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.575},
                                      size_hint=(0.9, 0.6),
                                      rows_num=10,
                                      column_data=[
                                          ("День (x)", dp(15)),
                                          ("Стоимость акции (y)", dp(20)),
                                          ("x-x(ср)", dp(15)),
                                          ("y-y(ср)", dp(20)),
                                          ("(x-x(ср))(y-y(ср))", dp(30)),
                                          ("x-x(ср)^2", dp(30)),
                                          ("y-y(ср)^2", dp(30))
                                      ],
                                      row_data=[
                                          ("{0:.0f}".format(self.days[i]),
                                           "{0:.2f}".format(self.stocks_prices[i]), self.divs_dif[i],
                                           self.prices_dif[i], self.dif[i], self.divs_dif_2[i],
                                           self.prices_dif_2[i])
                                          for i in range(10)]
                                      )
        self.add_widget(self.data_table)
        return layout

    def load_auto_end_dialog(self):
        self.dialog = MDDialog(title="Информация об акции",
                               text="Дисперсии: s(x)^2 = {0:.4f}, ".format(
                                   self.dispersion_x) + "s(y)^2 = {0:.4f}".format(
                                   self.dispersion_y) + "\nСтандартные отклонения: s(x) = {0:.4f} млн. руб., ".format(
                                   self.standard_dev_x) + "s(y) = {0:.4f} млн. руб.".format(
                                   self.standard_dev_y) + "\nКоэффициент ковариации: K(xy) = {0:.4f}".format(
                                   self.cov_ratio) + "\nКоэффициент корреляции: r(xy) = {0:.2f}".format(
                                   self.cor_ratio) + "\nУравнение парной регрессии: y = {0:.4f}x + ".format(
                                   self.b) + "{0:.3f}".format(self.a),
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()

    def load_auto_end_ready(self):
        self.dialog = MDDialog(title=" ",
                               text=self.lab_3,
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def on_enter(self):
        self.load_auto_end()
        self.load_auto_end_ready()

    def on_leave(self, *args):
        self.data_table.clear_widgets()

class Auto_end_10(Screen):
    days = []
    stocks_prices = []
    divs_dif = []
    prices_dif = []
    dif = []
    divs_dif_2 = []
    prices_dif_2 = []
    dispersion_x = float(0)
    dispersion_y = float(0)
    standard_dev_x = float(0)
    standard_dev_y = float(0)
    cov_ratio = float(0)
    cor_ratio = float(0)
    b = float(0)
    a = float(0)
    x = 0
    y = 0
    def load_auto_end(self):
        base_url = "http://iss.moex.com/iss/history/engines/stock/markets/index/boards/SNDX/securities.json"
        response = requests.get(base_url)
        result = json.loads(response.text)
        col_name = result['history']['columns']
        data_index = pd.DataFrame(columns=col_name)
        url_index = 'http://iss.moex.com/iss/history/engines/stock/markets/index/boards/SNDX/securities/imoex.json'
        response = requests.get(url_index)
        result = json.loads(response.text)
        resp_date = result['history']['data']
        data_index = pd.DataFrame(resp_date, columns=col_name)
        z1 = len(resp_date)
        z2 = 100
        while z1 == 100:
            url_opt = '?start=' + str(z2)
            url_next_page = (url_index + url_opt)
            response = requests.get(url_next_page)
            result = json.loads(response.text)
            resp_date = result['history']['data']
            data_next_page = pd.DataFrame(resp_date, columns=col_name)
            data_index = pd.concat([data_index, data_next_page], ignore_index=True)
            z1 = len(resp_date)
            z2 = z2 + 100
        i = int(0)
        for i in range(10):
            self.days.append(float(i + 1))
        for i in range(90,100):
            self.stocks_prices.append(float(resp_date[len(resp_date) - (i+1)][6]))
        average_day = float(0.0)
        average_stocks_price = float(0.0)
        for i in range(10):
            average_day = average_day + self.days[i]
            average_stocks_price = average_stocks_price + self.stocks_prices[i]
        average_stocks_price = average_stocks_price / 10
        average_day = average_day / 10
        i = 0
        for i in range(10):
            self.divs_dif.append(float(self.days[i] - average_day))
            self.prices_dif.append(float(self.stocks_prices[i] - average_stocks_price))
            self.dif.append(float(self.divs_dif[i] * self.prices_dif[i]))
            self.divs_dif_2.append(float(self.divs_dif[i] * self.divs_dif[i]))
            self.prices_dif_2.append(float(self.prices_dif[i] * self.prices_dif[i]))
        i = 0
        for i in range(10):
            self.dispersion_x = self.dispersion_x + self.divs_dif_2[i]
            self.dispersion_y = self.dispersion_y + self.prices_dif_2[i]
        self.dispersion_x = self.dispersion_x / 10
        self.dispersion_y = self.dispersion_y / 10
        self.standard_dev_x = float(math.sqrt(self.dispersion_x / 10))
        self.standard_dev_y = float(math.sqrt(self.dispersion_y / 10))
        i = 0
        for i in range(10):
            self.cov_ratio = self.cov_ratio + self.dif[i]
        self.cov_ratio = self.cov_ratio / 10
        self.cor_ratio = self.cov_ratio / (math.sqrt(self.dispersion_x) * math.sqrt(self.dispersion_y))
        self.b = float((self.cor_ratio * self.standard_dev_y) / self.standard_dev_x)
        self.a = float(average_stocks_price - (self.b * average_day))
        if (self.b > 0):
            self.lab_1 = "Сигнал тренда: ПОКУПАТЬ"
        elif (self.b < 0):
            self.x = 1
            self.lab_1 = "Сигнал тренда: ПРОДАВАТЬ"
        else:
            self.x = 2
            self.lab_1 = "Сигнал тренда: СТОЯТЬ"
        if (self.cor_ratio > 0.7):
            self.lab_2 = "Сигнал доверия: ПОКУПАТЬ"
        elif (self.cor_ratio < (-0.7)):
            self.y = 1
            self.lab_2 = "Сигнал доверия: ПРОДАВАТЬ"
        else:
            self.y = 2
            self.lab_2 = "Сигнал доверия: СТОЯТЬ"
        if (self.x == self.y):
            self.lab_3 = "Итоговая рекомендация робота: ПОКУПАТЬ"
        else:
            self.lab_3 = "Итоговая рекомендация робота: СТОЯТЬ"
        layout = MDBoxLayout
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.575},
                                      size_hint=(0.9, 0.6),
                                      rows_num=10,
                                      column_data=[
                                          ("День (x)", dp(15)),
                                          ("Стоимость акции (y)", dp(20)),
                                          ("x-x(ср)", dp(15)),
                                          ("y-y(ср)", dp(20)),
                                          ("(x-x(ср))(y-y(ср))", dp(30)),
                                          ("x-x(ср)^2", dp(30)),
                                          ("y-y(ср)^2", dp(30))
                                      ],
                                      row_data=[
                                          ("{0:.0f}".format(self.days[i]),
                                           "{0:.2f}".format(self.stocks_prices[i]), self.divs_dif[i],
                                           self.prices_dif[i], self.dif[i], self.divs_dif_2[i],
                                           self.prices_dif_2[i])
                                          for i in range(10)]
                                      )
        self.add_widget(self.data_table)
        return layout

    def load_auto_end_dialog(self):
        self.dialog = MDDialog(title="Информация об акции",
                               text="Дисперсии: s(x)^2 = {0:.4f}, ".format(
                                   self.dispersion_x) + "s(y)^2 = {0:.4f}".format(
                                   self.dispersion_y) + "\nСтандартные отклонения: s(x) = {0:.4f} млн. руб., ".format(
                                   self.standard_dev_x) + "s(y) = {0:.4f} млн. руб.".format(
                                   self.standard_dev_y) + "\nКоэффициент ковариации: K(xy) = {0:.4f}".format(
                                   self.cov_ratio) + "\nКоэффициент корреляции: r(xy) = {0:.2f}".format(
                                   self.cor_ratio) + "\nУравнение парной регрессии: y = {0:.4f}x + ".format(
                                   self.b) + "{0:.3f}".format(self.a),
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()

    def load_auto_end_ready(self):
        self.dialog = MDDialog(title=" ",
                               text=self.lab_3,
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def on_enter(self):
        self.load_auto_end()
        self.load_auto_end_ready()

    def on_leave(self, *args):
        self.data_table.clear_widgets()

class Auto_reb_1(Screen):
    sum = float(0)
    reb = []
    reb_stocks_prices = []
    lab = "Для ребалансировки портфеля понадобилось:\n"
    def load_manual_reb(self):
        self.sum = self.sum + (Auto_end_1.stocks_prices[0] * Auto.num[0])
        self.sum = self.sum + (Auto_end_2.stocks_prices[0] * Auto.num[1])
        self.sum = self.sum + (Auto_end_3.stocks_prices[0] * Auto.num[2])
        self.sum = self.sum + (Auto_end_4.stocks_prices[0] * Auto.num[3])
        self.sum = self.sum + (Auto_end_5.stocks_prices[0] * Auto.num[4])
        self.sum = self.sum + (Auto_end_6.stocks_prices[0] * Auto.num[5])
        self.sum = self.sum + (Auto_end_7.stocks_prices[0] * Auto.num[6])
        self.sum = self.sum + (Auto_end_8.stocks_prices[0] * Auto.num[7])
        self.sum = self.sum + (Auto_end_9.stocks_prices[0] * Auto.num[8])
        self.sum = self.sum + (Auto_end_10.stocks_prices[0] * Auto.num[9])
        layout = MDBoxLayout
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.575},
                                      size_hint=(0.9, 0.6),
                                      rows_num=10,
                                      column_data=[
                                          ("Номер акции", dp(40)),
                                          ("Стоимость акции", dp(40)),
                                          ("Количество активов", dp(40)),
                                          ("Доля из портфеля", dp(40)),
                                      ],
                                      row_data=[
                                          ('1', Auto_end_1.stocks_prices[0], "{0:.0f}".format(Auto.num[0]), "{0:.2f}".format(((Auto_end_1.stocks_prices[0]*Auto.num[0])/self.sum)*100) + "%",
                                           '2', Auto_end_2.stocks_prices[0], "{0:.0f}".format(Auto.num[1]), "{0:.2f}".format(((Auto_end_2.stocks_prices[0]*Auto.num[1])/self.sum)*100) + "%",
                                           '3', Auto_end_3.stocks_prices[0], "{0:.0f}".format(Auto.num[2]), "{0:.2f}".format(((Auto_end_3.stocks_prices[0]*Auto.num[2])/self.sum)*100) + "%",
                                           '4', Auto_end_4.stocks_prices[0], "{0:.0f}".format(Auto.num[3]), "{0:.2f}".format(((Auto_end_4.stocks_prices[0]*Auto.num[3])/self.sum)*100) + "%",
                                           '5', Auto_end_5.stocks_prices[0], "{0:.0f}".format(Auto.num[4]),
                                           "{0:.2f}".format(((Auto_end_5.stocks_prices[0]*Auto.num[4])/self.sum)*100) + "%",
                                           '6', Auto_end_6.stocks_prices[0], "{0:.0f}".format(Auto.num[5]),
                                           "{0:.2f}".format(((Auto_end_6.stocks_prices[0]*Auto.num[5])/self.sum)*100) + "%",
                                           '7', Auto_end_7.stocks_prices[0], "{0:.0f}".format(Auto.num[6]),
                                           "{0:.2f}".format(((Auto_end_7.stocks_prices[0]*Auto.num[6])/self.sum)*100) + "%",
                                           '8', Auto_end_8.stocks_prices[0], "{0:.0f}".format(Auto.num[7]),
                                           "{0:.2f}".format(((Auto_end_8.stocks_prices[0]*Auto.num[7])/self.sum)*100) + "%",
                                           '9', Auto_end_9.stocks_prices[0], "{0:.0f}".format(Auto.num[8]),
                                           "{0:.2f}".format(((Auto_end_9.stocks_prices[0]*Auto.num[8])/self.sum)*100) + "%",
                                           '10', Auto_end_10.stocks_prices[0], "{0:.0f}".format(Auto.num[9]),
                                           "{0:.2f}".format(((Auto_end_10.stocks_prices[0]*Auto.num[9])/self.sum)*100) + "%")
                                      ]
                                      )
        self.add_widget(self.data_table)
        return layout
    def on_enter(self):
        self.load_manual_reb()
    def on_leave(self, *args):
        self.data_table.clear_widgets()

class Auto_reb_2(Screen):
    reb = []
    reb_stocks_prices = []
    lab = "Для ребалансировки портфеля понадобилось:\n"
    def load_manual_reb(self):
        i = 0
        max_price = float(0)
        for i in range(10):
            self.reb.append(0)
        if ((Auto_end_1.stocks_prices[0]*Auto.num[0]) > max_price):
            max_price = Auto_end_1.stocks_prices[0]*Auto.num[0]
        if ((Auto_end_2.stocks_prices[0]*Auto.num[1]) > max_price):
            max_price = Auto_end_2.stocks_prices[0]*Auto.num[1]
        if ((Auto_end_3.stocks_prices[0]*Auto.num[2]) > max_price):
            max_price = Auto_end_3.stocks_prices[0]*Auto.num[2]
        if ((Auto_end_4.stocks_prices[0]*Auto.num[3]) > max_price):
            max_price = Auto_end_4.stocks_prices[0]*Auto.num[3]
        if ((Auto_end_5.stocks_prices[0]*Auto.num[4]) > max_price):
            max_price = Auto_end_5.stocks_prices[0]*Auto.num[4]
        if ((Auto_end_6.stocks_prices[0]*Auto.num[5]) > max_price):
            max_price = Auto_end_6.stocks_prices[0]*Auto.num[5]
        if ((Auto_end_7.stocks_prices[0]*Auto.num[6]) > max_price):
            max_price = Auto_end_7.stocks_prices[0]*Auto.num[6]
        if ((Auto_end_8.stocks_prices[0]*Auto.num[7]) > max_price):
            max_price = Auto_end_8.stocks_prices[0]*Auto.num[7]
        if ((Auto_end_9.stocks_prices[0]*Auto.num[8]) > max_price):
            max_price = Auto_end_9.stocks_prices[0]*Auto.num[8]
        if ((Auto_end_10.stocks_prices[0]*Auto.num[9]) > max_price):
            max_price = Auto_end_10.stocks_prices[0]*Auto.num[9]
        self.reb_stocks_prices.append(Auto_end_1.stocks_prices[0])
        self.reb_stocks_prices.append(Auto_end_2.stocks_prices[0])
        self.reb_stocks_prices.append(Auto_end_3.stocks_prices[0])
        self.reb_stocks_prices.append(Auto_end_4.stocks_prices[0])
        self.reb_stocks_prices.append(Auto_end_5.stocks_prices[0])
        self.reb_stocks_prices.append(Auto_end_6.stocks_prices[0])
        self.reb_stocks_prices.append(Auto_end_7.stocks_prices[0])
        self.reb_stocks_prices.append(Auto_end_8.stocks_prices[0])
        self.reb_stocks_prices.append(Auto_end_9.stocks_prices[0])
        self.reb_stocks_prices.append(Auto_end_10.stocks_prices[0])
        while (self.reb_stocks_prices[0] < max_price):
            self.reb_stocks_prices[0] = self.reb_stocks_prices[0] + Auto_end_1.stocks_prices[0]
            self.reb[0] = self.reb[0] + 1
        while (self.reb_stocks_prices[1] < max_price):
            self.reb_stocks_prices[1] = self.reb_stocks_prices[1] + Auto_end_2.stocks_prices[0]
            self.reb[1] = self.reb[1] + 1
        while (self.reb_stocks_prices[2] < max_price):
            self.reb_stocks_prices[2] = self.reb_stocks_prices[2] + Auto_end_3.stocks_prices[0]
            self.reb[2] = self.reb[2] + 1
        while (self.reb_stocks_prices[3] < max_price):
            self.reb_stocks_prices[3] = self.reb_stocks_prices[3] + Auto_end_4.stocks_prices[0]
            self.reb[3] = self.reb[3] + 1
        while (self.reb_stocks_prices[4] < max_price):
            self.reb_stocks_prices[4] = self.reb_stocks_prices[4] + Auto_end_5.stocks_prices[0]
            self.reb[4] = self.reb[4] + 1
        while (self.reb_stocks_prices[5] < max_price):
            self.reb_stocks_prices[5] = self.reb_stocks_prices[5] + Auto_end_6.stocks_prices[0]
            self.reb[5] = self.reb[5] + 1
        while (self.reb_stocks_prices[6] < max_price):
            self.reb_stocks_prices[6] = self.reb_stocks_prices[6] + Auto_end_7.stocks_prices[0]
            self.reb[6] = self.reb[6] + 1
        while (self.reb_stocks_prices[7] < max_price):
            self.reb_stocks_prices[7] = self.reb_stocks_prices[7] + Auto_end_8.stocks_prices[0]
            self.reb[7] = self.reb[7] + 1
        while (self.reb_stocks_prices[8] < max_price):
            self.reb_stocks_prices[8] = self.reb_stocks_prices[8] + Auto_end_9.stocks_prices[0]
            self.reb[8] = self.reb[8] + 1
        while (self.reb_stocks_prices[9] < max_price):
            self.reb_stocks_prices[9] = self.reb_stocks_prices[9] + Auto_end_10.stocks_prices[0]
            self.reb[9] = self.reb[9] + 1
        i = 0
        for i in range(10):
            if (self.reb[i] > 0):
                self.lab = self.lab + "- докупить акцию №" + str(i + 1) + " ещё " + str(self.reb[i]) + " раз(а)"
                if (i == 9):
                    self.lab = self.lab + "."
                else:
                    self.lab = self.lab + ";\n"
        layout = MDBoxLayout
        self.data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.575},
                                      size_hint=(0.9, 0.6),
                                      rows_num=10,
                                      column_data=[
                                          ("Номер акции", dp(30)),
                                          ("Исходная стоимость акции", dp(30)),
                                          ("Количество активов", dp(30)),
                                          ("Общая стоимость", dp(30)),
                                          ("Ребалансировання стоимость акции", dp(30)),
                                      ],
                                      row_data=[
                                          ('1', Auto_end_1.stocks_prices[0], "{0:.0f}".format(Auto.num[0]), "{0:.0f}".format(Auto_end_1.stocks_prices[0]*Auto.num[0]), self.reb_stocks_prices[0],
                                           '2', Auto_end_2.stocks_prices[0], "{0:.0f}".format(Auto.num[1]), "{0:.0f}".format(Auto_end_2.stocks_prices[0]*Auto.num[1]), self.reb_stocks_prices[1],
                                           '3', Auto_end_3.stocks_prices[0], "{0:.0f}".format(Auto.num[2]), "{0:.0f}".format(Auto_end_3.stocks_prices[0]*Auto.num[2]), self.reb_stocks_prices[2],
                                           '4', Auto_end_4.stocks_prices[0], "{0:.0f}".format(Auto.num[3]), "{0:.0f}".format(Auto_end_4.stocks_prices[0]*Auto.num[3]), self.reb_stocks_prices[3],
                                           '5', Auto_end_5.stocks_prices[0], "{0:.0f}".format(Auto.num[4]), "{0:.0f}".format(Auto_end_5.stocks_prices[0]*Auto.num[4]), self.reb_stocks_prices[4],
                                           '6', Auto_end_6.stocks_prices[0], "{0:.0f}".format(Auto.num[5]), "{0:.0f}".format(Auto_end_6.stocks_prices[0]*Auto.num[5]), self.reb_stocks_prices[5],
                                           '7', Auto_end_7.stocks_prices[0], "{0:.0f}".format(Auto.num[6]), "{0:.0f}".format(Auto_end_7.stocks_prices[0]*Auto.num[6]), self.reb_stocks_prices[6],
                                           '8', Auto_end_8.stocks_prices[0], "{0:.0f}".format(Auto.num[7]), "{0:.0f}".format(Auto_end_8.stocks_prices[0]*Auto.num[7]), self.reb_stocks_prices[7],
                                           '9', Auto_end_9.stocks_prices[0], "{0:.0f}".format(Auto.num[8]), "{0:.0f}".format(Auto_end_9.stocks_prices[0]*Auto.num[8]), self.reb_stocks_prices[8],
                                           '10', Auto_end_10.stocks_prices[0], "{0:.0f}".format(Auto.num[9]), "{0:.0f}".format(Auto_end_10.stocks_prices[0]*Auto.num[9]),self.reb_stocks_prices[9])
                                      ]
                                      )
        self.add_widget(self.data_table)
        return layout
    def load_manual_reb_dialog(self):
        self.dialog = MDDialog(title="Информация о ребалансировке",
                               text=self.lab,
                               buttons=[
                                   MDFlatButton(text='Выйти',
                                                on_release=self.close_dialog)
                               ])
        self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()
    def on_enter(self):
        self.load_manual_reb()
    def leave(self, *args):
        self.data_table.clear_widgets()
        Auto_end_1.days = []
        Auto_end_2.days = []
        Auto_end_3.days = []
        Auto_end_4.days = []
        Auto_end_5.days = []
        Auto_end_6.days = []
        Auto_end_7.days = []
        Auto_end_8.days = []
        Auto_end_9.days = []
        Auto_end_10.days = []
        Auto_end_1.stocks_prices = []
        Auto_end_2.stocks_prices = []
        Auto_end_3.stocks_prices = []
        Auto_end_4.stocks_prices = []
        Auto_end_5.stocks_prices = []
        Auto_end_6.stocks_prices = []
        Auto_end_7.stocks_prices = []
        Auto_end_8.stocks_prices = []
        Auto_end_9.stocks_prices = []
        Auto_end_10.stocks_prices = []
        Auto_end_1.divs_dif = []
        Auto_end_2.divs_dif = []
        Auto_end_3.divs_dif = []
        Auto_end_4.divs_dif = []
        Auto_end_5.divs_dif = []
        Auto_end_6.divs_dif = []
        Auto_end_7.divs_dif = []
        Auto_end_8.divs_dif = []
        Auto_end_9.divs_dif = []
        Auto_end_10.divs_dif = []
        Auto_end_1.prices_dif = []
        Auto_end_2.prices_dif = []
        Auto_end_3.prices_dif = []
        Auto_end_4.prices_dif = []
        Auto_end_5.prices_dif = []
        Auto_end_6.prices_dif = []
        Auto_end_7.prices_dif = []
        Auto_end_8.prices_dif = []
        Auto_end_9.prices_dif = []
        Auto_end_10.prices_dif = []
        Auto_end_1.dif = []
        Auto_end_2.dif = []
        Auto_end_3.dif = []
        Auto_end_4.dif = []
        Auto_end_5.dif = []
        Auto_end_6.dif = []
        Auto_end_7.dif = []
        Auto_end_8.dif = []
        Auto_end_9.dif = []
        Auto_end_10.dif = []
        Auto_end_1.divs_dif_2 = []
        Auto_end_2.divs_dif_2 = []
        Auto_end_3.divs_dif_2 = []
        Auto_end_4.divs_dif_2 = []
        Auto_end_5.divs_dif_2 = []
        Auto_end_6.divs_dif_2 = []
        Auto_end_7.divs_dif_2 = []
        Auto_end_8.divs_dif_2 = []
        Auto_end_9.divs_dif_2 = []
        Auto_end_10.divs_dif_2 = []
        Auto_end_1.prices_dif_2 = []
        Auto_end_2.prices_dif_2 = []
        Auto_end_3.prices_dif_2 = []
        Auto_end_4.prices_dif_2 = []
        Auto_end_5.prices_dif_2 = []
        Auto_end_6.prices_dif_2 = []
        Auto_end_7.prices_dif_2 = []
        Auto_end_8.prices_dif_2 = []
        Auto_end_9.prices_dif_2 = []
        Auto_end_10.prices_dif_2 = []
        Auto_end_1.reb = []
        Auto_end_2.reb = []
        Auto_end_3.reb = []
        Auto_end_4.reb = []
        Auto_end_5.reb = []
        Auto_end_6.reb = []
        Auto_end_7.reb = []
        Auto_end_8.reb = []
        Auto_end_9.reb = []
        Auto_end_10.reb = []
        Auto_end_1.reb_stocks_prices = []
        Auto_end_2.reb_stocks_prices = []
        Auto_end_3.reb_stocks_prices = []
        Auto_end_4.reb_stocks_prices = []
        Auto_end_5.reb_stocks_prices = []
        Auto_end_6.reb_stocks_prices = []
        Auto_end_7.reb_stocks_prices = []
        Auto_end_8.reb_stocks_prices = []
        Auto_end_9.reb_stocks_prices = []
        Auto_end_10.reb_stocks_prices = []
        Auto.num = []
        self.dispersion_x = float(0)
        self.dispersion_y = float(0)
        self.standard_dev_x = float(0)
        self.standard_dev_y = float(0)
        self.cov_ratio = float(0)
        self.cor_ratio = float(0)
        self.b = float(0)
        self.a = float(0)
        self.x = 0
        self.y = 0
        self.lab_1 = ""
        self.lab_2 = ""
        self.lab_3 = ""
        self.reb = []
        self.reb_stocks_prices = []
        self.lab = "Для ребалансировки портфеля понадобилось:\n"
        self.manager.current = 'choice'

class TradeBot(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Start(name='start'))
        sm.add_widget(Choice(name='choice'))
        sm.add_widget(Manual_1(name='manual_1'))
        sm.add_widget(Manual_2(name='manual_2'))
        sm.add_widget(Manual_3(name='manual_3'))
        sm.add_widget(Manual_4(name='manual_4'))
        sm.add_widget(Manual_5(name='manual_5'))
        sm.add_widget(Manual_6(name='manual_6'))
        sm.add_widget(Manual_7(name='manual_7'))
        sm.add_widget(Manual_8(name='manual_8'))
        sm.add_widget(Manual_9(name='manual_9'))
        sm.add_widget(Manual_10(name='manual_10'))
        sm.add_widget(Manual_end_1(name='manual_end_1'))
        sm.add_widget(Manual_end_2(name='manual_end_2'))
        sm.add_widget(Manual_end_3(name='manual_end_3'))
        sm.add_widget(Manual_end_4(name='manual_end_4'))
        sm.add_widget(Manual_end_5(name='manual_end_5'))
        sm.add_widget(Manual_end_6(name='manual_end_6'))
        sm.add_widget(Manual_end_7(name='manual_end_7'))
        sm.add_widget(Manual_end_8(name='manual_end_8'))
        sm.add_widget(Manual_end_9(name='manual_end_9'))
        sm.add_widget(Manual_end_10(name='manual_end_10'))
        sm.add_widget(Manual_reb_1(name='manual_reb_1'))
        sm.add_widget(Manual_reb_2(name='manual_reb_2'))
        sm.add_widget(Auto(name='auto'))
        sm.add_widget(Auto_end_1(name='auto_end_1'))
        sm.add_widget(Auto_end_2(name='auto_end_2'))
        sm.add_widget(Auto_end_3(name='auto_end_3'))
        sm.add_widget(Auto_end_4(name='auto_end_4'))
        sm.add_widget(Auto_end_5(name='auto_end_5'))
        sm.add_widget(Auto_end_6(name='auto_end_6'))
        sm.add_widget(Auto_end_7(name='auto_end_7'))
        sm.add_widget(Auto_end_8(name='auto_end_8'))
        sm.add_widget(Auto_end_9(name='auto_end_9'))
        sm.add_widget(Auto_end_10(name='auto_end_10'))
        sm.add_widget(Auto_reb_1(name='auto_reb_1'))
        sm.add_widget(Auto_reb_2(name='auto_reb_2'))
        screen = Builder.load_string(screen_menu)
        return screen

if __name__ == '__main__':
#    try:
#        if hasattr(sys, '_MEIPASS'):
#            resource_add_path(os.path.join(sys._MEIPASS))
        app = TradeBot()
        app.run()
#    except Exception as e:
#        print(e)
#        input("Press enter.")