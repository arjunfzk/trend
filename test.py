# Core Pkgs
import streamlit as st # NLP Pkgs
                      
from pytrends.request import TrendReq
pytrend = TrendReq()



def main():
    st.title("Google trends analysis App  ")
    menu = ["Top trends by Country","Search Google Trends"]
    choice = st.selectbox("Menu",menu)
    if choice == "Top trends by Country":
                    st.subheader("Select country")
                    menun = ["India","Worldwide"]
                    choice1 = st.selectbox("Menun",menun)

                    if choice1 == "India":
                        df = pytrend.trending_searches(pn='india')
                        st.write(df)

                    if choice1 == "Worldwide":
                        df = pytrend.trending_searches()
                        st.write(df)


    if choice == "Search Google Trends":
                    st.subheader("Enter Keywords")
                    raw_text = st.text_area("")
                    if len(raw_text)>1:
                        search_words = raw_text
                        kw_list = []
                        kw_list.append(raw_text)
                        pytrend.build_payload(kw_list,geo='IN',timeframe='now 7-d')
                        df=pytrend.interest_by_region(resolution='COUNTRY', inc_low_vol=True)
                        st.write(df)














if __name__ == '__main__':
    main()
