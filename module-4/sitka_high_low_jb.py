import csv
from datetime import datetime
from matplotlib import pyplot as plt
import sys

filename = 'sitka_weather_2018_simple.csv'

# Read data from CSV
dates, highs, lows = [], [], []
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        highs.append(int(row[5]))
        lows.append(int(row[6]))

# Function to plot highs
def plot_highs():
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')
    plt.title("Daily high temperatures - 2018", fontsize=20)
    plt.xlabel('', fontsize=12)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.show()

# Function to plot lows
def plot_lows():
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')
    plt.title("Daily low temperatures - 2018", fontsize=20)
    plt.xlabel('', fontsize=12)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.show()

# Main menu loop
while True:
    print("\nSelect an option: Highs / Lows / Exit")
    choice = input("jb: ").strip().lower()

    if choice == 'highs':
        plot_highs()
    elif choice == 'lows':
        plot_lows()
    elif choice == 'exit':
        print("Thanks for using the program. Goodbye!")
        sys.exit()
    else:
        print("Invalid choice. Please type Highs, Lows, or Exit.")