import pandas as pd
import streamlit as st

@st.cache( allow_output_mutation=True )
def get_data( path ):
    data = pd.read_csv( path )

    return data

def set_commercial( data ):


    st.sidebar.title( 'Commercial Options' )
    st.title( 'Commercial Attributes' )

    st.sidebar.subheader('Selling price  <  showroom price auto')

    # setup filters
    min_year = int( data['year'].min() )
    max_year = int( data['year'].max() )

    st.sidebar.subheader( 'Select Max Year' )
    f_year = st.sidebar.slider( 'Year Built Min', min_year, max_year, min_year )

    # setup filters
    min_km = int( data['km_driven'].min() )
    max_km = int( data['km_driven'].max() )

    st.sidebar.subheader( 'Select Max Km Driven' )
    f_km = st.sidebar.slider( 'Km Driven Max', min_km, max_km, min_km )

    # setup filters
    data['ownerint'] = data['owner'].apply(lambda x: 1 if x == '1st owner' else
    2 if x == '2nd owner' else
    3 if x == '3rd owner' else 4)

    min_owner = int(data['ownerint'].min())
    max_owner = int(data['ownerint'].max())


    st.sidebar.subheader( 'Select by Owner' )
    f_owner = st.sidebar.slider( 'Owner max', min_owner, max_owner, min_owner )

    # setup filters
    data['seller_int'] = data['seller_type'].apply(lambda x: 1 if x == 'Individual' else 2)
    min_seller = int(data['seller_int'].min())
    max_seller = int(data['seller_int'].max())

    st.sidebar.subheader( 'Select by Seller Type' )
    f_seller = st.sidebar.slider( 'Type seller, 1 for individual, 2 for Dealer', min_seller, max_seller, min_seller )


    st.header( 'Bikes to buy' )


    df = data.loc[(data['year'] >= f_year) &
                  (data['km_driven'] <= f_km) &
                  (data['ownerint'] == f_owner) &
                  (data['seller_int'] == f_seller) &
                  (data['selling_price'] < data['ex_showroom_price'])]

    st.write(df)

    return None

if __name__ == "__main__":
    # ETL

    path = 'D:/projeto mackenzie/bikes_completed.csv'

    # load data
    data = get_data(path)

    # transform data
    set_commercial(data)