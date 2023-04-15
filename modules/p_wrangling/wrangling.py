import pandas as pd

def wrangling_bicimad(df):
    df[['Longitude', 'Latitude']] = df['Coordinates'].str.strip('[]').str.split(pat = ',',\
                                                    expand = True, regex=False).apply(pd.to_numeric)
    df = df.drop('Coordinates', axis=1).reindex(columns=['BiciMAD Station','Station Location','Latitude','Longitude'])
    return df

def wrangling_places(df):
    df = df[['title','@type','address.street-address','location.latitude','location.longitude']]
    df = df.rename(columns={'title': 'Place of Interest','@type':'Type of Place',\
                                        'address.street-address':'Place Address',\
                                       'location.latitude':'Latitude','location.longitude':'Longitude'})
    df['Type of Place'] = df['Type of Place'].str.extract('/entidadesYorganismos/(\w+)')
    df['Type of Place'] = df['Type of Place'].str.findall('[A-Z][^A-Z]*').str.join(' ')
    df['Place Address'] = df['Place Address'].str.title()
    df=df.loc[df['Type of Place'] == "Templos Iglesias Catolicas"]

    return df