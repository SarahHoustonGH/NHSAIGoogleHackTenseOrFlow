import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

st.subheader("Tell us about yourself")
context = st.text_input("Describe your role in a sentence. This will help the model choose the best way to respond to your query.")

st.markdown("Find some useful examples below")

# Create four empty containers
example_container1, example_container2, example_container3 = st.columns(3)

# Define text outputs
example_1 = "I am a respiratory physician, interested in developing a new tool to analyse waveforms"
example_2 = "I am a GP, interested in learning more about my patients with cancer"
example_3 = "I am an NHS director, looking to understand performance in my region"

# Write text to each container
example_container1.write(example_1)
example_container2.write(example_2)
example_container3.write(example_3)



# Section for choosing data source
st.subheader("Choose a Data Source")

# Option 1: Local File Upload
col1, col2 = st.columns(2)
with col1:
  use_local_file = st.checkbox("Use Local File", value=False)
  if use_local_file:
    try:
      df = pd.read_csv("\DummyCSV.csv")
      st.success("Loaded data from dummy file")
    except FileNotFoundError:
      st.error("dummyCSV.csv not found. Please ensure it's in the same directory.")
      df = None

# Option 2: Drag and Drop
def create_chart(df, selected_options, chart_type):
  """
  Creates a chart based on user input for chart type and selected options.

  Args:
    df (pandas.DataFrame): The uploaded DataFrame containing the health data.
    selected_options (list): The list of selected options (column names) from the user.
    chart_type (str): The selected chart type ("bar", "line", or "scatter").

  Returns:
    None (for Matplotlib) or Matplotlib figure object (for Streamlit integration)
  """

  if chart_type:  # Check if a valid chart type is selected
    data_x = df[selected_options[0]]  # Assuming first option is for x-axis
    data_y = df[selected_options[1:]]  # Remaining options for y-axis

    plt.figure(figsize=(10, 6))  # Adjust figure size as needed

    if chart_type == "bar":
      plt.bar(data_x, data_y)
    elif chart_type == "line":
      plt.plot(data_x, data_y)
    elif chart_type == "scatter":
      plt.scatter(data_x, data_y)
    else:
      st.error("Error: Unexpected chart type.")  # Handle unexpected input

    # Add labels and title (common for all charts)
    plt.xlabel(selected_options[0])  # Use the first option as X-axis label
    plt.ylabel(", ".join(selected_options[1:]))  # Combine remaining options for Y-axis label
    plt.title("Chart")

    # Option 1: Display Matplotlib chart in a separate window (not recommended)
    # plt.show()

    # Option 2: Return the figure object for Streamlit integration
    return plt.figure()  # Return the created figure object

def main():
  """
  The main function of the Streamlit app for data exploration and visualization.
  """

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
      column_name_list
    )

    if selected_options:  # Check if at least two options are selected for visualization
      chart_type = st.selectbox("Select Chart Type", ("bar", "line", "scatter"))

      # Pass a copy of df to avoid modifications
      chart_figure = create_chart(df.copy(), selected_options, chart_type.lower())

      # Option 1: Display Matplotlib chart (not recommended)
      # plt.show()

      # Option 2: Display Matplotlib chart within Streamlit
      st.pyplot(chart_figure)  # Display the returned figure from create_chart

    else:
      st.warning("Please select at least two data options to create a chart.")

  else:
    st.info("Drag and drop your dataset here to start exploring!")

if __name__ == "__main__":
  main()

# Text input for problem with placeholder
st.subheader("Tell us your problem")
problem = st.text_input("What question would you want to answer with this data?", key="problem")

# Function to generate prompt feedback (replace with actual API call logic)
def get_better_prompt(original_prompt):
    # Placeholder logic for API call
    better_prompt = "...a suggested improvement based on your prompt"
    return better_prompt

# Generate prompt feedback based on user input (assuming API call)
if problem:  # Assuming 'problem' is a boolean variable
  better_prompt = get_better_prompt(problem)
  prompt_assessment = f"Your prompt could be improved. How about {better_prompt}?"
  link_text = "learn more [here](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design)"

  st.markdown(prompt_assessment)
  st.markdown(link_text)

  # Improved readability with better indentation and variable name
  new_prompt = st.text_input("Would you like to refine your prompt further?")
  if new_prompt:
      problem = new_prompt  # Update 'problem' with the user's new prompt (if provided)

# Submit button with conditional enabling
submit = st.button('Generate data analysis', disabled=not (uploaded_file and problem))

st.subheader("Here's a summary of the analysis")
if submit:
    with st.spinner(text="This may take a moment..."):
        # Placeholder for API analysis logic
        text2 = "API output (replace with analysis results)"
    st.write(text2)

# Create two empty containers for analysis
data1, data2 = st.columns(2)

text_result = "This is the text result"
graph_result = "This is the graphical result"

# Write text to each container
data1.write(text_result)
data2.write(graph_result)



st.subheader("We've checked the data and result for you. This is what we found")

# API response on data assessment
data_assessment = "Data assessment API response"

# API response on data assessment
data_citation = "Data citation to appear when pulling data from Google"

# API response on data assessment
data_reasoning = "Why Google chose this response"


# Create four empty containers
container1, container2, container3 = st.columns(3)


# Write text to each container
container1.write(data_assessment)
container2.write(data_citation)
container3.write(data_reasoning)


# Section for choosing data source
st.subheader("Find out more about the platform")

st.markdown("""
This is a proof of concept platform built using Google tools in the NHS AI Google Hackathon, May 2024. 

For feedback or more information, please contact us at chris.m.lewis@gmail.com
""")
