import tkinter as tk
import csv
import tkinter.filedialog as filedialog
import os  # For limited file opening functionality

# Define window and title
window = tk.Tk()
window.title("Information Collector")

# Create labels and entry fields for user input
label_nom = tk.Label(window, text="Nom:")
label_nom.grid(row=0, column=0)
nom_entry = tk.Entry(window)
nom_entry.grid(row=0, column=1)

label_prenom = tk.Label(window, text="Prénom:")
label_prenom.grid(row=1, column=0)
prenom_entry = tk.Entry(window)
prenom_entry.grid(row=1, column=1)

label_age = tk.Label(window, text="Âge:")
label_age.grid(row=2, column=0)
age_entry = tk.Entry(window)
age_entry.grid(row=2, column=1)

label_statut_social = tk.Label(window, text="Statut social:")
label_statut_social.grid(row=3, column=0)
statut_social_var = tk.StringVar()
statut_social_dropdown = tk.OptionMenu(window, statut_social_var, "Célibataire", "Marié", "Divorcé", "Veuf/Veuve")
statut_social_dropdown.grid(row=3, column=1)


# Function to generate and download CSV data
def download_csv():
    # Retrieve user input
    nom = nom_entry.get()
    prenom = prenom_entry.get()
    age = age_entry.get()
    statut_social = statut_social_var.get()

    # Create CSV header row
    csv_header = "nom,prenom,age,statut_social\n"

    # Create CSV data row with user input
    csv_data = f"{nom},{prenom},{age},{statut_social}\n"

    # Get save location and filename from the user
    save_location = filedialog.asksaveasfilename(
        title="Sélectionnez un emplacement pour le fichier CSV",
        defaultextension=".csv",
        filetypes=[("Fichiers CSV", "*.csv")],
    )

    # Check if the user canceled the save dialog
    if not save_location:
        return

    # Save the CSV data to the chosen file
    with open(save_location, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow([csv_header.strip()])
        writer.writerow([csv_data.strip()])

    # Option 1: Display Full Path
    confirmation_label.config(text=f"Données téléchargées dans: {save_location}")

    # Option 2: Button to Open File (Limited Functionality)
    def open_downloaded_file():
        if not save_location:  # Check if download happened
            return

        try:
            os.startfile(save_location)
        except FileNotFoundError:
            confirmation_label.config(text="Fichier introuvable!")

    open_file_button = tk.Button(window, text="Ouvrir le fichier", command=open_downloaded_file)
    open_file_button.grid(row=6, column=0, columnspan=2)

# Create download button
download_button = tk.Button(window, text="Télécharger CSV", command=download_csv)
download_button.grid(row=4, column=0, columnspan=2)

# Confirmation label
confirmation_label = tk.Label(window, text="")
confirmation_label.grid(row=5, column=0, columnspan=2)

# Start the main loop
window.mainloop()