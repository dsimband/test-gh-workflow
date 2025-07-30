import os
import sys

# Ensure the src directory is on the Python path for tests
ROOT = os.path.dirname(os.path.dirname(__file__))
SRC_PATH = os.path.join(ROOT, "src")
sys.path.insert(0, SRC_PATH)
