import sys
import tabula
import pandas as pd
def main():
    #Author: Santosh Kolur
    #Purpose: Convert tables in pdf to csv
    name=sys.argv
    for i in range(1,len(name)):
        df=tabula.read_pdf(name[i],pages='all')
        for j in range(len(df)):
            print('.',end='')
            file='table_'+str(j)+'.csv'
            file=name[i][:-4]+'/'+file
            df[j].to_csv(file)
if __name__=="__main__":
    main()
        