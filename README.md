# 🚀 Windows Passwort Finder – chntpw GUI



![image](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![image](https://img.shields.io/badge/PyQt6-6.0+-green?logo=qt&logoColor=white)
 
![image](https://img.shields.io/badge/License-GPL v3-blue.svg)
 

![image](https://img.shields.io/badge/Platform-Linux-lightgrey?logo=linux&logoColor=white)
![image](https://img.shields.io/badge/Version-1.06-orange)


**Eine moderne grafische Benutzeroberfläche für `chntpw` – das bekannte Tool zum
Zurücksetzen von Windows-Passwörtern unter Linux.**

- - -
## 📋 Inhaltsverzeichnis

- [Überblick](#-überblick)
- [Features](#-features)
- [Voraussetzungen](#-voraussetzungen)
- [Installation](#-installation)
- [Screenshots](#-screenshots)
- [Bedienung](#-bedienung)
- [Technische Details](#-technische-details)
- [Häufige Fragen (FAQ)](#-häufige-fragen-faq)
- [Fehlerbehebung](#-fehlerbehebung)
- [Mitwirken](#-mitwirken)
- [Lizenz](#-lizenz)

- - -
## 🎯 Überblick

**Windows Passwort Finder** ist eine benutzerfreundliche GUI für das Linux-Tool `
chntpw`. Es ermöglicht, Windows-Benutzerkonten anzuzeigen und deren Passwörter
zurückzusetzen oder zu ändern – ganz ohne Kommandozeilenkenntnisse.

Das Tool erkennt automatisch Windows-Partitionen, mountet sie bei Bedarf und
bietet eine übersichtliche Oberfläche mit Mehrsprachigkeit (Deutsch/Englisch),
einem Einstellungsmenü und automatischer Abhängigkeitsinstallation.

> ⚠️ **Wichtiger Hinweis:** Dieses Tool kann keine Passwörter anzeigen –
> Windows-Passwörter sind gehasht und können nicht entschlüsselt werden. Sie
> können jedoch Passwörter zurücksetzen (leeren) oder durch neue Passwörter
> ersetzen.

- - -
## ✨ Features

- **Automatische Partitionserkennung** – findet alle Windows-Partitionen
  (NTFS/FAT)
- **Smartes Mounten** – mountet Partitionen bei Bedarf mit `udisksctl`
- **Benutzerliste anzeigen** – zeigt alle Benutzer der SAM-Datei an
- **Passwort zurücksetzen** – setzt das Passwort auf leer (kein Passwort)
- **Passwort ändern** – legt ein neues Passwort für einen Benutzer fest
- **Mehrsprachigkeit** – Deutsch und Englisch (weitere Sprachen auf Anfrage)
- **Einstellungsmenü** – zum Umschalten der Sprache (gespeichert in `
  ~/.config/chntpw-gui/config.json`)
- **Menüleiste** – optisch an das Layout angepasst (Hover-Effekte, konsistente
  Farben)
- **Helles & dunkles Theme** – wechseln Sie mit einem Klick zwischen Hell- und
  Dunkelmodus
- **Automatische Abhängigkeitsinstallation** – installiert `chntpw`, `udisks2`
  und `PyQt6` bei Bedarf (mit Distribution-Erkennung)
- **Keine Root-Rechte beim Start** – Rechte werden erst bei kritischen Aktionen
  abgefragt
- **Moderne, schlanke Oberfläche** – keine doppelten Boxen, klare Struktur

- - -
## 📦 Voraussetzungen

### Systemanforderungen

- Linux-Distribution (Arch, Debian/Ubuntu, Fedora, openSUSE, Manjaro, etc.)
- Python 3.8 oder höher
- Internetverbindung (für automatische Installation der Abhängigkeiten)

### Benötigte Pakete

Die folgenden Pakete werden bei Bedarf automatisch installiert:


|Paket|Beschreibung|
|-|-|
|`chntpw`|Kern-Tool zum Manipulieren der SAM-Datei|
|`udisks2`|Für das Mounten von Partitionen (enthält `udisksctl`)|
|`PyQt6`|GUI-Framework (wird via `pip` installiert)|

- - -
## 🛠 Installation

### Methode 1: Automatische Installation (Empfohlen)

```bash
# Skript herunterladen
wget https://raw.githubusercontent.com/wergosam/chntpw-gui/main/chntpw-gui.py
# Ausführbar machen
chmod +x chntpw-gui.py
# Starten (Abhängigkeiten werden automatisch installiert)
./chntpw-gui.py
```
### Methode 2: Manuelle Installation

#### 1\. Systempakete installieren

**Arch Linux / Manjaro:**

```bash
sudo pacman -S chntpw udisks2
```
**Debian / Ubuntu / Linux Mint:**

```bash
sudo apt update
sudo apt install chntpw udisks2
```
**Fedora:**

```bash
sudo dnf install chntpw udisks2
```
**openSUSE:**

```bash
sudo zypper install chntpw udisks2
```
#### 2\. PyQt6 installieren

```bash
pip install --user PyQt6
```
#### 3\. Skript herunterladen und starten

```bash
wget https://raw.githubusercontent.com/wergosam/chntpw-gui/main/chntpw-gui.py
chmod +x chntpw-gui.py
./chntpw-gui.py
```
- - -
## 📸 Screenshots

### Hauptfenster (helles Design)


![image](/home/manjaro/Downloads/screenshots/chntpw-gui-hell.webp)


### Hauptfenster (dunkles Design)


![image](/home/manjaro/Downloads/screenshots/chntpw-gui-dunkel.webp)


## 🖥 Bedienung

### Schritt-für-Schritt-Anleitung

1.  **Tool starten:**

```bash
./chntpw-gui.py
```
2.  **Windows-Partition auswählen:**
  - Das Tool zeigt automatisch alle erkannten Windows-Partitionen an.
  - Klicken Sie auf die gewünschte Partition (meist die größte NTFS-Partition).

3.  **Partition mounten (falls nicht eingehängt):**
  - Klicken Sie auf **„Ausgewählte Partition mounten & Benutzer anzeigen"**.
  - Bestätigen Sie die Mount-Anfrage.
  - Geben Sie Ihr Passwort ein, wenn `pkexec` oder `sudo` danach fragt.

4.  **Benutzerliste anzeigen:**
  - Die SAM-Datei wird ausgelesen und alle Benutzer werden angezeigt.
  - Ein separates Fenster zeigt die vollständige Liste.

5.  **Passwort zurücksetzen oder ändern:**
  - Klicken Sie auf **„Passwort zurücksetzen/ändern"**.
  - Geben Sie den Benutzernamen ein (z. B. `Administrator`).
  - **Passwort-Feld leer lassen** = Passwort entfernen (leeres Passwort).
  - **Neues Passwort eingeben** = Passwort ändern.
  - Bestätigen Sie die Aktion.

6.  **Neu starten:**
  - Nach dem Reset müssen Sie das System neu starten, damit die Änderungen
    wirksam werden.

### Sprache umschalten

- Klicken Sie im Menü auf **Datei → Einstellungen**.
- Wählen Sie zwischen **Deutsch** und **Englisch**.
- Die Einstellung wird gespeichert und beim nächsten Start automatisch geladen.

- - -
## 🔧 Technische Details

### Funktionsweise

1.  **Partitionserkennung:**
  - Verwendet `lsblk -J` im JSON-Format.
  - Filtert nach NTFS/FAT/exFAT-Partitionen ≥ 10 GB.
  - Zeigt Gerätename, Dateisystem, Größe und Mount-Status an.
2.  **Mounten mit udisksctl:**
  - Verwendet `udisksctl mount -b /dev/sdXY`.
  - Fragt grafisch nach Passwort (über `pkexec`) oder über `sudo` (Terminal).
  - Ermittelt den Mount-Punkt aus der Ausgabe oder via `lsblk`.
3.  **SAM-Datei finden:**
  - Sucht nach `Windows/System32/config/SAM` und `WINNT/System32/config/SAM`.
  - Bei Erfolg wird die Datei für weitere Operationen verwendet.
4.  **Benutzerliste:**
  - Führt `chntpw -l SAM-PFAD` mit `pkexec` oder `sudo` aus.
  - Zeigt die Ausgabe in einem scrollbaren Dialog an.
5.  **Passwort zurücksetzen/ändern:**
  - Führt `chntpw -u BENUTZER -p "NEUES_PASSWORT" SAM-PFAD` aus.
  - Leeres Passwort-Feld → `\-p ""` (Passwort entfernen).
  - Mit Passwort → Passwort wird auf den eingegebenen Wert gesetzt.

### Abhängigkeitsmanagement

Das Tool prüft beim Start alle Abhängigkeiten und installiert fehlende Pakete
automatisch. Die Distribution wird über `/etc/os-release` erkannt. Unterstützt
werden:

- **Arch Linux** (und Derivate: Manjaro, EndeavourOS, Garuda)
- **Debian** (und Derivate: Ubuntu, Linux Mint, Pop\!_OS, Neon)
- **Fedora** (und Derivate: RHEL, CentOS, Nobara)
- **openSUSE** (Leap und Tumbleweed)

### Sicherheitsaspekte

- **Kein `sudo` beim Start** – das Skript läuft mit Benutzerrechten.
- **Kritische Aktionen** (Mounten, SAM auslesen, Passwort ändern) werden mit `
  pkexec` (grafisch) oder `sudo` (Terminal) ausgeführt.
- **Bestätigungsdialoge** vor jedem kritischen Schritt.
- **Log-Ausgabe** zeigt alle Aktionen transparent an.

- - -
## ❓ Häufige Fragen (FAQ)

**Kann das Tool das aktuelle Passwort anzeigen?** Nein. Windows-Passwörter sind
als Hash (Einweg-Verschlüsselung) gespeichert und können nicht entschlüsselt
werden. Das Tool kann nur das Passwort leeren oder ein neues Passwort festlegen.

**Funktioniert das Tool mit BitLocker-verschlüsselten Partitionen?** Nein. Bei
BitLocker-Verschlüsselung ist die SAM-Datei nicht lesbar. Die Partition muss
zuerst entschlüsselt werden.

**Warum brauche ich Root-Rechte?** Das Auslesen und Verändern der SAM-Datei
erfordert Administrator-Rechte, da es sich um sicherheitskritische
Systemdateien handelt.

**Kann ich das Passwort für Domänen-Benutzer zurücksetzen?** Nein. Das Tool
funktioniert nur für lokale Windows-Benutzer, nicht für
Active-Directory-Domänen-Benutzer.

**Welche Windows-Versionen werden unterstützt?** Windows 7, Windows 8/8.1,
Windows 10, Windows 11 sowie Windows Vista (mit Einschränkungen).

**Kann ich das Tool auch auf einem anderen Linux-Rechner verwenden?** Ja, das
Tool funktioniert auf allen gängigen Linux-Distributionen, solange die
Abhängigkeiten (`chntpw`, `udisks2`, `PyQt6`) installiert sind.

**Wie ändere ich die Sprache?** Klicken Sie im Menü auf **Datei → Einstellungen**
und wählen Sie die gewünschte Sprache aus. Die Einstellung bleibt dauerhaft
erhalten.

- - -
## 🐛 Fehlerbehebung

### „chntpw ist nicht installiert"

Das Tool installiert `chntpw` automatisch. Falls das nicht funktioniert, manuell
installieren:

```bash
# Arch / Manjaro
sudo pacman -S chntpw
# Debian / Ubuntu
sudo apt install chntpw
# Fedora
sudo dnf install chntpw
```
### „udisksctl nicht gefunden"

```bash
# Arch / Manjaro
sudo pacman -S udisks2
# Debian / Ubuntu
sudo apt install udisks2
# Fedora
sudo dnf install udisks2
```
### „Keine Windows-Partitionen gefunden"

1.  Prüfen Sie, ob die Partition vorhanden ist: `lsblk -f`
2.  Die Partition muss NTFS oder FAT32 formatiert sein.
3.  Die Partition muss mindestens 10 GB groß sein.

### „SAM-Datei nicht gefunden"

Die Partition ist möglicherweise:

- Keine Windows-Systempartition (nur Datenpartition)
- BitLocker-verschlüsselt
- Die Windows-Installation ist beschädigt

### „pkexec nicht gefunden" oder keine grafische Passwortabfrage

Installieren Sie `polkit`:

```bash
# Arch / Manjaro
sudo pacman -S polkit
# Debian / Ubuntu
sudo apt install policykit-1
# Fedora
sudo dnf install polkit
```
Alternativ wird `sudo` im Terminal verwendet – dann müssen Sie das Passwort im
Terminal eingeben.

### PyQt6 wird nicht installiert

```bash
# Manuell via pip
pip install --user PyQt6
# Oder über den Paketmanager
sudo pacman -S python-pyqt6        # Arch / Manjaro
sudo apt install python3-pyqt6     # Debian / Ubuntu
sudo dnf install python3-qt6       # Fedora
```
- - -
## 🤝 Mitwirken

Beiträge sind herzlich willkommen! So können Sie helfen:

1.  **Forken** Sie das Repository.
2.  **Erstellen** Sie einen neuen Branch: `git checkout -b feature/neue-funktion`
3.  **Committen** Sie Ihre Änderungen: `git commit -m 'Neue Funktion hinzugefügt'`
4.  **Pushen** Sie den Branch: `git push origin feature/neue-funktion`
5.  **Erstellen** Sie einen Pull Request.

### Entwicklungsumgebung einrichten

```bash
# Repository klonen
git clone https://github.com/wergosam/chntpw-gui.git
cd chntpw-gui
# Virtuelle Umgebung (optional)
python -m venv venv
source venv/bin/activate
# Abhängigkeiten installieren
pip install PyQt6
```
### Coding-Standards

- **PEP 8** – Style Guide für Python-Code
- **Docstrings** für alle Funktionen
- **Type Hints** für bessere Lesbarkeit
- **Klare Commit-Nachrichten**

- - -
## 📄 Lizenz

Dieses Projekt ist unter der **GNU General Public License v3.0** lizenziert. Sie
dürfen dieses Programm frei verwenden, verändern und weitergeben, solange
abgeleitete Werke ebenfalls unter der GPL v3 veröffentlicht werden. Siehe die
Datei [LICENSE](LICENSE) für den vollständigen Lizenztext oder besuchen Sie 
<https://www.gnu.org/licenses/gpl-3.0.html>.

- - -
## 👏 Danksagungen

- **chntpw-Entwickler** – für das großartige Tool `chntpw`
- **PyQt6-Entwickler** – für das GUI-Framework
- **Open-Source-Community** – für die vielen nützlichen Tools und Bibliotheken

- - -
## 📞 Kontakt / Support

Bei Fragen oder Problemen:

- **GitHub Issues:** <https://github.com/wergosam/chntpw-gui/issues>
- **E-Mail:** [wergosam@gmail.com](mailto:wergosam@gmail.com)

- - -
## 🔗 Weitere Informationen

- [chntpw auf GitHub](https://github.com/minacle/chntpw)
- [PyQt6 Dokumentation](https://doc.qt.io/qt-6/)
- [GNU GPL v3 Lizenz](https://www.gnu.org/licenses/gpl-3.0.html)
- [Linux Paketmanagement (Arch Wiki)](https://wiki.archlinux.org/title/Pacman)
# 🚀 Windows Passwort Finder – chntpw GUI

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![PyQt6](https://img.shields.io/badge/PyQt6-6.0+-green?logo=qt&logoColor=white)
![License](https://img.shields.io/badge/License-GPL%20v3-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Linux-lightgrey?logo=linux&logoColor=white)
![Version](https://img.shields.io/badge/Version-1.06-orange)

**Eine moderne grafische Benutzeroberfläche für `chntpw` – das bekannte Tool zum Zurücksetzen von Windows-Passwörtern unter Linux.**

---

## 📋 Inhaltsverzeichnis

- [Überblick](#-überblick)
- [Features](#-features)
- [Voraussetzungen](#-voraussetzungen)
- [Installation](#-installation)
- [Screenshots](#-screenshots)
- [Bedienung](#-bedienung)
- [Technische Details](#-technische-details)
- [Häufige Fragen (FAQ)](#-häufige-fragen-faq)
- [Fehlerbehebung](#-fehlerbehebung)
- [Mitwirken](#-mitwirken)
- [Lizenz](#-lizenz)

---

## 🎯 Überblick

**Windows Passwort Finder** ist eine benutzerfreundliche GUI für das Linux-Tool `chntpw`. Es ermöglicht, Windows-Benutzerkonten anzuzeigen und deren Passwörter zurückzusetzen oder zu ändern – ganz ohne Kommandozeilenkenntnisse.

Das Tool erkennt automatisch Windows-Partitionen, mountet sie bei Bedarf und bietet eine übersichtliche Oberfläche mit Mehrsprachigkeit (Deutsch/Englisch), einem Einstellungsmenü und automatischer Abhängigkeitsinstallation.

> ⚠️ **Wichtiger Hinweis:** Dieses Tool kann keine Passwörter anzeigen – Windows-Passwörter sind gehasht und können nicht entschlüsselt werden. Sie können jedoch Passwörter zurücksetzen (leeren) oder durch neue Passwörter ersetzen.

---

## ✨ Features

- **Automatische Partitionserkennung** – findet alle Windows-Partitionen (NTFS/FAT)
- **Smartes Mounten** – mountet Partitionen bei Bedarf mit `udisksctl`
- **Benutzerliste anzeigen** – zeigt alle Benutzer der SAM-Datei an
- **Passwort zurücksetzen** – setzt das Passwort auf leer (kein Passwort)
- **Passwort ändern** – legt ein neues Passwort für einen Benutzer fest
- **Mehrsprachigkeit** – Deutsch und Englisch (weitere Sprachen auf Anfrage)
- **Einstellungsmenü** – zum Umschalten der Sprache (gespeichert in `~/.config/chntpw-gui/config.json`)
- **Menüleiste** – optisch an das Layout angepasst (Hover-Effekte, konsistente Farben)
- **Helles & dunkles Theme** – wechseln Sie mit einem Klick zwischen Hell- und Dunkelmodus
- **Automatische Abhängigkeitsinstallation** – installiert `chntpw`, `udisks2` und `PyQt6` bei Bedarf (mit Distribution-Erkennung)
- **Keine Root-Rechte beim Start** – Rechte werden erst bei kritischen Aktionen abgefragt
- **Moderne, schlanke Oberfläche** – keine doppelten Boxen, klare Struktur

---

## 📦 Voraussetzungen

### Systemanforderungen

- Linux-Distribution (Arch, Debian/Ubuntu, Fedora, openSUSE, Manjaro, etc.)
- Python 3.8 oder höher
- Internetverbindung (für automatische Installation der Abhängigkeiten)

### Benötigte Pakete

Die folgenden Pakete werden bei Bedarf automatisch installiert:

| Paket | Beschreibung |
|-------|-------------|
| `chntpw` | Kern-Tool zum Manipulieren der SAM-Datei |
| `udisks2` | Für das Mounten von Partitionen (enthält `udisksctl`) |
| `PyQt6` | GUI-Framework (wird via `pip` installiert) |

---

## 🛠 Installation

### Methode 1: Automatische Installation (Empfohlen)

```bash
# Skript herunterladen
wget https://raw.githubusercontent.com/wergosam/chntpw-gui/main/chntpw-gui.py

# Ausführbar machen
chmod +x chntpw-gui.py

# Starten (Abhängigkeiten werden automatisch installiert)
./chntpw-gui.py
```

### Methode 2: Manuelle Installation

#### 1. Systempakete installieren

**Arch Linux / Manjaro:**
```bash
sudo pacman -S chntpw udisks2
```

**Debian / Ubuntu / Linux Mint:**
```bash
sudo apt update
sudo apt install chntpw udisks2
```

**Fedora:**
```bash
sudo dnf install chntpw udisks2
```

**openSUSE:**
```bash
sudo zypper install chntpw udisks2
```

#### 2. PyQt6 installieren

```bash
pip install --user PyQt6
```

#### 3. Skript herunterladen und starten

```bash
wget https://raw.githubusercontent.com/wergosam/chntpw-gui/main/chntpw-gui.py
chmod +x chntpw-gui.py
./chntpw-gui.py
```

---

## 📸 Screenshots

### Hauptfenster (helles Design)

![Hauptfenster hell](data:image/webp;base64,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XmekXkerY3DJErjDEqtGlHVdfdZZWtfP8F/94modd2aUzcmG5lWX8BkQ/6nPTKlcW8GF+XDc6qx45kUh68UbYPQN2fY1FsMrT0dNGhpK/Bf6zm7MURJoOay2aSE/AqG0/0OzCJ/o/Az4hdxQjjEGoiOvSzGT1Ss7NmfnxGrGxY5qyxcQAW3elUQBqxyEauLTct4Gvl84qNdm+X4/dVMBzs1doc3fB0CQT29bUonhZNy6G3VuSbykigoAAOZW+kqgAAABLxkosczAAAAJyOykqgAAAACyiBOAAABEN8aUQJwAAAAKKIE4AAAEQbASVQAAAAUxRY5mAAAAbauELBQAAAAIDHMwAAADbsNgRA2iwOYiEE+so61AZSFxbke+jYjRY6Q6sMdIdWGOkOrDHSHVhjpDqwx0h1YY6Q6sMdIdWGOj0E6y3J4qS0zG71MfReA30lUAAAAAABsh5ELC+cIZ0ehyA+kFRV9tm16fudDDwh2ckj0RNeN0rT///////////////////////////////////////////////////////////////////////jZ8bs0KRyn9iZjH/6d6yybuj9X/o0/mxCdgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA)

### Hauptfenster (dunkles Design)

![Hauptfenster dunkel](data:image/webp;base64,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)

### Menüleiste & Einstellungen

*(Screenshot folgt)*

### Dialog zum Ändern des Passworts

*(Screenshot folgt)*

### Benutzerliste anzeigen

*(Screenshot folgt)*

---

## 🖥 Bedienung

### Schritt-für-Schritt-Anleitung

1. **Tool starten:**
   ```bash
   ./chntpw-gui.py
   ```

2. **Windows-Partition auswählen:**
   - Das Tool zeigt automatisch alle erkannten Windows-Partitionen an.
   - Klicken Sie auf die gewünschte Partition (meist die größte NTFS-Partition).

3. **Partition mounten (falls nicht eingehängt):**
   - Klicken Sie auf **„Ausgewählte Partition mounten & Benutzer anzeigen"**.
   - Bestätigen Sie die Mount-Anfrage.
   - Geben Sie Ihr Passwort ein, wenn `pkexec` oder `sudo` danach fragt.

4. **Benutzerliste anzeigen:**
   - Die SAM-Datei wird ausgelesen und alle Benutzer werden angezeigt.
   - Ein separates Fenster zeigt die vollständige Liste.

5. **Passwort zurücksetzen oder ändern:**
   - Klicken Sie auf **„Passwort zurücksetzen/ändern"**.
   - Geben Sie den Benutzernamen ein (z. B. `Administrator`).
   - **Passwort-Feld leer lassen** = Passwort entfernen (leeres Passwort).
   - **Neues Passwort eingeben** = Passwort ändern.
   - Bestätigen Sie die Aktion.

6. **Neu starten:**
   - Nach dem Reset müssen Sie das System neu starten, damit die Änderungen wirksam werden.

### Sprache umschalten

- Klicken Sie im Menü auf **Datei → Einstellungen**.
- Wählen Sie zwischen **Deutsch** und **Englisch**.
- Die Einstellung wird gespeichert und beim nächsten Start automatisch geladen.

---

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
   - Führt `chntpw -u BENUTZER -p "NEUES_PASSWORT" SAM-PFAD` aus.
   - Leeres Passwort-Feld → `-p ""` (Passwort entfernen).
   - Mit Passwort → Passwort wird auf den eingegebenen Wert gesetzt.

### Abhängigkeitsmanagement

Das Tool prüft beim Start alle Abhängigkeiten und installiert fehlende Pakete automatisch. Die Distribution wird über `/etc/os-release` erkannt. Unterstützt werden:

- **Arch Linux** (und Derivate: Manjaro, EndeavourOS, Garuda)
- **Debian** (und Derivate: Ubuntu, Linux Mint, Pop!_OS, Neon)
- **Fedora** (und Derivate: RHEL, CentOS, Nobara)
- **openSUSE** (Leap und Tumbleweed)

### Sicherheitsaspekte

- **Kein `sudo` beim Start** – das Skript läuft mit Benutzerrechten.
- **Kritische Aktionen** (Mounten, SAM auslesen, Passwort ändern) werden mit `pkexec` (grafisch) oder `sudo` (Terminal) ausgeführt.
- **Bestätigungsdialoge** vor jedem kritischen Schritt.
- **Log-Ausgabe** zeigt alle Aktionen transparent an.

---

## ❓ Häufige Fragen (FAQ)

**Kann das Tool das aktuelle Passwort anzeigen?**
Nein. Windows-Passwörter sind als Hash (Einweg-Verschlüsselung) gespeichert und können nicht entschlüsselt werden. Das Tool kann nur das Passwort leeren oder ein neues Passwort festlegen.

**Funktioniert das Tool mit BitLocker-verschlüsselten Partitionen?**
Nein. Bei BitLocker-Verschlüsselung ist die SAM-Datei nicht lesbar. Die Partition muss zuerst entschlüsselt werden.

**Warum brauche ich Root-Rechte?**
Das Auslesen und Verändern der SAM-Datei erfordert Administrator-Rechte, da es sich um sicherheitskritische Systemdateien handelt.

**Kann ich das Passwort für Domänen-Benutzer zurücksetzen?**
Nein. Das Tool funktioniert nur für lokale Windows-Benutzer, nicht für Active-Directory-Domänen-Benutzer.

**Welche Windows-Versionen werden unterstützt?**
Windows 7, Windows 8/8.1, Windows 10, Windows 11 sowie Windows Vista (mit Einschränkungen).

**Kann ich das Tool auch auf einem anderen Linux-Rechner verwenden?**
Ja, das Tool funktioniert auf allen gängigen Linux-Distributionen, solange die Abhängigkeiten (`chntpw`, `udisks2`, `PyQt6`) installiert sind.

**Wie ändere ich die Sprache?**
Klicken Sie im Menü auf **Datei → Einstellungen** und wählen Sie die gewünschte Sprache aus. Die Einstellung bleibt dauerhaft erhalten.

---

## 🐛 Fehlerbehebung

### „chntpw ist nicht installiert"

Das Tool installiert `chntpw` automatisch. Falls das nicht funktioniert, manuell installieren:

```bash
# Arch / Manjaro
sudo pacman -S chntpw

# Debian / Ubuntu
sudo apt install chntpw

# Fedora
sudo dnf install chntpw
```

### „udisksctl nicht gefunden"

```bash
# Arch / Manjaro
sudo pacman -S udisks2

# Debian / Ubuntu
sudo apt install udisks2

# Fedora
sudo dnf install udisks2
```

### „Keine Windows-Partitionen gefunden"

1. Prüfen Sie, ob die Partition vorhanden ist: `lsblk -f`
2. Die Partition muss NTFS oder FAT32 formatiert sein.
3. Die Partition muss mindestens 10 GB groß sein.

### „SAM-Datei nicht gefunden"

Die Partition ist möglicherweise:
- Keine Windows-Systempartition (nur Datenpartition)
- BitLocker-verschlüsselt
- Die Windows-Installation ist beschädigt

### „pkexec nicht gefunden" oder keine grafische Passwortabfrage

Installieren Sie `polkit`:

```bash
# Arch / Manjaro
sudo pacman -S polkit

# Debian / Ubuntu
sudo apt install policykit-1

# Fedora
sudo dnf install polkit
```

Alternativ wird `sudo` im Terminal verwendet – dann müssen Sie das Passwort im Terminal eingeben.

### PyQt6 wird nicht installiert

```bash
# Manuell via pip
pip install --user PyQt6

# Oder über den Paketmanager
sudo pacman -S python-pyqt6        # Arch / Manjaro
sudo apt install python3-pyqt6     # Debian / Ubuntu
sudo dnf install python3-qt6       # Fedora
```

---

## 🤝 Mitwirken

Beiträge sind herzlich willkommen! So können Sie helfen:

1. **Forken** Sie das Repository.
2. **Erstellen** Sie einen neuen Branch: `git checkout -b feature/neue-funktion`
3. **Committen** Sie Ihre Änderungen: `git commit -m 'Neue Funktion hinzugefügt'`
4. **Pushen** Sie den Branch: `git push origin feature/neue-funktion`
5. **Erstellen** Sie einen Pull Request.

### Entwicklungsumgebung einrichten

```bash
# Repository klonen
git clone https://github.com/wergosam/chntpw-gui.git
cd chntpw-gui

# Virtuelle Umgebung (optional)
python -m venv venv
source venv/bin/activate

# Abhängigkeiten installieren
pip install PyQt6
```

### Coding-Standards

- **PEP 8** – Style Guide für Python-Code
- **Docstrings** für alle Funktionen
- **Type Hints** für bessere Lesbarkeit
- **Klare Commit-Nachrichten**

---

## 📄 Lizenz

Dieses Projekt ist unter der **GNU General Public License v3.0** lizenziert.
Sie dürfen dieses Programm frei verwenden, verändern und weitergeben, solange abgeleitete Werke ebenfalls unter der GPL v3 veröffentlicht werden.
Siehe die Datei [LICENSE](LICENSE) für den vollständigen Lizenztext oder besuchen Sie [https://www.gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/gpl-3.0.html).

---

## 👏 Danksagungen

- **chntpw-Entwickler** – für das großartige Tool `chntpw`
- **PyQt6-Entwickler** – für das GUI-Framework
- **Open-Source-Community** – für die vielen nützlichen Tools und Bibliotheken

---

## 📞 Kontakt / Support

Bei Fragen oder Problemen:

- **GitHub Issues:** [https://github.com/wergosam/chntpw-gui/issues](https://github.com/wergosam/chntpw-gui/issues)
- **E-Mail:** wergosam@gmail.com

---

## 🔗 Weitere Informationen

- [chntpw auf GitHub](https://github.com/minacle/chntpw)
- [PyQt6 Dokumentation](https://doc.qt.io/qt-6/)
- [GNU GPL v3 Lizenz](https://www.gnu.org/licenses/gpl-3.0.html)
- [Linux Paketmanagement (Arch Wiki)](https://wiki.archlinux.org/title/Pacman)
