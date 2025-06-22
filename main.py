import streamlit as st
import pandas as pd

# Sample data (you can load from CSV or DB)
texts = [
    "Apple is looking at buying a startup in the UK.",
    "The rain in Spain stays mainly in the plain.",
    "NASA launched a new satellite yesterday."
]

labels = ["Tech", "Weather", "Space", "Other"]

# Save annotations here
if "annotations" not in st.session_state:
    st.session_state.annotations = []

st.title("📝 Text Annotation Tool")

# Current index tracker
if "index" not in st.session_state:
    st.session_state.index = 0

if st.session_state.index < len(texts):
    text = texts[st.session_state.index]
    st.markdown(f"**Text #{st.session_state.index + 1}:** {text}")

    selected_label = st.radio("Choose a label:", labels, key="label_selector")

    if st.button("Submit Annotation"):
        st.session_state.annotations.append({
            "text": text,
            "label": selected_label
        })
        st.session_state.index += 1
        st.rerun()
else:
    st.success("🎉 Annotation Complete!")
    df = pd.DataFrame(st.session_state.annotations)
    st.dataframe(df)

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", csv, "annotations.csv", "text/csv")
