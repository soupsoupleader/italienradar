# ⚡ Quick Deployment Checklist - Italia Money Radar

## 🎯 Sofort-Aktionen (5-10 Minuten)

### 1. Cloudflare Deployment prüfen
```
✅ Gehe zu: https://dash.cloudflare.com/
✅ Workers & Pages → italienradar
✅ Prüfe: Letztes Deployment erfolgreich?
✅ Teste: https://italienradar.soupsoupleader.workers.dev/
```

### 2. Google Search Console - Sitemap einreichen
```
✅ Gehe zu: https://search.google.com/search-console
✅ Property auswählen/hinzufügen
✅ Sitemaps → Neue Sitemap hinzufügen
✅ URL: https://italienradar.soupsoupleader.workers.dev/sitemap.xml
✅ "Senden" klicken
```

### 3. Indexierung beantragen (für schnellere Sichtbarkeit)
```
✅ Google Search Console → URL-Prüfung
✅ Artikel 1: /was-kostet-ein-neustart-in-italien.html
✅ Artikel 2: /mit-1000-euro-in-italien-leben.html
✅ Artikel 3: /leben-in-neapel-kosten.html
✅ Ratgeber: /ratgeber.html
✅ Jeweils "Indexierung beantragen" klicken
```

---

## 🔍 Schnell-Tests (2 Minuten)

### Website-Funktionalität:
- [ ] Startseite lädt: https://italienradar.soupsoupleader.workers.dev/
- [ ] Artikel 1 lädt: /was-kostet-ein-neustart-in-italien.html
- [ ] Artikel 2 lädt: /mit-1000-euro-in-italien-leben.html
- [ ] Artikel 3 lädt: /leben-in-neapel-kosten.html
- [ ] Ratgeber lädt: /ratgeber.html
- [ ] Kostenrechner funktioniert: /italien-kostenrechner.html

### Interne Links:
- [ ] Startseite → Artikel-Links funktionieren
- [ ] Artikel → Related Links funktionieren
- [ ] Footer → Ratgeber-Link funktioniert
- [ ] Ratgeber → Artikel-Links funktionieren

---

## 📊 Performance-Check (optional, 3 Minuten)

```
✅ PageSpeed Insights: https://pagespeed.web.dev/
✅ URL eingeben: https://italienradar.soupsoupleader.workers.dev/
✅ Ziel: Score > 90
```

---

## ✅ Fertig-Status

Wenn alle Punkte oben erledigt sind:
- ✅ Website ist live
- ✅ Google kennt die Sitemap
- ✅ Indexierung läuft
- ✅ Traffic kann kommen

**Nächster Check:** In 3-7 Tagen Google Search Console prüfen → "Leistung" → Erste Impressionen?

---

## 🚨 Falls Probleme auftreten

### Website lädt nicht:
1. Cloudflare Dashboard → Deployment-Status prüfen
2. GitHub Repository → Letzter Commit erfolgreich?
3. Wrangler neu deployen (falls Node.js installiert): `wrangler deploy`

### Google Search Console Fehler:
1. Sitemap-URL korrekt? (mit .xml am Ende)
2. robots.txt erlaubt Crawling? (ja, bereits konfiguriert)
3. Warte 24-48h, Google braucht Zeit

### Artikel nicht indexiert:
1. Geduld: Google braucht 1-2 Wochen
2. Indexierung manuell beantragen (siehe oben)
3. Interne Links prüfen (Artikel müssen von Startseite erreichbar sein)

---

## 📞 Support-Ressourcen

- **Cloudflare Docs:** https://developers.cloudflare.com/workers/
- **Google Search Console Hilfe:** https://support.google.com/webmasters/
- **Schema.org Validator:** https://validator.schema.org/

---

**Viel Erfolg! 🚀**
