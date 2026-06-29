# 🚀 Git & GitHub Setup Guide für Italia Money Radar

## Status
✅ Projektstruktur vorbereitet (Schritt 1.1-1.3)
✅ .gitignore erstellt
✅ README.md erstellt
⏳ Git Repository Setup erforderlich

---

## Schritt 1.4: Git Setup & GitHub (In VS Code oder Terminal)

### 1️⃣ Git installieren (falls nicht vorhanden)
Wenn Git nicht verfügbar ist: https://git-scm.com/download/win

### 2️⃣ Git konfigurieren (Terminal in VS Code)
```bash
git config --global user.name "Dein Name"
git config --global user.email "deine-email@example.com"
```

### 3️⃣ Git Repository initialisieren
```bash
cd Documents/ItalienRadar
git init
```

### 4️⃣ Erste Dateien hinzufügen
```bash
git add .
git status  # Überprüfung
```

### 5️⃣ Ersten Commit erstellen
```bash
git commit -m "Initial project foundation"
```

### 6️⃣ GitHub Repository erstellen
- Gehe auf https://github.com
- Klick auf "New" → Neues Repository
- Name: `italia-money-radar`
- Visibility: Private (wegen Impressum!)
- Nicht initialisieren (wir haben schon Dateien)

### 7️⃣ Lokales Projekt mit GitHub verbinden
```bash
git branch -M main
git remote add origin https://github.com/DEIN-NAME/italia-money-radar.git
git push -u origin main
```

### 8️⃣ Sicherheitscheck vor dem Push
- ✅ Keine Passwörter in Dateien
- ✅ Keine echten sensiblen Daten
- ✅ .gitignore ist aktiv
- ✅ README dokumentiert das Projekt

### 9️⃣ Version taggen (Optional, aber professionell)
```bash
git tag v0.1-foundation
git push origin v0.1-foundation
```

---

## ⚠️ Wichtig: Private Repository
Da die `impressum.html` echte Kontaktdaten enthält, **muss** das Repository **PRIVAT** sein!

---

## Schritt 1.4: ✅ Fertig!
Wenn alle Schritte abgeschlossen:
- [ ] Git ist installiert und konfiguriert
- [ ] `.gitignore` wurde erstellt
- [ ] `README.md` wurde erstellt
- [ ] Erster Commit wurde gemacht
- [ ] GitHub-Repository wurde erstellt
- [ ] Lokales Projekt mit GitHub verbunden
- [ ] Erstes Push war erfolgreich
- [ ] Repository ist **PRIVAT**

Danach: **Schritt 1.5** - Deployment vorbereiten
