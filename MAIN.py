import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

st.image("SRGB_Logo.png",width=100)
st.title("SAURASHTRA GRAMIN BANK")
st.markdown(
    """
    ## WELCOME TO REGION OFFICE BHAVNAGAR
    """
)

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Menpower of RO-4","Dep ADV Data","FI Daily Data","Contact"],
    )
if selected == "Menpower of RO-4":
        st.header("Menpower of RO-4")
        st.write("Update Soon")
if selected =="Dep ADV Data":
        st.header("Deposits Advances Data")
        st.write("update soon")
if selected == ("FI Daily Data"):
        st.header("Financial Inclusion Data")
        st.write("Update Soon")
if selected == ("Contact"):
        st.write("Mr. Yashpalsinh G Gohil_7574808400")
        st.write("Mr. George Daniel_7574808042")
        st.write("Mr. J K Chudasama_7574808041")
        st.write("Kindly Contact Mr. H D Kar_7574808048 - for Techno Releted Work")
        st.write("Kindly Contact Mr. K T Purohit_7574808047 - for Audit Work")
        st.write("Kindly Contact Mr. P D Andharia_75")

def main():
    st.title("Main Menu")
    options=["Menpower of RO-4","Dep ADV Data","FI Daily Data","Contact"]
    choice = st.sidebar.selectbox("Main Menu",options)
    if choice == "Menpower of RO-4":
        st.header("Menpower of RO-4")
        st.write("Update Soon")
    elif choice =="Dep ADV Data":
        st.header("Deposits Advances Data")
        st.write("update soon")
    elif choice == ("FI Daily Data"):
        st.header("Financial Inclusion Data")
        st.write("Update Soon")
    elif choice == ("Contact"):
        st.write("Mr. Yashpalsinh G Gohil_7574808400")
        st.write("Mr. George Daniel_7574808042")
        st.write("Mr. J K Chudasama_7574808041")
        st.write("Kindly Contact Mr. H D Kar_7574808048 - for Techno Releted Work")
        st.write("Kindly Contact Mr. K T Purohit_7574808047 - for Audit Work")
        st.write("Kindly Contact Mr. P D Andharia_7574808046 - for PDS & Various Work")
    if __name__ == "__main__":
        main()

    

        

