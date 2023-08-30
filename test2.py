import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv(r"C:\Users\JeAdkins\OneDrive - CreditOne Bank\Documents\Data_Test.csv", dtype="unicode")

clist = df['Vintage'].unique()
clist1 = df['FirstSecond'].unique()
clist2 = df['Branding']. unique()
clist3 = df['Channel'].unique()
clist4 = df['Source'].unique()
clist5 = df['Association'].unique()
clist6 = df['AnnualFeeGroup'].unique()
clist7 = df['OriginalCreditLineRange'].unique()

#initialize default dataframe to hold ALL csv data
if 'df_default' not in st.session_state:
    st.session_state['df_default'] = df
    
#initialize blank dataframe to hold new df created from user filters
if 'blank_df' not in st.session_state:
    st.session_state['blank_df'] = pd.DataFrame(columns=[
        "Vintage", "FirstSecond", 'Branding', 'Channel', 'Source', 
        'Association', 'AnnualFeeGroup', "OriginalCreditLineRange", "MonthsOnBooks", "NewAccountIndicator", 
        "ActiveAccountIndicator", "PreTaxIncome", "EndingReceivable", "CumlNewAccountIndicator", "CumlActiveAccountIndicator", 
        "CumlPreTaxIncome", "CumlEndingReceivable", "AverageActives", "AverageReceivable", "CumlROA", "CumlROAAnnualized"])

if "added_df" not in st.session_state:
    st.session_state['added_df'] = pd.DataFrame(columns=[
        "Vintage", "FirstSecond", 'Branding', 'Channel', 'Source', 
        'Association', 'AnnualFeeGroup', "OriginalCreditLineRange", "MonthsOnBooks", "NewAccountIndicator", 
        "ActiveAccountIndicator", "PreTaxIncome", "EndingReceivable", "CumlNewAccountIndicator", "CumlActiveAccountIndicator", 
        "CumlPreTaxIncome", "CumlEndingReceivable", "AverageActives", "AverageReceivable", "CumlROA", "CumlROAAnnualized"])

if "isOnLoadDisplay" not in st.session_state:
    st.session_state['isOnLoadDisplay'] = True;
    
if "isDfAdded" not in st.session_state:
    st.session_state['isDfAdded'] = False;
    

    

def main():
    if submit:
        #filter original df using selected values
        #create a new df from the filtered entire df
        df_new = df.loc[(df['Vintage'] == selected) 
              & (df['FirstSecond'] == FirstSecond) 
              & (df['Branding'] == Branding) 
              & (df['Channel'] == Channel) 
              & (df['Source'] == Source) 
              & (df['Association'] == Association) 
              & (df['AnnualFeeGroup'] == AnnualFeeGroup) 
              & (df['OriginalCreditLineRange'] == OriginalCreditLineRange)]
        #store this new df into blank_df made earlier
        st.session_state['blank_df'] = pd.concat([st.session_state['blank_df'], df_new], axis=0) 

      

def add_to_main():
    if add:
        df_add = df.loc[(df['Vintage'] == selected) 
              & (df['FirstSecond'] == FirstSecond) 
              & (df['Branding'] == Branding) 
              & (df['Channel'] == Channel) 
              & (df['Source'] == Source) 
              & (df['Association'] == Association) 
              & (df['AnnualFeeGroup'] == AnnualFeeGroup) 
              & (df['OriginalCreditLineRange'] == OriginalCreditLineRange)]
        st.session_state['added_df'] = pd.concat([st.session_state['blank_df'], df_add], axis=0)
        st.session_state['isDfAdded'] = True;


with st.form('my_form'):
    with st.sidebar:
        # options = st.multiselect("Select vintages:", clist, key="vintages_selected")
        selected = st.selectbox("Selected Vintages:", clist, key="current_vintage")
        FirstSecond = st.selectbox("FirstSecond:",clist1)
        Branding = st.selectbox("Branding", clist2)
        Channel = st.selectbox("Channel", clist3)
        Source = st.selectbox("Source", clist4)
        Association = st.selectbox("Association", clist5)
        AnnualFeeGroup = st.selectbox("AnnualFeeGroup", clist6)
        OriginalCreditLineRange = st.selectbox("OriginalCreditLineRange", clist7)
        submit = st.form_submit_button('submit')
        add = st.form_submit_button('add')
        
        
st.header("Vintage Comparison")

#LOAD THE ENTIRE DF AND ALL PLOT LINES ON LOAD, this is default case
if st.session_state['blank_df'].empty == True:
    st.write(df)
    fig1 = px.line(df.melt(id_vars="Vintage"),x=df['MonthsOnBooks'], y=df['ActiveAccountIndicator'], color=df['Vintage'], markers=True, title='Active Accounts', labels={'y':'Active Accounts', 'x':'Months on Book', "color":"Vintage"})
    st.plotly_chart(fig1)
    fig2 = px.line(df.melt(id_vars="Vintage"),x=df['MonthsOnBooks'], y=df['CumlROAAnnualized'], color=df['Vintage'], markers=True, title='CumlROAAnnualized', labels={'y':'ROAAnnualized', 'x':'Months on Book', "color":"Vintage"})
    fig2.update_layout(yaxis_ticksuffix = ".3%")
    st.plotly_chart(fig2)
    fig3 = px.line(df.melt(id_vars="Vintage"),x=df['MonthsOnBooks'], y=df['CumlPreTaxIncome'], color=df['Vintage'], markers=True, title='CumlPreTaxIncome', labels={'y':'PreTaxIncome', 'x':'Months on Book', "color":"Vintage"})
    st.plotly_chart(fig3)
    fig4 = px.line(df.melt(id_vars="Vintage"),x=df['MonthsOnBooks'], y=df['EndingReceivable'], color=df['Vintage'], markers=True, title='EndingReceivable', labels={'y':'EndingReceivable', 'x':'Months on Book', "color":"Vintage"})
    st.plotly_chart(fig4)
elif st.session_state['blank_df'].empty == False and st.session_state['isDfAdded'] == False:
    st.dataframe(st.session_state['blank_df'])
    fig2a = px.line(st.session_state['blank_df'].melt(id_vars="Vintage"),x=st.session_state['blank_df']['MonthsOnBooks'], y=st.session_state['blank_df']['ActiveAccountIndicator'], color=st.session_state['blank_df']['Vintage'], markers=True, title='Active Accounts', labels={'y':'Active Accounts', 'x':'Months on Book', "color":"Vintage"})
    st.plotly_chart(fig2a)
elif st.session_state['added_df'].empty == False and st.session_state['isDfAdded'] == True:
    st.dataframe(st.session_state['added_df'])
    fig3a = px.line(st.session_state['added_df'].melt(id_vars="Vintage"),x=st.session_state['added_df']['MonthsOnBooks'], y=st.session_state['added_df']['ActiveAccountIndicator'], color=st.session_state['added_df']['Vintage'], markers=True, title='Active Accounts', labels={'y':'Active Accounts', 'x':'Months on Book', "color":"Vintage"})
    st.plotly_chart(fig3a)


if __name__ == "__main__":
    main()
   
if __name__ == "__main__":
    add_to_main()





