import pandas as pd


df = pd.read_csv("C:/Users/bjgun/OneDrive - King's College London/CANDOWN/mc_files/CANDOWN_megafile.csv")

df["ResponseButton"] = df["ResponseButton"].str.replace('Left','go')
df["ResponseButton"] = df["ResponseButton"].str.replace('Right','go')


df.Condition.unique()
df.Outcome.unique()


df.ResponseButton.unique()
df.ResponseButton.value_counts()
df.ChosenPosition.unique()

#%% 

def drug (row):
   if row['SubjectID'] == '03':
       return 'PLB'
   if row['SubjectID'] == 'CAD001B':
       return 'PLB'
   if row['SubjectID'] == 'CAD002A':
       return 'PLB'
   if row['SubjectID'] == 'CAD003A':
       return 'THC'
   if row['SubjectID'] == 'CAD004A':
       return 'PLB'
   if row['SubjectID'] == 'CAD004B':
       return 'THC'
   if row['SubjectID'] == 'CAD005A':
       return 'PLB'
   if row['SubjectID'] == 'CAD005B':
       return 'THC'
   if row['SubjectID'] == 'CAD006A':
       return 'PLB'
   if row['SubjectID'] == 'CAD006B':
       return 'THC'
   if row['SubjectID'] == 'CAD007A':
       return 'THC'
   if row['SubjectID'] == 'CAD007B':
       return 'THC'
   if row['SubjectID'] == 'CAD008A':
       return 'THC'
   if row['SubjectID'] == 'CAD008B':
       return 'PLB'
   if row['SubjectID'] == 'CAD009A':
       return 'THC'
   if row['SubjectID'] == 'CAD009B':
       return 'PLB'
   if row['SubjectID'] == 'CAD010A':
       return 'THC'
   if row['SubjectID'] == 'CAD010B':
       return 'PLB'
   if row['SubjectID'] == 'CAD011A':
       return 'PLB'
   if row['SubjectID'] == 'CAD011B':
       return 'THC'
   if row['SubjectID'] == 'CAD012A':
       return 'PLB'
   if row['SubjectID'] == 'CAD012B':
       return 'THC'
   if row['SubjectID'] == 'CAD013A':
       return 'THC'
   if row['SubjectID'] == 'CAD013B':
       return 'PLB'
   if row['SubjectID'] == 'CAD014A':
       return 'PLB'
   if row['SubjectID'] == 'CAD014B':
       return 'THC'
   if row['SubjectID'] == 'CAD015B':
       return 'PLB'
   if row['SubjectID'] == 'CANDOWN02':
       return 'THC'
   if row['SubjectID'] == 'CANDOWN15':
       return 'THC'
   if row['SubjectID'] == 'CANDOWN16':
       return 'THC'
   else:
       return 'False'

#%%
drug= df.apply (lambda row: drug(row), axis=1).copy()
drug = drug.to_frame()
drug.rename(columns={0: 'drug'}, inplace=True)


df = pd.merge(df, drug, how='outer', left_index=True, right_index=True)

df['SubjectID'] = df['SubjectID'].str.replace(r'\D', '').astype(int)
df= df.sort_values(by=['SubjectID'], ascending=True)
df = df.reset_index()
df.drop(['index'], axis=1, inplace=True)


df['SubjectID'] = df['SubjectID'].apply(str)
df['SubjectID'] = df['SubjectID'] + df['Visit']


paired = df[df.SubjectID != 1].copy()
paired = paired[paired.SubjectID != 16]

unpaired = df.copy()


#%%
    #2) RT time of GO trials= (TimeAtResponse - ImageOnset)
go_trials = paired[paired['Condition'].isin(['Gain', 'Loss'])].copy()

go_trials["ImageOnset"] = pd.to_numeric(go_trials["ImageOnset"])
go_trials["TimeAtResponse"]= pd.to_numeric(go_trials["TimeAtResponse"], errors='coerce')


rt_time= (go_trials.TimeAtResponse - go_trials.ImageOnset).copy()
rt_time = rt_time.to_frame()
rt_time.rename(columns={0: 'rt_time'}, inplace=True)

go_trials = pd.merge(go_trials, rt_time, how='outer', left_index=True, right_index=True)

go_trials.groupby(['drug']).rt_time.agg(['mean', 'std']) 

go_trials = go_trials.dropna(subset=['rt_time'])


#NOTE, use 
#response.groupby(['SubjectID']).agg(['mean', 'std'])
#for all columns
#Just have to drop uncessary columns if want

#%%


    #3) % of GO responses= ResponseButton(Left+Right/Left+None+Right)

counts= df.groupby(['SubjectID', 'ResponseButton', 'drug']).size().copy()
percentage = counts.groupby(level=0).apply(lambda x:
                                                 100 * x / float(x.sum()))
percentage = percentage.to_frame()
percentage.rename(columns={0: 'percent'}, inplace=True)

percentage.groupby(['ResponseButton', 'drug']).percent.agg(['mean', 'std']) 


#%%

    #4) % of correct responses= ((Condition[Gain]+Outcome[Gain]+(Condition[Loss]+Outcome[Nothing]) / (Condition[Gain]+Condition[Loss])) *100
def correct_response (row):
   if row['Condition'] == 'Gain' and row['Outcome'] == 'Gain':
       return 'True'
   if row['Condition'] == 'Loss' and row['Outcome'] == 'nothing':
       return 'True'
   else:
       return 'False'
   
correct= df.apply (lambda row: correct_response(row), axis=1).copy()
correct = correct.to_frame()
correct.rename(columns={0: 'correct'}, inplace=True)


df = pd.merge(df, correct, how='outer', left_index=True, right_index=True)

correct_counts= df.groupby(['SubjectID', 'correct']).size()


correct_percentage = correct_counts.groupby(level=0).apply(lambda x:
                                                 100 * x / float(x.sum()))

    
#df.to_csv('df.csv', index=False)
       
        




