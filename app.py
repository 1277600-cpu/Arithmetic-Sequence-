import streamlit as st

def arithmetic_sequence(first_term: float, common_difference: float, num_terms: int):
    """Generate an arithmetic sequence."""
    return [first_term + i * common_difference for i in range(num_terms)]

st.title("Arithmetic Sequence Generator")

st.write(
    """
    Enter the details below to generate an arithmetic sequence:
    - **First term:** The starting number of your sequence.
    - **Common difference:** The constant amount between consecutive terms.
    - **Number of terms:** How many numbers you want to list.
    """
)

first_term = st.number_input("First term (a₁)", value=1.0, format="%.4f")
common_difference = st.number_input("Common difference (d)", value=1.0, format="%.4f")
num_terms = st.number_input("Number of terms (n)", min_value=1, value=10, step=1)

if st.button("Generate Sequence"):
    sequence = arithmetic_sequence(first_term, common_difference, num_terms)
    st.write("**Arithmetic Sequence:**")
    st.code(sequence)