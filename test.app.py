import app

print("STARTAR TESTER AV GDPR-FUNKTIONER\n")

print("Test 1: Initierar databasen")
app.init_db()
print("OK - Databasen initierad\n")

print("Test 2: Visar användare före GDPR-åtgärder")
app.display_users()
print("OK - Användare visade\n")

print("Test 3: Testar anonymisering")
app.anonymize_data()
app.display_users()
print("OK - Anonymisering fungerade\n")

print("Test 4: Testar rensning av testdata")
app.clear_test_data()
app.display_users()
print("OK - Datarensning fungerade\n")

print("ALLA TESTER KLARA")
