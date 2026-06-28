#!/usr/bin/env python3
# chntpw-gui-autoinstall.py – Windows Passwort Finder mit automatischer Abhängigkeitsinstallation

import os
import sys
import shutil
import subprocess
import importlib
import importlib.util
from pathlib import Path

# ─── Distribution erkennen ──────────────────────────────────────────────
def detect_distro():
    info = {}
    for path in ("/etc/os-release", "/usr/lib/os-release"):
        p = Path(path)
        if p.exists():
            for line in p.read_text(encoding="utf-8").splitlines():
                if "=" in line:
                    k, _, v = line.partition("=")
                    info[k.strip()] = v.strip().strip('"')
            break
    return info

def get_distro_family(info):
    ids = set()
    for key in ("ID", "ID_LIKE"):
        ids.update(info.get(key, "").lower().split())
    if ids & {"arch", "manjaro", "endeavouros", "garuda", "cachyos"}:
        return "arch"
    if ids & {"fedora", "rhel", "centos", "nobara"}:
        return "fedora"
    if ids & {"opensuse", "suse", "opensuse-leap", "opensuse-tumbleweed"}:
        return "suse"
    if ids & {"debian", "ubuntu", "linuxmint", "pop", "neon", "zorin", "elementary"}:
        return "debian"
    return "unknown"

DISTRO_INFO   = detect_distro()
DISTRO_FAMILY = get_distro_family(DISTRO_INFO)
DISTRO_NAME   = DISTRO_INFO.get("PRETTY_NAME") or DISTRO_INFO.get("NAME") or "Unbekannte Distribution"

# ─── Systempaket-Installationsbefehle ──────────────────────────────────
def get_system_install_commands():
    distro = DISTRO_INFO.get("ID", "unknown")
    cmds = {
        "arch":      "sudo pacman -S --needed chntpw udisks2",
        "manjaro":   "sudo pacman -S --needed chntpw udisks2",
        "debian":    "sudo apt update && sudo apt install -y chntpw udisks2",
        "ubuntu":    "sudo apt update && sudo apt install -y chntpw udisks2",
        "fedora":    "sudo dnf install -y chntpw udisks2",
        "opensuse":  "sudo zypper install -y chntpw udisks2",
        "opensuse-leap": "sudo zypper install -y chntpw udisks2",
        "opensuse-tumbleweed": "sudo zypper install -y chntpw udisks2",
    }
    return cmds.get(distro, None)

# ─── Hilfsfunktionen für Installation ──────────────────────────────────
def run_command(cmd, description="Befehl", check=True):
    print(f"▶ {description} …")
    try:
        if isinstance(cmd, str):
            cmd = cmd.split()
        proc = subprocess.run(cmd, check=check, capture_output=True, text=True)
        if proc.stdout:
            print(proc.stdout)
        if proc.stderr:
            print(proc.stderr, file=sys.stderr)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Fehler bei {description}:", e.stderr or e.stdout or e)
        return False

def install_pyqt6():
    pip_cmd = shutil.which("pip") or shutil.which("pip3")
    if not pip_cmd:
        print("⚠ pip nicht gefunden. Versuche python3 -m pip …")
        pip_cmd = "python3 -m pip"
    else:
        pip_cmd = f"{pip_cmd}"
    cmd = [pip_cmd, "install", "--user", "PyQt6"]
    print(f"📦 Installiere PyQt6 via {pip_cmd} …")
    return run_command(cmd, "PyQt6 Installation")

def install_system_packages():
    cmd = get_system_install_commands()
    if not cmd:
        print(f"❌ Kein Installationsbefehl für {DISTRO_NAME} bekannt.")
        print("   Bitte installieren Sie manuell: chntpw und udisks2")
        return False
    print(f"📦 Installiere Systempakete für {DISTRO_NAME} …")
    print(f"   Befehl: {cmd}")
    return run_command(cmd, "Systempaket-Installation")

# ─── Hauptprüfung ──────────────────────────────────────────────────────
def ensure_dependencies():
    missing = []
    try:
        import PyQt6
    except ImportError:
        missing.append("PyQt6")

    if not shutil.which("chntpw"):
        missing.append("chntpw")
    if not shutil.which("udisksctl"):
        missing.append("udisksctl (aus Paket udisks2)")

    if not missing:
        print("✅ Alle Abhängigkeiten sind vorhanden.")
        return True

    print("⚠ Folgende Abhängigkeiten fehlen:")
    for pkg in missing:
        print(f"   - {pkg}")
    print()

    answer = input("Möchten Sie die fehlenden Pakete installieren? (j/n): ").strip().lower()
    if answer not in ("j", "ja", "y", "yes"):
        print("❌ Installation abgelehnt. Das Programm wird beendet.")
        return False

    success = True
    if "PyQt6" in missing:
        print("\n🔧 Installiere PyQt6 …")
        success &= install_pyqt6()
        if not success:
            print("⚠ PyQt6 konnte nicht installiert werden. Bitte installieren Sie es manuell:")
            print("   pip install --user PyQt6")
            return False

    system_missing = [p for p in missing if p in ("chntpw", "udisksctl") or p.startswith("udisksctl")]
    if system_missing:
        print("\n🔧 Installiere Systempakete …")
        success &= install_system_packages()
        if not success:
            print("❌ Systempakete konnten nicht installiert werden.")
            return False

    # Nachinstallation prüfen
    if not shutil.which("chntpw") or not shutil.which("udisksctl"):
        print("⚠ Nach der Installation immer noch nicht gefunden. Bitte manuell nachhelfen.")
        return False

    try:
        import PyQt6
    except ImportError:
        print("⚠ PyQt6 immer noch nicht importierbar. Bitte manuell installieren.")
        return False

    print("\n✅ Alle Abhängigkeiten erfolgreich installiert.")
    return True

# ─── GUI-Code (wie zuvor, aber jetzt innerhalb von main) ──────────────
def main():
    if not ensure_dependencies():
        sys.exit(1)

    # Jetzt PyQt6 importieren
    from PyQt6.QtWidgets import (
        QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
        QListWidget, QListWidgetItem, QPushButton, QLabel, QTextEdit,
        QFrame, QMessageBox, QDialog, QDialogButtonBox, QLineEdit, QFormLayout,
        QProgressBar
    )
    from PyQt6.QtCore import Qt, QThread, pyqtSignal

    # ─── Hilfsfunktionen für Windows-Erkennung ──────────────────────
    import json

    def get_windows_partitions():
        try:
            output = subprocess.check_output(
                ["lsblk", "-J", "-o", "NAME,TYPE,FSTYPE,LABEL,MOUNTPOINT,SIZE"],
                text=True
            )
            data = json.loads(output)
        except Exception:
            return []

        partitions = []
        def walk(dev):
            if dev.get("type") == "part":
                fstype = dev.get("fstype") or ""
                label = dev.get("label") or ""
                mountpoint = dev.get("mountpoint")
                size = dev.get("size", "0")
                try:
                    if size.endswith("G"):
                        size_gb = float(size[:-1])
                    elif size.endswith("M"):
                        size_gb = float(size[:-1]) / 1024
                    elif size.endswith("T"):
                        size_gb = float(size[:-1]) * 1024
                    else:
                        size_gb = 0
                except:
                    size_gb = 0
                if fstype.lower() in ["ntfs", "fat", "vfat", "exfat"] and size_gb >= 10:
                    partitions.append({
                        "device": f"/dev/{dev['name']}",
                        "label": label,
                        "fstype": fstype,
                        "mountpoint": mountpoint,
                        "size_gb": round(size_gb, 1)
                    })
            for child in dev.get("children", []):
                walk(child)
        for block in data.get("blockdevices", []):
            walk(block)
        return partitions

    def mount_partition(device):
        try:
            proc = subprocess.run(
                ["udisksctl", "mount", "-b", device],
                capture_output=True,
                text=True,
                check=False
            )
            if proc.returncode != 0:
                error = proc.stderr.strip() or proc.stdout.strip()
                return None, f"udisksctl mount fehlgeschlagen:\n{error}"
            output = proc.stdout.strip()
            if " at " in output:
                mount_path = output.split(" at ")[-1].strip()
                if mount_path and Path(mount_path).is_dir():
                    return mount_path, None
            result = subprocess.check_output(
                ["lsblk", "-o", "MOUNTPOINT", device],
                text=True
            )
            lines = result.strip().splitlines()
            if len(lines) > 1:
                mp = lines[1].strip()
                if mp:
                    return mp, None
            return None, "Mountpunkt konnte nicht ermittelt werden."
        except Exception as e:
            return None, str(e)

    def find_sam_file_on_mount(mount_path):
        base = Path(mount_path)
        for win_dir in ["Windows", "WINNT"]:
            sam = base / win_dir / "System32" / "config" / "SAM"
            if sam.is_file():
                return str(sam)
        return None

    def run_chntpw_command(cmd_args):
        if not shutil.which("chntpw"):
            return None, "chntpw ist nicht installiert."
        try:
            if shutil.which("pkexec"):
                output = subprocess.check_output(
                    ["pkexec", "chntpw"] + cmd_args,
                    stderr=subprocess.STDOUT,
                    text=True
                )
            else:
                output = subprocess.check_output(
                    ["sudo", "chntpw"] + cmd_args,
                    stderr=subprocess.STDOUT,
                    text=True
                )
            return output, None
        except subprocess.CalledProcessError as e:
            return None, f"Fehler (Code {e.returncode}):\n{e.output}"
        except Exception as e:
            return None, str(e)

    # ─── Worker-Thread ──────────────────────────────────────────────
    class WorkerThread(QThread):
        finished = pyqtSignal(object)
        error = pyqtSignal(str)
        def __init__(self, func, *args, **kwargs):
            super().__init__()
            self.func = func
            self.args = args
            self.kwargs = kwargs
        def run(self):
            try:
                result = self.func(*self.args, **self.kwargs)
                self.finished.emit(result)
            except Exception as e:
                self.error.emit(str(e))

    # ─── Theme-Definitionen ──────────────────────────────────────────
    THEMES = {
        "light": {
            "bg_page": "#f5f4ef", "bg_card": "#ffffff", "bg_header": "#ffffff",
            "bg_distro": "#fef3c7", "bg_log": "#fafaf8", "border_card": "#e5e4de",
            "border_distro": "#fde68a", "border_strong": "#d1d0ca", "divider": "#f0efe9",
            "text_primary": "#1a1a1a", "text_secondary": "#6b7280", "text_hint": "#9ca3af",
            "text_distro": "#92400e", "accent": "#d97706", "accent_hover": "#b45309",
            "accent_press": "#92400e", "accent_light": "#fef3c7", "accent_border": "#fde68a",
            "danger_fg": "#dc2626", "btn_run_fg": "#ffffff", "btn_run_dis_bg": "#e5e4de",
            "btn_run_dis_fg": "#9ca3af", "btn_small_fg": "#6b7280", "btn_session_bg": "#ffffff",
            "btn_logout_fg": "#374151", "btn_reboot_fg": "#d97706", "btn_reboot_hbg": "#fef3c7",
            "btn_reboot_hbd": "#fde68a", "btn_shut_fg": "#dc2626", "btn_shut_hbg": "#fef2f2",
            "btn_shut_hbd": "#fecaca", "log_fg": "#374151", "scroll_bg": "#f5f4ef",
            "scroll_handle": "#d1d0ca", "scroll_hover": "#9ca3af", "cb_border": "#d1d0ca",
            "cb_bg": "#ffffff", "toggle_icon": "🌙", "toggle_tip": "Dunkles Design aktivieren",
        },
        "dark": {
            "bg_page": "#1e1e2e", "bg_card": "#24273a", "bg_header": "#1e1e2e",
            "bg_distro": "#2a2040", "bg_log": "#181825", "border_card": "#363a4f",
            "border_distro": "#494d64", "border_strong": "#494d64", "divider": "#2d3047",
            "text_primary": "#cdd6f4", "text_secondary": "#6e738d", "text_hint": "#494d64",
            "text_distro": "#b8b4e8", "accent": "#8aadf4", "accent_hover": "#a5c0f5",
            "accent_press": "#c6d4f8", "accent_light": "#2a3a5a", "accent_border": "#4a6a9a",
            "danger_fg": "#f38ba8", "btn_run_fg": "#1e1e2e", "btn_run_dis_bg": "#363a4f",
            "btn_run_dis_fg": "#494d64", "btn_small_fg": "#8aadf4", "btn_session_bg": "#313244",
            "btn_logout_fg": "#cdd6f4", "btn_reboot_fg": "#fab387", "btn_reboot_hbg": "#3a2a1a",
            "btn_reboot_hbd": "#6a4a2a", "btn_shut_fg": "#f38ba8", "btn_shut_hbg": "#3a1a1a",
            "btn_shut_hbd": "#6a2a2a", "log_fg": "#a6adc8", "scroll_bg": "#1e1e2e",
            "scroll_handle": "#494d64", "scroll_hover": "#6e738d", "cb_border": "#494d64",
            "cb_bg": "#1e1e2e", "toggle_icon": "☀️", "toggle_tip": "Helles Design aktivieren",
        }
    }

    QSS_TEMPLATE = """
* {{
    font-family: 'Inter', 'Noto Sans', 'Cantarell', 'Segoe UI', sans-serif;
    font-size: 15px;
    color: {text_primary};
}}
QWidget {{ background-color: {bg_page}; }}
QFrame#distroBar {{
    background-color: {bg_distro};
    border: 1px solid {border_distro};
    border-radius: 8px;
}}
QListWidget {{
    background-color: {bg_card};
    border: 1px solid {border_card};
    border-radius: 8px;
    padding: 4px;
    color: {text_primary};
}}
QListWidget::item {{ padding: 6px 8px; }}
QListWidget::item:selected {{
    background-color: {accent_light};
    border: 1px solid {accent_border};
}}
QLabel {{ background: transparent; color: {text_primary}; }}
QLabel#title {{ font-size: 22px; font-weight: 700; color: {text_primary}; }}
QLabel#subtitle {{ font-size: 13px; color: {text_secondary}; }}
QLabel#sectionLabel {{ font-size: 11px; font-weight: 700; color: {text_hint}; letter-spacing: 1px; }}
QLabel#hint {{
    font-size: 14px;
    color: {text_distro};
    background-color: {accent_light};
    border: 1px solid {accent_border};
    border-radius: 6px;
    padding: 10px 14px;
}}
QLabel#distroInfo {{ font-size: 12px; color: {text_distro}; background: transparent; padding: 2px 0; }}
QPushButton#btnSmall {{
    background: transparent;
    color: {btn_small_fg};
    border: 1px solid {border_strong};
    border-radius: 6px;
    padding: 6px 14px;
    font-size: 13px;
}}
QPushButton#btnSmall:hover {{ border-color: {accent}; color: {accent}; }}
QPushButton#btnMount {{
    background: transparent;
    color: {text_distro};
    border: 1px solid {border_card};
    border-radius: 8px;
    padding: 10px 20px;
    font-size: 15px;
}}
QPushButton#btnMount:hover {{ background-color: {accent_light}; border-color: {accent_border}; }}
QPushButton#btnReset {{
    background: transparent;
    color: {danger_fg};
    border: 1px solid {border_card};
    border-radius: 8px;
    padding: 10px 20px;
    font-size: 15px;
}}
QPushButton#btnReset:hover {{ background-color: {accent_light}; border-color: {danger_fg}; }}
QPushButton#btnTheme {{
    background: transparent;
    border: 1px solid {border_strong};
    border-radius: 6px;
    padding: 4px 10px;
    font-size: 17px;
    color: {text_primary};
    min-width: 32px;
}}
QPushButton#btnTheme:hover {{ border-color: {accent}; background-color: {accent_light}; }}
QTextEdit {{
    background-color: {bg_log};
    border: 1px solid {border_card};
    border-radius: 8px;
    padding: 8px;
    color: {log_fg};
    font-family: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
    font-size: 13px;
}}
QScrollBar:vertical {{ background: {scroll_bg}; width: 10px; border-radius: 5px; }}
QScrollBar::handle:vertical {{ background: {scroll_handle}; border-radius: 5px; min-height: 20px; }}
QScrollBar::handle:vertical:hover {{ background: {scroll_hover}; }}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{ height: 0; }}
QProgressBar {{ background-color: {bg_card}; border: 1px solid {border_card}; border-radius: 6px; height: 20px; }}
QProgressBar::chunk {{ background-color: {accent}; border-radius: 6px; }}
"""

    def build_stylesheet(theme_name):
        return QSS_TEMPLATE.format(**THEMES[theme_name])

    def make_divider(theme_name="light"):
        color = THEMES[theme_name]["divider"]
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setStyleSheet(f"background: {color}; max-height: 1px; border: none;")
        return line

    def make_section_label(text):
        lbl = QLabel(text.upper())
        lbl.setObjectName("sectionLabel")
        return lbl

    def confirm(parent, title, text):
        dlg = QMessageBox(parent)
        dlg.setWindowTitle(title)
        dlg.setIcon(QMessageBox.Icon.Warning)
        dlg.setText(text)
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        dlg.button(QMessageBox.StandardButton.Yes).setText("Ja, jetzt")
        dlg.button(QMessageBox.StandardButton.Cancel).setText("Abbrechen")
        return dlg.exec() == QMessageBox.StandardButton.Yes

    class PasswordDialog(QDialog):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setWindowTitle("Passwort zurücksetzen / ändern")
            self.setMinimumWidth(400)
            layout = QVBoxLayout(self)
            form = QFormLayout()
            self.username_edit = QLineEdit()
            self.password_edit = QLineEdit()
            self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
            form.addRow("Benutzername:", self.username_edit)
            form.addRow("Neues Passwort (leer = Passwort löschen):", self.password_edit)
            layout.addLayout(form)
            hint = QLabel("Hinweis: Wenn Sie das Passwort-Feld leer lassen, wird das Passwort entfernt (leeres Passwort).")
            hint.setWordWrap(True)
            hint.setStyleSheet("color: #6b7280; font-size: 12px;")
            layout.addWidget(hint)
            buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
            buttons.accepted.connect(self.accept)
            buttons.rejected.connect(self.reject)
            layout.addWidget(buttons)

        def get_data(self):
            return self.username_edit.text().strip(), self.password_edit.text()

    # ─── Hauptfenster ──────────────────────────────────────────────────
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle(f"Windows Passwort Finder – {DISTRO_NAME}")
            self.setMinimumSize(900, 700)
            self.current_sam_path = None
            self.partitions = []
            self._theme_name = "light"
            self._setup_ui()
            self._apply_theme()
            self.refresh_partitions()

        def _setup_ui(self):
            central = QWidget()
            self.setCentralWidget(central)
            root = QVBoxLayout(central)
            root.setContentsMargins(24, 20, 24, 20)
            root.setSpacing(16)

            # Header
            hdr = QHBoxLayout()
            title = QLabel("🔐  Windows Passwort Finder")
            title.setObjectName("title")
            sub = QLabel(f"Benutzer anzeigen · Passwort zurücksetzen/ändern  ·  {DISTRO_NAME}")
            sub.setObjectName("subtitle")
            sub.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            self.btn_theme = QPushButton("🌙")
            self.btn_theme.setObjectName("btnTheme")
            self.btn_theme.setFixedSize(40, 36)
            self.btn_theme.setToolTip("Dunkles Design aktivieren")
            self.btn_theme.clicked.connect(self._toggle_theme)
            hdr.addWidget(title)
            hdr.addStretch()
            hdr.addWidget(sub)
            hdr.addWidget(self.btn_theme)
            root.addLayout(hdr)

            # Distro-Bar
            distro_bar = QFrame()
            distro_bar.setObjectName("distroBar")
            db_layout = QHBoxLayout(distro_bar)
            db_layout.setContentsMargins(12, 8, 12, 8)
            info_text = f"🐧  {DISTRO_NAME}  ·  chntpw: {'✔' if shutil.which('chntpw') else '✗'}  ·  udisksctl: {'✔' if shutil.which('udisksctl') else '✗'}"
            distro_lbl = QLabel(info_text)
            distro_lbl.setObjectName("distroInfo")
            db_layout.addWidget(distro_lbl)
            root.addWidget(distro_bar)
            root.addWidget(make_divider(self._theme_name))

            # Hinweis (ohne Karte)
            hint_text = QLabel(
                "• Dieses Tool zeigt die Benutzernamen der Windows‑SAM‑Datei an.\n"
                "• Das aktuelle Passwort kann nicht angezeigt werden (es ist gehasht).\n"
                "• Mit 'Passwort zurücksetzen/ändern' können Sie ein neues Passwort setzen.\n"
                "• Lassen Sie das Passwort-Feld leer, wird das Passwort entfernt (leer).\n"
                "• Für alle Aktionen werden Administrator‑Rechte benötigt (pkexec/sudo)."
            )
            hint_text.setObjectName("hint")
            hint_text.setWordWrap(True)
            root.addWidget(hint_text)
            root.addWidget(make_divider(self._theme_name))

            # Partitionenliste (ohne Karte)
            root.addWidget(make_section_label("Windows‑Partitionen"))
            self.list_widget = QListWidget()
            self.list_widget.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
            root.addWidget(self.list_widget)
            self.progress = QProgressBar()
            self.progress.setVisible(False)
            root.addWidget(self.progress)

            # Buttons
            btn_row = QHBoxLayout()
            self.refresh_btn = QPushButton("Partitionen neu scannen")
            self.refresh_btn.setObjectName("btnSmall")
            self.refresh_btn.clicked.connect(self.refresh_partitions)
            self.mount_btn = QPushButton("Ausgewählte Partition mounten & Benutzer anzeigen")
            self.mount_btn.setObjectName("btnMount")
            self.mount_btn.setEnabled(False)
            self.mount_btn.clicked.connect(self.on_mount_clicked)
            self.reset_btn = QPushButton("Passwort zurücksetzen/ändern")
            self.reset_btn.setObjectName("btnReset")
            self.reset_btn.setEnabled(False)
            self.reset_btn.clicked.connect(self.on_reset_clicked)
            btn_row.addWidget(self.refresh_btn)
            btn_row.addWidget(self.mount_btn)
            btn_row.addWidget(self.reset_btn)
            root.addLayout(btn_row)
            root.addWidget(make_divider(self._theme_name))

            # Log
            root.addWidget(make_section_label("Ausgabe"))
            self.log = QTextEdit()
            self.log.setReadOnly(True)
            self.log.setMinimumHeight(150)
            self.log.setPlaceholderText("Hier erscheint die Ausgabe der Aktionen …")
            root.addWidget(self.log)

        def _apply_theme(self):
            t = self._theme_name
            self.setStyleSheet(build_stylesheet(t))
            self.btn_theme.setText(THEMES[t]["toggle_icon"])
            self.btn_theme.setToolTip(THEMES[t]["toggle_tip"])

        def _toggle_theme(self):
            self._theme_name = "dark" if self._theme_name == "light" else "light"
            self._apply_theme()

        def refresh_partitions(self):
            self.progress.setVisible(True)
            self.progress.setRange(0, 0)
            self.refresh_btn.setEnabled(False)
            self.mount_btn.setEnabled(False)
            self.reset_btn.setEnabled(False)
            self.log.clear()
            self.worker = WorkerThread(get_windows_partitions)
            self.worker.finished.connect(self.on_partitions_loaded)
            self.worker.error.connect(self.on_worker_error)
            self.worker.start()

        def on_partitions_loaded(self, partitions):
            self.progress.setVisible(False)
            self.refresh_btn.setEnabled(True)
            self.partitions = partitions
            self.list_widget.clear()
            if not partitions:
                self.list_widget.addItem("Keine Windows‑Partitionen gefunden.")
                self.mount_btn.setEnabled(False)
                self.reset_btn.setEnabled(False)
                return
            for p in partitions:
                status = f"{p['device']}  ({p['fstype']})  {p['size_gb']} GB"
                if p['label']:
                    status += f"  [{p['label']}]"
                if p['mountpoint']:
                    status += f"  eingehängt unter {p['mountpoint']}"
                else:
                    status += "  nicht eingehängt"
                item = QListWidgetItem(status)
                item.setData(Qt.ItemDataRole.UserRole, p)
                self.list_widget.addItem(item)
            self.mount_btn.setEnabled(True)
            self.current_sam_path = None
            self.reset_btn.setEnabled(False)

        def on_worker_error(self, error_msg):
            self.progress.setVisible(False)
            self.refresh_btn.setEnabled(True)
            QMessageBox.critical(self, "Fehler", f"Fehler beim Scannen:\n{error_msg}")

        def on_mount_clicked(self):
            selected = self.list_widget.currentItem()
            if not selected:
                QMessageBox.information(self, "Hinweis", "Bitte wählen Sie eine Partition aus.")
                return
            part = selected.data(Qt.ItemDataRole.UserRole)
            if not part:
                return
            device = part["device"]
            mountpoint = part["mountpoint"]
            if mountpoint and Path(mountpoint).is_dir():
                sam_path = find_sam_file_on_mount(mountpoint)
                if sam_path:
                    self.show_user_list(sam_path)
                    return
                else:
                    QMessageBox.critical(self, "Fehler",
                                         f"In {mountpoint} wurde keine SAM‑Datei gefunden.\n"
                                         "Möglicherweise ist es keine Windows‑Systempartition.")
                    return
            reply = QMessageBox.question(self, "Mounten",
                                         f"Soll die Partition {device} gemountet werden?\n"
                                         "Dazu werden Administrator‑Rechte benötigt.",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reply != QMessageBox.StandardButton.Yes:
                return
            self.progress.setVisible(True)
            self.progress.setRange(0, 0)
            self.mount_btn.setEnabled(False)
            self.refresh_btn.setEnabled(False)
            self.worker = WorkerThread(mount_partition, device)
            self.worker.finished.connect(lambda res: self.on_mount_finished(res, device))
            self.worker.error.connect(self.on_worker_error)
            self.worker.start()

        def on_mount_finished(self, result, device):
            self.progress.setVisible(False)
            self.mount_btn.setEnabled(True)
            self.refresh_btn.setEnabled(True)
            if result is None:
                return
            mount_path, error = result
            if error:
                QMessageBox.critical(self, "Mountfehler", f"Fehler beim Mounten von {device}:\n{error}")
                return
            if not mount_path:
                QMessageBox.critical(self, "Mountfehler", "Mountpunkt konnte nicht ermittelt werden.")
                return
            sam_path = find_sam_file_on_mount(mount_path)
            if sam_path:
                self.show_user_list(sam_path)
                self.refresh_partitions()
            else:
                QMessageBox.critical(self, "Fehler",
                                     f"In {mount_path} wurde keine SAM‑Datei gefunden.\n"
                                     "Bitte prüfen Sie, ob die Partition wirklich Windows enthält.")

        def show_user_list(self, sam_path):
            self.current_sam_path = sam_path
            self.reset_btn.setEnabled(True)
            self.log.append(f"📂  SAM‑Datei: {sam_path}")
            output, error = run_chntpw_command(["-l", sam_path])
            if error:
                QMessageBox.critical(self, "Fehler beim Auslesen", error)
                return
            self.log.append("📋  Benutzerliste:\n" + output)
            dialog = QMessageBox(self)
            dialog.setWindowTitle("Benutzerliste")
            dialog.setText(f"SAM-Datei: {sam_path}")
            text_edit = QTextEdit()
            text_edit.setPlainText(output)
            text_edit.setReadOnly(True)
            dialog.layout().addWidget(text_edit, 0, 0, 1, dialog.layout().columnCount())
            dialog.exec()

        def on_reset_clicked(self):
            if not self.current_sam_path:
                QMessageBox.critical(self, "Fehler", "Keine SAM‑Datei gefunden. Bitte zuerst eine Partition auswählen.")
                return
            dialog = PasswordDialog(self)
            if dialog.exec() != QDialog.DialogCode.Accepted:
                return
            username, new_password = dialog.get_data()
            if not username:
                QMessageBox.warning(self, "Fehler", "Der Benutzername darf nicht leer sein.")
                return
            if new_password:
                msg = f"Das Passwort für Benutzer '{username}' wird auf '{new_password}' gesetzt."
            else:
                msg = f"Das Passwort für Benutzer '{username}' wird entfernt (leeres Passwort)."
            reply = QMessageBox.question(self, "Bestätigung",
                                         msg + "\n\nFortfahren?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reply != QMessageBox.StandardButton.Yes:
                return
            self.log.append(f"🔄  Setze Passwort für '{username}' …")
            cmd_args = ["-u", username, "-p", new_password, self.current_sam_path]
            output, error = run_chntpw_command(cmd_args)
            if error:
                QMessageBox.critical(self, "Fehler beim Zurücksetzen", error)
                self.log.append("❌  Fehler: " + error)
            else:
                if new_password:
                    self.log.append(f"✅  Passwort für '{username}' erfolgreich geändert.")
                else:
                    self.log.append(f"✅  Passwort für '{username}' erfolgreich geleert.")
                QMessageBox.information(self, "Erfolg", f"Passwort für Benutzer '{username}' wurde erfolgreich gesetzt.\n\n{output}")

    # ─── App starten ──────────────────────────────────────────────────
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()