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
        options=["Menpower of RO-4","Branch Categorization & Staff Scalewise","Dep ADV Data","FI Daily Data","Contact"],
    )
if selected == "Menpower of RO-4":
        st.header("Menpower of RO-4")
        import streamlit as st
        import pandas as pd
        excel_file = "excel1.csv"
        df = pd.read_csv(excel_file)

    # Allow users to select a column for filtering
        selected_category = st.selectbox("Select a Category:", df['Branch Nmae'].unique())

    # Create a filter for the selected column
        filtered_df = df[df['Branch Nmae'] == selected_category]

    # Display the filtered DataFrame
        st.write(filtered_df)
        st.write(df[["Branch Nmae","PF Code","Name Of Employee","Cader","AGE AS ON TODAY","TIME PERIOD"]])
        
        selected_category = st.selectbox("Select a Category:", df['TIME PERIOD'].unique())
        filtered_df = df[df['TIME PERIOD'] == selected_category]
        st.write(filtered_df)

if selected =="Branch Categorization & Staff Scalewise":
    st.header("Staff Scalewise")
    data = {
           'Cader': ['SMGS-IV', 'MMGS-III', 'MMGS-II', 'JMGS-I', 'Office Assistant', 'Office Attendant'],
           'No of Staff': [2, 8, 27, 58, 65, 11]
    }
# Create the bar chart
        fig = px.bar(data, x='Cader', y='No of Staff', labels={'No of Staff': 'No of Staff'})
# Show the chart in Streamlit app
        st.plotly_chart(fig)

    
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



    

        

