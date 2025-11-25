# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 09:13:24 2024

@author: USER
"""

#%%

"""
文件字串說明: -->
    增加程式碼可讀性、輔助測式和使用。
    PEP 257 規範方式:
        撰寫方式：三重雙(單)引號包圍，放在定義的第一行，。
    
        讀取方式：使用 __doc__ 屬性或 help() 函數。
"""
#%%

"""文件字串方-->式一
abc
ddd
fff"""


'''文件字串-->方式二
111
222
333
'''


#%%

def test():
    """nothing to do --> comment out"""
    pass

#%%

#文件字串預設屬性 (attribute) __doc__ ，利用 print() 函數印出 test() 函數的文件字串。

print(test.__doc__)

#%%


def calculator_value(Nowvalue,double,value=1):# 10 , True , 5

    """
        說明程式動作:
            執行一個分數的計算。
    
        參數：
            Nowvalue: 第一個數字。
            double: 第二個數字。
    
        返回：
            計算後的數據: Nowvalue。
    """
    

    if double == True:
        value=value*2
    Nowvalue = Nowvalue + value
    return Nowvalue


value=5
Nowvalue=10

New_value = calculator_value(Nowvalue,True,value)
print(New_value)


New2_value = calculator_value(Nowvalue,True)
print(New2_value)


#%%

print(calculator_value.__doc__)