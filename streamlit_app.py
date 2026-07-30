"""Stuck Label Rescue: a deterministic, surface-aware removal planner."""
from __future__ import annotations

import streamlit as st

from planner import SURFACES, build_plan


st.set_page_config(page_title="Stuck Label Rescue", page_icon="🏷️", layout="centered")
st.markdown(
    """
    <style>
    .block-container {max-width: 760px; padding-top: 2rem;}
    .result {border: 1px solid #d9ccb8; border-radius: 14px; padding: 1rem 1.2rem;
             background: #fffaf2; margin: .8rem 0;}
    .small-note {color: #5c554c; font-size: .92rem;}
    </style>
    """,
    unsafe_allow_html=True,
)

if "case_number" not in st.session_state:
    st.session_state.case_number = 1


def reset_case() -> None:
    for key in ("plan", "summary"):
        st.session_state.pop(key, None)
    st.session_state.case_number += 1


st.title("Stuck Label Rescue")
st.write("Choose what the label is stuck to. Get a short removal sequence with a clear stop rule before the item gets damaged.")

with st.form("label_case"):
    surface = st.selectbox("What is underneath the label?", list(SURFACES))
    label = st.radio("What kind of label is it?", ["Paper label", "Plastic film or tape"], horizontal=True)
    age = st.radio("How long has it been there?", ["Fresh (under a week)", "Old or unknown"], horizontal=True)
    priority = st.radio("What matters most?", ["Protect the item", "Finish sooner"], horizontal=True)
    submitted = st.form_submit_button("Build my removal plan", type="primary", use_container_width=True)

if submitted:
    st.session_state.plan = build_plan(surface, label, age, priority)
    st.session_state.summary = f"{label} on {surface.lower()} · {age.lower()} · {priority.lower()}"

if "plan" in st.session_state:
    plan = st.session_state.plan
    st.markdown(f"<div class='result'><strong>{plan['badge']}</strong><br><span class='small-note'>{st.session_state.summary}</span></div>", unsafe_allow_html=True)
    st.subheader("Your safest sequence")
    for number, step in enumerate(plan["steps"], 1):
        st.markdown(f"**{number}.** {step}")
    st.warning(f"**Stop rule:** {plan['stop']}")
    st.success(f"**Do this now:** {plan['first_action']}")
    st.button("Start a new case", on_click=reset_case, use_container_width=True)

with st.expander("About this tool"):
    st.write("This tool favors common household methods, surface-specific limits, and early stop signals. It does not recommend strong solvents or sharp scrapers.")
    st.caption("Privacy: Your choices stay in this browser session. Nothing is uploaded, stored, or sent to an external API.")
