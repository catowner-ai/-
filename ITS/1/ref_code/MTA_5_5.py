# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 20:01:52 2021

@author: OfficePC
"""

import os

def get_file_message(file):
    if os.path.isfile(file):
        with open(file,'r') as file:
            return file.readline()
    else:
            return "檔案不存在"