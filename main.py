# Imports

from modules.p_acquisition import acquisition as aq
from modules.p_wrangling import wrangling as wr
from modules.p_analysis import analysis as an
from fuzzywuzzy import process

# Inputs

db1 = './data/raw/bicimad.db'
db2 = 'https://datos.madrid.es/egob/catalogo/209426-0-templos-catolicas.json'

# Argparse function

args = an.parse_arguments()

# Pipeline Execution

if args.all:
    bicimad_df1, places_df1 = aq.acquisition(db1, db2)
    bicimad_df = wr.wrangling_bicimad(bicimad_df1)
    places_df = wr.wrangling_places(places_df1)
    combined_df = an.combine_df(places_df, bicimad_df)
    df_distance = an.distance_df(combined_df)
    df_final = an.final_df(df_distance)
    csv_complete = an.create_csv(df_final)
    print('\n', csv_complete, '\n')
    
elif args.place:
    bicimad_df1, places_df1 = aq.acquisition(db1, db2)
    bicimad_df = wr.wrangling_bicimad(bicimad_df1)
    places_df = wr.wrangling_places(places_df1)
    place_name = args.place
    place_match = process.extractOne(place_name, places_df['Place of Interest'])
    if place_match[1] < 80:
        print("Sorry, no place was found matching the entered name.")
    else:
        place_name = place_match[0]
        combined_df = an.combine_df(places_df, bicimad_df)
        df_distance = an.distance_df(combined_df)
        df_final = an.final_df(df_distance)
        df_place = an.filter_place(df_final, place_name)
        csv_place = an.create_csv(df_place)
        print('\n', csv_place, '\n')
else:
    print('Please, select a valid option. Use argument --all to create a complete table or --place to indicate a place of interest.')