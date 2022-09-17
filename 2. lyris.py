#######################config################################


from ast import Num
import requests
import time
import json
import pandas as pd
from bs4 import BeautifulSoup
import re
from tqdm import tqdm

import time
import pickle
Path = '/Volumes/GoogleDrive/내 드라이브/nlp_project/전처리/'


##############################함수##############################함수##############################함수##############################함수##############################함수
# list_song_id => lyris 가져오기 함수
def songid_To_lyris(list_title,list_song_id):
  list_lyris=[]
  dic_title_lyris={}
  for i,songId in tqdm(enumerate(list_song_id)):
    print('\n###############################################################################################################################################\n')
    print(i,list_title[i])
    # url request
    url_gasa = 'https://www.melon.com/song/detail.htm?songId={}'.format(songId)
    hdr={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    ,'Cookie': 'PCID=16631321531394943825803; PC_PCID=16631321531394943825803; __T_=1; POC=MP10; _T_ANO=kiwyPHxx7ujR9u8DsF1u6lVCVZqXNAL9MOkgDVRHb+LYMC9fiuxj5Z9QwpYXGqnFwUxc4a7zHuxnuy/Gj1m5w69gzcgqU9Ih9GWjxvV2QozAt4dDR9xPLqHA6jrmy3SOdCJLqPr4Rg/oLXyKlRzlJIm1rm5TXMy3Rvb2gzpsxuWfkRxpeH3lgqILfi01s4PbMYgccVZux7rK7poCK+uDSU9FTiSgjB++4g9rhbBWe/G+RBOLChIwM/GrQg7891G+uJRv27gt6gTgkA2Mvk1SrumBfBgCYv27mo3CGGlWuJ3EnMpHsOu4oH2F+ECEibShd9jkatnapUDXNLLuS7fv7A==; wcs_bt=s_f9c4bde066b:1663214508'
    ,'Referer': 'https://www.melon.com/song/detail.htm?songId=35626990'
    }    
    time.sleep(5)
    res = requests.get(url_gasa, headers= hdr)
    print(res,res.url)

    # soup tags
    soup = BeautifulSoup(res.text, 'html.parser')
    div_tags = soup.select('div.lyric')
    print('가사 유무:',len(div_tags))
    if(len(div_tags) == 0 ):
      lyris='준비중'
    else: 
      str_div = str(div_tags)
      lyris = str_div.split('-->')[1].split('</div')[0]
    #print('가사:',lyris)
    list_lyris.append(lyris)
  dic_title_lyris['list_title'] = list_title
  dic_title_lyris['list_lyris'] = list_lyris
  df_title_lyris = pd.DataFrame(dic_title_lyris)
  print(df_title_lyris)
  return df_title_lyris


##############################함수##############################함수##############################함수##############################함수##############################함수
def songidTolyris(df,si,ei):
  ### list_song_id => lyris 가져오기 함수
  df_title_lyris = songid_To_lyris(df['list_title'],df['list_song_id'])
  print(df_title_lyris)
  # csv 저장하기@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  df_title_lyris.to_csv(Path+"df_title_lyris_{}_{}.csv".format(si,ei), encoding='utf-8-sig')



##############################본문##############################본문##############################본문##############################본문##############################본문

# df pickle 불러오기!!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
with open(Path+'df_dropdup_title_songid_0~300.pkl', 'rb') as f:
    df_title_songid = pickle.load(f)
print(df_title_songid)
print(len(df_title_songid))


# 1000 단위로 8만곡 가져오기
# 1~85까지
"""for i in tqdm(range(10,12)):
  size = 1000
  si = size * i - size
  ei = size * i  
  df= df_title_songid.iloc[si:ei]
  df.drop(['index'],axis=1,inplace=True)
  df.reset_index(inplace=True)
  print(df)
  songidTolyris(df,si,ei)
"""
  
for j in range (1,8):
  start= j *10
  end = start + 2
  for i in tqdm(range(start,end)):
    size = 1000
    si = size * i - size
    ei = size * i  
    df= df_title_songid.iloc[si:ei]
    df.drop(['index'],axis=1,inplace=True)
    df.reset_index(inplace=True)
    print(df)
    songidTolyris(df,si,ei)
  



