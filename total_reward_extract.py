import os
import glob
import pandas as pd
import pingouin as pt



os.chdir("C:/Users/bjgun/OneDrive - King's College London/CANDOWN/mc_files")


extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]


#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
combined_csv = (combined_csv.loc[[89, 90]])


subj= (combined_csv.loc[[89]])
reward = (combined_csv.loc[[90]])

subj.reset_index(drop=True, inplace=True)
reward.reset_index(drop=True, inplace=True)


Merge = pd.merge(subj, reward, how='outer', left_index=True, right_index=True).copy()
Merge = Merge[['SubjectID_x', 'SubjectID_y', 'Visit_x']].copy()
Merge[['A', 'total_reward']] = Merge['SubjectID_y'].str.split('£', 1, expand=True)

Merge.drop(['SubjectID_y', 'A'], axis=1, inplace=True)

Merge["total_reward"]= pd.to_numeric(Merge["total_reward"], errors='coerce')

drug = {'drug': ['PLB','PLB','PLB','THC','PLB','THC','PLB','THC','PLB','THC','THC','PLB','THC','PLB','THC','PLB','THC','PLB','PLB','THC','PLB','THC','THC','PLB','PLB','THC','PLB','THC','THC','THC','x' ]}
drug = pd.DataFrame(data=drug)


Merge = pd.merge(Merge, drug, how='outer', left_index=True, right_index=True)
Merge = Merge.drop([30])
Merge = Merge.drop([1, 29]) #These do not have pairs. See 'scans and mc files' spreadsheet

Merge['SubjectID_x'] = Merge['SubjectID_x'].str.replace(r'\D', '').astype(int)
Merge= Merge.sort_values(by=['SubjectID_x'], ascending=True)
Merge = Merge.reset_index()
Merge.drop(['index'], axis=1, inplace=True)



Merge.groupby(['drug']).total_reward.agg(['mean', 'std']) 

thc = Merge.query('drug == "THC"')['total_reward'].copy()
plb = Merge.query('drug == "PLB"')['total_reward'].copy()

test = pt.ttest(plb, thc, paired=True)
