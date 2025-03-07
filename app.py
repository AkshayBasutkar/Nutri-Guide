import streamlit as st

st.title("SGPA Calculator")

st.write("""
Enter the grade points (on a 0–10 scale) for each subject below.
The SGPA is calculated using the credit-weighted average of all credit courses.
""")

# Define the subjects and their credit values
subjects = {
    "Mathematical Foundation for Machine Learning": 3,
    "Computer Organisation and Architecture": 3,
    "Data Structures": 4,
    "Probability and Statistics for Machine Learning": 3,
    "Object Oriented Programming": 3,
    "Database Management": 3,
    "Theoretical Foundations of Computation": 3,
    "Additional Mathematics (Optional, Non-credit)": 0
}

# Dictionary to store the input scores for each subject
scores = {}

# Create number inputs for each subject
for subject, credit in subjects.items():
    if credit == 0:
        st.write(f"**{subject}** (Optional, Non-credit)")
    else:
        st.write(f"**{subject}** ({credit} credits)")
    # Using number input to get grade points; you can adjust min, max, and step as needed
    scores[subject] = st.number_input(f"Enter grade points for {subject}:", min_value=0.0, max_value=10.0, value=0.0, step=0.1)

# Button to trigger SGPA calculation
if st.button("Calculate SGPA"):
    total_weighted_points = 0
    total_credits = 0
    for subject, credit in subjects.items():
        if credit > 0:
            total_weighted_points += scores[subject] * credit
            total_credits += credit

    if total_credits > 0:
        sgpa = total_weighted_points / total_credits
        st.success(f"Your SGPA is: **{sgpa:.2f}**")
    else:
        st.error("No credit courses entered. Cannot calculate SGPA.")