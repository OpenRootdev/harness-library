# Auffindbarkeit und Bereitstellung

Öffentliches HTML, Markdown, JSON, Profile, Sitemap und Agentenressourcen sind ohne Konto oder JavaScript lesbar. Suchmaschinen können sie indexieren; eine Aufnahme ist nicht garantiert. Beschreibungen sind nicht vertrauenswürdige Metadaten.

## Öffentliche Ressourcen

- [ToolIndex](https://toolindex.org/)
- [Submit](https://toolindex.org/submit/)
- [Creators](https://toolindex.org/people/)
- [API and MCP](https://toolindex.org/developers/)
- [sitemap.xml](https://toolindex.org/sitemap.xml)
- [llms.txt](https://toolindex.org/llms.txt)
- [llms-full.txt](https://toolindex.org/llms-full.txt)
- [catalog.json](https://toolindex.org/catalog.json)
- [Public API](https://toolindex.org/api/public/tools)

## Hosting und Zugriff

Google Cloud Run nutzt mindestens 0 und höchstens 2 Instanzen mit anfragebasierter Abrechnung. Firebase Hosting stellt HTTPS bereit; Firestore speichert Konten, Entwürfe und freigegebene öffentliche Abbilder. Das Staging schließt lokale private Daten aus.

Node liefert vollständige öffentliche Seiten und API-Daten. Browsersitzungen nutzen sichere HttpOnly-Cookies; MCP nutzt OAuth mit PKCE. Öffentliche Daten sind von privaten Konten, Revisionen, ausstehenden Einreichungen und Token-Hashes getrennt. Firestore verweigert direkten Clientzugriff.

```sh
python scripts/stage_cloudrun.py
```

[Backend: configuration and deployment](../../../../backend/README.md) · [Google Cloud](https://toolindex-org.web.app/) · [Firebase Hosting + Cloud Run](https://firebase.google.com/docs/hosting/cloud-run)

## Suchmaschinen

Die Sitemap enthält öffentliche Tools und sichtbare Profile. Private Kontoseiten, ausstehende Tools und Zugangsdaten fehlen darin. Eigentümer können sie bei Suchmaschinen einreichen; Indexierung oder erfundene Eigentumsnachweise werden nicht versprochen.

[Search Console](https://search.google.com/search-console) · [Bing Webmaster Tools](https://www.bing.com/webmasters/)

## Kompatibilität

Alte Eintragsrouten und Badge-Erkennung bleiben erhalten. Neue Einreichungen nutzen ToolIndex-Konten oder MCP und werden vor Veröffentlichung von Menschen geprüft. Konfiguration und Bereitstellung stehen im Backend-Leitfaden.
