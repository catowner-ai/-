# -*- coding: utf-8 -*-
"""
Created on Mon May  8 20:42:46 2023

@author: USER
"""




import threading
import time

import datetime


def job():
    print("thread is working")
    time.sleep(60)

# 建立一個子執行緒
child_thread = threading.Thread(target = job)

# 執行該子執行緒
child_thread.start()

# 主執行緒繼續執行自己的工作
print("Main thread:")

# time.sleep(60)
print("wait for doughter thread ending:")
# 等待 t 這個子執行緒結束
child_thread.join()

print("Done.")  