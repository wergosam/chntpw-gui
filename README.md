# 🚀 Windows Passwort Finder – chntpw GUI

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![PyQt6](https://img.shields.io/badge/PyQt6-6.0+-green?logo=qt&logoColor=white)
![Lizenz](https://img.shields.io/badge/Lizenz-GPL--3.0-blue)
![Platform](https://img.shields.io/badge/Platform-Linux-lightgrey?logo=linux&logoColor=white)
![Version](https://img.shields.io/badge/Version-1.06-orange)

**Eine moderne grafische Benutzeroberfläche für `chntpw` – das bekannte Tool zum Zurücksetzen von Windows-Passwörtern unter Linux.**

---

# 🇩🇪 Deutsch

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

![Hauptfenster hell](/screenshots/chntpw-gui-hell.webp)

### Hauptfenster (dunkles Design)

![Hauptfenster dunkel](/screenshots/chntpw-gui-dunkel.webp)

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

Dieses Projekt ist unter der **GNU General Public License v3.0** lizenziert. Sie dürfen dieses Programm frei verwenden, verändern und weitergeben, solange abgeleitete Werke ebenfalls unter der GPL v3 veröffentlicht werden. Siehe die Datei [LICENSE](LICENSE) für den vollständigen Lizenztext oder besuchen Sie <https://www.gnu.org/licenses/gpl-3.0.html>.

---

## 👏 Danksagungen

- **chntpw-Entwickler** – für das großartige Tool `chntpw`
- **PyQt6-Entwickler** – für das GUI-Framework
- **Open-Source-Community** – für die vielen nützlichen Tools und Bibliotheken

---

## 📞 Kontakt / Support

Bei Fragen oder Problemen:

- **GitHub Issues:** <https://github.com/wergosam/chntpw-gui/issues>
- **E-Mail:** [wergosam@gmail.com](mailto:wergosam@gmail.com)

---

## 🔗 Weitere Informationen

- [chntpw auf GitHub](https://github.com/minacle/chntpw)
- [PyQt6 Dokumentation](https://doc.qt.io/qt-6/)
- [GNU GPL v3 Lizenz](https://www.gnu.org/licenses/gpl-3.0.html)
- [Linux Paketmanagement (Arch Wiki)](https://wiki.archlinux.org/title/Pacman)

---
---

# 🇬🇧 English

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features-1)
- [Requirements](#-requirements)
- [Installation](#-installation-1)
- [Screenshots](#-screenshots-1)
- [Usage](#-usage)
- [Technical Details](#-technical-details)
- [Frequently Asked Questions (FAQ)](#-frequently-asked-questions-faq)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

**Windows Password Finder** is a user-friendly GUI for the Linux tool `chntpw`. It lets you view Windows user accounts and reset or change their passwords – no command-line knowledge required.

The tool automatically detects Windows partitions, mounts them if needed, and offers a clean interface with multi-language support (German/English), a settings menu, and automatic dependency installation.

> ⚠️ **Important note:** This tool cannot display passwords – Windows passwords are hashed and cannot be decrypted. However, you can reset (clear) passwords or replace them with new ones.

---

## ✨ Features

- **Automatic partition detection** – finds all Windows partitions (NTFS/FAT)
- **Smart mounting** – mounts partitions on demand using `udisksctl`
- **Display user list** – shows all users found in the SAM file
- **Reset password** – clears the password (no password)
- **Change password** – sets a new password for a user
- **Multi-language support** – German and English (more languages on request)
- **Settings menu** – to switch language (saved in `~/.config/chntpw-gui/config.json`)
- **Menu bar** – visually matched to the layout (hover effects, consistent colors)
- **Light & dark theme** – switch between light and dark mode with a single click
- **Automatic dependency installation** – installs `chntpw`, `udisks2`, and `PyQt6` as needed (with distribution detection)
- **No root privileges required at startup** – privileges are only requested for critical actions
- **Modern, lightweight interface** – no duplicate boxes, clean structure

---

## 📦 Requirements

### System Requirements

- A Linux distribution (Arch, Debian/Ubuntu, Fedora, openSUSE, Manjaro, etc.)
- Python 3.8 or higher
- Internet connection (for automatic dependency installation)

### Required Packages

The following packages are installed automatically if needed:

| Package | Description |
|---------|-------------|
| `chntpw` | Core tool for manipulating the SAM file |
| `udisks2` | For mounting partitions (provides `udisksctl`) |
| `PyQt6` | GUI framework (installed via `pip`) |

---

## 🛠 Installation

### Method 1: Automatic Installation (Recommended)

```bash
# Download the script
wget https://raw.githubusercontent.com/wergosam/chntpw-gui/main/chntpw-gui.py

# Make it executable
chmod +x chntpw-gui.py

# Run it (dependencies are installed automatically)
./chntpw-gui.py
```

### Method 2: Manual Installation

#### 1. Install system packages

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

#### 2. Install PyQt6

```bash
pip install --user PyQt6
```

#### 3. Download the script and run it

```bash
wget https://raw.githubusercontent.com/wergosam/chntpw-gui/main/chntpw-gui.py
chmod +x chntpw-gui.py
./chntpw-gui.py
```

---

## 📸 Screenshots

### Main window (light theme)

![Main window light](/screenshots/chntpw-gui-hell.webp)

### Main window (dark theme)

![Main window dark](/screenshots/chntpw-gui-dunkel.webp)

### Menu bar & settings

*(Screenshot coming soon)*

### Change password dialog

*(Screenshot coming soon)*

### User list view

*(Screenshot coming soon)*

---

## 🖥 Usage

### Step-by-step guide

1. **Start the tool:**
   ```bash
   ./chntpw-gui.py
   ```

2. **Select the Windows partition:**
   - The tool automatically shows all detected Windows partitions.
   - Click the desired partition (usually the largest NTFS partition).

3. **Mount the partition (if not already mounted):**
   - Click **"Mount selected partition & show users"**.
   - Confirm the mount request.
   - Enter your password when prompted by `pkexec` or `sudo`.

4. **View the user list:**
   - The SAM file is read and all users are displayed.
   - A separate window shows the full list.

5. **Reset or change a password:**
   - Click **"Reset/Change password"**.
   - Enter the username (e.g. `Administrator`).
   - **Leave the password field empty** = remove the password (blank password).
   - **Enter a new password** = change the password.
   - Confirm the action.

6. **Restart:**
   - After the reset, you must reboot the system for the changes to take effect.

### Switching language

- Click **File → Settings** in the menu.
- Choose between **German** and **English**.
- The setting is saved and loaded automatically on the next start.

---

## 🔧 Technical Details

### How it works

1. **Partition detection:**
   - Uses `lsblk -J` in JSON format.
   - Filters for NTFS/FAT/exFAT partitions ≥ 10 GB.
   - Shows device name, file system, size, and mount status.

2. **Mounting with udisksctl:**
   - Uses `udisksctl mount -b /dev/sdXY`.
   - Prompts for a password graphically (via `pkexec`) or via `sudo` (terminal).
   - Determines the mount point from the output or via `lsblk`.

3. **Locating the SAM file:**
   - Searches for `Windows/System32/config/SAM` and `WINNT/System32/config/SAM`.
   - On success, the file is used for further operations.

4. **User list:**
   - Runs `chntpw -l SAM-PATH` with `pkexec` or `sudo`.
   - Displays the output in a scrollable dialog.

5. **Resetting/changing the password:**
   - Runs `chntpw -u USER -p "NEW_PASSWORD" SAM-PATH`.
   - Empty password field → `-p ""` (removes the password).
   - With a password → the password is set to the entered value.

### Dependency management

The tool checks all dependencies at startup and automatically installs any missing packages. The distribution is detected via `/etc/os-release`. Supported distributions:

- **Arch Linux** (and derivatives: Manjaro, EndeavourOS, Garuda)
- **Debian** (and derivatives: Ubuntu, Linux Mint, Pop!_OS, Neon)
- **Fedora** (and derivatives: RHEL, CentOS, Nobara)
- **openSUSE** (Leap and Tumbleweed)

### Security aspects

- **No `sudo` at startup** – the script runs with normal user privileges.
- **Critical actions** (mounting, reading the SAM file, changing passwords) are executed via `pkexec` (graphical) or `sudo` (terminal).
- **Confirmation dialogs** before every critical step.
- **Log output** shows all actions transparently.

---

## ❓ Frequently Asked Questions (FAQ)

**Can the tool display the current password?**
No. Windows passwords are stored as a hash (one-way encryption) and cannot be decrypted. The tool can only clear the password or set a new one.

**Does the tool work with BitLocker-encrypted partitions?**
No. With BitLocker encryption, the SAM file cannot be read. The partition must first be decrypted.

**Why do I need root privileges?**
Reading and modifying the SAM file requires administrator privileges, since it is a security-critical system file.

**Can I reset the password for domain users?**
No. The tool only works for local Windows users, not for Active Directory domain users.

**Which Windows versions are supported?**
Windows 7, Windows 8/8.1, Windows 10, Windows 11, as well as Windows Vista (with limitations).

**Can I use the tool on a different Linux machine?**
Yes, the tool works on all common Linux distributions as long as the dependencies (`chntpw`, `udisks2`, `PyQt6`) are installed.

**How do I change the language?**
Click **File → Settings** in the menu and select the desired language. The setting is saved permanently.

---

## 🐛 Troubleshooting

### "chntpw is not installed"

The tool installs `chntpw` automatically. If that fails, install it manually:

```bash
# Arch / Manjaro
sudo pacman -S chntpw

# Debian / Ubuntu
sudo apt install chntpw

# Fedora
sudo dnf install chntpw
```

### "udisksctl not found"

```bash
# Arch / Manjaro
sudo pacman -S udisks2

# Debian / Ubuntu
sudo apt install udisks2

# Fedora
sudo dnf install udisks2
```

### "No Windows partitions found"

1. Check whether the partition exists: `lsblk -f`
2. The partition must be formatted as NTFS or FAT32.
3. The partition must be at least 10 GB in size.

### "SAM file not found"

The partition may be:
- Not a Windows system partition (data partition only)
- BitLocker-encrypted
- A damaged Windows installation

### "pkexec not found" or no graphical password prompt

Install `polkit`:

```bash
# Arch / Manjaro
sudo pacman -S polkit

# Debian / Ubuntu
sudo apt install policykit-1

# Fedora
sudo dnf install polkit
```

Alternatively, `sudo` is used in the terminal – in that case you need to enter the password in the terminal.

### PyQt6 won't install

```bash
# Manually via pip
pip install --user PyQt6

# Or via the package manager
sudo pacman -S python-pyqt6        # Arch / Manjaro
sudo apt install python3-pyqt6     # Debian / Ubuntu
sudo dnf install python3-qt6       # Fedora
```

---

## 🤝 Contributing

Contributions are very welcome! Here's how you can help:

1. **Fork** the repository.
2. **Create** a new branch: `git checkout -b feature/new-feature`
3. **Commit** your changes: `git commit -m 'Add new feature'`
4. **Push** the branch: `git push origin feature/new-feature`
5. **Open** a Pull Request.

### Setting up a development environment

```bash
# Clone the repository
git clone https://github.com/wergosam/chntpw-gui.git
cd chntpw-gui

# Virtual environment (optional)
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install PyQt6
```

### Coding standards

- **PEP 8** – Python style guide
- **Docstrings** for all functions
- **Type hints** for better readability
- **Clear commit messages**

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0**. You are free to use, modify, and redistribute this program, as long as derivative works are also released under the GPL v3. See the [LICENSE](LICENSE) file for the full license text, or visit <https://www.gnu.org/licenses/gpl-3.0.html>.

---

## 👏 Acknowledgements

- **chntpw developers** – for the excellent `chntpw` tool
- **PyQt6 developers** – for the GUI framework
- **Open source community** – for the many useful tools and libraries

---

## 📞 Contact / Support

For questions or issues:

- **GitHub Issues:** <https://github.com/wergosam/chntpw-gui/issues>
- **E-mail:** [wergosam@gmail.com](mailto:wergosam@gmail.com)

---

## 🔗 Further Information

- [chntpw on GitHub](https://github.com/minacle/chntpw)
- [PyQt6 documentation](https://doc.qt.io/qt-6/)
- [GNU GPL v3 license](https://www.gnu.org/licenses/gpl-3.0.html)
- [Linux package management (Arch Wiki)](https://wiki.archlinux.org/title/Pacman)
