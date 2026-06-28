# 🚀 Windows Passwort Finder – chntpw-gui

[https://img.shields.io/badge/Python-3.8+-blue.svg](https://img.shields.io/badge/Python-3.8+-blue.svg)  
[https://img.shields.io/badge/PyQt6-6.0+-green.svg](https://img.shields.io/badge/PyQt6-6.0+-green.svg)  
[https://img.shields.io/badge/License-MIT-yellow.svg](https://img.shields.io/badge/License-MIT-yellow.svg)  
[https://img.shields.io/badge/Platform-Linux-lightgrey.svg](https://img.shields.io/badge/Platform-Linux-lightgrey.svg)

Eine moderne grafische Benutzeroberfläche für **chntpw** – das bekannte Tool zum Zurücksetzen von Windows-Passwörtern unter Linux.

## 📋 Inhaltsverzeichnis

- Überblick

- Features

- Voraussetzungen

- Installation

- Screenshots

- Bedienung

- Technische Details

- Häufige Fragen (FAQ)

- Fehlerbehebung

- Mitwirken

- Lizenz

## 🎯 Überblick

**Windows Passwort Finder** ist eine benutzerfreundliche GUI für das Linux-Tool `chntpw`. Es ermöglicht Ihnen, Windows-Benutzerkonten anzuzeigen und deren Passwörter zurückzusetzen oder zu ändern – ganz ohne Kommandozeilenkenntnisse.

Das Tool erkennt automatisch Windows-Partitionen, mountet sie bei Bedarf und bietet eine übersichtliche Oberfläche für alle wichtigen Funktionen.

⚠️ **Wichtiger Hinweis:** Dieses Tool kann **keine Passwörter anzeigen** – Windows-Passwörter sind gehasht und können nicht entschlüsselt werden. Sie können jedoch Passwörter **zurücksetzen (leeren)** oder **durch neue Passwörter ersetzen**.

## ✨ Features

- **Automatische Partitionserkennung** – findet alle Windows-Partitionen (NTFS/FAT)

- **Smartes Mounten** – mountet Partitionen bei Bedarf mit `udisksctl`

- **Benutzerliste anzeigen** – zeigt alle Benutzer der SAM-Datei an

- **Passwort zurücksetzen** – setzt das Passwort auf **leer** (kein Passwort)

- **Passwort ändern** – legt ein **neues Passwort** für einen Benutzer fest

- **Distribution-Erkennung** – passt sich an Arch, Debian/Ubuntu, Fedora, openSUSE an

- **Automatische Abhängigkeitsinstallation** – installiert `chntpw`, `udisks2` und `PyQt6` bei Bedarf

- **Helles & dunkles Theme** – wechseln Sie mit einem Klick zwischen Hell- und Dunkelmodus

- **Mehrsprachige Oberfläche** – Deutsch (weitere Sprachen auf Anfrage)

- **Keine Root-Rechte beim Start** – Rechte werden erst bei kritischen Aktionen abgefragt

## 📦 Voraussetzungen

### Systemanforderungen

- **Linux-Distribution** (Arch, Debian/Ubuntu, Fedora, openSUSE, Manjaro, etc.)

- **Python 3.8 oder höher**

- **Internetverbindung** (für automatische Installation der Abhängigkeiten)

### Benötigte Pakete (werden bei Bedarf automatisch installiert)

- **`chntpw`** – das Kern-Tool zum Manipulieren der SAM-Datei

- **`udisks2`** – für das Mounten von Partitionen (enthält `udisksctl`)

- **`PyQt6`** – das GUI-Framework (wird via `pip` installiert)

## 🛠 Installation

### Methode 1: Automatische Installation (Empfohlen)

1. **Skript herunterladen:**

bash

```
wget https://raw.githubusercontent.com/yourusername/windows-passwort-finder/main/chntpw-gui.py
```

2. **Ausführbar machen:**

bash

```
chmod +x chntpw-gui.py
```

3. **Starten:**

bash

```
./chntpw-gui.py
```

Das Skript prüft beim ersten Start alle Abhängigkeiten und installiert sie bei Bedarf mit Ihrer Zustimmung.

### Methode 2: Manuelle Installation

#### 1. Systempakete installieren

**Arch Linux / Manjaro:**

bash

```
sudo pacman -S chntpw udisks2
```

**Debian / Ubuntu / Linux Mint:**

bash

```
sudo apt update

sudo apt install chntpw udisks2
```

**Fedora:**

bash

```
sudo dnf install chntpw udisks2
```

**openSUSE:**

bash

```
sudo zypper install chntpw udisks2
```

#### 2. PyQt6 installieren

bash

```
pip install --user PyQt6
```

#### 3. Skript herunterladen

bash

```
wget https://raw.githubusercontent.com/yourusername/windows-passwort-finder/main/chntpw-gui.py
```

## 📸 Screenshots

### Hauptfenster (helles Design)

[https://screenshots/main\_light.png](https://screenshots/main_light.png)

### Hauptfenster (dunkles Design)

[https://screenshots/main\_dark.png](https://screenshots/main_dark.png)

### Dialog zum Ändern des Passworts

[https://screenshots/password\_dialog.png](https://screenshots/password_dialog.png)

### Benutzerliste anzeigen

[https://screenshots/user\_list.png](https://screenshots/user_list.png)

## 🖥 Bedienung

### Schritt-für-Schritt-Anleitung

1. **Tool starten:**

bash

```
./chntpw-gui.py
```

2. **Windows-Partition auswählen:**

   - Das Tool zeigt automatisch alle erkannten Windows-Partitionen an.

   - Klicken Sie auf die gewünschte Partition (meist die größte NTFS-Partition).

3. **Partition mounten (falls nicht eingehängt):**

   - Klicken Sie auf **"Ausgewählte Partition mounten & Benutzer anzeigen"**.

   - Bestätigen Sie die Mount-Anfrage.

   - Geben Sie Ihr Passwort ein, wenn `pkexec` oder `sudo` danach fragt.

4. **Benutzerliste anzeigen:**

   - Die SAM-Datei wird ausgelesen und alle Benutzer werden angezeigt.

   - Ein separates Fenster zeigt die vollständige Liste.

5. **Passwort zurücksetzen oder ändern:**

   - Klicken Sie auf **"Passwort zurücksetzen/ändern"**.

   - Geben Sie den Benutzernamen ein (z. B. `Administrator`).

   - **Passwort-Feld leer lassen** = Passwort entfernen (leeres Passwort).

   - **Neues Passwort eingeben** = Passwort ändern.

   - Bestätigen Sie die Aktion.

6. **Abmelden oder Neustart:**

   - Nach dem Reset müssen Sie sich abmelden oder das System neu starten, damit die Änderungen wirksam werden.

## 🔧 Technische Details

### Funktionsweise

1. **Partitionserkennung:**

   - Verwendet `lsblk -J` im JSON-Format.

   - Filtert nach NTFS/FAT/exFAT-Partitionen ≥ 10 GB.

   - Zeigt Gerätename, Dateisystem, Größe und Mount-Status an.

2. **Mounten mit udisksctl:**

   - Verwendet `udisksctl mount -b /dev/sdXY`.

   - Fragt grafisch nach Passwort (über `pkexec`) oder über `sudo` (Terminal).

   - Ermittelt den Mount-Punkt aus der Ausgabe oder via `lsblk`.

3. **SAM-Datei finden:**

   - Sucht nach `Windows/System32/config/SAM` und `WINNT/System32/config/SAM`.

   - Bei Erfolg wird die Datei für weitere Operationen verwendet.

4. **Benutzerliste:**

   - Führt `chntpw -l SAM-PFAD` mit `pkexec` oder `sudo` aus.

   - Zeigt die Ausgabe in einem scrollbaren Dialog an.

5. **Passwort zurücksetzen/ändern:**

   - Führt `chntpw -u BENUTZER -p "NEUES\_PASSWORT" SAM-PFAD` aus.

   - Leeres Passwort-Feld → `-p ""` (Passwort entfernen).

   - Mit Passwort → Passwort wird auf den eingegebenen Wert gesetzt.

### Abhängigkeitsmanagement

Das Tool prüft beim Start:

- **PyQt6** – wird mit `pip install --user PyQt6` installiert.

- **chntpw** – wird über den Paketmanager der Distribution installiert.

- **udisksctl** – wird über den Paketmanager der Distribution installiert.

Die Distribution wird über `/etc/os-release` erkannt. Unterstützt werden:

- Arch Linux (und Derivate: Manjaro, EndeavourOS, Garuda)

- Debian (und Derivate: Ubuntu, Linux Mint, Pop!\_OS, Neon)

- Fedora (und Derivate: RHEL, CentOS, Nobara)

- openSUSE (Leap und Tumbleweed)

### Sicherheitsaspekte

- **Kein `sudo` beim Start** – das Skript läuft mit Benutzerrechten.

- **Kritische Aktionen** (Mounten, SAM auslesen, Passwort ändern) werden mit `pkexec` (grafisch) oder `sudo` (Terminal) ausgeführt.

- **Bestätigungsdialoge** vor jedem kritischen Schritt.

- **Log-Ausgabe** zeigt alle Aktionen transparent an.

## ❓ Häufige Fragen (FAQ)

### Kann das Tool das aktuelle Passwort anzeigen?

**Nein.** Windows-Passwörter sind als **Hash** (Einweg-Verschlüsselung) gespeichert und können nicht entschlüsselt werden. Das Tool kann nur:

- Das Passwort **leeren** (auf leer setzen)

- Ein **neues Passwort** festlegen

### Funktioniert das Tool mit BitLocker-verschlüsselten Partitionen?

**Nein.** Bei BitLocker-Verschlüsselung ist die SAM-Datei nicht lesbar. Sie müssen die Partition zuerst entschlüsseln.

### Warum brauche ich Root-Rechte?

Das Auslesen und Verändern der SAM-Datei erfordert Administrator-Rechte, da es sich um sicherheitskritische Systemdateien handelt.

### Kann ich das Passwort für Domänen-Benutzer zurücksetzen?

**Nein.** Das Tool funktioniert nur für **lokale Windows-Benutzer**, nicht für Active-Directory-Domänen-Benutzer.

### Welche Windows-Versionen werden unterstützt?

- Windows 10

- Windows 11

- Windows 8/8.1

- Windows 7

- Windows Vista (mit Einschränkungen)

### Kann ich das Tool auch auf einem anderen Linux-Rechner verwenden?

Ja, das Tool funktioniert auf **allen gängigen Linux-Distributionen**, solange die Abhängigkeiten (`chntpw`, `udisks2`, `PyQt6`) installiert sind.

## 🐛 Fehlerbehebung

### Problem: "chntpw ist nicht installiert"

**Lösung:** Das Tool installiert `chntpw` automatisch bei fehlender Installation. Falls das nicht funktioniert, installieren Sie es manuell:

bash

```
\# Arch

sudo pacman -S chntpw

\# Debian/Ubuntu

sudo apt install chntpw

\# Fedora

sudo dnf install chntpw
```

### Problem: "udisksctl nicht gefunden"

**Lösung:** Installieren Sie `udisks2`:

bash

```
\# Arch

sudo pacman -S udisks2

\# Debian/Ubuntu

sudo apt install udisks2

\# Fedora

sudo dnf install udisks2
```

### Problem: "Keine Windows-Partitionen gefunden"

**Lösung:**

1. Prüfen Sie, ob die Partition überhaupt vorhanden ist: `lsblk -f`

2. Die Partition muss NTFS oder FAT32 formatiert sein.

3. Die Partition muss mindestens 10 GB groß sein.

### Problem: "SAM-Datei nicht gefunden"

**Lösung:** Die Partition ist möglicherweise:

- Keine Windows-Systempartition (nur Datenpartition)

- BitLocker-verschlüsselt

- Die Windows-Installation ist beschädigt

### Problem: "pkexec nicht gefunden" oder keine grafische Passwortabfrage

**Lösung:** Installieren Sie `policykit-1`:

bash

```
\# Arch

sudo pacman -S polkit

\# Debian/Ubuntu

sudo apt install policykit-1

\# Fedora

sudo dnf install polkit
```

Alternativ wird `sudo` im Terminal verwendet – dann müssen Sie das Passwort im Terminal eingeben.

### Problem: PyQt6 wird nicht installiert

**Lösung:** Manuelle Installation:

bash

```
pip install --user PyQt6
```

Oder über den Paketmanager:

bash

```
\# Arch

sudo pacman -S python-pyqt6

\# Debian/Ubuntu

sudo apt install python3-pyqt6

\# Fedora

sudo dnf install python3-qt6
```

## 🤝 Mitwirken

Wir freuen uns über Beiträge! So können Sie helfen:

1. **Forken** Sie das Repository.

2. **Erstellen** Sie einen neuen Branch (`git checkout -b feature/neue-funktion`).

3. **Committen** Sie Ihre Änderungen (`git commit -m 'Neue Funktion hinzugefügt'`).

4. **Pushen** Sie den Branch (`git push origin feature/neue-funktion`).

5. **Erstellen** Sie einen Pull Request.

### Entwicklungsumgebung einrichten

bash

```
\# Repository klonen

git clone https://github.com/yourusername/windows-passwort-finder.git

cd windows-passwort-finder


\# Virtuelle Umgebung (optional)

python -m venv venv

source venv/bin/activate


\# Abhängigkeiten installieren

pip install PyQt6
```

### Coding-Standards

- **PEP 8** – Style Guide für Python-Code.

- **Docstrings** für alle Funktionen.

- **Type Hints** für bessere Lesbarkeit.

- **Klare Commit-Nachrichten**.

## 📄 Lizenz

Dieses Projekt ist unter der **MIT-Lizenz** lizenziert – siehe die Datei [LICENSE](https://LICENSE/) für Details.

## 👏 Danksagungen

- **chntpw-Entwickler** – für das großartige Tool `chntpw`

- **PyQt6-Entwickler** – für das GUI-Framework

- **Open-Source-Community** – für die vielen nützlichen Tools und Bibliotheken

## 📞 Kontakt / Support

Bei Fragen oder Problemen:

- **GitHub Issues** – [https://github.com/yourusername/windows-passwort-finder/issues](https://github.com/yourusername/windows-passwort-finder/issues)

- **E-Mail** – your.email@example.com

## 🔗 Weitere Informationen

- [chntpw auf GitHub](https://github.com/minacle/chntpw)

- [PyQt6 Dokumentation](https://doc.qt.io/qt-6/)

- [Linux Paketmanagement](https://wiki.archlinux.org/title/Pacman)

