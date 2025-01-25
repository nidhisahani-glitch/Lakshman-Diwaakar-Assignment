# Mutual Fund Allocation Change Tracker(AI INTERN ASSIGNMENT)
This is a Python-based framework that allows users to track changes in mutual fund allocations over time. The application takes multiple Excel files containing monthly portfolio data and compares the changes in fund allocations, including quantity, market value, and percentage to NAV (Net Asset Value).

## Features :
- Upload multiple Excel files (each representing a month’s data).
- View the changes in fund allocations between consecutive months.
- Filter and visualize the top 10 changes in market value.
- Download the results as an Excel file.

## Installation :

### 1. Clone the repository: 
git clone https://github.com/nidhisahani-glitch/Lakshman-Diwaakar-Assignment.git

### 2. Install dependencies: 
pip install -r requirements.txt

### 3. Run the Streamlit App: 
streamlit run app.py

### 4. Upload your Excel files through the Streamlit UI and view the fund allocation changes:

## Deployment on Render :

#### 1. Go to Render.com and sign up/login.
#### 2. Select the Web Service option.
#### 3. Link your GitHub repository to Render.
#### 4. Set the environment to Python.
#### 5. In the "Build Command" field, enter:
pip install -r requirements.txt
#### 6. In the "Start Command" field, enter:
streamlit run app.py
#### 7. Deploy:
Once you configure the settings, Render will automatically build and deploy the app. The URL will be provided once the deployment is complete, and here is the live demo url--- https://lakshman-diwaakar-assignment.onrender.com
