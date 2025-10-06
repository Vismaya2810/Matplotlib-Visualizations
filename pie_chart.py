import matplotlib.pyplot as plt

# Data to plot
subjects = ['Mathematics', 'Science', 'Social Science', 'English', 'Hindi']
marks = [90,60,85,89,93]
colors = ['#66b3ff', '#99ff99', '#ffcc99', '#ff9999', '#c2c2f0']

# Pie Chart
plt.figure(figsize=(6,6)) # Plotting area
plt.pie(marks, labels=subjects, colors=colors, autopct='%1.1f%%', startangle=90,shadow=True)
plt.title("Mark obtained in examination", fontsize=14)
plt.axis('equal') 
plt.show()