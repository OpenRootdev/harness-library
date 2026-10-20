# Auffindbarkeit und Indexierung

Aktueller Standort seit `2026-10-20`: [OpenRootdev/harness-library](https://github.com/OpenRootdev/harness-library) und das [Verzeichnis](https://openrootdev.github.io/harness-library/). Die historischen Hinweise unten beschreiben den vorherigen Umzug.

Das öffentliche Verzeichnis veröffentlicht vollständiges HTML unter stabilen URLs. Suchmaschinen, Browser ohne JavaScript und Agenten können Installation, Voraussetzungen, Quelle, Distribution und Prüfumfang jedes genehmigten Harness direkt lesen. JavaScript verbessert nur Filterung, Kopieren und die frühere Hash-Navigation.

## Öffentliche Ressourcen

- [Verzeichnis](https://openrootdev.github.io/harness-library/) und [Einreichungsleitfaden](https://openrootdev.github.io/harness-library/submit/).
- [Sitemap](https://openrootdev.github.io/harness-library/sitemap.xml): nur kanonische HTML-Seiten. Tägliche Badge-Prüfungen erfinden keine Änderungsdaten für Inhalte.
- [llms.txt](https://openrootdev.github.io/harness-library/llms.txt): ein kompakter Wegweiser zu Markdown-Installationsseiten und Daten.
- [llms-full.txt](https://openrootdev.github.io/harness-library/llms-full.txt): zusammengefasster öffentlicher Text.
- [catalog.json](https://openrootdev.github.io/harness-library/catalog.json): geprüfte Einträge, kanonische Seiten-URLs, Installation, manuelle Einrichtung und Belege mit definiertem Umfang.
- Jede kanonische HTML-Seite hat ein entsprechendes `index.md`, verlinkt mit `rel="alternate" type="text/markdown"`.

Jede HTML-Seite besitzt einen eindeutigen Titel, eine Beschreibung und eine kanonische URL, Metadaten für soziale Vorschauen und passendes JSON-LD. Strukturierte Daten beschreiben das tatsächliche Verzeichnis, den Maintainer und die Harnesses; sie erfinden keine Bewertungen, Downloads oder universelle Kompatibilität. Unbekannte Pfade liefern den GitHub-Pages-Status 404 über die noindex-Fehlerseite. Alte Hash-Links für Einträge werden weiterhin unterstützt.

## Einrichtung durch den Eigentümer

1. Fügen Sie in [Google Search Console](https://search.google.com/search-console) eine **URL-Präfix-Property** für `https://openrootdev.github.io/harness-library/` hinzu. Das begrenzt die Property auf das Projekt. Nutzen Sie die für Ihr Konto angebotene Verifizierungsmethode; eine HTML-Verifizierungsdatei kann in `site/` abgelegt werden, sobald ihr exakter Dateiname und Inhalt vorliegen.
2. Reichen Sie `sitemap.xml` in dieser Property ein. Prüfen Sie Startseite, Einreichungsleitfaden und Harness-URLs; beantragen Sie Indexierung, wenn das Werkzeug sie anbietet. Eine Einreichung ist ein Hinweis zur Entdeckung, keine Indexierungsgarantie.
3. Fügen Sie dieselbe Website in [Bing Webmaster Tools](https://www.bing.com/webmasters/) hinzu und reichen Sie die Sitemap ein. Falls das Konto Import aus Google Search Console anbietet, kann die verifizierte Property wiederverwendet werden.
4. Sehen Sie die Indexierungsberichte nach dem Deployment erneut durch. Beheben Sie gemeldete Crawl- oder Inhaltsprobleme anhand von Belegen. Betrachten Sie weder eine `site:`-Suche noch einen Lighthouse-Wert als Beweis für Indexierungsabdeckung oder Rankings.

Die Verifizierung benötigt das Konto des Eigentümers oder dessen bereitgestelltes Verifizierungsartefakt. Veröffentlichen Sie keine geratenen Verifizierungstokens. Eine ergänzte HTML-Verifizierungsdatei muss außerhalb der Sitemap bleiben und in Builds erhalten werden.

## Benachrichtigungen über veröffentlichte Änderungen

Nach dem Deployment eines normalen Pushs benachrichtigt der Pages-Workflow [IndexNow](https://www.indexnow.org/documentation) mit den kanonischen URLs aus der erzeugten Sitemap. Tägliche Badge-Aktualisierungen überspringen diese Benachrichtigung. Diese Migration ändert alle fünf Seiten; begrenzen Sie Einreichungen bei einem größeren Verzeichnis auf geänderte Seiten. Google nutzt Search Console und normales Crawling; es erfolgt keine Einreichung bei Google über IndexNow.

Das Projekt hostet `indexnow-key.txt` und gibt dessen exakten `keyLocation` an. Damit wird die Eigentümerschaft auf `/harness-library/` begrenzt, ohne andere Projekte auf dem gemeinsamen Host einzubeziehen. Der Schlüssel muss zur Protokollverifizierung öffentlich ausgeliefert werden; er ist keine Zugangsinformation zu einem Webmaster-Konto. Login, kostenpflichtiger Dienst oder zusätzliche Abhängigkeit sind nicht erforderlich. Ein vorübergehender API-Fehler macht ein erfolgreiches Website-Deployment nicht rückgängig.

Für eine bewusste Inhaltsänderung außerhalb des Workflows führen Sie zuerst den Build aus und dann `python scripts/notify_indexnow.py --dry-run`, um die URL-Liste zu prüfen, oder `python scripts/notify_indexnow.py`, um sie einzureichen. HTTP 200 bedeutet empfangen; HTTP 202 bedeutet empfangen bei noch ausstehender Schlüsselprüfung. Keiner der beiden Status beweist Indexierung oder Rankings. Vermeiden Sie wiederholte Einreichungen bei unveränderten Inhalten.

## GitHub Pages und robots.txt

Robots-Regeln werden im **Host-Stammverzeichnis** unter `https://openrootdev.github.io/robots.txt` gelesen, nicht unter `/harness-library/robots.txt`. Eine projektlokale Datei steuert das Crawling des gemeinsamen Hosts nicht. Die Projektdatei verweist nur auf die aktuelle Sitemap. Reichen Sie die Sitemap über Webmaster-Konten ein.

Fügt der Eigentümer später ein Root-Site-Repository oder eine eigene Domain hinzu, prüfen Sie die maßgebliche Robots-Datei vor der Einführung von Einschränkungen. Ändern Sie Regeln anderer Projekte auf demselben Host niemals leichtfertig.

## Migration zur Organisation

Repository und Verzeichnis wurden am 10. Oktober 2026 zu [Kaelux Labs](https://github.com/OpenRootdev/harness-library) verschoben. GitHub leitet die alte Repository-URL um. Ein kleines [Pages-Repository des Kontos](https://github.com/Ker102/ker102.github.io) erhält die alten Verzeichnisseiten mit sofortigen Weiterleitungen und kanonischen Links und liefert bestehende Badge-Bilder weiter aus. Seine `robots.txt` an der Host-Wurzel erlaubt Crawling und verlinkt die aktuelle Sitemap.

Bestehende Badge-Rücklinks mit alter oder aktueller Verzeichnis-URL bleiben berechtigt. Eine Änderung dieser Links startet einen bestehenden 14-Tage-Boost nicht neu; die ursprünglichen Nachweisdaten bleiben maßgeblich.

## Auffindbarkeit für Agenten

Agenten können gewöhnliches HTML, den JSON-Katalog oder Markdown-Spiegel nutzen. `llms.txt` ist ein Vorschlag zur Vereinfachung, kein Google-Rankingfaktor oder Erfordernis. Google erklärt, dass seine KI-Suchfunktionen dieselben grundlegenden SEO-Praktiken wie gewöhnliche Suche nutzen. Crawlbarer Text, klare Seitenlinks, genaue Belege und nützliche Inhalte sind wichtig; keine Konfiguration garantiert Aufnahme oder Zitate.

Primärquellen: [Google JavaScript SEO](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics), [Sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap), [Robots-Spezifikation](https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec), [KI-Funktionen](https://developers.google.com/search/docs/appearance/ai-features), [llms.txt-Vorschlag](https://llmstxt.org/).
