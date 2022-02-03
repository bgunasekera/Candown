import pandas as pd
import seaborn as sns


df = pd.read_csv("C:/Users/bjgun/OneDrive - King's College London/CANDOWN/mc_files/CANDOWN_megafile.csv")
df.Condition.unique()

#%%

sns.set_theme(style="ticks", color_codes=True)

sns.catplot(x="ResponseButton", col="SubjectID", data=df, kind="count", col_wrap=6,
                height=4, aspect=.7);
#%%
sns.catplot(x="ChosenPosition", col="SubjectID", data=df, kind="count", col_wrap=6,
                height=4, aspect=.7);

#%%
matrix = df[['SubjectID', 'Visit','Condition', 'Outcome', 'ConditionStimPos', 'ChosenPosition']].copy()
matrix = matrix[matrix['Condition'] != 'Look']

#%%
def conditions(s):
    if (s['Condition'] == 'Gain') and (s['ConditionStimPos'] == 'Top'):
        return 21
    if (s['Condition'] == 'Gain') and (s['ConditionStimPos'] == 'Bottom'):
        return 12
    if (s['Condition'] == 'Loss') and (s['ConditionStimPos'] == 'Top'):
        return 43
    if (s['Condition'] == 'Loss') and (s['ConditionStimPos'] == 'Bottom'):
        return 34   
    
matrix['type'] = matrix.apply(conditions, axis=1)


#%%
matrix["SubjectID"] = matrix["SubjectID"] + matrix["Visit"]

#%%
def conditions(s):
    if (s['ConditionStimPos'] == 'Top'):
        return 1
    if (s['ConditionStimPos'] == 'Bottom'):
        return 0

matrix['choice'] = matrix.apply(conditions, axis=1)


#%%         
def conditions(s):
    if (s['Condition'] == 'Gain') and (s['Outcome'] == 'Gain'):
        return 1
    if (s['Condition'] == 'Gain') and (s['Outcome'] == 'nothing'):
        return 0
    if (s['Condition'] == 'Loss') and (s['Outcome'] == 'nothing'):
        return 0
    if (s['Condition'] == 'Loss') and (s['Outcome'] == 'Loss'):
        return -1    
    
matrix['reward'] = matrix.apply(conditions, axis=1)

#%%
matrix = matrix.drop(columns=['Visit', 'Condition', 'Outcome', 'ConditionStimPos', 'ChosenPosition'])
matrix = matrix.rename(columns={'SubjectID': 'subjID'})
matrix = matrix.dropna()



#%%
matrix.to_csv('RL_matrix_pstQ.csv', index=False)
