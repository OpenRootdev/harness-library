# Einen Harness einreichen

ToolIndex umfasst alle Werkzeuge, die KI-Agenten nutzen können: Skills, MCP-Server, CLIs, APIs, Bibliotheken, Plugins, Workflows und Harnesses. Gehostete und kommerzielle Werkzeuge sind willkommen, wenn Zugang, Preise, Authentifizierung und Bedingungen klar sind. Jeder Eintrag verlinkt direkt auf das Quellrepository oder die offizielle Dokumentation.

Ein Logo oder eigenes Bild ist optional. Falls vorhanden, bitte Quelle und Alternativtext angeben; sonst zeigt der Eintrag neutrale Initialen. Wähle einen Werkzeugtyp und beschreibe Installation oder Dienstzugang. Quellen außerhalb von GitHub sind erlaubt; automatische README-Badge-Prüfungen unterstützen derzeit nur GitHub.

**Neue Einreichungen sind willkommen.** Wir suchen praktische, wiederverwendbare Agent-Konfigurationen, auch kleine Skill-Ordner. Harneloop ist optional.

Der einfachste Weg benötigt weder Fork noch Pull Request:

1. [Öffnen Sie das GitHub-Einreichungsformular](https://github.com/OpenRootdev/toolindex/issues/new?template=submit-tool.yml). Teilen Sie Repository, Name und Aufgabe/Kategorie mit.
2. Erklären Sie Installation, gezielte Distribution, Version/Lizenz und manuelle Verbindungen. Zusätzliche Angaben zur Zusammensetzung und Testnachweise sind optional.
3. Maintainer prüfen Ihr Issue, fragen dort bei Bedarf nach fehlenden Angaben und veröffentlichen genehmigte Einträge. Spätere Änderungen können in einem weiteren Issue oder PR eingereicht werden.

Für das Formular benötigen Sie nur ein GitHub-Konto. Der [Website-Leitfaden](https://toolindex.org/submit/) erklärt denselben Ablauf.

Für einen PR kopieren Sie `docs/listing.example.json` nach `data/listings/your-slug.json`. Verwenden Sie denselben kleingeschriebenen Slug im Dateinamen und in `id`. Führen Sie `python scripts/catalog.py validate` und die im README beschriebenen Tests aus.

Erforderliche Angaben:

- Name, kurze Zusammenfassung, Kategorie, Quellrepository, Lizenz und Version oder festgelegte Revision.
- URL der gezielten Distribution, deren Inhalt und die Angabe, ob das Quellrepository auch irrelevantes Material enthält. Nutzen Sie für gemischte Repositorys ein herunterladbares Paket oder einen eigenen Harness-Branch; verlangen Sie nicht, dass Nutzer ein großes, sachfremdes Projekt klonen.
- Klare, geordnete Installationsanweisungen. Nennen Sie Arbeitsverzeichnis, Voraussetzungen, Agent-/Client-Integration und Einstieg. Verlinken Sie clientspezifische Hinweise, wenn sich die Erkennung unterscheidet.
- Manuelle Verbindungen/Konfiguration, erforderliche MCPs oder Werkzeuge, gegebenenfalls Zugangsdaten und weitere Hinweise. Verwenden Sie leere Listen, wenn nichts erforderlich ist. Reichen Sie niemals Geheimnisse ein.

Optional: Skill-/Referenz-/Dateizahlen, Anzahl der MCP-Werkzeuge auf oberster Ebene, Ausführungswerkzeuge, detaillierte Zusammensetzung und ein belegter Herkunftshinweis „Built with Harneloop“. Unterscheiden Sie optionale von erforderlichen Werkzeugen sowie Dispatch-Werkzeuge auf oberster Ebene von nachgelagerten Operationen.

Erlaubte Kategorien: Creative, 3D & Blender, Coding, Research, Data, Operations, Other. Schlagen Sie im Issue eine neue Kategorie vor, wenn keine passt.

Ergänzen Sie keine Prüf- oder Boost-Felder in Ihrem Eintrag und ändern Sie keine Maintainer-Nachweise. Maintainer verwalten `data/reviews.json` und `data/boosts.json`. Herkunftsangaben und Testbehauptungen benötigen Belege; ein veröffentlichtes Paket allein beweist nicht, dass es korrekt läuft. Maintainer prüfen Anweisungen, Quellumfang, Lizenzen, URLs und behauptete Artefakte; eingereichte Skripte werden niemals automatisch ausgeführt.

Halten Sie Änderungen eng auf ihren Zweck begrenzt. Aktualisierungen von Quellpaketen oder Installationsschritten sollten Version und Änderungen nennen. Fehlerhafte Installationen können über ein normales Issue gemeldet werden.
