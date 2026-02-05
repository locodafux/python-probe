print("""### 13. Virtual Environments
- Create a virtual environment
- Activate / deactivate venv
- Install packages inside venv
""")

uv python install 3.13
uv venv --python 3.13
source .venv/bin/activate
uv pip install -r requirements.txt

#To deactivate the virtual environment just type
deactivate
