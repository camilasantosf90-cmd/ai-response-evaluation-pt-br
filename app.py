
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="EvalLab AI",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 EvalLab AI")
st.subheader("AI Response Evaluation & Quality Intelligence")

st.markdown(
    "A platform for comparing, evaluating, "
    "and analyzing AI-generated responses."
)

st.divider()

st.header("📊 Response Evaluation")

prompt = st.text_area(
    "User prompt",
    placeholder="Enter the original user question..."
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Response A")
    response_a = st.text_area(
        "Model A response",
        key="response_a"
    )
    score_a = st.slider(
        "Response A quality score",
        0, 10, 5,
        key="score_a"
    )

with col2:
    st.subheader("Response B")
    response_b = st.text_area(
        "Model B response",
        key="response_b"
    )
    score_b = st.slider(
        "Response B quality score",
        0, 10, 5,
        key="score_b"
    )

if st.button("Compare responses"):
    if not prompt.strip():
        st.warning("Please enter the original user prompt.")
    elif not response_a.strip() or not response_b.strip():
        st.warning("Please provide both responses.")
    else:
        st.success("Comparison completed!")

        winner = (
            "Response A" if score_a > score_b
            else "Response B" if score_b > score_a
            else "Tie"
        )

        st.metric("Preferred response", winner)

        results = pd.DataFrame({
            "Response": ["A", "B"],
            "Quality score": [score_a, score_b]
        })

        st.bar_chart(
            results.set_index("Response")
        )

st.divider()

st.caption(
    "EvalLab AI | Independent software project "
    "| Built for AI quality evaluation"
)
