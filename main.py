import pyautogui as pa
from time import sleep
import pyperclip as pc
import requests
import random
import psutil
from nsetools import Nse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
from codes import Currencycodes
from singal import Signals

codes = Currencycodes()
QUOTE_KEY = 'quote'
STOP_KEY = 'bye'
SHUTDOWN_KEY = 'shutdown'


CHECK_NEW_MESSAGE_IN_SEC = 600


def convert(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


battery = psutil.sensors_battery()
nse = Nse()

QUOTE_API = "https://type.fit/api/quotes"
QUOTES = requests.get("https://type.fit/api/quotes").json()

user_choose = int(input(f'which one you want? press 1 for Trading signals or press 2 for Whatsapp bot :   '))

if user_choose == 2:
    CHATTING = True

    while CHATTING:

        sleep(5)
        share = pa.locateOnScreen('share.png', confidence=0.9)
        pa.moveTo(share, duration=2)
        sleep(2)
        pa.moveRel(0, -50)
        s = pa.position()

        if battery.percent < 10:
            time = convert(battery.secsleft)
            pa.moveTo(share[0] + 100, share[1] + 10, duration=1)
            pa.click()
            pa.typewrite(
                f"hey bro Your battery percentage is {battery.percent}\n power plugged :{battery.power_plugged}\n "
                f"Battery left:{time}\n can i turn off PC(key:shutdown)")
            sleep(300)

        # ________checking for new messages__________#

        if pa.pixelMatchesColor(s[0], s[1], (255, 255, 255), tolerance=10):
            pa.rightClick()
            pa.moveRel(20, -190, 2)
            pa.doubleClick()
            sleep(2)
            message = []
            msg = pc.paste()
            message.append(msg)

            if SHUTDOWN_KEY == message[0]:
                pa.moveTo(share[0] + 100, share[1] + 10, duration=2)
                pa.doubleClick()
                pa.typewrite("bye bye ")
                os.system("shutdown /s /t 1")

            # ________checking for quote_______________#

            if QUOTE_KEY in message[0]:
                print('match')
                pa.moveTo(share[0] + 100, share[1] + 10, duration=2)
                pa.doubleClick()
                random_number = random.randint(0, 1643)
                pa.typewrite(f"{QUOTES[random_number]['text']} - {QUOTES[random_number]['author']}")
                pa.press('enter')

            # ________checking to stop the script_________#

            if STOP_KEY in message[0]:
                sleep(5)
                CHATTING = False

            # _________checking for stockcodes_____________#

            for code in codes.STOCK_CODES:
                if code == message[0].lower() or code == message[0].upper():
                    totalsell_q = nse.get_quote(message[0])['totalSellQuantity']  # NOQA
                    company_name = nse.get_quote(message[0])['companyName']
                    day_high = nse.get_quote(message[0])['dayHigh']
                    base_price = nse.get_quote(message[0])['basePrice']
                    sell_quantity = nse.get_quote(message[0])['sellQuantity1']
                    pchange = nse.get_quote(message[0])['pChange']    # NOQA
                    total_traded_value = nse.get_quote(message[0])['totalTradedValue']
                    average_price = nse.get_quote(message[0])['averagePrice']
                    open = nse.get_quote(message[0])['open']    # NOQA
                    close_price = nse.get_quote(message[0])['closePrice']
                    change = nse.get_quote(message[0])['change']
                    last_price = nse.get_quote(message[0])['lastPrice']
                    pa.moveTo(share[0] + 100, share[1] + 10, duration=2)
                    pa.click()
                    pa.typewrite(
                        f"Name:{company_name}\n OpenPrice:{open}\n LastPrice:{last_price}\n Change:{change}\n"
                        f"AveragePrice:{average_price}\n TotalTradedValue:{total_traded_value}\n pchange:{pchange}\n"
                        f"SellQuality:{sell_quantity}\n DayHigh:{day_high}\n BasePrice:{base_price}\n"
                        f"TotalSellQuantity:{totalsell_q}\n ")

            if message[0].upper() in codes.FOREX_CURRENCIES_CODES:
                ser_obj = Service("C:/New folder/chromedriver.exe")
                driver = webdriver.Chrome(service=ser_obj)
                driver.get(url="https://in.investing.com/currencies/streaming-forex-rates-majors")

                currency_name_list = []
                for i in range(1, 40 + 2):
                    currency_name = driver.find_element(By.XPATH, f'//*[@id="js-main-container"]/section[1]/div/section[2]/section/div[1]/div/table/tbody/tr[{i}]/td[3]/a')  # NOQA
                    currency_name_list.append(currency_name.text)

                bid_price_list = []
                for i in range(1, 40 + 2):
                    bid_price = driver.find_element(By.XPATH, f'//*[@id="js-main-container"]/section[1]/div/section[2]/section/div[1]/div/table/tbody/tr[{i}]/td[4]/span')   # NOQA
                    bid_price_list.append(bid_price.text)

                ask_price_list = []
                for i in range(1, 40 + 2):
                    ask_price = driver.find_element(By.XPATH, f'//*[@id="js-main-container"]/section[1]/div/section[2]/section/div[1]/div/table/tbody/tr[{i}]/td[5]/span')   # NOQA
                    ask_price_list.append(ask_price.text)

                high_price_list = []
                for i in range(1, 40 + 2):
                    high_price = driver.find_element(By.XPATH, f'//*[@id="js-main-container"]/section[1]/div/section[2]/section/div[1]/div/table/tbody/tr[{i}]/td[6]/span')   # NOQA
                    high_price_list.append(high_price.text)

                low_price_list = []
                for i in range(1, 40 + 2):
                    low_price = driver.find_element(By.XPATH, f'//*[@id="js-main-container"]/section[1]/div/section[2]/section/div[1]/div/table/tbody/tr[{i}]/td[7]/span')   # NOQA
                    low_price_list.append(low_price.text)

                change_price_list = []
                for i in range(1, 40 + 2):
                    change_price = driver.find_element(By.XPATH, f'//*[@id="js-main-container"]/section[1]/div/section[2]/section/div[1]/div/table/tbody/tr[{i}]/td[8]/span')   # NOQA
                    change_price_list.append(change_price.text)

                change_percentage_list = []
                for i in range(1, 40 + 2):
                    change_percentage = driver.find_element(By.XPATH, f'//*[@id="js-main-container"]/section[1]/div/section[2]/section/div[1]/div/table/tbody/tr[{i}]/td[9]/span')  # NOQA
                    change_percentage_list.append(change_percentage.text)

                time_list = []
                for i in range(1, 40 + 2):
                    time = driver.find_element(By.XPATH, f'//*[@id="js-main-container"]/section[1]/div/section[2]/section/div[1]/div/table/tbody/tr[{i}]/td[10]/time')   # NOQA
                    time_list.append(time.text)
                driver.quit()
                sleep(10)
                pa.moveTo(share[0] + 100, share[1] + 10, duration=2)
                pa.doubleClick()
                index = currency_name_list.index(message[0])
                pa.typewrite(f"Currency Name:{currency_name_list[index]}\n Bid Price:{bid_price_list[index]}\n"
                             f" Ask Price:{ask_price_list[index]}\n High Price:{high_price_list[index]}\n "
                             f"Low Price:{low_price_list[index]}\n Change:{change_price_list[index]}\n "
                             f"Change in %:{change_percentage_list[index]}\n Time:{time_list[index]}\n ")

        else:
            sleep(CHECK_NEW_MESSAGE_IN_SEC)

if user_choose == 1:
    signal = Signals()
    signal.Inputs()
