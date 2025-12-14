# GDPR Testdata System

## Syfte
Detta projekt visar hur ett enkelt system för
hantering av testdata kan byggas enligt GDPR. Projektet använder endast
testdata och inga riktiga personuppgifter.

Systemet demonstrerar Python, SQLite, Docker, Git/GitHub och CI/CD med
GitHub Actions.

---

## Tekniker
- Python 3.9
- SQLite
- Docker & Docker Compose
- Git & GitHub
- GitHub Actions (CI/CD)

---

## Funktionalitet
- SQLite-databas med tabellen `users`
- Två testanvändare skapas automatiskt:
  - peja@test.se
  - matilda@test.se

### GDPR-funktioner
- `anonymize_data()`  
  Anonymiserar namn och e-post (GDPR – anonymisering)

- `clear_test_data()`  
  Rensar all användardata (GDPR – Right to be Forgotten)

---

## Installation och start
1. Klona repot från GitHub
2. Gå till projektmappen
3. Starta applikationen med Docker:

```bash
docker-compose up --build -d

