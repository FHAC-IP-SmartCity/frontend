## 1. Projektübersicht
**Projektname**: Smart City

**Beschreibung**:  
Dieses Projekt ist ein Smart City System, das Daten von verschiedenen Sensoren (z. B. Temperatur, Gas und Parken) sammelt und in Echtzeit mit Grafana visualisiert. Das System verwendet PostgreSQL für die Datenspeicherung und Grafana für die Datenvisualisierung.
---
## 2. Funktionen
- Echtzeit-Datenerfassung und -visualisierung.
- Vorgefertigte Dashboards zur Überwachung von Sensordaten.
- Sicher gespeicherte Daten in einer PostgreSQL-Datenbank.
- Einfach erweiterbare Architektur für das Hinzufügen neuer Sensoren oder Dashboards.
---
## 3. Systemarchitektur
Ein Überblick über das System:
- **Datenbank**: PostgreSQL zur Datenspeicherung.
- **Visualisierungstool**: Grafana für Echtzeit-Dashboards.
- **Datenbereitstellung**: Automatisiert mit Docker und Bereitstellungsdateien.
- **Web Server**: Der Flask-Webserver dient als Zwischenschritt für den Empfang der Daten vom Mikrocontroller.
- **Proto.exe**: ist ein APP, der dazu dient, die Sensor Daten von Mikrocontroller an unserem Server schicken
---
## 4. Voraussetzungen
- **Software**:
  - Docker und Docker Compose müssen installiert sein. Docker (Desktop) für eine vereinfachte Handhabung der verschiedenen       Services.
  - GitHub Desktop kann die Handhabung erleichtern.
- **Kenntnisse**:
  - Grundkenntnisse über Docker und Grafana.
---
## 5. Installation und Einrichtung
### Schritt-für-Schritt-Anleitung:
1. **Repository klonen**:
   - Verwenden Sie Git:
     ```bash
     git clone <https://github.com/FHAC-IP-SmartCity/frontend.git>
     cd <repository-folder>
     ```
   - Oder klonen Sie es einfach mit GitHub Desktop (https://github.com/FHAC-IP-SmartCity/frontend.git)
2. **Dienste mit Docker Compose starten**:
   - Öffnen Sie die Eingabeaufforderung und navigieren Sie zum `Frontend`-Ordner:
     ```bash
     cd /path/to/Frontend
     docker-compose up --build
     ```
3. **Grafana im Browser öffnen**:
   - Adresse: [http://localhost:3000]
   - Anmeldedaten:
     - **Benutzername**: `admin`
     - **Passwort**: `admin` (oder ein von Ihnen festgelegtes Passwort).
4. **Dashboard importieren**:
   - Das Dashboard befindet sich in der Datei `frontend/prov/dashboards/Stadt_Dashboard.json`.
   - Öffnen Sie Grafana, klicken Sie auf **Dashboards**, und wählen Sie **Dashboard importieren**.
5. **Datenbankverbindung einrichten**:
   - Die Verbindung zur Datenbank wird automatisch definiert, benötigt jedoch ein Passwort.
   - Gehen Sie in Grafana zu **Datenquellen** (die Standard-Datenquelle ist voreingestellt).
   - Geben Sie das Passwort `kunde` ein.
   - Drücken Sie **Speichern und testen**. Der erste Versuch gibt möglicherweise einen Fehler aus – drücken Sie erneut, und es sollte funktionieren.
---
## 6. Verwendung
### Sensor-Daten empfangen
Mit der **Proto-App** können die Sensordaten vom Mikrocontroller empfangen und an den Server gesendet werden. Folgen Sie diesen Schritten:
1. **USB anschließen**:
   - Verbinden Sie den Mikrocontroller über USB mit dem Computer.
2. **USB-Ports identifizieren**:
   - Öffnen Sie die Eingabeaufforderung (CMD) im Verzeichnis (z. B. `cd /path/to/Frontend`), in dem die Proto-App gespeichert ist.
   - Führen Sie den folgenden Befehl aus, um die angeschlossenen USB-Geräte aufzulisten:
     ```bash
     proto list
     ```
   - Notieren Sie die entsprechenden COM-Ports (z. B. `COM3`).
3. **Daten von allen Controllern empfangen**:
   - Öffnen Sie für jeden angeschlossenen USB-Port ein separates Terminal.
   - Führen Sie den folgenden Befehl aus, um die Daten an den Server zu senden:
     ```bash
     proto listen -s COM3 --web -d http://127.0.0.1:3000
     ```
   - Ersetzen Sie `COM3` durch den entsprechenden Port, der in Schritt 2 identifiziert wurde.
---
### Dashboards anzeigen
- Navigieren Sie in Grafana zu **Dashboards**.
- Wählen Sie das gewünschte Dashboard aus (z. B. `Stadt_Dashboard.json`).
---
### Daten abfragen
- Verwenden Sie PostgreSQL, um historische Daten bei Bedarf abzufragen.
---
### Anpassung
1. **Dashboards bearbeiten oder hinzufügen**:
   - Fügen Sie neue Dashboard-Dateien in den Ordner `provisioning/dashboards/` ein.
   - Bearbeiten Sie vorhandene Dashboards, um weitere Datenquellen oder Visualisierungen hinzuzufügen.
2. **Neue Sensoren hinzufügen**:
   - Aktualisieren Sie das Datenbankschema und die Bereitstellungsdateien (`init.sql` und `provisioning/datasources.yaml`), um neue Sensoren zu integrieren.
---
Mit diesen Schritten können die Sensordaten effizient empfangen und visualisiert werden. Passen Sie das System bei Bedarf an, um neue Anforderungen zu erfüllen.
## 7. Dateien und Verzeichnisse
Hier sind die wichtigsten Dateien und Verzeichnisse im Projekt:
- `docker-compose.yml`: Konfiguration zum Ausführen des Projekts mit Docker.
- `prov/datasources.yaml`: Definiert die Grafana-Datenquellenkonfiguration.
- `prov/dashboards/`: Enthält vorgefertigte Grafana-Dashboard-JSON-Dateien.
- `init.sql`: Initialisiert das Datenbankschema und die Tabellen.
