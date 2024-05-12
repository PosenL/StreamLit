import streamlit as st
import pandas as pd
import plotly.express as px

# Third edtion of upload

def main():
    st.title("My first Streamlit application")
    name = st.text_input("Please input your name: ")
    if name:
        st.write("Welcome {} !!!".format(name))

    #Upload file
    upload_file = st.file_uploader("Please upload your file (csv) here", type = ["csv", "xlsx"])
    if upload_file is not None:
        file_extension = upload_file.name.split(".")[-1]
        if file_extension.lower() =="csv":
            df = pd.read_csv(upload_file)
        else:
            df = pd.read_excel(upload_file)

        st.write("Oringal Data: ")

        #Show DataFrame
        show_data = st.checkbox("Show data")
        if show_data: 
            multiselected_columns = st.multiselect("Choose which columns to be shown", df.columns)
            if multiselected_columns:
                st.write(df[multiselected_columns])
            else:
                st.write(df)

        show_summary = st.checkbox("Show summary")
        if show_summary: 
            st.write(df.describe())
    
    #Visualization
        selected_col_list = df.columns.values.tolist()
        selected_col_list.remove("日期")
        chart_type = st.selectbox("Choose chart type", ["Bar Chart", "Line Chart", "Pie Chart"])
        selected_column = st.selectbox("Choose which columns to be visualized in bar chart", selected_col_list)

        st.subheader("Data Visualization ({})".format(chart_type))
        if chart_type == "Bar Chart":
            st.bar_chart(df[["日期", selected_column]].set_index("日期"))
        elif chart_type == "Line Chart":
            st.line_chart(df[["日期", selected_column]].set_index("日期"))
        else:
            fig = px.pie(df[selected_column], 
                         values = df[selected_column],
                         names = df[selected_column],
                         title='number of {}'.format(selected_column))
            st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
