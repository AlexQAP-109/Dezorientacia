#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from Pages.base import WebPage
from Pages.elements import WebElement
from Pages.elements import ManyWebElements


class LoginPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://mevikon.ru/login/'

        super().__init__(web_driver, url)


    """СТРАНИЦА АВТОРИЗАЦИИ В АДМИН"""
    login = WebElement(xpath='/html/body/div[2]/form/input[2]')

    passw = WebElement(xpath='/html/body/div[2]/form/input[3]')

    button_enter = WebElement(xpath='/html/body/div[2]/form/button')