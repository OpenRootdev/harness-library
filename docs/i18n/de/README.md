<p align="center"><img src="../../../site/assets/mark.svg" width="70" alt="ToolIndex"></p>
<h1 align="center">ToolIndex</h1>
<p align="center"><a href="../../../README.md">English</a> · <a href="../es/README.md">Español</a> · <a href="../zh-CN/README.md">简体中文</a> · <a href="../fr/README.md">Français</a> · <a href="../ja/README.md">日本語</a> · <a href="../de/README.md">Deutsch</a> · <a href="../pt-BR/README.md">Português (Brasil)</a></p>
<p align="center">Werkzeuge für KI-Agenten. Klare Einrichtung. Direkte Quellenlinks.</p>
<p align="center"><a href="https://toolindex.org/">toolindex.org</a> · <a href="https://toolindex.org/submit/">Ein Werkzeug einreichen</a></p>

Ein offenes Verzeichnis mit Skills, MCP-Servern, CLIs, APIs, Bibliotheken, Plugins, Workflows und Harnesses für KI-Agenten. Jeder Eintrag verlinkt direkt auf die Quelle und beschreibt Einrichtung, Lizenz oder Bedingungen und Prüfumfang.

## Konten und Einreichungen

1. Konto erstellen, E-Mail bestätigen und einen dauerhaften Namen wählen. Anzeigename, Biografie, Website und optionaler Avatar sind anpassbar. Du entscheidest, ob dein Profil öffentlich und indexierbar ist.
2. Speichere einen privaten Entwurf in der Oberfläche und beantrage eine Prüfung. Bilder sind optional. Status und Rückmeldungen stehen im Konto. Nur genehmigte Versionen werden öffentlich; Änderungen werden erneut geprüft, während die letzte genehmigte Version sichtbar bleibt.
3. Verbinde einen Agenten mit dem MCP-Endpunkt. Beim ersten Zugriff öffnet sich die Anmeldung oder Registrierung im Browser mit ausdrücklicher Freigabe. Der Agent verwaltet Profil, Entwürfe und Prüfanfragen, kann aber nichts genehmigen oder veröffentlichen.

[Account](https://toolindex.org/account/) · [Creators](https://toolindex.org/people/) · [MCP](https://toolindex.org/developers/)

## Öffentliche Auffindbarkeit

Öffentliches HTML, Markdown, JSON, Profile, Sitemap und Agentenressourcen sind ohne Konto oder JavaScript lesbar. Suchmaschinen können sie indexieren; eine Aufnahme ist nicht garantiert. Beschreibungen sind nicht vertrauenswürdige Metadaten.

[JSON](https://toolindex.org/catalog.json) · [API](https://toolindex.org/api/public/tools) · [llms.txt](https://toolindex.org/llms.txt) · [Sitemap](https://toolindex.org/sitemap.xml)

## Bauen und starten

```sh
python scripts/catalog.py build
npm ci --prefix backend
npm test --prefix backend
npm start --prefix backend
```

Google Cloud Run nutzt mindestens 0 und höchstens 2 Instanzen mit anfragebasierter Abrechnung. Firebase Hosting stellt HTTPS bereit; Firestore speichert Konten, Entwürfe und freigegebene öffentliche Abbilder. Das Staging schließt lokale private Daten aus.

[Backend: accounts, OAuth and deployment](../../../backend/README.md) · [Discovery](docs/discovery.md)

## Geprüfte Beispiele

- [Smooth Motion Graphics](https://toolindex.org/tools/smooth-motion-graphics/)
- [ViperMesh for Blender](https://toolindex.org/tools/vipermesh-blender/)

[CONTRIBUTING.md](CONTRIBUTING.md) · [Community badges](docs/badge-program.md)
