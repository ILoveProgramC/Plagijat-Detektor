from nltk.tokenize import word_tokenize
from tkinter import filedialog
from tkinter import Tk, Label, Button, Scale, IntVar, Scrollbar, Text, Entry, StringVar
from tkinter import ttk
import threading
import time
import random
import PlagiarismAlgorithm


def update_status_label(status_label, window):
    """
    Funkcija za ažuriranje statusne poruke tokom provere.
    """
    # Definisanje mogućih statusnih poruka
    status_messages = ["Provjera u toku", "Ovo ce potrajati...", "Zavrsavam", "Uradite par sklekova...", "Popijte kafu...", "Provjeravam dokument",
                       "Ovo bas traje dugo...", "Da li je svemir beskonacan ili ne?", "Da bi zaspali moramo se praviti da spavamo", "Da li slijepi ljudi vide u snovima?!",
                       "Andrew Tate je izmisljen lik", "Ovaj program ne valja cim dugo ovo radi!", "Nadam se da cu proci ispit"]

    # Prikazivanje prvih nekoliko poruka
    for i in range(2):
        status_label.config(text=status_messages[i], fg="purple")
        window.update()
        time.sleep(2)

    # Resetovanje promenljive done
    PlagiarismAlgorithm.done = False

    # Ažuriranje statusne poruke dok se provjera ne završi
    while not PlagiarismAlgorithm.done:
        status_label.config(text=random.choice(status_messages[2:]), fg="purple")
        window.update()
        if PlagiarismAlgorithm.done:
            break
        time.sleep(2)

    # Brisanje statusne poruke kada se provjera završi
    status_label.config(text="")


def select_file_and_check_plagiarism(progress_bar, status_label, result_label, window):
    """
    Funkcija za izbor datoteke i pokretanje provere.
    """
    # Resetovanje promenljive done
    PlagiarismAlgorithm.done = False

    # Brisanje prethodnih rezultata
    result_label.config(state='normal')
    result_label.delete('1.0', "end")
    result_label.config(state='disabled')

    # Izbor datoteke
    filepath = filedialog.askopenfilename()

    # Prekid ako datoteka nije izabrana
    if not filepath:
        return

    # Provjera da li datoteka ima dovoljno riječi
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        selected_text = file.read()
    if len(word_tokenize(selected_text.lower())) < 20:
        result_label.config(state='normal')
        result_label.delete('1.0', "end")
        result_label.insert("end", "Izabrani dokument mora imati više od 20 riječi.")
        result_label.config(fg="red", font=("Arial", 14))
        result_label.tag_configure("center", justify='center')
        result_label.tag_add("center", 1.0, "end")
        result_label.config(state='disabled')
        return

    # Pokretanje provjere
    status_label.config(text="Provjera u toku", fg="purple")
    progress_bar.start(20)
    threading.Thread(target=PlagiarismAlgorithm.check_plagiarism, args=(filepath, result_label, progress_bar)).start()
    if PlagiarismAlgorithm.done:
        return
    threading.Thread(target=update_status_label, args=(status_label, window)).start()


def create_gui():
    """
    Funkcija za kreiranje korisničkog interfejsa.
    """
    # Kreiranje prozora
    window = Tk()
    window.title("Plagijat Detektor")
    window.geometry("600x600")

    # Dodavanje elemenata u prozor
    title_label = Label(window, text="Plagijat Detektor", font=("Helvetica", 20), bg="lightblue")
    title_label.pack(pady=10)

    description_label = Label(window, text="Dobrodošli u Plagijat Detektor. Ovaj detektor vrši poređenje između izabranog dokumenta i baze dokumenata. Ako procenat sličnosti premašuje prag od 60% tekst će biti označen kao plagijat. Kliknite na 'IZABERI' i izaberite željeni dokument.", font=("Helvetica", 14), wraplength=400)
    description_label.pack(pady=20)

    select_button = Button(window, text="IZABERI", command=lambda: select_file_and_check_plagiarism(progress_bar, status_label, result_label, window), bg="blue", fg="white", width=20, height=3, font=("Helvetica", 12, "bold"))
    select_button.pack()

    progress_bar = ttk.Progressbar(window, length=200, mode='determinate')
    progress_bar.pack(pady=10)

    status_label = Label(window, text="", font=("Helvetica", 14))
    status_label.pack(pady=3)

    scrollbar = Scrollbar(window)
    scrollbar.pack(side="right", fill="y")

    result_label = Text(window, wrap="word", yscrollcommand=scrollbar.set, state='disabled')
    result_label.pack(pady=40)

    scrollbar.config(command=result_label.yview)

    # Pokretanje prozora
    window.mainloop()


if __name__ == "__main__":
    create_gui()
