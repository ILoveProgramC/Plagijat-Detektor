from nltk.tokenize import word_tokenize, sent_tokenize
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

def check_plagiarism(filepath, result_label, progress_bar):
    global done  # Globalna promjenljiva done koja označava da se provjera završila
    done = False

    # Učitavanje teksta iz datoteke
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        selected_text = file.read()

    # Učitavanje modela mBERT
    model = SentenceTransformer('distiluse-base-multilingual-cased-v2')

    # Kodiranje izabranog teksta
    new_vec = model.encode([selected_text.lower()])[0]

    # Definisanje direktorijuma
    directory = os.path.dirname(os.path.realpath(__file__))

    # Inicijalizacija lista za dokumente i imena datoteka
    documents = []
    filenames = []

    # Prolazak kroz sve datoteke u direktorijumu
    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)

        # Provjera da li datoteka ima ekstenziju .txt i da nije izabrana datoteka
        if filename.endswith(".txt") and filename != os.path.basename(filepath):
            with open(full_path, 'r', encoding='utf-8', errors='ignore') as file:
                text = file.read()

            # Preskakanje datoteka koje imaju manje od 20 reči
            if len(word_tokenize(text.lower())) < 20:
                continue

            # Bolje čišćenje teksta: Uklanjanje nepotrebnih znakova i bjelina
            text_cleaned = ' '.join(word_tokenize(text.lower()))

            # Dodavanje teksta i imena datoteke u liste
            documents.append(text_cleaned)
            filenames.append(filename)

    # Kodiranje svih dokumenata
    embeddings = model.encode(documents)

    # Promjena praga sličnosti
    similarity_threshold = 0.6

    # Pronalaženje sličnih datoteka
    similar_files = [(filenames[i], cosine_similarity([new_vec], [embeddings[i]])[0][0]) for i in range(len(documents)) if cosine_similarity([new_vec], [embeddings[i]])[0][0] > similarity_threshold]

    # Zaustavljanje progress bara
    progress_bar.stop()

    # Ažuriranje rezultata
    result_label.config(state='normal')
    result_label.delete('1.0', "end")
    if similar_files:
        result_text = "\nVeliki procenat sličnosti je detektovan u sljedećim dokumentima:\n\n"
        for filename, similarity in similar_files:
            result_text += f"{filename}   ===>   {similarity * 100:.2f}% sličnosti\n"
        result_label.insert("end", result_text)
        result_label.config(fg="red", font=("Arial", 14))
    else:
        result_label.insert("end", "Nema velikog procenta sličnosti. Vaš tekst je originalan.")
        result_label.config(fg="green", font=("Arial", 14))
    result_label.tag_configure("center", justify='center')
    result_label.tag_add("center", 1.0, "end")
    result_label.config(state='disabled')

    # Postavljanje done na True da se oznaci da je provjera završena
    done = True
