
import streamlit as st
import pandas as pd
from evaluator import evaluate_responses

st.set_page_config(
    page_title="EvalLab AI",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 EvalLab AI")
st.caption("AI Response Evaluation & Quality Intelligence Platform")

st.markdown("""
Evaluate, compare and analyze AI-generated responses
through structured quality assessment.
""")

if "history" not in st.session_state:
    st.session_state.history = []

st.divider()

st.header("Response Comparison")

prompt = st.text_area(
    "Original user prompt",
    placeholder="Enter the user prompt..."
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Response A")
    response_a = st.text_area(
        "Model A output",
        key="response_a"
    )
    score_a = st.slider(
        "Quality score — A",
        0, 10, 5
    )

with col2:
    st.subheader("Response B")
    response_b = st.text_area(
        "Model B output",
        key="response_b"
    )
    score_b = st.slider(
        "Quality score — B",
        0, 10, 5
    )

if st.button("Evaluate responses", type="primary"):
    if not prompt.strip():
        st.warning("Please enter the original prompt.")
    else:
        try:
            result = evaluate_responses(
                response_a,
                response_b,
                score_a,
                score_b
            )

            result["prompt"] = prompt
            st.session_state.history.append(result)

            st.success("Evaluation completed!")

            col_a, col_b, col_c = st.columns(3)

            col_a.metric("Preferred response", result["winner"])
            col_b.metric("Score A", result["score_a"])
            col_c.metric("Score B", result["score_b"])

            st.metric(
                "Score difference",
                result["score_difference"]
            )

        except ValueError as error:
            st.error(str(error))

st.divider()

st.header("Evaluation History")

if st.session_state.history:
    history_df = pd.DataFrame(
        st.session_state.history
    )

    st.dataframe(
        history_df,
        use_container_width=True
    )

    st.download_button(
        "Download evaluation report",
        history_df.to_csv(index=False),
        file_name="evallab_report.csv",
        mime="text/csv"
    )
else:
    st.info("No evaluations recorded yet.")

st.divider()

st.caption(
    "EvalLab AI | Independent software project"
)
