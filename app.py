import streamlit as st
import json
import tempfile
import os
from final_pipeline import main as run_pipeline  # Ensure final_pipeline.py is in same folder
import pandas as pd
# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Speaker Diarization & Role Detection",
    page_icon="🎙",
    layout="wide"
)

# ---------------- HEADER ----------------
# ---------------- HEADER ----------------
st.markdown(
    """
    <style>
    .big-title {
        font-size: 200px;
        font-weight: bold;
        text-align: center;
        background: -webkit-linear-gradient(45deg, #ff4b4b, #ffbb00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
    }
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #cccccc;
        margin-top: 0;
    }
    </style>
    <p class="big-title">SPEAKER DIARIZATION AND ROLE DETECTION</p>
    """,
    unsafe_allow_html=True
)


st.markdown('<p class="subtitle">Upload an audio file to detect speakers, transcribe speech, detect languages, and assign roles.</p>', unsafe_allow_html=True)

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader("📂 Upload an audio file", type=["wav", "mp3", "flac"])

if uploaded_file is not None:
    # Save uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(uploaded_file.read())
        audio_path = tmp.name

    st.audio(audio_path, format="audio/wav")

    with st.status("Processing audio...", expanded=True) as status:
        st.write("🔍 Running diarization...")
        output_folder = run_pipeline(audio_path, return_folder=True)

        st.write("📄 Reading output JSON...")
        final_json_path = os.path.join(output_folder, "final_output.json")
        with open(final_json_path, "r", encoding="utf-8") as f:
            result_json = json.load(f)

        st.write("🖼 Preparing timeline image...")
        timeline_img_path = os.path.join(output_folder, "timeline.png")

        transcript_path = os.path.join(output_folder, "final_transcript.docx")

        st.write("✅ Done!")
        status.update(label="Processing complete!", state="complete")

    # ---------------- SUMMARY STATS ----------------
    total_speakers = len(result_json["speakers"])
    total_time = result_json["segments"][-1]["endSec"] if result_json["segments"] else 0
    detected_langs = ", ".join(result_json.get("detectedLanguages", [])) or "Unknown"

    col1, col2, col3 = st.columns(3)
    col1.metric("🗣 Speakers", total_speakers)
    col2.metric("⏱ Duration (s)", f"{total_time:.1f}")
    col3.metric("🌎 Languages", detected_langs)

    st.markdown("---")

    # ---------------- LAYOUT: JSON + TIMELINE/TABLE ----------------
    left_col, right_col = st.columns([1, 1])

    with left_col:
        st.subheader("📄 Output JSON")
        st.json(result_json)

        # Download JSON
        st.download_button(
            label="⬇ Download JSON",
            data=json.dumps(result_json, indent=2),
            file_name="final_output.json",
            mime="application/json"
        )

    with right_col:
        st.subheader("🕒 Speaker Timeline")
        if os.path.exists(timeline_img_path):
            st.image(timeline_img_path, use_column_width=True)
            with open(timeline_img_path, "rb") as img_file:
                st.download_button(
                    label="⬇ Download Timeline PNG",
                    data=img_file,
                    file_name="timeline.png",
                    mime="image/png"
                )

        st.subheader("📊 Speakers & Roles")
        sp_table = []
        for sp in result_json["speakers"]:
            role_badge = f"<span class='badge {sp['role']}'>{sp['role']}</span>"
            sp_table.append({
                "Speaker ID": sp["id"],
                "Role": role_badge,
                "Confidence": sp["confidence"]
            })
        st.write(
            "<style>table td:nth-child(2) {text-align: center;}</style>",
            unsafe_allow_html=True
        )
        st.write(
            pd.DataFrame(sp_table).to_html(escape=False, index=False),
            unsafe_allow_html=True
        )

        # Download Transcript
        if os.path.exists(transcript_path):
            with open(transcript_path, "rb") as doc_file:
                st.download_button(
                    label="⬇ Download Transcript DOCX",
                    data=doc_file,
                    file_name="final_transcript.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
