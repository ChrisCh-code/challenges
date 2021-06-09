import pandas as pd



def main():
    url = 'https://data.cityofnewyork.us/api/views/833y-fsy8/rows.csv?accessType=DOWNLOAD'
    df = pd.read_csv(url)
    
    sorted_column_name = sorted(list(df.columns.values))
    row_count = df.shape[0]
    
    df['COORD'] = df['X_COORD_CD'].str.replace(',','').astype(int) + df['Y_COORD_CD'].str.replace(',','').astype(int)
    
    print('Sorted columns: ', sorted_column_name)
    print('row count: ', row_count)
    
    df.to_csv('new_data.csv')
    
