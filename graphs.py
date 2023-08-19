import matplotlib.pyplot as plt

# Years
years = [1950, 1970, 1990, 2010, 2020]

# Corresponding world population in billions
population = [2.5, 3.7, 5.3, 7.0, 7.8]

# Create a bar graph
plt.figure(figsize=(10, 5))
plt.bar(years, population, color='blue')
plt.title('World Population Over Time (Bar Graph)')
plt.xlabel('Year')
plt.ylabel('Population (Billions)')
plt.show()

# Create a line graph
plt.figure(figsize=(10, 5))
plt.plot(years, population, marker='o', linestyle='-', color='green')
plt.title('World Population Over Time (Line Graph)')
plt.xlabel('Year')
plt.ylabel('Population (Billions)')
plt.grid(True)
plt.show()

# Create a pie chart
plt.figure(figsize=(6, 6))
labels = [f'{year}: {pop}B' for year, pop in zip(years, population)]
plt.pie(population, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('World Population Distribution (Pie Chart)')
plt.show()


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
