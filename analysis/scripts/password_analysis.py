import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/mock-data.csv')

df['password_length'] = df['password'].apply(len)

def classify_strength(pw):
    if len(pw) < 6:
        return 'Weak'
    elif len(pw) < 10:
        return 'Medium'
    else:
        return 'Strong'

df['strength'] = df['password'].apply(classify_strength)

plt.hist(df['password_length'], bins=range(1, 15), color='skyblue', edgecolor='black')
plt.title('Distribution of Password Lengths')
plt.xlabel('Password Length')
plt.ylabel('Number of Users')
plt.savefig('../results/visuals/password_lengths.png')
plt.close()

strength_counts = df['strength'].value_counts()
strength_counts.plot(kind='bar', color=['red','orange','green'])
plt.title('Password Strength Classification')
plt.xlabel('Strength')
plt.ylabel('Number of Users')
plt.savefig('../results/visuals/password_strength.png')
plt.close()

print("Analysis complete. Charts saved in results/visuals/")
