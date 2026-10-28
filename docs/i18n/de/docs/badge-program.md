# Listed in ToolIndex: kostenloser Community-Boost von 14 Tagen

Das Programm belohnt Mitwirkende dafür, wiederverwendbare Harnesses leichter auffindbar zu machen. Es gibt keine Zahlung und keine Pflicht, Harneloop zu verwenden.

1. Lassen Sie Ihren Eintrag genehmigen.
2. Kopieren Sie den Badge-Code von der Detailseite im Verzeichnis und platzieren Sie ihn innerhalb der **ersten 30 Zeilen** des README im Standardbranch des Quellrepositorys.
3. Lassen Sie das Bild mit Ihrem exakten Eintrag verlinkt. Der nächste Verifizierungslauf gewährt einen einmaligen **Zeitraum von 14 Tagen**, beginnend mit der ersten erfolgreichen Prüfung in UTC.

Beispiel:

```md
[![Listed in ToolIndex](https://toolindex.org/badges/your-slug.svg)](https://toolindex.org/tools/your-slug/)
```

Exaktes Markdown oder ein gleichwertiges verlinktes HTML-Bild wird unterstützt. Der Alternativtext des Bildes muss „Listed in ToolIndex“ sein. Beispiele in Code-Fences oder HTML-Kommentaren zählen nicht.

Früher ausgegebene Rücklinks `https://toolindex.org/#your-slug` bleiben berechtigt und führen zur entsprechenden Seite. Nutzen Sie für neue Badges die echte Seiten-URL.

Aktive Einträge erscheinen vor regulären Einträgen; innerhalb beider Gruppen wird alphabetisch sortiert. Suche und Kategoriefilter gelten weiterhin. Das Verzeichnis zeigt auf der Detailseite ein **Community boost**-Label und dessen Ablaufdatum. Dies ist eine Werbeplatzierung; Prüfstatus und Qualitätsaussagen bleiben unabhängig.

Der tägliche Workflow auf dem vertrauenswürdigen main-Branch liest nur öffentliche GitHub-README-Metadaten. Er speichert die erste Gewährung, den Ablauf, die zuletzt festgestellte Badge-Präsenz und den Prüfzeitpunkt in `data/boosts.json`. Er führt keinen Code aus einem Harness-Repository aus. Wird das Badge entfernt, endet der Boost nach der nächsten Prüfung. Erneutes Einfügen kann nur die verbleibende ursprüngliche Laufzeit wiederherstellen. Abgelaufene Gewährungen verlängern sich niemals automatisch. Doppelte Einreichungen, Slug-Änderungen oder Repository-Transfers berechtigen denselben Harness nicht zu einer zweiten Erstbelohnung; Maintainer prüfen die Identität.

Ist GitHub vorübergehend nicht verfügbar, wird kein neuer Boost vergeben. Bereits geprüfte Badges bleiben ohne neue Prüfung höchstens 48 Stunden berechtigt und nie über ihr ursprüngliches Ablaufdatum hinaus. Sowohl statischer Build als auch Browser prüfen die Zeitstempel erneut. Nachweise benötigen die Zustimmung eines Maintainers; das Ändern eines JSON-Felds in einer Einreichung kann keinen Boost vergeben.

Das Badge kann nach Ablauf bleiben. Eine neue Richtlinie würde öffentlich diskutiert; es gibt keine versteckte wiederkehrende Werbung oder bezahlte Rangfolge.

Vor der Kaelux-Labs-Migration unter `https://toolindex.org/` ausgegebene Badges bleiben berechtigt. Die Migration startet das ursprüngliche 14-Tage-Fenster nicht neu. Aktualisieren Sie Bild und Rücklink bei Gelegenheit auf die neue kanonische Adresse.

ToolIndex umfasst alle Werkzeuge, die KI-Agenten nutzen können: Skills, MCP-Server, CLIs, APIs, Bibliotheken, Plugins, Workflows und Harnesses. Gehostete und kommerzielle Werkzeuge sind willkommen, wenn Zugang, Preise, Authentifizierung und Bedingungen klar sind. Jeder Eintrag verlinkt direkt auf das Quellrepository oder die offizielle Dokumentation.

Ein Logo oder eigenes Bild ist optional. Falls vorhanden, bitte Quelle und Alternativtext angeben; sonst zeigt der Eintrag neutrale Initialen. Wähle einen Werkzeugtyp und beschreibe Installation oder Dienstzugang. Quellen außerhalb von GitHub sind erlaubt; automatische README-Badge-Prüfungen unterstützen derzeit nur GitHub.
