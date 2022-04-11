import csv
import questionary
from pathlib import Path

header = ["Lender","Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]
def save_csv(data):
    csvpath = questionary.text("Please enter a name for your file (.csv):").ask()
    csvpath = Path(csvpath)
    print("Writing data to a CSV file...")

    with open(csvpath,'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile,delimiter = ',')
        csvwriter.writerow(header)
        for entry in data:
            csvwriter.writerow(entry)
    #print(entry.keys())
