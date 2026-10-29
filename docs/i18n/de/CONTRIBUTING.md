# Checkliste für Einreichungen

Ein offenes Verzeichnis mit Skills, MCP-Servern, CLIs, APIs, Bibliotheken, Plugins, Workflows und Harnesses für KI-Agenten. Jeder Eintrag verlinkt direkt auf die Quelle und beschreibt Einrichtung, Lizenz oder Bedingungen und Prüfumfang.

## Konten und Einreichungen

Konto erstellen, E-Mail bestätigen und einen dauerhaften Namen wählen. Anzeigename, Biografie, Website und optionaler Avatar sind anpassbar. Du entscheidest, ob dein Profil öffentlich und indexierbar ist.

Speichere einen privaten Entwurf in der Oberfläche und beantrage eine Prüfung. Bilder sind optional. Status und Rückmeldungen stehen im Konto. Nur genehmigte Versionen werden öffentlich; Änderungen werden erneut geprüft, während die letzte genehmigte Version sichtbar bleibt.

Verbinde einen Agenten mit dem MCP-Endpunkt. Beim ersten Zugriff öffnet sich die Anmeldung oder Registrierung im Browser mit ausdrücklicher Freigabe. Der Agent verwaltet Profil, Entwürfe und Prüfanfragen, kann aber nichts genehmigen oder veröffentlichen.

[UI](https://toolindex.org/account/) · [MCP](https://toolindex.org/developers/) · [Guide](https://toolindex.org/submit/)

## Checkliste für Einreichungen

Beschreibe Aufgabe, Quelle oder offizielle Dokumentation, Typ, Kategorie, Version, Lizenz oder Bedingungen, Installation oder Verbindung, Anmeldung und Kosten. Niemals Geheimnisse einreichen.

[JSON example](../../listing.example.json)

## Prüfung und Eigentum

Nur Eigentümer bearbeiten oder entfernen ihre Einreichungen. Nur ausdrücklich konfigurierte und bestätigte Prüfer dürfen veröffentlichen. Öffentliche Prüfnachweise gelten für ihren beschriebenen Umfang und garantieren nicht jedes Modell oder jede Plattform. Ablehnungen und ausstehende Inhalte bleiben privat.

## Beiträge zum Quellcode

Oberfläche und MCP benötigen kein Issue und keinen Pull Request. Codebeiträge bleiben willkommen. Bestehende Einträge sowie Prüf- und Badge-Belege bleiben versioniert; Maintainer-Belege bei einer Einreichung nicht verändern.

```sh
python scripts/catalog.py validate
python -m unittest discover -s tests -v
python scripts/validate_i18n.py
npm ci --prefix backend
npm test --prefix backend
```

[README.md](README.md) · [Backend](../../../backend/README.md) · [Badge program](docs/badge-program.md)
