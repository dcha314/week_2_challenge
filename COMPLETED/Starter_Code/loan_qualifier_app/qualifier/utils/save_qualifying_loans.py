import csv
import questionary
from qualifier.utils.save_csv import save_csv

def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    # YOUR CODE HERE!
    save_data = questionary.confirm("Would you like to save your data?").ask()
    if save_data == 1:
        save_csv(qualifying_loans)
        print("Data saved!")
        print("Congratulations on your loans, Jinal!")
    else:
            print("Data omitted...")
            