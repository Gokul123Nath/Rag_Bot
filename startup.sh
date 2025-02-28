#!/bin/sh

# Start the Uvicorn server
uvicorn "src.api:create_app" --reload --factory &

# Start the Streamlit application
streamlit run src/ui.py
