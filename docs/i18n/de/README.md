<p align="center"><img src="../../../site/assets/mark.svg" width="70" alt="ToolIndex"></p>
<h1 align="center">ToolIndex</h1>
<p align="center"><a href="../../../README.md">English</a> · <a href="../es/README.md">Español</a> · <a href="../zh-CN/README.md">简体中文</a> · <a href="../fr/README.md">Français</a> · <a href="../ja/README.md">日本語</a> · <a href="../de/README.md">Deutsch</a> · <a href="../pt-BR/README.md">Português (Brasil)</a></p>
<p align="center">Werkzeuge für KI-Agenten. Klare Einrichtung. Direkte Quellenlinks.</p>
<p align="center"><a href="https://toolindex.org/">toolindex.org</a> · <a href="https://github.com/OpenRootdev/toolindex/issues/new?template=submit-tool.yml">Ein Werkzeug einreichen</a></p>

ToolIndex ist ein offenes Verzeichnis für Skills, MCP-Server, CLIs, APIs, Bibliotheken, Plugins, Workflows und Harnesses, die KI-Agenten nutzen können. Lokale Pakete, gehostete Dienste und kommerzielle Werkzeuge sind willkommen, wenn Zugang, Preise und Bedingungen klar sind.

## Welche Werkzeuge passen

Nützliche Werkzeuge für eine konkrete Aufgabe, vom kleinen Skill-Ordner bis zur Dienst-API. Jeder Eintrag verlinkt direkt zum Quellrepository oder zur offiziellen Dokumentation und erklärt Installation oder Verbindung, manuelle Einrichtung, Lizenz oder Bedingungen, Version und Prüfumfang.

## Ein Werkzeug einreichen

1. Öffne das GitHub-Formular mit Name, Typ, Quelle und Zweck des Werkzeugs.
2. Beschreibe Paket oder Dienst, Installations- oder Zugangsschritte, Version, Lizenz oder Bedingungen, benötigte Zugangsdaten und Kosten. Keine Geheimnisse einreichen.
3. Ein Logo oder eigenes Bild ist optional. Gib gegebenenfalls URL, Quelle und Alternativtext an; sonst zeigt der Eintrag neutrale Initialen.
4. Die Verantwortlichen prüfen und veröffentlichen freigegebene Einträge. Fork, Pull Request oder ToolIndex-Konto sind nicht nötig; das Formular benötigt ein GitHub-Konto.

[CONTRIBUTING.md](CONTRIBUTING.md) · [JSON](../../../docs/listing.example.json)

## Geprüfte Beispiele

Ein Skill für Markenanimationen und ein Blender-MCP-Connector zeigen zwei mögliche Werkzeugtypen. Quellcode und Releases bleiben in den eigenen Repositories.

- [Smooth Motion Graphics](https://toolindex.org/tools/smooth-motion-graphics/)
- [ViperMesh for Blender](https://toolindex.org/tools/vipermesh-blender/)

## Bauen und Vorschau

Python 3.11+ erstellt die statische Website. Das Frontend nutzt HTML, CSS und JavaScript; die Suche ergänzt Seiten, die auch ohne JavaScript lesbar bleiben.

```sh
python scripts/catalog.py validate
python -m unittest discover -s tests -v
python scripts/catalog.py build
python -m http.server 4201 --directory dist
```

`http://localhost:4201/`

## Google-Cloud-Hosting

Cloud Run betreibt die Website mit mindestens 0 und höchstens 2 Instanzen sowie anfragebasierter Abrechnung. Firebase Hosting übernimmt HTTPS für die Domain und leitet Anfragen weiter. Das Staging-Skript schließt private Workspace-Dateien aus. Die Domainaktivierung hängt von DNS- und Zertifikatsprüfung ab.

`python scripts/stage_cloudrun.py` · [`firebase.json`](../../../firebase.json) · [docs/discovery.md](docs/discovery.md)

## Prüfungen und Community-Badges

Einrichtungs- und Artefaktprüfungen beschreiben konkrete Nachweise, keine universelle Kompatibilität. Ein optionales Badge ermöglicht einen transparenten Community-Boost für 14 Tage. Harneloop-Attribution ist optional; kein Framework ist vorgeschrieben.

[docs/badge-program.md](docs/badge-program.md)
