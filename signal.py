from tradingview_ta import TA_Handler, Interval, Exchange
import time

class Signals:

    def Inputs(self):
         symbol = input('enter the symbol :  ')
         screener = input('enter the screener :  ')
         exchange = input('enter the exchange :  ')
         print(f'the INTERVAL is 5MINUTES now .If you want you can change from the follwing path'
               'my_personal_whatsapp_bot-master/singal.py the code is(interval=Interval.INTERVAL_5_MINUTES)')


         while True:
             data = TA_Handler(
                 symbol=symbol,
                 screener=screener,
                 exchange=exchange,
                 interval=Interval.INTERVAL_5_MINUTES
             )

             rec = data.get_analysis()
             RSI = rec.indicators["RSI"]
             MACD = rec.indicators["MACD.macd"]
             MACD_SIG = rec.indicators['MACD.signal']
             if RSI > 70 and MACD > 0:
                 print('potential SELL <--')

             if RSI < 30 and MACD < 0:
                 print('--> potential BUY')

             else:
                 print('Not a good time ! Wait.....')
                 time.sleep(1)

