import streamlit as st

st.title("SGPA Calculator")

st.write("""
Enter the grade points for each subject. In this example:
- Most subjects have 3 credits.
- Data Structures has 4 credits.
- Additional Maths is a non-credit course (it will not affect the SGPA).
""")

# Define subjects with their respective credit values
subjects = {
    "Subject 1": 3,
    "Subject 2": 3,
    "Subject 3": 3,
    "Data Structures": 4,
    "Additional Maths": 0,  # Non-credit course
    "Subject 4": 3,
    "Subject 5": 3
}

# Dictionary to hold the entered grade points for each subject
scores = {}

# Create input fields for each subject
for subject, credit in subjects.items():
    if credit == 0:
        st.write(f"**{subject}** (Non-credit course)")
    else:
        st.write(f"**{subject}** ({credit} credits)")
    score = st.number_input(f"Enter grade points for {subject}:", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
    scores[subject] = score

# Button to trigger SGPA calculation
if st.button("Calculate SGPA"):
    total_weighted = 0
    total_credits = 0
    # Calculate weighted sum only for courses with credits
    for subject, credit in subjects.items():
        if credit > 0:
            total_weighted += scores[subject] * credit
            total_credits += credit

    if total_credits > 0:
        sgpa = total_weighted / total_credits
        st.success(f"Your SGPA is: **{sgpa:.2f}**")
    else:
        st.error("No credit courses entered. Cannot calculate SGPA.")