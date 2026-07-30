# Stuck Label Rescue

A small Streamlit tool that turns the label material, underlying surface, age,
and user's priority into a bounded removal sequence, a stop rule, and one
immediate action.

## Run locally

```bash
python -m pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Test

```bash
python -m compileall -q streamlit_app.py tests
pytest -q
```

No external API, account, database, analytics, or sensitive data is used.
