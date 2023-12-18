import pytest
import time
from Pages.auth_page import AuthPage
from Pages.login_page import LoginPage
from Pages.class_env import *

"""Позитивные Тест -Кейсы на основной функционал.( Кейс №3 . Компания "Дезориентация" ) для ручного и атоматизированного тестирования."""

def test_keys_1(web_browser):
    """Через фикстуру подлючаемся к драйверу с настройками хром"""
    page = AuthPage(web_browser)
    """Записываем URL"""
    url = page.get_current_url()
    text1 = page.blok_news.get_text()
    print(text1)
    print(f'Урл 1  {url}   ==   Урл 2 {"https://mevikon.ru/"}')
    assert url == 'https://mevikon.ru/'
    assert text1 == ('07-15 ДЕКАБРЯ\n'
 'PRO-FEST\n'
 'Онлайн-фестиваль о карьерном самоопределении\n'
 'Записаться')


def test_keys_2(web_browser):
    page = AuthPage(web_browser)
    """Забираем текст из кнопки"""
    button_text = page.button_rec.get_text()
    page.button_rec.click()
    heading = page.heading.get_text()
    clicabile = page.button_rec.is_clickable()
    print(f'эта кнопка кликабельна == {clicabile}')
    assert clicabile == True
    print(f'Текст кнопки {button_text} == "Записаться"')
    assert button_text == "Записаться"
    print(f'Заголовок перехода {heading} == "Убедись, что фестиваль будет тебе полезен"')
    assert heading == "Убедись, что фестиваль будет тебе полезен"


def test_keys_3(web_browser):
    page = AuthPage(web_browser)
    """Skroll страницы"""
    page.scroll_down()
    """Выбираем текст из целого блока и сравниваем по названиям"""
    text1 = page.blok_4_card.get_text()
    heading_big = 'Что тебя ждет'
    heading_card1 = 'Экспертные'
    heading_card2 = 'Стенд-ап'
    heading_card3 = '10 серьезных'
    heading_card4 = 'Бизнес-завтрак'
    button_text = 'Записаться на PRO-FEST'
    print(f'Заголовок блока соответствует =={heading_big}')
    assert heading_big in text1
    assert heading_card1 in text1
    assert heading_card2 in text1
    assert heading_card3 in text1
    assert heading_card4 in text1
    print(f'Блок имеет 4 карточки с заголовками.')
    print(f'Текст кнопки == {button_text}')
    assert button_text in text1


def test_keys_4(web_browser):
    page = AuthPage(web_browser)
    """Забираем текст из кнопки"""
    button_text = page.button_rec_pro_fest.get_text()
    page.button_rec_pro_fest.click()
    heading = page.heading.get_text()
    clicabile = page.button_rec_pro_fest.is_clickable()
    print(f'эта кнопка кликабельна == {clicabile}')
    assert clicabile == True
    print(f'Текст кнопки {button_text} == "Записаться на PRO-FEST"')
    assert button_text == "Записаться на PRO-FEST"
    print(f'Заголовок перехода {heading} == "Убедись, что фестиваль будет тебе полезен"')
    assert heading == "Убедись, что фестиваль будет тебе полезен"


def test_keys_5(web_browser):
    page = AuthPage(web_browser)
    """Skroll страницы"""
    page.scroll_down()
    """Выбираем текст из целого блока и сравниваем по названиям"""
    text1 = page.blok_4_card2.get_text()
    heading_big = 'Разыграем'
    heading_card1 = 'Метафорические'
    heading_card2 = 'Сменные'
    heading_card3 = 'Чехол'
    heading_card4 = 'Кофейные'
    button_text = 'Записаться на PRO-FEST'
    print(f'Заголовок блока соответствует =={heading_big}')
    assert heading_big in text1
    assert heading_card1 in text1
    assert heading_card2 in text1
    assert heading_card3 in text1
    assert heading_card4 in text1
    print(f'Блок имеет 4 карточки с заголовками.')
    print(f'Текст кнопки == {button_text}')
    assert button_text in text1


def test_keys_6(web_browser):
    page = AuthPage(web_browser)
    """Забираем текст из кнопки"""
    button_text = page.button_rec_pro_fest2.get_text()
    page.button_rec_pro_fest2.click()
    heading = page.heading.get_text()
    clicabile = page.button_rec_pro_fest2.is_clickable()
    print(f'эта кнопка кликабельна == {clicabile}')
    assert clicabile == True
    print(f'Текст кнопки {button_text} == "Записаться на PRO-FEST"')
    assert button_text == "Записаться на PRO-FEST"
    print(f'Заголовок перехода {heading} == "Убедись, что фестиваль будет тебе полезен"')
    assert heading == "Убедись, что фестиваль будет тебе полезен"


def test_keys_7(web_browser):
    page = AuthPage(web_browser)
    """Забираем изначальный URL"""
    url = page.get_current_url()
    """Проверяем на кликабельность логотип потом кликаем по нему"""
    clicabile = page.logotip_top_banner.is_clickable()
    page.logotip_top_banner.click()
    """Забираем URL страницы на которую перешли"""
    url2 = page.get_current_url()
    print(f'Логотип кликабелен == {clicabile}')
    assert clicabile == True
    print(f'{url} != {url2}')
    assert url != url2

"""Кейс должен упасть"""
def test_keys_8(web_browser):
    page = AuthPage(web_browser)
    """Забираем изначальный URL"""
    url = page.get_current_url()
    """Проверяем на кликабельность логотип потом кликаем по нему"""
    clicabile = page.logotipe_ffoter.is_clickable()
    page.logotipe_ffoter.click()
    """Забираем URL страницы на которую перешли"""
    url2 = page.get_current_url()
    print(f'Логотип кликабелен == {clicabile}')
    assert clicabile == True
    print(f'{url} != {url2}')
    assert url != url2


def test_keys_9(web_browser):
    page = AuthPage(web_browser)
    """Забрали Url"""
    url = page.get_current_url()
    clicable = page.dogovor.is_clickable()
    page.dogovor.click()
    url2 = page.get_current_url()
    print(f'{clicable} == True')
    assert clicable == True
    print(f'URL {url} != {url2}')
    assert url != url2

"""Тест кейс № 10 отсутствует не прошел ручное тестирование"""


def test_keys_11(web_browser):
    page = AuthPage(web_browser)
    """Забрали Url"""
    url = page.get_current_url()
    clicable = page.politic_conf.is_clickable()
    page.politic_conf.click()
    url2 = page.get_current_url()
    print(f'{clicable} == True')
    assert clicable == True
    print(f'URL {url} != {url2}')
    assert url != url2

"""Тест Кейс № 12; № 13; №14 -отсутствует не прошел ручное тестирование"""


def test_keys_15(web_browser):
    page = AuthPage(web_browser)
    input_user1 = page.input_usser.send_keys('Попов Валера')
    """Отправляем запрос, нажимаем кнопку"""
    page.button_send.click()
    time.sleep(1)
    response_user = page.respons_user.get_text()
    print(f'Вводим {response_user} - отображается в чате {response_user}')
    assert response_user == 'Попов Валера'

    input_usser2 = page.input_usser.send_keys('28')
    page.button_send.click()
    time.sleep(1)
    response_user2 = page.respons_user2.get_text()
    print(f'Вводим {response_user2} - отображается в чате {response_user2}')
    assert response_user2 == '28'

    input_usser3 = page.input_usser.send_keys('Музыкант')
    page.button_send.click()
    time.sleep(1)
    response_user3 = page.respons_user3.get_text()
    print(f'Вводим {response_user3} - отображается в чате {response_user3}')
    assert response_user3 == 'Музыкант'

    input_usser4 = page.input_usser.send_keys('10')
    page.button_send.click()
    time.sleep(1)
    response_user4 = page.respons_user4.get_text()
    print(f'Вводим {response_user4} - отображается в чате {response_user4}')
    assert response_user4 == '10'

    input_usser5 = page.input_usser.send_keys('Ялта')
    page.button_send.click()
    time.sleep(1)
    response_user5 = page.respons_user5.get_text()
    print(f'Вводим {response_user5} - отображается в чате {response_user5}')
    assert response_user5 == 'Ялта'

    input_usser6 = page.input_usser.send_keys('30000')
    page.button_send.click()
    time.sleep(1)
    response_user6 = page.respons_user6.get_text()
    print(f'Вводим {response_user6} - отображается в чате {response_user6}')
    assert response_user6 == '30000'

    input_usser7 = page.input_usser.send_keys('+79787777777')
    page.button_send.click()
    time.sleep(1)
    response_user7 = page.respons_user7.get_text()
    print(f'Вводим {response_user7} - отображается в чате {response_user7}')
    assert response_user7 == '+79787777777'

    input_usser8 = page.input_usser.send_keys('Да')
    page.button_send.click()
    time.sleep(1)
    response_user8 = page.respons_user8.get_text()
    print(f'Вводим {response_user8} - отображается в чате {response_user8}')
    assert response_user8 == 'Да'

    """Кликаем кнопку смотреть результат"""
    page.button_rezultate.click()
    heading_dostigator = page.heading_dostigator.get_text()
    linc_podelitsa = page.linc_podelitsa.get_text()
    button_zabrat_stik = page.button_zabrat_stik.get_text()
    if 'Достигатор' in heading_dostigator:
        print('Слово "Достигатор" есть в заголовке')
    if 'Поделиться' in linc_podelitsa:
        print('Слово "Поделиться" есть в ссылке')
    if 'Забрать' in button_zabrat_stik:
        print('Слово "Забрать" есть в кнопке')
    assert 'Достигатор' in heading_dostigator
    assert 'Поделиться' in linc_podelitsa
    assert 'Забрать' in button_zabrat_stik


def test_keys_16(web_browser):
    page = LoginPage(web_browser)
    url = page.get_current_url()
    """Заполняем форму нажимаем кнопку отправить"""
    login = page.login.send_keys(Env.valid_login)
    passw = page.passw.send_keys(Env.valid_pass)
    page.button_enter.click()
    url2 = page.get_current_url()
    print(f'{url} !=  {url2}')
    assert url != url2


"""Чек-Лис №2 С негативными сценариями для формы входа в административный отдел"""
"""Параметризуем поле "Логин" значениями , а поле ПАРОЛЬ -валидное значение"""
@pytest.mark.parametrize('invalid_login', ['', 'ADMIN',' admin','a dmin',
                                           'admin ', '1admin', 'ad6min',
                                           'admin0', ',admin', 'admin,',
                                           'adm,in', 'a,d,m,i,n', '-admin',
                                           'admin-', 'a-d-mi-n', '_admin',
                                           'ad_mi_n', 'admin_', 'a.dmi:n'
                                           'a!d.mi?n', '"admin>', "Логин: от 8-50 знаков, любые символы, обязательно содержащий не менее ДВУХ ЛЮБЫХ знаков препинания и/или знаков цифр117 символов и еще добавляем символов чтобы было 200 кенуцгенукгценкугенцкеуцкуенгц.", ' <userlogin>admin<userlogin>', '‘ or ‘a’ = ‘a’; DROP TABLE user;'
                                                                           ' SELECT * FROM blog WHERE code LIKE ‘a%’;'], ids=['', 'ADMIN', ' admin', 'a dmin',
                                           'admin ', '1admin', 'ad6min',
                                           'admin0', ',admin', 'admin,',
                                           'adm,in', 'a,d,m,i,n', '-admin',
                                           'admin-', 'a-d-mi-n', '_admin',
                                           'ad_mi_n', 'admin_', 'a.dmi:n'
                                           'a!d.mi?n', '"admin>', "Логин: от 8-50 знаков, любые символы, обязательно содержащий не менее ДВУХ ЛЮБЫХ знаков препинания и/или знаков цифр117 символов и еще добавляем символов чтобы было 200 кенуцгенукгценкугенцкеуцкуенгц.", ' <userlogin>admin<userlogin>', '‘ or ‘a’ = ‘a’; DROP TABLE user;'
                                                                           ' SELECT * FROM blog WHERE code LIKE ‘a%’;'])
def test_chek_list_2(web_browser, invalid_login):
    page = LoginPage(web_browser)
    url = page.get_current_url()
    """Заполняем форму"""
    login = page.login.send_keys(f'{invalid_login}')
    passw = page.passw.send_keys(Env.valid_pass)
    page.button_enter.click()
    url2 = page.get_current_url()
    assert url == url2

"""Параметризуем поле "Пароль" значениями , а поле Логин -валидное значение"""
@pytest.mark.parametrize('invalid_passw',['', 'ADMIN',' admin','a dmin',
                                           'admin ', '1admin', 'ad6min',
                                           'admin0', ',admin', 'admin,',
                                           'adm,in', 'a,d,m,i,n', '-admin',
                                           'admin-', 'a-d-mi-n', '_admin',
                                           'ad_mi_n', 'admin_', 'a.dmi:n'
                                           'a!d.mi?n', '"admin>', "Логин: от 8-50 знаков, любые символы, обязательно содержащий не менее ДВУХ ЛЮБЫХ знаков препинания и/или знаков цифр117 символов и еще добавляем символов чтобы было 200 кенуцгенукгценкугенцкеуцкуенгц.", ' <userlogin>admin<userlogin>', '‘ or ‘a’ = ‘a’; DROP TABLE user;'
                                                                           ' SELECT * FROM blog WHERE code LIKE ‘a%’;'])
def test_chek_list_2_2(web_browser, invalid_passw):
    page = LoginPage(web_browser)
    url = page.get_current_url()
    """Заполняем форму"""
    login = page.login.send_keys(Env.valid_login)
    passw = page.passw.send_keys(f'{invalid_passw}')
    page.button_enter.click()
    url2 = page.get_current_url()
    print(invalid_passw)
    assert url == url2