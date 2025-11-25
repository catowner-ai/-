# -*- coding: utf-8 -*-
"""

@author: OfficePC
"""

import pandas as pd
euro12=pd.read_csv('data/Euro2012_stats.csv')


print(euro12)
print(euro12.info())
print(euro12.describe())

#%%

#只想要分析這四個欄位的資料
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards','Goals']]
print(discipline)

#依紅牌數量由大到小排序
team_Red_cards=discipline.sort_values('Red Cards', ascending=False)
print(team_Red_cards)


#依黃牌數量由大到小排序
team_Yellow_Cards=discipline.sort_values('Yellow Cards', ascending=False)
print(team_Yellow_Cards)


#依紅牌做主要排序，黃牌做次要排序，由大到小排序
discipline_sort_values=discipline.sort_values(['Red Cards','Yellow Cards'], ascending=False)
print(discipline_sort_values)



#%%

#16個隊伍黃牌數的平均值
print(discipline['Yellow Cards'].mean())

#16個隊伍黃牌數的平均值(取到小數點2位)
print(round(discipline['Yellow Cards'].mean(),2))

#16個隊伍黃牌數的平均值(取到整數位)
print(round(discipline['Yellow Cards'].mean()))


#%%

#找出euro12的dataframe裡的Team欄位的資料
team_data=euro12['Team']
print(team_data)

#找出euro12的dataframe裡的Team欄位的資料
team_data2=euro12.Team
print(team_data2)


#找出隊伍名稱開頭P的隊伍
print(euro12[euro12.Team.str.startswith('P')])
