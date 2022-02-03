import os
import glob
import pandas as pd
os.chdir("C:/Users/bjgun/OneDrive - King's College London/CANDOWN/mc_files")


extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]


#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
combined_csv = combined_csv.drop(combined_csv.index[90:98])


#export to csv
combined_csv.to_csv( "CANDOWN_megafile.csv", index=False, encoding='utf-8-sig') 





