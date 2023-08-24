import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.express as px

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
        options=["Staff-Position of RO-4","Branch Categorization & Staff Scalewise","Deposits Advances Data","FI Data","VISION & MISSION"]
    )
if selected == "Menpower of RO-4":
    st.header("Menpower of RO-4")
    import streamlit as st
    import pandas as pd
    excel_file = "STAFF.csv"
    df = pd.read_csv(excel_file)
    selected_category = st.selectbox("Select a Category:",df['Branch Name'].unique())
    filtered_df = df[df['Branch Name'] == selected_category]
    st.write(filtered_df)
    st.write(df[["Branch Name","PF Code","Name Of Employee","Cader","AGE AS ON TODAY","TIME PERIOD"]])

if selected == "Branch Categorization & Staff Scalewise":
    st.header("Staff Scalewise")
    data = {
        'Cader': ['SMGS-V','SMGS-IV','MMGS-III','MMGS-II','JMGS-I','OFFICE ASSISTANT','OFFICE ATTENDANT'],
        'No of Staff': [1, 1, 9, 27, 61, 62, 11]
    }
    fig = px.bar(data, x='Cader', y='No of Staff', labels={'No of Staff': 'No of Staff'})
    st.plotly_chart(fig)

if selected == "Deposits Advances Data":
    import streamlit as st
    import pandas as pd
    import openpyxl
    st.header("DEPOSITS As of 21.08.23")
    excel_file1 = "210823ADV.xlsx"
    df = pd.read_excel(excel_file1)
    selected_category = st.selectbox("Select a Category:",df['BRANCH'].unique())
    filtered_df = df[df['BRANCH'] == selected_category]
    st.write(filtered_df[["CODE","BRANCH","DEP 31.03.23","DEP 31.07.23","DEP 21.08.23","VARIANCE MAR-23","VARIANCE JULY-23"]])
    st.header("ADVANCES As of 21.08.23")
    excel_file2 = "210823ADV.xlsx"
    df2 = pd.read_excel(excel_file2,"ADV")
    st.dataframe(df2)
    st.header("TOTAL BUSINESS As of 21.08.23")
    excel_file2 = "210823ADV.xlsx"
    df2 = pd.read_excel(excel_file2,"TOTAL")
    st.dataframe(df2,width=2000)

if selected == "FI Data":
    import pandas as pd
    import openpyxl
    st.header("Finance Inclusion & Cross Selling Data As on 21.08.23")
    excel_file1 = "210823ADV.xlsx"
    df = pd.read_excel(excel_file1,"FI")
    selected_category = st.selectbox("Select a Category:",df['Branch Name'].unique())
    filtered_df = df[df['Branch Name'] == selected_category]
    st.dataframe(filtered_df,width=1500)
    st.dataframe(df,width=1500)

if selected == "VISION & MISSION":
    import streamlit as st
    st.title("VISION")
    st.markdown("### Building a Professionally sound institute to cater to the Banking needs of the people of Saurashtra inter-alia covering deprived masses.")
    st.title("MISSION")
    st.markdown("### To cater to the banking needs of people of Saurashtra through ace products, delighted customer service and financial improvement of the targeted mass with a team of self-motivated manpower,advanced technology and well defined system & procedures.")





    
    
   
