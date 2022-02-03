from pathlib import Path
import glob
import os
import pandas as pd
import sys

#Variables in mc file
n = "nothing"
L = "Loss"
G = "Gain"
Lo = "Look"






var_table = {"names{1}='Outcome_Nothing'":[0,0], "names{2}='Outcome_Loss'": [0, 0], "names{3}='Outcome_Gain'": [0, 0], "names{4}='Outcome_Look'": [0, 0], "names{5}='Condition_Loss'": [0, 0], "names{6}='Condition_Gain'": [0, 0], "names{7}='Condition_Look'": [0, 0]}                                                                                    
var_table = pd.DataFrame(data=var_table)
var_table = var_table.drop(var_table.index[0:2])
var_table = var_table.T


zero = [0]



# root_dir needs a trailing slash (i.e. /root/dir/)
root = "C:/Users/bjgun/OneDrive - King's College London/CANDOWN/mc_files"
for filepath in glob.iglob(os.path.join(root, '**/*.csv'), recursive=True):
    f = Path(filepath)
    print(f"{f.name}:{f}")
    df = pd.read_csv(f)
    
    df = df.drop(df.index[90:98])
        
    nothing = df[df['Outcome'] == n]
    nothing = nothing.FeedbackOnset
    
    
    Outcome_nothing = []  
    for i in nothing:
        for z in zero:
            Outcome_nothing.append ([i, z])
            
    Outcome_nothing = pd.DataFrame (Outcome_nothing, columns= ["onsets{1}= [", "durations{1}= ["])
    Outcome_nothing.loc[len(Outcome_nothing)]=[']',']'] 
    
    Outcome_nothingT = Outcome_nothing.T
    
    Loss = df[df['Outcome'] == L]
    Loss = Loss.FeedbackOnset
    
    
    Outcome_Loss = []  
    for i in Loss:
        for z in zero:
            Outcome_Loss.append ([i, z])
            
    Outcome_Loss = pd.DataFrame (Outcome_Loss, columns= ["onsets{2}= [", "durations{2}= ["])
    Outcome_Loss.loc[len(Outcome_Loss)]=[']',']'] 
    
    Outcome_L_T = Outcome_Loss.T
    
       
    Gain = df[df['Outcome'] == G]
    Gain = Gain.FeedbackOnset
    
    
    Outcome_Gain = []  
    for i in Gain:
        for z in zero:
            Outcome_Gain.append ([i, z])
            
    Outcome_Gain = pd.DataFrame (Outcome_Gain, columns= ["onsets{3}= [", "durations{3}= ["])
    Outcome_Gain.loc[len(Outcome_Gain)]=[']',']'] 
    
    Outcome_G_T = Outcome_Gain.T
    
        
    Look = df[df['Outcome'] == Lo]
    Look = Look.FeedbackOnset
    
    
    Outcome_Look = []  
    for i in Look:
        for z in zero:
            Outcome_Look.append ([i, z])
            
    Outcome_Look = pd.DataFrame (Outcome_Look, columns= ["onsets{4}= [", "durations{4}= ["])
    Outcome_Look.loc[len(Outcome_Look)]=[']',']'] 
    
    Outcome_Lo_T = Outcome_Look.T
    
        
    Loss = df[df['Condition'] == L]
    Loss = Loss.FeedbackOnset
    

    Condition_Loss = []  
    for i in Loss:
        for z in zero:
            Condition_Loss.append ([i, z])
            
    Condition_Loss = pd.DataFrame (Condition_Loss, columns= ["onsets{5}= [", "durations{5}= ["])
    Condition_Loss.loc[len(Condition_Loss)]=[']',']'] 
    
    Condition_L_T = Condition_Loss.T
    
       
    Gain = df[df['Condition'] == G]
    Gain = Gain.FeedbackOnset
    
    
    Condition_Gain = []  
    for i in Gain:
        for z in zero:
            Condition_Gain.append ([i, z])
            
    Condition_Gain = pd.DataFrame (Condition_Gain, columns= ["onsets{6}= [", "durations{6}= ["])
    Condition_Gain.loc[len(Condition_Gain)]=[']',']'] 
    
    Condition_G_T = Condition_Gain.T
    
        
    Look = df[df['Condition'] == Lo]
    Look = Look.FeedbackOnset
    
    
    Condition_Look = []  
    for i in Look:
        for z in zero:
            Condition_Look.append ([i, z])
            
    Condition_Look = pd.DataFrame (Condition_Look, columns= ["onsets{7}= [", "durations{7}= ["])
    Condition_Look.loc[len(Condition_Look)]=[']',']'] 
    
    Condition_Lo_T = Condition_Look.T
    
    
    
    #SAVING
    mc = pd.concat([var_table, Outcome_nothingT, Outcome_L_T, Outcome_G_T, Outcome_Lo_T, Condition_L_T, Condition_G_T, Condition_Lo_T], axis=0)
    mc.to_csv(f'{filepath}_', sep='\t', header=False)
    
    save = (f'save mc_{f.name}') 
    save = save.replace(".csv", ".mat")  
    
    file = open(f'{filepath}_','a+')
    file.write('\n')
    file.write(str(save))
    file.close()  




folder = "C:/Users/bjgun/OneDrive - King's College London/CANDOWN/mc_files"
for filename in os.listdir(folder):
    infilename = os.path.join(folder,filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace('.csv_', '.m')
    output = os.rename(infilename, newname)

   



    
   
   
   
   
    
    
    
    
    
    
    
    
