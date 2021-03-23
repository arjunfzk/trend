# Core Pkgs
import streamlit as st # NLP Pkgs
import tweepy
import tweepy as tw
import pandas as pd
df=pd.DataFrame()
auth = tweepy.OAuthHandler('', '')
auth.set_access_token('', '')

api = tweepy.API(auth)







def main():
    """A Simple NLP app with Spacy-Streamlit"""
    st.title("Twitter trends analysis App  ")
    menu = ["Top trends by Country","Search twitter"]
    choice = st.selectbox("Menu",menu)
    if choice == "Top trends by Country":
                    st.subheader("Select country")
                    menun = ["India","Worldwide"]
                    choice1 = st.selectbox("Menun",menun)

                    if choice1 == "India":
                        trends=api.trends_place(23424848)
                        lis1=[]
                        lis2=[]
                        for tweet in trends[0]['trends']:
                            lis1.append(tweet['name'])
                            lis2.append(tweet['tweet_volume'])
                        df['Name']=lis1
                        df['Count']=lis2
                        st.write(df)

                    if choice1 == "Worldwide":
                        trends=api.trends_place(1)
                        lis1=[]
                        lis2=[]
                        for tweet in trends[0]['trends']:
                            lis1.append(tweet['name'])
                            lis2.append(tweet['tweet_volume'])
                        df['Name']=lis1
                        df['Count']=lis2
                        st.write(df)


    if choice == "Search twitter":
                    st.subheader("Enter Keywords")
                    raw_text = st.text_area("")
                    if len(raw_text)>1:
                        search_words = raw_text
                        new_search = search_words + " -filter:retweets"
                        tweets = tw.Cursor(api.search,
                                  q=new_search,
                                  lang="en",).items(10)
                        for tweet in tweets:
                               st.markdown(tweet.text)














if __name__ == '__main__':
    main()
