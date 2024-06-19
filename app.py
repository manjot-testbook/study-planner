import streamlit as st

options_set_1 = ["Select an Option", "Full time Aspirant", "Working Professional", "College going student"]
options_set_2 = ["Select an Option", "2 - 4 hours", "4 - 6 hours", "6 - 8 hours"]
options_set_3 = ["Yes", "No"]

st.title("Study Plan Creator")

selected_option_1 = st.selectbox("What kind of UPSC aspirant are you?", options_set_1)
selected_option_2 = st.selectbox("How much daily time do you spend preparing for UPSC", options_set_2)
selected_option_3 = st.selectbox("Have you chosen your optional:", options_set_3)
selected_option_4 = st.selectbox("Have you appeared for UPSC:", options_set_3)
selected_option_5 = st.selectbox("Are you familiar with UPSC Curriculum", options_set_3)

pdf_url = "https://github.com/mickee00000/201951090_Research_Internship_2022/raw/main/Report%20&%20Presentation/Project_Report_Summer%20Research%20Intership%202022%20.pdf"

pdf_mapping = {
    (opt1, opt2, opt3, opt4, opt5): pdf_url
    for opt1 in options_set_1[1:] 
    for opt2 in options_set_2[1:] 
    for opt3 in options_set_3  
    for opt4 in options_set_3 
    for opt5 in options_set_3 
}

selected_options = (selected_option_1, selected_option_2, selected_option_3, selected_option_4, selected_option_5)

pdf_link = pdf_mapping.get(selected_options)

if selected_option_1 == "Select an Option" or selected_option_2 == "Select an Option":
    st.write("Select the listed options above to generate a PDF")
elif pdf_link:
    download_button = f'<a href="{pdf_link}" download><button>Download PDF</button></a>'
    st.markdown(download_button, unsafe_allow_html=True)
else:
    st.write("No PDF available for the selected options.")
