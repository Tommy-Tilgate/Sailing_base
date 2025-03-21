# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KMFcOzFxKfGn5ZZY1i_t1RV-H6f57ozK
"""

!pip freeze > requirements.txt

!pip install streamlit

with open('requirements.txt', 'w') as f:
    f.write('streamlit\n')
    f.write('pandas\n')

from google.colab import files
files.download('requirements.txt')

