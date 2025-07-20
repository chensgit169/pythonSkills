import pandas as pd

path = 'BUG舞团春晚选舞和团建统计_数据详情表_原始数据_202411281716.xlsx'
data = pd.read_excel(path)

karting_data = data['Q5_团建参与']
# print(karting_data)
go_karting = karting_data.str.contains("卡丁车", na=False)
print("卡丁车参与人数:", go_karting.sum()+1)

dinner = karting_data.str.contains("吃饭", na=False)
print("吃饭人数:", dinner.sum())


play_data = data['Q3_想要参加的表演节目']
bug = play_data.str.contains("BUG", na=False)
china = play_data.str.contains("国风", na=False)
happy = play_data.str.contains("欢乐", na=False)
print("BUG舞团意愿人数:", bug.sum())
print("国风舞意愿人数:", china.sum())
print("欢乐舞意愿人数:", happy.sum())