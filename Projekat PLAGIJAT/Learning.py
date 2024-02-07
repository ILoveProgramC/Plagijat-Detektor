from sentence_transformers import SentenceTransformer, InputExample, losses
from nltk.tokenize import sent_tokenize
from torch.utils.data import DataLoader
import os

# Učitavanje mBERT modela
model = SentenceTransformer('distiluse-base-multilingual-cased-v2')

# Definisanje skupa podataka za obuku
train_examples = []
directory = os.path.dirname(os.path.realpath(__file__))

# Prolazak kroz sve datoteke u direktorijumu
for filename in os.listdir(directory):
    full_path = os.path.join(directory, filename)

    # Provera da li datoteka ima ekstenziju .txt
    if filename.endswith(".txt"):
        with open(full_path, 'r', encoding='utf-8', errors='ignore') as file:
            text = file.read()

        # Tokenizacija teksta na rečenice
        sentences = sent_tokenize(text)

        # Dodavanje parova uzastopnih rečenica u skup za obuku
        for i in range(len(sentences) - 1):
            train_examples.append(InputExample(texts=[sentences[i], sentences[i+1]], label=1.0))

# Definisanje DataLoader-a i funkcije gubitka
train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=16)
train_loss = losses.CosineSimilarityLoss(model)

# Obuka modela
model.fit(train_objectives=[(train_dataloader, train_loss)], epochs=1, warmup_steps=10)

# Čuvanje modela
model.save("model_l")
