# Plagijat Detektor

Ovaj program omogućava korisnicima da detektuju plagijat u tekstualnim dokumentima. Program se sastoji od dva glavna modula i treći modul koji je opcionalan:

1. **PlagiarismGUI**: Modul koji pruža grafičko korisničko pročelje za izbor datoteka i pokretanje provjere plagijata.
   
2. **PlagiarismAlgorithm**: Modul koji sadrži logiku iza detekcije plagijata, koristeći NLTK za tokenizaciju reči, Sentence Transformers za kodiranje teksta i sklearn za izračunavanje kosinusne sličnosti.

3. **Learning**: Modul koji se koristi za obuku modela nad svojim tekstovima (nije obavezan ali se može iskoristiti za jačanje same detekcije).

## Opis programa

Cilj ovog programa je detekcija plagijata, to jest detekcija velikog procenta sličnosti između izabrane datoteke i baze datoteka. Napomena: u pitanju su samo tekstualne datoteke. U samom programu je dodan prag koji ako se prekorači, datoteka će biti označena kao slična (ne mora nužno biti plagijat ali može imati veći procenat sličnosti). Prag se može namjestiti od samog korisnika ali je po "defaultu" namješteno ako datoteka ima sličnost sa drugim datotekama preko 60%, biće označena kao slična. Takođe program provjerava sve tekstualne datoteke koje se nalaze u samom direktorijumu programa i poredi svaku takvu datoteku sa izabranom datotekom (datoteku koju je korisnik uzeo da provjerava). Ako ima više datoteka koje su slične izabranoj, u grafičkom korisničkom pročelju će se ispisati nazivi takvih datoteka i procenat sličnosti. Algoritam takođe primjećuje sličnosti između tekstova koji su napisani na raziličitom jeziku ali imaju ista značenja.

## Funkcionalnost algoritma

Algoritam funkcioniše u nekoliko koraka:
1. Učitavanje Teksta: Program učitava tekst iz izabrane datoteke koju korisnik želi da provjeri.
3. Učitavanje Modela: Učitava se model Sentence Transformers, tačnije mBERT (multilingual BERT), koji je prethodno obučen na velikom skupu podataka na više jezika. Ovaj model je sposoban da generiše reprezentacije ugnježđenih riječi i rečenica visokog kvaliteta.
4. Kodiranje Teksta: Nakon učitavanja modela, izabrani tekst se kodira u vektor, odnosno u numerički oblik koji model može da obradi.
5. Učitavanje Dokumenata: Algoritam prolazi kroz sve druge tekstualne dokumente u istom direktorijumu, osim izabrane datoteke, kako bi se provjerila njihova sličnost sa izabranim tekstom.
6. Tokenizacija i Kodiranje Dokumenata: Za svaki od tih dokumenata, prvo se vrši tokenizacija teksta, a zatim se taj tokenizovani tekst kodira u vektor koristeći isti mBERT model koji je korišćen za kodiranje izabranog teksta.
7. Izračunavanje Kosinusne Sličnosti: Nakon što su svi dokumenti kodirani u vektore, algoritam izračunava kosinusnu sličnost između kodiranog izabranog teksta i svakog od kodiranih dokumenata. Kosinusna sličnost se izračunava kao kosinus ugla između vektora i daje vrijednost između -1 i 1, gdje veće vrijednosti ukazuju na veću sličnost.
8. Identifikacija Plagijata: Dokumenti sa kosinusnom sličnošću iznad određenog praga, koji je postavljen na 0.6 u ovom slučaju, smatraju se plagijatima. Algoritam identifikuje te dokumente i prikazuje ih kao rezultate.

## Upotreba

### Pokretanje programa

Program se pokreće pokretanjem `PlagiarismGUI.py`. Nakon pokretanja, korisniku će se prikazati korisničko pročelje koje omogućava izbor tekstualne datoteke koju želi da provjeri.

### Izbor datoteke

Klikom na dugme "IZABERI", korisnik može odabrati tekstualnu datoteku koju želi da provjeri.

### Provjera plagijata

Nakon izbora datoteke, program će pokrenuti provjeru plagijata. Tokom ovog procesa, korisniku će biti prikazivane statusne poruke o toku provere. Po završetku provjere, program će prikazati rezultate u korisničkom pročelju, ukazujući na eventualne plagijate ili obaveštavajući da tekst nije pronađen kao plagijat.

## Alatke korištene u programu

- Python 3.x
- NLTK
- Sentence Transformers
- scikit-learn

