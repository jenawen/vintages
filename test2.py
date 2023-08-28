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
# st.write(selected)
FirstSecond = st.sidebar.selectbox("FirstSecond:",clist1)
Branding = st.sidebar.selectbox("Branding", clist2)
Channel = st.sidebar.selectbox("Channel", clist3)
Source = st.sidebar.selectbox("Source", clist4)
Association = st.sidebar.selectbox("Association", clist5)
AnnualFeeGroup = st.sidebar.selectbox("AnnualFeeGroup", clist6)
OriginalCreditLineRange = st.sidebar.selectbox("OriginalCreditLineRange", clist7)



##Need an empty array to store all the filtered objects 
frames2 = []

st.header("Vintage Comparison")

#initiate session state of df_result for the dataframe to be updated 
if 'df_result' not in st.session_state:
    st.session_state['df_result'] = df

# df.loc[(df['Vintage'].isin(options))]

def main():
    submit = st.sidebar.button('submit')
    if submit:
        # st.session_state['df_result'] = st.session_state['df_result'].loc[(df['Vintage'] == selected)]
        st.session_state['df_result'] = st.session_state['df_result'].loc[(df['Vintage'] == selected) & (df['FirstSecond'] == FirstSecond) & (df['Branding'] == Branding) & (df['Channel'] == Channel) & (df['Source'] == Source)
                    & (df['Association'] == Association) & (df['AnnualFeeGroup'] == AnnualFeeGroup) & (df['OriginalCreditLineRange'] == OriginalCreditLineRange)
]
     

df1 = st.session_state['df_result']
    # st.session_state

if 'df_result2' not in st.session_state:
    st.session_state['df_result2'] = df


## SUBMIT / ADD ALGORITHM:
### on add, push the sorted csv data to the frames array
#### use the options variable to get the number of vintages selected 
#### use for loop for # of vintages selected
### on submit, display the frames

##Need to initalize as many session states as # of vintages selected 
### onClick of add button, append the new filtered object to the array
for i in enumerate(options):
    if f"df_result_{i[0]}" not in st.session_state:
        st.session_state[f"df_result_{i[0]}"] = f"df_{i[0]}"

def add_to_main():
    add = st.sidebar.button('add')
    if add:
        st.session_state["df_result2"] = st.session_state["df_result2"].loc[(df['Vintage'] == selected) & (df['FirstSecond'] == FirstSecond) & (df['Branding'] == Branding) & (df['Channel'] == Channel) & (df['Source'] == Source)
                    & (df['Association'] == Association) & (df['AnnualFeeGroup'] == AnnualFeeGroup) & (df['OriginalCreditLineRange'] == OriginalCreditLineRange) ]
        
df2 = st.session_state['df_result2']

        
        # for i in enumerate(options):
                # st.session_state[f"df_result_{i[0]}"] = st.session_state[f"df_result_{i[0]}"].loc[(df['Vintage'] == selected) & (df['FirstSecond'] == FirstSecond) & (df['Branding'] == Branding) & (df['Channel'] == Channel) & (df['Source'] == Source)
                #     & (df['Association'] == Association) & (df['AnnualFeeGroup'] == AnnualFeeGroup) & (df['OriginalCreditLineRange'] == OriginalCreditLineRange) ]
                # frames2.append( st.session_state[f"df_result_{i[0]}"])
                # st.write('hi', frames2)
   
        
        
        

frames = [df1, df2]
result = pd.concat(frames)
st.write(result)

fig = px.line(result.melt(id_vars="Vintage"),x=result['MonthsOnBooks'], y=result['ActiveAccountIndicator'], color=result['Vintage'], markers=True, title='Active Accounts', labels={'y':'Active Accounts', 'x':'Months on Book', "color":"Vintage"})

# fig.add_trace(connectgaps=False)
st.plotly_chart(fig)

fig2 = px.line(result.melt(id_vars="Vintage"),x=result['MonthsOnBooks'], y=result['CumlROAAnnualized'], color=result['Vintage'], markers=True, title='CumlROAAnnualized', labels={'y':'ROAAnnualized', 'x':'Months on Book', "color":"Vintage"})

fig2.update_layout(yaxis_ticksuffix = ".3%")
st.plotly_chart(fig2)

fig3 = px.line(result.melt(id_vars="Vintage"),x=result['MonthsOnBooks'], y=result['CumlPreTaxIncome'], color=result['Vintage'], markers=True, title='CumlPreTaxIncome', labels={'y':'PreTaxIncome', 'x':'Months on Book', "color":"Vintage"})
st.plotly_chart(fig3)

fig4 = px.line(result.melt(id_vars="Vintage"),x=result['MonthsOnBooks'], y=result['EndingReceivable'], color=result['Vintage'], markers=True, title='EndingReceivable', labels={'y':'EndingReceivable', 'x':'Months on Book', "color":"Vintage"})
st.plotly_chart(fig4)

        
    
if __name__ == "__main__":
    main()

   
if __name__ == "__main__":
    add_to_main()






