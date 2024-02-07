# Plagijat Detektor

Ovaj program omogućava korisnicima da detektuju plagijat u tekstualnim dokumentima. Program se sastoji od dva glavna modula:

1. **PlagiarismGUI**: Modul koji pruža korisnički interfejs za izbor datoteka i pokretanje provere plagijata.
   
2. **PlagiarismAlgorithm**: Modul koji sadrži logiku iza detekcije plagijata, koristeći NLTK za tokenizaciju reči, Sentence Transformers za kodiranje teksta i sklearn za izračunavanje kosinusne sličnosti.

## Opis programa

Cilj ovog programa je detekcija plagijata, to jest detekcija velikog procenta sličnosti između 2 datoteke. Napomena: u pitanju su samo tekstualne datoteke. U samom programu je dodan prag koji ako se prekorači, datoteka će biti označena kao plagijat. Prag se može namjestiti od samog korisnika ali je po "defaultu" namješteno ako datoteka ima sličnost sa drugim datotekama preko 60%, biće označena kao plagijat. Takođe program provjerava sve tekstualne datoteke koje se nalaze u samom direktorijumu programa i poredi svaku takvu datoteku sa izabranom datotekom (datoteku koju je korisnik uzeo da provjerava). Ako ima više datoteka koje su slične izabranoj u grafičkom korisničkom pročelju će se ispisati nazivi takvih datoteka i procenat sličnosti. 


## Upotreba

### Pokretanje programa

Program se pokreće pokretanjem `PlagiarismGUI.py`. Nakon pokretanja, korisniku će se prikazati korisnički interfejs koji omogućava izbor tekstualne datoteke koju želi da proveri na plagijat.

### Izbor datoteke

Klikom na dugme "IZABERI", korisnik može odabrati tekstualnu datoteku koju želi da proveri na plagijat.

### Provera plagijata

Nakon izbora datoteke, program će pokrenuti proveru plagijata. Tokom ovog procesa, korisniku će biti prikazivane statusne poruke o toku provere. Po završetku provere, program će prikazati rezultate u korisničkom interfejsu, ukazujući na eventualne plagijate ili obaveštavajući da tekst nije pronađen kao plagijat.

## Zahtevi

- Python 3.x
- NLTK
- Sentence Transformers
- scikit-learn

## Autor

Ovaj program je razvio [Vaše Ime/Organizacija], inspirisan potrebom za efikasnom detekcijom plagijata u tekstualnim dokumentima.

## Licence

Ovaj program je dostupan pod [navesti naziv licence]. Za više informacija pogledajte `LICENSE` datoteku.

---
*Napomena: Ovaj README fajl može biti ažuriran ili modifikovan kako bi se odražavale promene ili dodavale nove funkcionalnosti programa.*
