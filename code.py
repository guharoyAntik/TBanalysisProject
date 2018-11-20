import pandas as pd 
import geopandas as gpd
    
def plotMap(merged):
    colors = 10
    cmap = 'Blues'
    col = 'Subjects'
    figsize = (16, 10)
    
    ax = merged.dropna().plot(column = col, cmap=cmap, figsize = figsize, scheme ='quantiles', k = colors, legend = True)

if __name__ == '__main__':
    df = pd.read_csv('TB_dataset.csv', usecols=['country', 'c_newinc'])
    df.fillna(value = 0, inplace = True)
    df = df.groupby('country').sum()
    df = df.reset_index()

    info = pd.DataFrame()
    
    for curCountry in df['country']:
        cur = df[df['country'] == curCountry]
        info = pd.concat([info, cur])

    info.columns = ['NAME', 'Subjects']
       
    world = gpd.read_file('countries.shx')[['NAME', 'geometry']]
    merged = world.merge(info, left_on = 'NAME', right_on = 'NAME')
    
    plotMap(merged)