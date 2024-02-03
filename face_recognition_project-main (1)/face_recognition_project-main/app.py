import streamlit as st
import pandas as pd
import os
import time 
from datetime import datetime

ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")

# Construct the file path using os.path.join
file_path = os.path.join("C:/Users/atulb/Downloads/face_recognition_project-main (1)/face_recognition_project-main/Attendance/Attendance_"+ date + ".csv")

# Check if the file exists before reading it
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    st.dataframe(df.style.highlight_max(axis=0))
else:
    st.write(f"File not found: {file_path}")
