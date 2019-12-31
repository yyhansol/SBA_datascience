# %%

import pandas as pd

df = pd.read_excel("../data/math_func_q_k_k1.xlsx")
df.head()

# %%

import platform

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# sns.set()

from matplotlib import font_manager, rc

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
else:
    print("It's unknown system. Hangul fonts are not supported!")

# plt.rcParams['axes.unicode_minus'] = False
plt.rcParams["figure.figsize"] = [12, 6]



# %%

df.tail()

# %%

from konlpy.tag import Kkma

kkma = Kkma()

from konlpy.tag import Okt

okt = Okt()

df["kkma"] = ''
df["okt"] = ''

for i in range(0, len(df)):
    # df['kkma'][i] = kkma.morphs(df["질문"][i])
    # df['okt'][i] = okt.morphs(df["질문"][i])
    df['kkma'][i] = kkma.pos(df["질문"][i])
    df['okt'][i] = okt.pos(df["질문"][i])

df.head()

# %%

import re

df["model"] = ''
df["model_answer"] = ''

for i in range(0, len(df)):
    if re.compile(
            "보다 [\w]{1,9} ['더 가지고 있습니다, 더 가지고 있습니까, 더 많이 가지고 있는지, 더 팔았습니까, 더 많았다고 합니다, 더 많습니까, 더 많은지, 더 많을까요, 더 많이 먹었습니까, 더 적게']").findall(
            df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        if int(a[0]) < int(a[1]):
            df["model"][i] = [int(a[1]), "-", int(a[0])]
            df["model_answer"][i] = (int(a[1]) - int(a[0]))
        elif int(a[0]) > int(a[1]):
            df["model"][i] = [int(a[0]), '-', int(a[1])]
            df["model_answer"][i] = ((int(a[0]) - int(a[1])))

for i in range(0, len(df)):
    if re.compile("[\w]{1,9} ['더 많이 가지고 있는지,더 붙일 수 있습니까']").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        if int(a[0]) < int(a[1]):
            df["model"][i] = [int(a[1]), "-", int(a[0])]
            df["model_answer"][i] = (int(a[1]) - int(a[0]))
        elif int(a[0]) > int(a[1]):
            df["model"][i] = [int(a[0]), '-', int(a[1])]
            df["model_answer"][i] = ((int(a[0]) - int(a[1])))

for i in range(0, len(df)):
    if re.compile("몇  [\w]{1,4}를 ['주었습니다. , 주었더니 ,줬습니다']").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        if int(a[0]) < int(a[1]):
            df["model"][i] = [int(a[1]), "-", int(a[0])]
            df["model_answer"][i] = (int(a[1]) - int(a[0]))
        elif int(a[0]) > int(a[1]):
            df["model"][i] = [int(a[0]), '-', int(a[1])]
            df["model_answer"][i] = ((int(a[0]) - int(a[1])))

for i in range(0, len(df)):
    if re.compile("몇  [\w]{1,4}를 ['주었습니다. , 주었더니 ,줬습니다']").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        if int(a[0]) < int(a[1]):
            df["model"][i] = [int(a[1]), "-", int(a[0])]
            df["model_answer"][i] = (int(a[1]) - int(a[0]))
        elif int(a[0]) > int(a[1]):
            df["model"][i] = [int(a[0]), '-', int(a[1])]
            df["model_answer"][i] = ((int(a[0]) - int(a[1])))

for i in range(0, len(df)):
    if re.compile("나누어").findall(df["질문"][i]) != []:
        if re.compile("['를 가졌다면, 를 주었다면, 먼저,  를 쥐었다면']").findall(df["질문"][i]) != []:
            a = re.compile("[\d]{1,4}").findall(df["질문"][i])
            if int(a[0]) < int(a[1]):
                df["model"][i] = [int(a[1]), "-", int(a[0])]
                df["model_answer"][i] = (int(a[1]) - int(a[0]))
            elif int(a[0]) > int(a[1]):
                df["model"][i] = [int(a[0]), '-', int(a[1])]
                df["model_answer"][i] = ((int(a[0]) - int(a[1])))

for i in range(0, len(df)):
    if re.compile("['주었더니, 하였더니']").findall(df["질문"][i]) != []:
        if re.compile("남았습니다.").findall(df["질문"][i]) != []:
            a = re.compile("[\d]{1,4}").findall(df["질문"][i])
            if int(a[0]) < int(a[1]):
                df["model"][i] = [int(a[1]), "-", int(a[0])]
                df["model_answer"][i] = (int(a[1]) - int(a[0]))
            elif int(a[0]) > int(a[1]):
                df["model"][i] = [int(a[0]), '-', int(a[1])]
                df["model_answer"][i] = ((int(a[0]) - int(a[1])))

for i in range(0, len(df)):
    if re.compile("에게  [\w]{1,10}['을,를'] 한 [\w]{1,4}씩").findall(df["질문"][i]) != []:
        if re.compile("몇  [\w]{1,4} 더 필요합니까").findall(df["질문"][i]) != []:
            a = re.compile("[\d]{1,4}").findall(df["질문"][i])
            if int(a[0]) < int(a[1]):
                df["model"][i] = [int(a[1]), "-", int(a[0])]
                df["model_answer"][i] = (int(a[1]) - int(a[0]))
            elif int(a[0]) > int(a[1]):
                df["model"][i] = [int(a[0]), '-', int(a[1])]
                df["model_answer"][i] = ((int(a[0]) - int(a[1])))

for i in range(0, len(df)):
    if re.compile("와 똑같은  [\w]{1,10} 가지려면").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        if int(a[0]) < int(a[1]):
            df["model"][i] = [int(a[1]), "-", int(a[0])]
            df["model_answer"][i] = (int(a[1]) - int(a[0]))
        elif int(a[0]) > int(a[1]):
            df["model"][i] = [int(a[0]), '-', int(a[1])]
            df["model_answer"][i] = ((int(a[0]) - int(a[1])))

for i in range(0, len(df)):
    if re.compile("와 같아질까요").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        if int(a[0]) < int(a[1]):
            df["model"][i] = [int(a[1]), "-", int(a[0])]
            df["model_answer"][i] = (int(a[1]) - int(a[0]))
        elif int(a[0]) > int(a[1]):
            df["model"][i] = [int(a[0]), '-', int(a[1])]
            df["model_answer"][i] = ((int(a[0]) - int(a[1])))

for i in range(0, len(df)):
    if re.compile("같은 수의  [\w]{1,10} 갖기 위하여").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        if int(a[0]) < int(a[1]):
            df["model"][i] = [int(a[1]), "-", int(a[0])]
            df["model_answer"][i] = (int(a[1]) - int(a[0]))
        elif int(a[0]) > int(a[1]):
            df["model"][i] = [int(a[0]), '-', int(a[1])]
            df["model_answer"][i] = ((int(a[0]) - int(a[1])))

for i in range(0, len(df)):
    if re.compile("만큼  [\w]{1,10}을 가지려면").findall(df["질문"][i]) != []:
        if re.compile("만큼  [\w]{1,10}을 가지려면  [\w]{1,10} 몇 [\w]{1,4}가 더 있어야").findall(df["질문"][i]) != []:
            a = re.compile("[\d]{1,4}").findall(df["질문"][i])
            if int(a[0]) < int(a[1]):
                df["model"][i] = [int(a[1]), "-", int(a[0])]
                df["model_answer"][i] = (int(a[1]) - int(a[0]))
            elif int(a[0]) > int(a[1]):
                df["model"][i] = [int(a[0]), '-', int(a[1])]
                df["model_answer"][i] = ((int(a[0]) - int(a[1])))

for i in range(0, len(df)):
    if re.compile("['중 , 그중 , 그 중에서, 이 중, 이 중에서, 중에서']").findall(df["질문"][i]) != []:
        if re.compile("['남았습니다, 주었습니다, 남습니까, 잃었습니다, 남은,  나가서, 부러졌습니다, 몇 [\w]{1,4}입니까']").findall(df["질문"][i]) != []:
            a = re.compile("[\d]{1,4}").findall(df["질문"][i])
            if int(a[0]) < int(a[1]):
                df["model"][i] = [int(a[1]), "-", int(a[0])]
                df["model_answer"][i] = (int(a[1]) - int(a[0]))
            elif int(a[0]) > int(a[1]):
                df["model"][i] = [int(a[0]), '-', int(a[1])]
                df["model_answer"][i] = ((int(a[0]) - int(a[1])))

for i in range(0, len(df)):
    if re.compile("['잠시 후, 얼마 후, 잠시후, 며칠 후에, 며칠 후']").findall(df["질문"][i]) != []:
        if re.compile("['남아있는,  남았습니까, 날아갔습니다., 졌습니다, 돌아가서']").findall(df["질문"][i]) != []:
            a = re.compile("[\d]{1,4}").findall(df["질문"][i])
            if int(a[0]) < int(a[1]):
                df["model"][i] = [int(a[1]), "-", int(a[0])]
                df["model_answer"][i] = (int(a[1]) - int(a[0]))
            elif int(a[0]) > int(a[1]):
                df["model"][i] = [int(a[0]), '-', int(a[1])]
                df["model_answer"][i] = ((int(a[0]) - int(a[1])))

            # 더하기
p = ['줬습니다', '합', '더했더니']
xx = ['어떤', '얼마', '몇']

for i in range(0, len(df)):
    li = []
    for j in range(0, len(df["kkma"][i])):
        if df["kkma"][i][j][1] == "NR" and (
                (df["kkma"][i][j][0] != "이") and (df["kkma"][i][j][0] != "몇") and (df["kkma"][i][j][0] != "하나")):
            li.append(int(df["kkma"][i][j][0]))
        elif (df["kkma"][i][j][1] == "MAG") and (df["okt"][i][j][0] == h for h in p):
            li.append('+')
        elif (df["kkma"][i][j][1] == "MDT") and (df["okt"][i][k][0] == x for x in xx):
            li.append('x')
    df["model"][i] = li
    a1 = []
    for k in df["model"][i]:
        if type(k) == int:
            a1.append(k)
    if "+" in df["model"][i]:
        res = 0
        for g in a1:
            res += g
        df["model_answer"][i] = res

    # 예외처리
    if type(df["model"][i][-1]) == int:
        a = []
        for k in df["model"][i]:
            if type(k) == int:
                a.append(k)
        df["model"][i] = [a[1], '-', a[0]]
        df["model_answer"][i] = (int(a[1]) - int(a[0]))



    # 예외처리
    ##어떤 수와 15의 합은 51
    ##어떤 수에 1을 더했더니 10
    elif re.compile("어떤 수와 [\d]{1,4}의 합은 [\d]{1,4}").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        df["model"][i] = [int(a[1]), '-', int(a[0])]
        df["model_answer"][i] = (int(a[1]) - int(a[0]))
    elif re.compile("[\d]{1,4}와 어떤 수의 합은 [\d]{1,4}").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        df["model"][i] = [int(a[1]), '-', int(a[0])]
        df["model_answer"][i] = (int(a[1]) - int(a[0]))
    elif re.compile("어떤 수에 [\d]{1,4}을 더했더니 [\d]{1,4}").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        df["model"][i] = [int(a[1]), '-', int(a[0])]
        df["model_answer"][i] = (int(a[1]) - int(a[0]))

    elif re.compile("몇 [\w]{1,2} 더").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        df["model"][i] = [int(a[1]), '-', int(a[0])]
        df["model_answer"][i] = (int(a[1]) - int(a[0]))








    # 상자문제
    # for i in range(0,len(df)):
    elif re.compile("[\d]{1,4}['을,를'] 넣었더니 [\d]{1,4}").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        if int(a[0]) < int(a[1]):
            df["model"][i] = [int(a[1]), "-", int(a[0]), '+', int(a[2])]
            df["model_answer"][i] = (int(a[1]) - int(a[0]) + int(a[2]))
        elif int(a[0]) > int(a[1]):
            df["model"][i] = [int(a[2]), '-(', int(a[0]), '-', int(a[1]), ')']
            df["model_answer"][i] = (int(a[2]) - int(a[0]) + int(a[1]))
    elif re.compile("[\d]{1,4}['을,를'] 넣으면 [\d]{1,4}").findall(df["질문"][i]) != []:
        a = re.compile("[\d]{1,4}").findall(df["질문"][i])
        if int(a[0]) < int(a[1]):
            df["model"][i] = [int(a[1]), "-", int(a[0]), '+', int(a[2])]
            df["model_answer"][i] = (int(a[1]) - int(a[0]) + int(a[2]))
        elif int(a[0]) > int(a[1]):
            df["model"][i] = [int(a[2]), '-(', int(a[0]), '-', int(a[1]), ')']
            df["model_answer"][i] = (int(a[2]) - int(a[0]) + int(a[1]))

#%%
