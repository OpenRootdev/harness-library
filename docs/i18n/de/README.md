<p align="center"><img src="../../../site/assets/mark.svg" width="70" alt="Harness Library"></p>
<h1 align="center">Harness Library</h1>
<p align="center"><a href="../../../README.md">English</a> · <a href="../es/README.md">Español</a> · <a href="../zh-CN/README.md">简体中文</a> · <a href="../fr/README.md">Français</a> · <a href="../ja/README.md">日本語</a> · <a href="README.md">Deutsch</a> · <a href="../pt-BR/README.md">Português (Brasil)</a></p>
<p align="center">Wiederverwendbare Agent-Harnesses entdecken, installieren und teilen.</p>
<p align="center"><a href="https://openrootdev.github.io/harness-library/">Bibliothek durchsuchen</a> · <a href="https://github.com/OpenRootdev/harness-library/issues/new?template=submit-harness.yml">Harness einreichen</a> · <a href="CONTRIBUTING.md">Einreichungsleitfaden</a></p>

Ein offenes Verzeichnis von Anweisungen, Skills, Werkzeugen und Workflows, die einem Agenten helfen, eine bestimmte Aufgabe gut zu erledigen. Ein Harness kann aus wenigen Dateien oder einer umfangreicheren Werkzeugkonfiguration bestehen. Jeder Eintrag erklärt die Installation, erforderliche manuelle Einstellungen und den benötigten Teil des Quellrepositorys.

Die ersten Einträge sind [Smooth Motion Graphics](https://github.com/Ker102/smooth-motion-graphics) und [ViperMesh for Blender](https://github.com/OpenRootdev/vipermesh-blender). Das bestehende Repository und die Releases von ViperMesh werden unverändert aufgeführt. Harneloop ist optional; damit erstellte Harnesses können nach Prüfung einen entsprechenden Herkunftshinweis anzeigen.

## Einen Harness in Aktion sehen

Das Harneloop-Erklärvideo zeigt den Animationsstil hinter dem [Smooth Motion Graphics Harness](https://openrootdev.github.io/harness-library/harnesses/smooth-motion-graphics/) der Bibliothek: gut lesbare Szenen, geschwungene Verbindungen und ruhige Übergänge. Es erklärt außerdem, wie Harneloop Harness-Einheiten erstellt und verbessert.

<p align="center"><a href="https://harneloop.kaelux.dev/media/harneloop-how-it-works.mp4"><img src="https://harneloop.kaelux.dev/media/harneloop-video-poster.png" alt="Die lautlose Harneloop-Motion-Graphics-Demo ansehen" width="860"></a></p>
<p align="center"><a href="https://harneloop.kaelux.dev/media/harneloop-how-it-works.mp4">Vollständiges Video ansehen · 3:40 · Ohne Ton, mit Erklärungen im Bild</a></p>

Das Video wird separat gehostet. Das eigene Installationspaket und den Beispielrenderer des Harness finden Sie über dessen Eintrag.

## Einen Harness einreichen

**Neue Einreichungen sind willkommen.** Wir suchen nützliche Harnesses für Programmierung, Recherche, Daten, kreative Arbeit, Blender und Betrieb. Wenige Skills können ausreichen; Harneloop ist nicht erforderlich.

1. [Öffnen Sie das kurze GitHub-Einreichungsformular](https://github.com/OpenRootdev/harness-library/issues/new?template=submit-harness.yml) und nennen Sie Ihr Repository sowie die Aufgabe, bei der es einem Agenten hilft.
2. Ergänzen Sie klare Installationsschritte, Kategorie, Lizenz, Versions- und Distributionsumfang sowie alle manuellen Einstellungen. Komponentenzahlen und Testnachweise sind optional.
3. Ein Maintainer prüft die Einrichtung, fragt bei Bedarf in Ihrem Issue nach und veröffentlicht genehmigte Einträge.

**Weder Fork noch Pull Request noch Harness-Library-Konto sind nötig.** Für das Formular ist ein GitHub-Konto erforderlich. Alternativ können Sie einen PR einreichen, der eine JSON-Datei in `data/listings/` ergänzt. Siehe [öffentlicher Einreichungsleitfaden](https://openrootdev.github.io/harness-library/submit/), [CONTRIBUTING.md](CONTRIBUTING.md) und [Vorlage](../../../docs/listing.example.json).

Ein Repository mit gemischten Inhalten muss ein gezieltes Paket oder einen eigenen Harness-Branch anbieten. Einreichende legen keine Verifizierungs- oder Werbelabel fest. Maintainer prüfen Einrichtung, Umfang und etwaige Nachweise vor der Veröffentlichung. „Artifacts checked“ bedeutet, dass die dokumentierten Artefakte geprüft wurden; es bedeutet nicht, dass alle Modelle, Plattformen oder Anwendungsfälle funktionieren.

## Kostenloses Badge-Programm

Fügen Sie das exakte Badge „Listed in Harness Library“ mit Rücklink zum Eintrag innerhalb der ersten 30 Zeilen Ihres Quell-README ein. Nach Verifizierung erhält Ihr Eintrag **einen einmaligen Community-Boost von 14 Tagen**, im Verzeichnis klar gekennzeichnet. Ein Boost beeinflusst die Reihenfolge, nicht den Prüfstatus. Er ist kostenlos, optional und läuft automatisch ab. Entfernen und erneutes Einfügen des Badges startet ihn nicht neu. [Richtlinie und Verifizierung](docs/badge-program.md).

## Entwicklung

Es sind weder Frontend-Abhängigkeiten noch ein Backend-Dienst nötig. Python 3.11+ führt Validator und Builder aus; die Oberfläche besteht aus einfachem HTML, CSS und JavaScript.

```sh
python scripts/catalog.py validate
python -m unittest discover -s tests -v
python scripts/catalog.py build
python -c "import shutil; shutil.copytree('dist', '.preview/harness-library', dirs_exist_ok=True)"
python -m http.server 4201 --directory .preview
```

Öffnen Sie `http://localhost:4201/harness-library/`. Die Vorschaukopie bedient den Produktionsbasispfad korrekt; aktualisieren Sie sie nach einem erneuten Build. Asset- und Navigationspfade entsprechen bewusst der GitHub-Pages-Projekt-URL.

`site/layout.html`, `site/style.css` und `scripts/publishing.py` erzeugen vollständige HTML-Seiten für das Verzeichnis, jeden Harness, den Einreichungsleitfaden und die Informationsseite. JavaScript ergänzt schrittweise Suche, Filter und Kopieren; Installationsinhalte und Navigation bleiben ohne JavaScript nutzbar. Builds veröffentlichen außerdem eine Sitemap, Markdown-Spiegel der Seiten, `llms.txt` und den geprüften JSON-Katalog. Siehe [Auffindbarkeit und Indexierung](docs/discovery.md) für die Einrichtung durch den Eigentümer und Crawl-Details.

`python scripts/catalog.py refresh` verifiziert freiwillig eingebundene Badges durch Lesen öffentlicher GitHub-README-Inhalte. Eingereichter Code wird niemals ausgeführt. GitHub Pages veröffentlicht den geprüften main-Branch; ein täglicher Workflow aktualisiert Badge-Nachweise und führt den Build erneut aus. Prüfungen externer PRs besitzen nur Leserechte.

Quelldaten und Prüfnachweise liegen in diesem Repository. Harness-Quellcode und Release-Assets liegen in den jeweiligen eigenen Repositorys. Mit dem Harneloop-Framework werden keine Harness-Videos, Abhängigkeiten oder privaten Entwicklungsaufzeichnungen installiert.
