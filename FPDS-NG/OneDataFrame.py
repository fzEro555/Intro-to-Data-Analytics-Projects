# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 11:06:10 2018

@author: Subha Karanam
"""

import openpyxl
import pandas as pd

class OneDataFrame:
    #removing summary page
    def removeSummary(workbook):
        sheetnames = workbook.get_sheet_names()
        std = workbook.get_sheet_by_name(sheetnames[0])
        workbook.remove_sheet(std)
        return workbook
    
    #merging the three dataframes into a single dataframe csv
    def mergeData(dataFrame1,dataFrame2,dataFrame3,dataFrame4):
        frames = [dataFrame1,dataFrame2,dataFrame3,dataFrame4]
        result = pd.concat(frames)
        return result
        
