import pandas as pd
import streamlit as st

def add_bg_from_url():
    st.markdown(
        """
        <style>
        .stApp {{
            background-image: url("marek-okon-tWWCqIMiUmg-unsplash.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function to add the background image
add_bg_from_url()

df=pd.read_csv('genres_v2.csv')

df=df.drop(['Unnamed: 0','type','id','uri','track_href','analysis_url','song_name','title','key','mode','time_signature'],axis=1)
df=df.dropna(axis=0)
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['genre']=le.fit_transform(df['genre'])

x=df.iloc[:,[0]].values

from sklearn.cluster import KMeans

km=KMeans(n_clusters=3)
y_hat1=km.fit_predict(x)

df1=pd.read_csv('genres_v2.csv')
cx=df1.iloc[:,:].values

s2=pd.DataFrame()
s2['high danceability']=pd.DataFrame(cx[y_hat1==1,13])
s2['danceability']=df1[['danceability']]

s2=s2.sort_values(by='danceability',ascending=False)
s2=s2.iloc[:5,:]
print(s2)

##streamlit framework 



def reset_state():
    st.session_state.q3 = 'Select Your Mode'
    st.session_state.open_playlist = False
    st.session_state.show_dance = False
    st.session_state.show_rap = False

def reset_state2():
    st.session_state.open_playlist = False
    st.session_state.show_dance = False
    st.session_state.show_rap = False

if st.button('Home'):
    reset_state()
st.title('Welcome to song world')



# Initialize session state
if 'q3' not in st.session_state:
    st.session_state.q3 = 'Select Your Mode'
if 'open_playlist' not in st.session_state:
    st.session_state.open_playlist = False
if 'show_dance' not in st.session_state:
    st.session_state.show_dance = False
if 'show_rap' not in st.session_state:
    st.session_state.show_rap = False

q3 = st.selectbox("Listen Songs of Your Mood", options=('Select Your Mode', 'happy', 'sad'), index=('Select Your Mode', 'happy', 'sad').index(st.session_state.q3))    


if q3 == 'happy':
    reset_state2()
    st.session_state.q3 ='happy'
    st.write('Chill by listening to these happy songs')

# Main button to open the playlist
if st.button('Open Playlist'):
    st.session_state.open_playlist = True

# Display the playlist options if the playlist is open
if st.session_state.open_playlist:
    st.header("Playlist")
    col1, col2 = st.columns(2)
    with col1:
        if st.button('🎧 For Dance'):
            st.session_state.show_dance = True
            st.session_state.show_rap = False  # Reset the other button state
    with col2:
        if st.button('rap'):
            st.session_state.show_dance = False  # Reset the other button state
            st.session_state.show_rap = True

    # Display the corresponding playlist based on the button clicked
    if st.session_state.show_dance:
        st.write("High Danceability Songs")
        for index, row in s2.iterrows():
            st.write(f'{row[0]}')
            st.write(f'[Click to Listen]({row[0]})')
    if st.session_state.show_rap:
        st.write("High Rap Songs")
        # Add your code for rap songs here
    








