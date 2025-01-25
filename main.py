import pandas as pd
import os
import matplotlib.pyplot as plt
import streamlit as st

# Function to load data from an uploaded Excel file
def load_data(file):
    try:
        df = pd.read_excel(file, header=3)
        df = df[['Name of the Instrument', 'ISIN', 'Quantity', 'Market value\n(Rs. in Lakhs)', '% to NAV']].dropna()
        df.columns = ['Instrument', 'ISIN', 'Quantity', 'Market Value', 'Percentage to NAV']
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Function to calculate allocation changes
def compute_changes(files):
    changes = []
    for prev_file, curr_file in zip(files, files[1:]):
        prev_df, curr_df = load_data(prev_file), load_data(curr_file)
        if prev_df is None or curr_df is None:
            continue
        merged = prev_df.merge(curr_df, on='Instrument', suffixes=('_Prev', '_Curr'))
        merged['Quantity Change'] = merged['Quantity_Curr'] - merged['Quantity_Prev']
        merged['Market Value Change'] = merged['Market Value_Curr'] - merged['Market Value_Prev']
        merged['NAV Change'] = merged['Percentage to NAV_Curr'] - merged['Percentage to NAV_Prev']
        changes.append(merged[['Instrument', 'ISIN_Curr', 'Quantity Change', 'Market Value Change', 'NAV Change']])
    return pd.concat(changes, ignore_index=True) if changes else None

# Function to visualize changes
def plot_changes(df):
    df = df.sort_values('Market Value Change', ascending=False).head(10)
    st.bar_chart(df.set_index('Instrument')['Market Value Change'])

# Streamlit App
st.title("Mutual Fund Allocation Change Tracker")

uploaded_files = st.file_uploader("Upload monthly portfolio files", type=["xlsx"], accept_multiple_files=True)

if uploaded_files:
    changes_df = compute_changes(uploaded_files)
    if changes_df is not None:
        st.write("### Fund Allocation Changes")
        st.dataframe(changes_df)
        plot_changes(changes_df)
        
        output_file = "Fund_Changes.xlsx"
        changes_df.to_excel(output_file, index=False)
        with open(output_file, "rb") as f:
            st.download_button("Download Results", f, file_name=output_file)