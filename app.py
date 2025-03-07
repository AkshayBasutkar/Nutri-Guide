import streamlit as st

def marks_to_grade(marks: float) -> float:
    """
    Convert marks (0–100) to a grade on a 10-point scale.
    Adjust the thresholds as per your institution's grading policy.
    """
    if marks >= 90:
        return 10
    elif marks >= 80:
        return 9
    elif marks >= 70:
        return 8
    elif marks >= 60:
        return 7
    elif marks >= 50:
        return 6
    elif marks >= 40:
        return 5
    else:
        return 0

# Dictionary of subjects and their respective credits
subjects = {
    "Mathematical foundation for machine learning": 3,
    "Computer organisation and architecture": 3,
    "Data structures": 4,
    "Probability and statistics for machine learning": 3,
    "Object oriented programming": 3,
    "Database management": 3,
    "Theoretical foundations of computation": 3,
    "Additional mathematics (Non-credit, optional)": 0
}

st.title("SGPA Calculator (Marks-Based)")

st.write("""
Enter your marks (out of 100) for each subject below.
We'll convert them to a grade (0–10 scale) and then compute your SGPA.
""")

# Create input fields for each subject using session state.
grades = {}

for subject, credit in subjects.items():
    if credit > 0:
        st.subheader(f"{subject} [{credit} credits]")
    else:
        st.subheader(f"{subject} [No credit]")
    
    # Use the subject name as the key for session state
    marks = st.number_input(
        f"Enter marks for {subject} (0–100):",
        min_value=0, 
        max_value=100, 
        value=st.session_state.get(subject, 0),
        step=1,
        key=subject
    )
    # Convert marks to grade and store
    grade = marks_to_grade(marks)
    grades[subject] = grade

# Layout for the buttons in two columns
col1, col2 = st.columns(2)

with col1:
    if st.button("Calculate SGPA"):
        total_credits = 0
        total_grade_points = 0
        
        for subject, credit in subjects.items():
            if credit > 0:
                total_grade_points += grades[subject] * credit
                total_credits += credit
        
        if total_credits > 0:
            sgpa = total_grade_points / total_credits
            st.success(f"Your SGPA is: **{sgpa:.2f}**")
        else:
            st.error("No credit-bearing subjects found. Cannot calculate SGPA.")

with col2:
    if st.button("Clear Form"):
        # Reset all input fields by updating session state for each subject
        for subject in subjects:
            st.session_state[subject] = 0
        st.experimental_rerun()  # Rerun the app to reflect cleared values