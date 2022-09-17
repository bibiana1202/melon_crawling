import requests
import time
import json
import pandas as pd
from bs4 import BeautifulSoup
import re
import time
from tqdm import tqdm
import pickle

Path = '/Volumes/GoogleDrive/내 드라이브/project/NLP_project/크롤링/'
start_page=0
end_page=300

########################################## 노래 제목, Songid LIST 만들어주는 함수########################################################
########################################## 노래 제목, Songid LIST 만들어주는 함수########################################################
########################################## 노래 제목, Songid LIST 만들어주는 함수########################################################
def make_title_songid_list(gnr):
  list_title=[]
  list_song_id=[]
  
  ##### 200 page 도는 for문!!!!(700페이지에서 터짐) ##############################
  # 200*50 = 10000곡....
  start_index=0 # 0~300 page
  
  for page in tqdm(range(start_index+start_page,start_index+end_page)):
    print('###############################################################################################################################################')
    url_page = 50 * page + 1
    print(gnr,'gnr',page,'page',url_page,'grade')
    time.sleep(4)
    url = "https://www.melon.com/genre/song_listPaging.htm?startIndex={}&pageSize=50&gnrCode={}&dtlGnrCode=&orderBy=NEW&steadyYn=N".format(url_page,gnr)
    hdr={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    ,'Cookie': '__T_=1; PC_PCID=16631563285767874076636; PCID=16631563285767874076636; POC=WP10; wcs_bt=s_f9c4bde066b:1663156864; _T_ANO=D1p5pHkCi4UZgITrzyDhJuyv4/S1yJpEs4DVul2v0su07PV3NtTuvJAvk+kP382/PC230QK2JUhQ8xB+QoSAaUyLzivM4d+nWoVPvi99v6bVTpmSiskNnIEEt/vLLU/gZS+NxNSsW77JcQvZV5ZDlV/t3/aeZeubbSfktjQMItaNe7jLPljHU/bO8owf2gORzxveR5yesGx++scXKrhYbXXdrsOeGblrz7qc6MpL5ytLm5H/PEu9l/kXrDgQzVpYK+RQLtcX3zL2eNbBsA/Xq+Y0Zy5PFCOc6PV6WZPGZFaaqWj9baDPxCsaMg19IOtkVtKBOiM7zDwFG6UfsVkOWQ=='
    ,'Referer': 'https://www.melon.com/genre/song_list.htm?gnrCode=GN0100&dtlGnrCode='
    }

    res = requests.get(url, headers=hdr)
    # text 존재함? print
    print(res,len(res.text),res.url)

    soup = BeautifulSoup(res.text, 'html.parser')
    soup.select('tbody tr div.wrap a')[1]
    a_tags = soup.select('tbody tr div.wrap a.btn.button_icons')
    print(len(a_tags))

    for i,v in tqdm(enumerate(a_tags)):
      href= a_tags[i]['href']
      # song_id 가져오기
      song_id = re.sub(r'[^0-9]', '', href)
      # title 가져오기
      title=a_tags[i]['title'].split('곡정보')[0]
      list_title.append(title)
      list_song_id.append(song_id)

    print(len(list_title),len(list_song_id))
    print(list_title[url_page-1],list_song_id[url_page-1]) # 1등, 51등, 101등,..
    print('###############################################################################################################################################')
   ################################################################################


  import pickle
  # 혹시 몰라 list pickle 저장
  with open(Path+'save/list_title_{}_{}~{}.pkl'.format(gnr,start_page,end_page),"wb") as f:
    pickle.dump(list_title, f)
   # 혹시 몰라 list pickle 저장
  with open(Path+'save/list_song_id_{}_{}~{}.pkl'.format(gnr,start_page,end_page),"wb") as f:
    pickle.dump(list_song_id, f)

  return list_title,list_song_id

############################################################################################################################################

# dic 에 저장하기

    # 1. 발라드 GN0100
    # 2. 댄스 GN0200
    # 3. 랩/힙합 GN0300
    # 4. R&B GN0400
    # 5. 인디 GN0500
    # 6. 록 메탈 GN0600
    # 7. 트로트 GN0700
    # 8. 포크 GN0800


# 1.노래 제목, song_id list 만들어 주는 함수
list_title_1, list_song_id_1 = make_title_songid_list('GN0100')
list_title_2, list_song_id_2 = make_title_songid_list('GN0200')
list_title_3, list_song_id_3 = make_title_songid_list('GN0300')
list_title_4, list_song_id_4 = make_title_songid_list('GN0400')
list_title_5, list_song_id_5 = make_title_songid_list('GN0500')
list_title_6, list_song_id_6 = make_title_songid_list('GN0600')
list_title_7, list_song_id_7 = make_title_songid_list('GN0700')
list_title_8, list_song_id_8 = make_title_songid_list('GN0800')


print(len(list_title_1),len(list_song_id_1))
print(len(list_title_2),len(list_song_id_2))
print(len(list_title_3),len(list_song_id_3))
print(len(list_title_4),len(list_song_id_4))
print(len(list_title_5),len(list_song_id_5))
print(len(list_title_6),len(list_song_id_6))
print(len(list_title_7),len(list_song_id_7))
print(len(list_title_8),len(list_song_id_8))

# list -> dic로 만들기
dic_title_songid_ver ={}


dic_title_songid_ver['list_title_1'] = list_title_1
dic_title_songid_ver['list_title_2'] = list_title_2
dic_title_songid_ver['list_title_3'] = list_title_3
dic_title_songid_ver['list_title_4'] = list_title_4
dic_title_songid_ver['list_title_5'] = list_title_5
dic_title_songid_ver['list_title_6'] = list_title_6
dic_title_songid_ver['list_title_7'] = list_title_7
dic_title_songid_ver['list_title_8'] = list_title_8

dic_title_songid_ver['list_song_id_1'] = list_song_id_1
dic_title_songid_ver['list_song_id_2'] = list_song_id_2
dic_title_songid_ver['list_song_id_3'] = list_song_id_3
dic_title_songid_ver['list_song_id_4'] = list_song_id_4
dic_title_songid_ver['list_song_id_5'] = list_song_id_5
dic_title_songid_ver['list_song_id_6'] = list_song_id_6
dic_title_songid_ver['list_song_id_7'] = list_song_id_7
dic_title_songid_ver['list_song_id_8'] = list_song_id_8


# dic -> df 만들기
df_title_songid_ver  = pd.DataFrame(dic_title_songid_ver)

# df pickle 저장@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
with open(Path+"df_title_songid_ver_{}_{}~{}.pkl".format(len(df_title_songid_ver),start_page,end_page),"wb") as f:
    pickle.dump(df_title_songid_ver, f)
# df pickle 저장@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

print(len(dic_title_songid_ver),len(dic_title_songid_ver['list_title_1']))


# 모아서 dic !!

dic_title_songid ={}

list_title =[]
list_song_id=[]
list_title.extend(list_title_1)
list_title.extend(list_title_2)
list_title.extend(list_title_3)
list_title.extend(list_title_4)
list_title.extend(list_title_5)
list_title.extend(list_title_6)
list_title.extend(list_title_7)
list_title.extend(list_title_8)


list_song_id.extend(list_song_id_1)
list_song_id.extend(list_song_id_2)
list_song_id.extend(list_song_id_3)
list_song_id.extend(list_song_id_4)
list_song_id.extend(list_song_id_5)
list_song_id.extend(list_song_id_6)
list_song_id.extend(list_song_id_7)
list_song_id.extend(list_song_id_8)

dic_title_songid['list_title'] = list_title
dic_title_songid['list_song_id'] = list_song_id

# dic->df
df_title_songid  = pd.DataFrame(dic_title_songid)

# df 중복치 제거
df_title_songid.drop_duplicates(['list_title'],inplace=True)

df_title_songid.drop_duplicates(['list_song_id'],inplace=True)

df_title_songid.reset_index(inplace=True)

print(len(df_title_songid.columns),len(df_title_songid),len(df_title_songid['list_title']))
print(df_title_songid)

# df pickle 저장@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
with open(Path+"df_dropdup_title_songid_{}~{}.pkl".format(start_page,end_page),"wb") as f:
    pickle.dump(df_title_songid, f)





