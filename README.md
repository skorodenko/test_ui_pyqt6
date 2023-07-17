# test_ui_pyqt6
## How to run:
1. Install dependencies (or create .venv with poetry)
2. Run the following command
```
python3 main.py
```

## Some notes:
1. Only 64 length strings can be used to fill the table (can be changed)
2. All the interactions (save as, add column/row) are located in app menu. (Can be triggered by alt + __first letter of menu item__)
3. Do not save large tables to docx file (limitation of python-docx module)
