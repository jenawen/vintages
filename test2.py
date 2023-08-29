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

options = st.multiselect("Select vintages:", clist, key="vintages_selected")

selected = st.sidebar.selectbox("Selected Vintages:", options, key="current_vintage")

FirstSecond = st.sidebar.selectbox("FirstSecond:",clist1)
Branding = st.sidebar.selectbox("Branding", clist2)
Channel = st.sidebar.selectbox("Channel", clist3)
Source = st.sidebar.selectbox("Source", clist4)
Association = st.sidebar.selectbox("Association", clist5)
AnnualFeeGroup = st.sidebar.selectbox("AnnualFeeGroup", clist6)
OriginalCreditLineRange = st.sidebar.selectbox("OriginalCreditLineRange", clist7)

st.header("Vintage Comparison")

#initialize default dataframe to hold ALL csv data
if 'df_default' not in st.session_state:
    st.session_state['df_default'] = df
    
#initialize blank dataframe to hold new df created from user filters
if 'blank_df' not in st.session_state:
    st.session_state['blank_df'] = pd.DataFrame(columns=["Vintage", "FirstSecond", 'Branding', 'Channel', 'Source', 'Association', 'AnnualFeeGroup', "OriginalCreditLineRange", "MonthsOnBooks", "NewAccountIndicator", "ActiveAccountIndicator", "PreTaxIncome", "EndingReceivable", "CumlNewAccountIndicator", "CumlActiveAccountIndicator", "CumlPreTaxIncome", "CumlEndingReceivable", "AverageActives", "AverageReceivable", "CumlROA", "CumlROAAnnualized"])

if "onLoad_display" not in st.session_state:
    st.session_state['onLoad_display'] = True;
    
def toggle_display():
    st.session_state['onLoad_display'] = False;

def main():
    submit = st.sidebar.button('submit', on_click=toggle_display)
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
        #new dataframe
        st.dataframe(st.session_state['blank_df'])
        #assign the df that contains all csv data to df1
        df1 = st.session_state['df_default']
        #assign the new filtered df to df2
        df2 = st.session_state['blank_df']
        #frames list made of the default df and the new filtered df
        frames = [df1, df2]
        #concat these 
        result = pd.concat(frames)
        #write result to screen
        if df2.empty == True:
            fig1 = px.line(df1.melt(id_vars="Vintage"),x=df1['MonthsOnBooks'], y=df1['ActiveAccountIndicator'], color=df1['Vintage'], markers=True, title='Active Accounts', labels={'y':'Active Accounts', 'x':'Months on Book', "color":"Vintage"})
            st.plotly_chart(fig1)
            # fig2 = px.line(result.melt(id_vars="Vintage"),x=result['MonthsOnBooks'], y=result['CumlROAAnnualized'], color=result['Vintage'], markers=True, title='CumlROAAnnualized', labels={'y':'ROAAnnualized', 'x':'Months on Book', "color":"Vintage"})
            # fig2.update_layout(yaxis_ticksuffix = ".3%")
            # st.plotly_chart(fig2)
            # fig3 = px.line(result.melt(id_vars="Vintage"),x=result['MonthsOnBooks'], y=result['CumlPreTaxIncome'], color=result['Vintage'], markers=True, title='CumlPreTaxIncome', labels={'y':'PreTaxIncome', 'x':'Months on Book', "color":"Vintage"})
            # st.plotly_chart(fig3)
            # fig4 = px.line(result.melt(id_vars="Vintage"),x=result['MonthsOnBooks'], y=result['EndingReceivable'], color=result['Vintage'], markers=True, title='EndingReceivable', labels={'y':'EndingReceivable', 'x':'Months on Book', "color":"Vintage"})
            # st.plotly_chart(fig4)
        else:
            fig2 = px.line(df2.melt(id_vars="Vintage"),x=df2['MonthsOnBooks'], y=df2['ActiveAccountIndicator'], color=df2['Vintage'], markers=True, title='Active Accounts', labels={'y':'Active Accounts', 'x':'Months on Book', "color":"Vintage"})
            st.plotly_chart(fig2)
            # fig2 = px.line(result.melt(id_vars="Vintage"),x=result['MonthsOnBooks'], y=result['CumlROAAnnualized'], color=result['Vintage'], markers=True, title='CumlROAAnnualized', labels={'y':'ROAAnnualized', 'x':'Months on Book', "color":"Vintage"})
            # fig2.update_layout(yaxis_ticksuffix = ".3%")
            # st.plotly_chart(fig2)
            # fig3 = px.line(result.melt(id_vars="Vintage"),x=result['MonthsOnBooks'], y=result['CumlPreTaxIncome'], color=result['Vintage'], markers=True, title='CumlPreTaxIncome', labels={'y':'PreTaxIncome', 'x':'Months on Book', "color":"Vintage"})
            # st.plotly_chart(fig3)
            # fig4 = px.line(result.melt(id_vars="Vintage"),x=result['MonthsOnBooks'], y=result['EndingReceivable'], color=result['Vintage'], markers=True, title='EndingReceivable', labels={'y':'EndingReceivable', 'x':'Months on Book', "color":"Vintage"})
            # st.plotly_chart(fig4)
           

# if 'df_result2' not in st.session_state:
#     st.session_state['df_result2'] = df

# def add_to_main():
#     add = st.sidebar.button('add')
#     if add:
#         st.session_state['df_result2'] = st.session_state['df_result2'].loc[(df['Vintage'] == selected) & (df['FirstSecond'] == FirstSecond) & (df['Branding'] == Branding) & (df['Channel'] == Channel) & (df['Source'] == Source)
#                     & (df['Association'] == Association) & (df['AnnualFeeGroup'] == AnnualFeeGroup) & (df['OriginalCreditLineRange'] == OriginalCreditLineRange) ]
#         # st.session_state['df_result'].append(df.loc[(df['Vintage'] == selected) & (df['FirstSecond'] == FirstSecond) & (df['Branding'] == Branding) & (df['Channel'] == Channel) & (df['Source'] == Source)
#         #             & (df['Association'] == Association) & (df['AnnualFeeGroup'] == AnnualFeeGroup) & (df['OriginalCreditLineRange'] == OriginalCreditLineRange)])

# df2 = st.session_state['df_result2']


if st.session_state['onLoad_display']:
    st.write(df)
    fig1 = px.line(df.melt(id_vars="Vintage"),x=df['MonthsOnBooks'], y=df['ActiveAccountIndicator'], color=df['Vintage'], markers=True, title='Active Accounts', labels={'y':'Active Accounts', 'x':'Months on Book', "color":"Vintage"})
    st.plotly_chart(fig1)
    st.write('ON LOAD DISPLAY')
# else:
#     None



        
    
if __name__ == "__main__":
    main()
   
# if __name__ == "__main__":
#     add_to_main()






