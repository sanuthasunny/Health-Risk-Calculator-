import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('health_risk_data.db')
c = conn.cursor()

# Create table for storing user input and predictions
c.execute('''
    CREATE TABLE IF NOT EXISTS risk_predictions (
        id INTEGER PRIMARY KEY,
        age INTEGER,
        gender TEXT,
        sysBP INTEGER,
        diaBP INTEGER,
        bmi REAL,
        cholesterol INTEGER,
        diabetes INTEGER,
        smoker INTEGER,
        risk_prediction INTEGER,
        risk_probability REAL
    )
''')

# Insert user data and prediction
c.execute('''
    INSERT INTO risk_predictions (age, gender, sysBP, diaBP, bmi, cholesterol, diabetes, smoker, risk_prediction, risk_probability)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (age, gender, sysBP, diaBP, bmi, cholesterol, diabetes, smoker, risk_prediction, risk_probability))

# Commit and close connection
conn.commit()
conn.close()
