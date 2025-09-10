import streamlit as st
import math

def arithmetic_sequence(first_term: float, common_difference: float, num_terms: int):
    """Generate an arithmetic sequence."""
    return [first_term + i * common_difference for i in range(num_terms)]

def geometric_sequence(first_term: float, common_ratio: float, num_terms: int):
    """Generate a geometric sequence."""
    return [first_term * (common_ratio ** i) for i in range(num_terms)]

def geometric_series_sum(first_term: float, common_ratio: float, num_terms: int):
    """Calculate the sum of a finite geometric series."""
    if common_ratio == 1:
        return first_term * num_terms
    else:
        return first_term * (1 - common_ratio ** num_terms) / (1 - common_ratio)

st.title("Sequence Generator")

# Mode selection
sequence_type = st.radio(
    "Select sequence type:",
    ["Arithmetic Sequence", "Geometric Sequence"],
    horizontal=True
)

if sequence_type == "Arithmetic Sequence":
    st.header("Arithmetic Sequence Generator")
    
    st.write(
        """
        Enter the details below to generate an arithmetic sequence:
        - **First term:** The starting number of your sequence.
        - **Common difference:** The constant amount between consecutive terms.
        - **Number of terms:** How many numbers you want to list.
        """
    )
    
    first_term = st.number_input("First term (a₁)", value=1.0, format="%.4f", key="arith_first")
    common_difference = st.number_input("Common difference (d)", value=1.0, format="%.4f", key="arith_diff")
    num_terms = st.number_input("Number of terms (n)", min_value=1, value=10, step=1, key="arith_terms")
    
    if st.button("Generate Arithmetic Sequence"):
        sequence = arithmetic_sequence(first_term, common_difference, num_terms)
        st.write("**Arithmetic Sequence:**")
        st.code(sequence)

else:  # Geometric Sequence
    st.header("Geometric Sequence Generator")
    
    st.write(
        """
        Enter the details below to generate a geometric sequence:
        - **First term:** The starting number of your sequence.
        - **Common ratio:** The constant factor between consecutive terms.
        - **Number of terms:** How many numbers you want to list.
        """
    )
    
    first_term = st.number_input("First term (a₁)", value=1.0, format="%.4f", key="geom_first")
    common_ratio = st.number_input("Common ratio (r)", value=2.0, format="%.4f", key="geom_ratio")
    num_terms = st.number_input("Number of terms (n)", min_value=1, value=10, step=1, key="geom_terms")
    
    if st.button("Generate Geometric Sequence"):
        sequence = geometric_sequence(first_term, common_ratio, num_terms)
        series_sum = geometric_series_sum(first_term, common_ratio, num_terms)
        
        st.write("**Geometric Sequence:**")
        st.code(sequence)
        
        st.write("**Sum of Geometric Series:**")
        if common_ratio == 1:
            st.write(f"Since the common ratio is 1, the sum is: **{series_sum:.4f}**")
            st.latex(f"S_n = a_1 \\times n = {first_term} \\times {num_terms} = {series_sum:.4f}")
        else:
            st.write(f"The sum of the first {num_terms} terms is: **{series_sum:.4f}**")
            st.latex(f"S_n = a_1 \\times \\frac{{1 - r^n}}{{1 - r}} = {first_term} \\times \\frac{{1 - {common_ratio}^{{{num_terms}}}}}{{1 - {common_ratio}}} = {series_sum:.4f}")
