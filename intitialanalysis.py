import pandas as pd
import streamlit as st
import plotly.express as px
import os
import io



dir_path='/home/michael/NoahsRug/5784/'
filenames = os.listdir(dir_path)
selected_filename = st.selectbox('Select a file', filenames, key = 'fileselect')

buffer = io.StringIO()

def dataloading(selected_filename):
####    df_exists = st.session_state.get('chosendata')
####    fnmatch = st.session_state.get("filename") == filename  
####    if df_exists is not None and not df_exists.empty and fnmatch:
    if st.session_state.get("initfilename") is None or selected_filename !=  st.session_state.get("initfilename"):
        st.session_state["initfilename"] = selected_filename
    filename = os.path.join(dir_path, st.session_state["initfilename"])
    if filename is not None and st.session_state.get(filename) is not None:
        st.write('hello')
        df = st.session_state[filename]
    elif filename.endswith(".xlsx"): 
        excelfile = pd.ExcelFile(filename)
        sheetname = st.selectbox('Select a sheet', excelfile.sheet_names, key = 'pageselect')
        st.session_state[filename] = excelfile.parse(sheet_name=sheetname) 
        df=st.session_state[filename]
    elif filename.endswith(".csv"): 
        st.session_state[filename] = pd.read_csv(filename)
        df=st.session_state[filename]
    elif os.path.isdir(filename):
        errormessage = "Chosen path is a directory!"
        df = pd.DataFrame()
        st.write(errormessage)
        print(errormessage)
    else:
        raise ValueError('Invalid input please try something else!')
    return df 
df = dataloading(selected_filename)
st.title(":blue[Initial Analysis]")
rows, columns = df.shape
df.info(buf=buffer)
infostring = buffer.getvalue()
st.subheader(":red[Initial Dataframe Info]", divider='red')
st.metric("Total Rows", rows)
st.metric("Total Columns", columns)
st.code(infostring)
st.subheader(":green[General Stats]", divider='green')
st.dataframe(df.describe()) ####type:ignore
st.subheader(":orange[Example]", divider='orange')
st.dataframe(df.head()) #####type:ignore

