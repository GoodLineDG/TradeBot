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
from kivymd.uix.label import MDLabel

screen_menu = """
ScreenManager:
    id: screen_manager
    Start:
    Choice:
    Manual_1:
    Manual_end:
    Manual_reb:
    Auto_end:
    Auto_reb:
<Start>:
    name: 'start'
    MDTopAppBar:
        title: 'TradeBot v1.0'
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
        on_release: sys.exit(0)
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
            root.manager.current = 'auto_end'
    MDRectangleFlatButton:
        text: 'Вернуться в главное меню'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_release: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'start'
<Manual_1>:
    name: 'manual_1'
    MDTopAppBar:
        title: 'Введите стоимость ваших акций'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDTextField:
        id: field_1
        hint_text: "Акция 1"
        helper_text: "в млн. рублей"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.8}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_2
        hint_text: "Акция 2"
        helper_text: "в млн. рублей"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_3
        hint_text: "Акция 3"
        helper_text: "в млн. рублей"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_4
        hint_text: "Акция 4"
        helper_text: "в млн. рублей"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_5
        hint_text: "Акция 5"
        helper_text: "в млн. рублей"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.25, 'center_y': 0.4}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_6
        hint_text: "Акция 6"
        helper_text: "в млн. рублей"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.8}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_7
        hint_text: "Акция 7"
        helper_text: "в млн. рублей"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_8
        hint_text: "Акция 8"
        helper_text: "в млн. рублей"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_9
        hint_text: "Акция 9"
        helper_text: "в млн. рублей"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id: field_10
        hint_text: "Акция 10"
        helper_text: "в млн. рублей"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.4}
        size_hint_x:None
        width:300
    MDRectangleFlatButton:
        text: 'Готово'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_release:
            root.manager.screens[2].input()
            root.manager.transition.direction = 'left'
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_release:
            root.manager.transition.direction = 'right'
            root.manager.current = 'choice'
<Manual_end>:
    name: 'manual_end'
    MDTopAppBar:
        title: 'Ваш портфель готов!'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Ребалансировка'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'manual_reb'
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_release: 
            root.manager.screens[3].load_manual_end_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'choice'
<Manual_reb>:
    name: 'manual_reb'
    MDTopAppBar:
        title: 'Ребалансированный портфель'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.screens[4].load_manual_reb_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'choice'
<Auto_end>:
    name: 'auto_end'
    MDTopAppBar:
        title: 'Ваш портфель готов!'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: 'Ребалансировка'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'auto_reb'
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_release: 
            root.manager.screens[5].load_auto_end_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'choice'
<Auto_reb>:
    name: 'auto_reb'
    MDTopAppBar:
        title: 'Ребалансированный портфель'
        pos_hint: {'center_x':0.5,'center_y':0.95}
    MDRectangleFlatButton:
        text: '?'
        pos_hint: {'center_x':0.25,'center_y':0.05}
        on_release: 
            root.manager.screens[6].load_auto_reb_dialog()
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.75,'center_y':0.05}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'choice'
"""

class Start(Screen):
    pass

class Choice(Screen):
    pass

class Manual_1(Screen):
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
        if ((self.ids.field_1.text != '') and (self.ids.field_2.text != '') and (self.ids.field_3.text != '') and (self.ids.field_4.text != '') and (self.ids.field_5.text != '') and (self.ids.field_6.text != '') and (self.ids.field_7.text != '') and (self.ids.field_8.text != '') and (self.ids.field_9.text != '') and (self.ids.field_10.text != '')):
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
            self.manager.current = 'manual_end'
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

class Manual_end(Screen):
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
                                     ("День", dp(15)),
                                     ("Стоимость актива", dp(15)),
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
                               text=self.lab_1 + "\n" + self.lab_2 + "\n" + self.lab_3,
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
        Manual_1.days = []
        Manual_1.stocks_prices = []
        Manual_1.divs_dif = []
        Manual_1.prices_dif = []
        Manual_1.dif = []
        Manual_1.divs_dif_2 = []
        Manual_1.prices_dif_2 = []
        Manual_1.reb = []
        Manual_1.reb_stocks_prices = []
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

class Manual_reb(Screen):
    reb = []
    reb_stocks_prices = []
    lab = "Для ребалансировки портфеля понадобилось:\n"
    def load_manual_reb(self):
        i = 0
        max_price = 0
        for i in range(10):
            self.reb.append(0)
            if (Manual_1.stocks_prices[i] > max_price):
                max_price = Manual_1.stocks_prices[i]
        i = 0
        for i in range(10):
            self.reb_stocks_prices.append(Manual_1.stocks_prices[i])
            while (self.reb_stocks_prices[i] < max_price):
                self.reb_stocks_prices[i] = self.reb_stocks_prices[i] + Manual_1.stocks_prices[i]
                self.reb[i] = self.reb[i] + 1
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
                                          ("День", dp(15)),
                                          ("Стоимость актива", dp(15)),
                                          ("x-x(ср)", dp(15)),
                                          ("y-y(ср)", dp(20)),
                                          ("(x-x(ср))(y-y(ср))", dp(30)),
                                          ("x-x(ср)^2", dp(30)),
                                          ("y-y(ср)^2", dp(30))
                                      ],
                                      row_data=[
                                          ("{0:.0f}".format(Manual_1.days[i]),
                                           "{0:.2f}".format(self.reb_stocks_prices[i]), Manual_1.divs_dif[i],
                                           Manual_1.prices_dif[i], Manual_1.dif[i], Manual_1.divs_dif_2[i],
                                           Manual_1.prices_dif_2[i])
                                          for i in range(10)]
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
    def on_leave(self, *args):
        self.data_table.clear_widgets()
        Manual_1.days = []
        Manual_1.stocks_prices = []
        Manual_1.divs_dif = []
        Manual_1.prices_dif = []
        Manual_1.dif = []
        Manual_1.divs_dif_2 = []
        Manual_1.prices_dif_2 = []
        Manual_1.reb = []
        Manual_1.reb_stocks_prices = []
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

class Auto_end(Screen):
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
        i = 0
        for i in range(10):
            self.stocks_prices.append(float(resp_date[len(resp_date) - (i + 1)][6]))
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
                                          ("День", dp(15)),
                                          ("Стоимость актива", dp(15)),
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
        self.dialog = MDDialog(title="Информация о портфеле",
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
        self.dialog = MDDialog(title="Ваш портфель готов!",
                               text=self.lab_1 + "\n" + self.lab_2 + "\n" + self.lab_3,
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
        Manual_1.days = []
        Manual_1.stocks_prices = []
        Manual_1.divs_dif = []
        Manual_1.prices_dif = []
        Manual_1.dif = []
        Manual_1.divs_dif_2 = []
        Manual_1.prices_dif_2 = []
        Manual_1.reb = []
        Manual_1.reb_stocks_prices = []
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

class Auto_reb(Screen):
    reb = []
    reb_stocks_prices = []
    lab = "Для ребалансировки портфеля понадобилось:\n"
    def load_auto_reb(self):
        i = 0
        max_price = 0
        for i in range(10):
            self.reb.append(0)
            if (Auto_end.stocks_prices[i] > max_price):
                max_price = Auto_end.stocks_prices[i]
        i = 0
        for i in range(10):
            self.reb_stocks_prices.append(Auto_end.stocks_prices[i])
            while (self.reb_stocks_prices[i] < max_price):
                self.reb_stocks_prices[i] = self.reb_stocks_prices[i] + Auto_end.stocks_prices[i]
                self.reb[i] = self.reb[i] + 1
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
                                          ("День", dp(15)),
                                          ("Стоимость актива", dp(15)),
                                          ("x-x(ср)", dp(15)),
                                          ("y-y(ср)", dp(20)),
                                          ("(x-x(ср))(y-y(ср))", dp(30)),
                                          ("x-x(ср)^2", dp(30)),
                                          ("y-y(ср)^2", dp(30))
                                      ],
                                      row_data=[
                                          ("{0:.0f}".format(Auto_end.days[i]),
                                           "{0:.2f}".format(self.reb_stocks_prices[i]), Auto_end.divs_dif[i],
                                           Auto_end.prices_dif[i], Auto_end.dif[i], Auto_end.divs_dif_2[i],
                                           Auto_end.prices_dif_2[i])
                                          for i in range(10)]
                                      )
        self.add_widget(self.data_table)
        return layout
    def load_auto_reb_dialog(self):
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
        self.load_auto_reb()
    def on_leave(self, *args):
        self.data_table.clear_widgets()
        Manual_1.days = []
        Manual_1.stocks_prices = []
        Manual_1.divs_dif = []
        Manual_1.prices_dif = []
        Manual_1.dif = []
        Manual_1.divs_dif_2 = []
        Manual_1.prices_dif_2 = []
        Manual_1.reb = []
        Manual_1.reb_stocks_prices = []
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

class TradeBot(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Start(name='start'))
        sm.add_widget(Choice(name='choice'))
        sm.add_widget(Manual_1(name='manual_1'))
        sm.add_widget(Manual_end(name='manual_end'))
        sm.add_widget(Manual_reb(name='manual_reb'))
        sm.add_widget(Auto_end(name='auto_end'))
        sm.add_widget(Auto_reb(name='auto_reb'))
        screen = Builder.load_string(screen_menu)
        return screen

TradeBot().run()