

import streamlit as st
import getpass
import pandas as pd
import os

# Define authorized usernames
AUTHORIZED_USERS = ["prathvik.sampath", "user2", "user3"]

# Get system username
system_username = getpass.getuser()

# Check if user is authorized
if system_username not in AUTHORIZED_USERS:
    st.error("Sorry, you do not have access to this app.")
else:
    # App content goes here
    st.write("Hello, {}!".format(system_username))
    st.write("This is a restricted app.")

    def run_analysis(date, file, selected_df):
        if selected_df == "PS_flex":
            st.success('start')
            df = pd.read_excel(file, engine='openpyxl')
            # file_path = os.path.dirname(file.name)
            output_file_path = '/home/appuser/BT/Streamlit/output_FLEX.csv'  # Update with desired output file path
            df.to_csv(output_file_path, index=False)
            st.write("Performing analysis on DataFrame 1")
            st.success('End')
            return df
            # return output_file_path

        elif selected_df == "PS_Liam":
            # Perform analysis on DataFrame 2
            st.write("Performing analysis on DataFrame 2")
            # ...
        elif selected_df == "Intergy":
            # Perform analysis on DataFrame 3
            st.write("Performing analysis on DataFrame 3")
            # ...
        else:
            st.error("Invalid DataFrame selected.")

    st.title("AUDIT App")

    # Date picker
    date = st.date_input("Select a date")

    # File picker
    file = st.file_uploader("Upload a file")

    # DataFrame selection dropdown
    selected_df = st.selectbox("Select DataFrame for analysis", ["PS_flex", "PS_Liam", "Intergy"])

    # Run button
    if st.button("Run Analysis"):
        if file is not None:
            # output_file_path = run_analysis(date, file, selected_df)
            df = run_analysis(date, file, selected_df)
            # if output_file_path:
            if df is not None and not df.empty:
                st.success("Analysis completed!")
                st.write("Download the output file:")
                st.download_button(
                    label="Download Output",
                    # data=output_file_path,
                    data=df,
                    file_name="output_FLEX.csv",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            else:
                st.error("Unable to generate the output file.")
        else:
            st.error("Please upload a file first.")
