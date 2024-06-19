import streamlit as st

options_set_1 = ["Select an Option", "Full time Aspirant", "Working Professional", "College going student"]
options_set_2 = ["Select an Option", "2 - 4 hours", "4 - 6 hours", "6 - 8 hours"]
options_set_3 = [ "Yes", "No"]

st.title("Study Plan Creator")

# st.set_page_config(page_title="PDF Downloader", page_icon=":page_facing_up:")

selected_option_1 = st.selectbox("Select an option from set 1:", options_set_1)
selected_option_2 = st.selectbox("Select an option from set 2:", options_set_2)
selected_option_3 = st.selectbox("Have you chosen your optional:", options_set_3)
selected_option_4 = st.selectbox("Have you appreared for UPSC:", options_set_3)
selected_option_5 = st.selectbox("Are you familiar with UPSC Curriculum", options_set_3)

pdf_mapping = {
    ("Option 1.1", "Option 2.1", "Option 3.1"): "https://github.com/mickee00000/201951090_Research_Internship_2022/raw/main/Report%20&%20Presentation/Project_Report_Summer%20Research%20Intership%202022%20.pdf",
    ("Option 1.1", "Option 2.1", "Option 3.2"): "https://github.com/mickee00000/201951090_Research_Internship_2022/raw/main/Report%20&%20Presentation/Project_Report_Summer%20Research%20Intership%202022%20.pdf",
    ("Option 1.1", "Option 2.2", "Option 3.3"): "https://github.com/mickee00000/201951090_Research_Internship_2022/raw/main/Report%20&%20Presentation/Project_Report_Summer%20Research%20Intership%202022%20.pdf",
    ("Option 1.2", "Option 2.3", "Option 3.4"): "https://github.com/mickee00000/201951090_Research_Internship_2022/raw/main/Report%20&%20Presentation/Project_Report_Summer%20Research%20Intership%202022%20.pdf"
}

pdf_url = pdf_mapping.get((selected_option_1, selected_option_2, selected_option_3, selected_option_4))

if (selected_option_1, selected_option_2, selected_option_3, selected_option_4) == ("Select an Option","Select an Option","Select an Option"):
    st.write("Select the listed options above to generate a PDF")
elif pdf_url:
    st.write("")
    download_button = f'<a href="{pdf_url}" download><button>Download PDF</button></a>'
    st.markdown(download_button, unsafe_allow_html=True)
else:
    st.write("No PDF available for the selected options.")
