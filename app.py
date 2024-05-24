import streamlit as st
import pandas as pd

# Set a tab title
st.set_page_config(page_title="WISE")

# Set a title for your app
st.title("WISE: Wellbeing Insights Streamlined and Explained :owl:")

# Welcome message
st.markdown("""
Welcome to WISE, your personal analytical assistant!

**Please Note:**

* To ensure optimal performance, please limit the size of your dataset.
* For best results, ensure your dataset is well-structured and contains relevant health data.

We're here to help you discover insights from your data. Feel free to ask questions or explore visualizations.
""")

context = st.text_input("Can you please describe your role in a sentence")

# Section for choosing data source
st.markdown("Choose Data Source:")

# Option 1: Local File Upload
col1, col2 = st.columns(2)
with col1:
  use_local_file = st.checkbox("Use Local File", value=False)
  if use_local_file:
    try:
      df = pd.read_csv("/DummyCSV.csv")
      st.success("Loaded data from ddummy file")
    except FileNotFoundError:
      st.error("dummyCSV.csv not found. Please ensure it's in the same directory.")
      df = None

# Option 2: Drag and Drop
with col2:
  uploaded_file = st.file_uploader("Upload your health dataset:", type=['csv', 'xlsx'], key="uploaded_file")

  if uploaded_file is not None:
    # Placeholder message for uploaded file
    st.write("File uploaded! Analyzing data...")

    # Read the file into a DataFrame
    if uploaded_file.name.endswith('.csv'):
      df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
      df = pd.read_excel(uploaded_file)

    # Extract column names
    column_name_list = df.columns.tolist()

    selected_options = st.multiselect(
      "What data would you like to explore?",
      column_name_list)

    # (Your data analysis code using the uploaded file content, prompt and column name list)

    # Success message after analysis (replace with specific results)
    st.success("Data analysis complete! See summary below.")
  else:
    st.info("Drag and drop your dataset here to start exploring!")


# Text input for problem with placeholder
problem = st.text_input("What question would you want to answer with this data?", key="problem")

# Function to generate prompt feedback (replace with actual API call logic)
def get_better_prompt(original_prompt):
    # Placeholder logic for API call
    better_prompt = "This is a suggested improvement based on your prompt."
    return better_prompt

# Generate prompt feedback based on user input (assuming API call)
if problem:
    better_prompt = get_better_prompt(problem)
    prompt_assessment = f"Your prompt could be improved. How about {better_prompt}?"
    st.markdown(f"<p style='color:orange'>{prompt_assessment}</p>", unsafe_allow_html=True)

# Submit button with conditional enabling
submit = st.button('Generate data analysis', disabled=not (uploaded_file and problem))

if submit:
    st.subheader("Summary:")
    with st.spinner(text="This may take a moment..."):
        # Placeholder for API analysis logic
        text2 = "API output (replace with analysis results)"
    st.write(text2)

# API response on data assessment
data_assessment = "Your data is terrible, it is not reliable"
st.markdown(f"<p style='color:orange'>Data assessment: {data_assessment}</p>", unsafe_allow_html=True)

# API response on data assessment
data_score = "xx%"

data_assessment = "Your data is terrible, it is not reliable"
st.markdown(f"<p style='color:orange'>Data assessment: {data_assessment}</p>", unsafe_allow_html=True)

st.markdown("""
This is a proof of concept platform built using Google tools in the NHS AI Google Hackathon, May 2024. 

For feedback or more information, please contact us at chris.m.lewis@gmail.com
""")
