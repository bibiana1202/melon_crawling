from distutils.errors import DistutilsFileError
import pandas as pd

# concat
path='/Volumes/GoogleDrive/내 드라이브/nlp_project/전처리/'


# 연도별 데이터 불러와 각각 dataframe 만들기
df1 = pd.read_csv(path+"df_title_lyris_0_1000.csv", sep=',', index_col=False, dtype='unicode')
df2 = pd.read_csv(path+"df_title_lyris_1000_2000.csv", sep=',', index_col=False, dtype='unicode')
df3 = pd.read_csv(path+"df_title_lyris_2000_3000.csv", sep=',', index_col=False, dtype='unicode')
df4 = pd.read_csv(path+"df_title_lyris_3000_4000.csv", sep=',', index_col=False, dtype='unicode')
df5 = pd.read_csv(path+"df_title_lyris_4000_5000.csv", sep=',', index_col=False, dtype='unicode')
df6 = pd.read_csv(path+"df_title_lyris_5000_6000.csv", sep=',', index_col=False, dtype='unicode')
df7 = pd.read_csv(path+"df_title_lyris_6000_7000.csv", sep=',', index_col=False, dtype='unicode')
df8 = pd.read_csv(path+"df_title_lyris_7000_8000.csv", sep=',', index_col=False, dtype='unicode')
df9 = pd.read_csv(path+"df_title_lyris_8000_9000.csv", sep=',', index_col=False, dtype='unicode')
df10 = pd.read_csv(path+"df_title_lyris_9000_10000.csv", sep=',', index_col=False, dtype='unicode')
df11 = pd.read_csv(path+"df_title_lyris_19000_20000.csv", sep=',', index_col=False, dtype='unicode')
df12 = pd.read_csv(path+"df_title_lyris_20000_21000.csv", sep=',', index_col=False, dtype='unicode')
df13 = pd.read_csv(path+"df_title_lyris_29000_30000.csv", sep=',', index_col=False, dtype='unicode')
df14 = pd.read_csv(path+"df_title_lyris_30000_31000.csv", sep=',', index_col=False, dtype='unicode')
df15 = pd.read_csv(path+"df_title_lyris_39000_40000.csv", sep=',', index_col=False, dtype='unicode')
df16 = pd.read_csv(path+"df_title_lyris_40000_41000.csv", sep=',', index_col=False, dtype='unicode')
df17 = pd.read_csv(path+"df_title_lyris_49000_50000.csv", sep=',', index_col=False, dtype='unicode')
df18 = pd.read_csv(path+"df_title_lyris_50000_51000.csv", sep=',', index_col=False, dtype='unicode')
df19 = pd.read_csv(path+"df_title_lyris_59000_60000.csv", sep=',', index_col=False, dtype='unicode')
df20 = pd.read_csv(path+"df_title_lyris_60000_61000.csv", sep=',', index_col=False, dtype='unicode')
df21 = pd.read_csv(path+"df_title_lyris_69000_70000.csv", sep=',', index_col=False, dtype='unicode')

# 여러 dataframe 연결해 하나의 dataframe으로 만들기
df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10,df11,df12,df13,df14,df15,df16,df17,df18,df19,df20,df21]
               , ignore_index=True)
print(df)

df.to_csv(path+'df_title_lyris.csv')