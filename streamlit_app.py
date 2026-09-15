"""
Streamlit Cloud Entrypoint for AI-Powered Multi-Device Mobile Testing Agent.
"""

import sys
import runpy
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

app_path = BASE_DIR / "web" / "app.py"
runpy.run_path(str(app_path), run_name="__main__")
