# Password Weakness Analysis Script
# This script loads mock user data and checks for weak passwords.

import pandas as pd

# Load mock data
data = pd.read_csv('../data/mock-data.csv')

# Define a list of weak/common passwords
weak_passwords = ["12345", "password", "qwerty", "abc123", "iloveyou", "dragon", "monkey", "football", "princess", "welcome"]

# Check which users have weak passwords
weak_users = data[data['password'].isin(weak_passwords)]

print("Users with weak passwords:")
print(weak_users)
