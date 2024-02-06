## Glossar
|Begriff|Beschreibung|
|--------|-----------|
|UAT     | User Acceptance Testing|
|QA | Quality Assurance
| SKA | Service Level Agreement|
| SUT | System under test |
| SDLC | System development life cycle |
| SDE | Software Development Environment |

## Kriterien für gute Testfälle
- Aus Tests, welche eine hohe Wahrscheinlichkeit von Fehler aufzeigen
- Aus Tests, die nicht dasselbe testen (keine Redundanz)
- Aus Tests, die unabhängig von einander sind
- Aus Tests, die möglichst viel Code abdecken
## V-Model
![[Pasted image 20231216104124.png]]
- **Anforderungsdefinition** mit den Wünschen und Anforderungen des Auftraggebers
- **Funktionaler Systementwurf** wo die Anforderungen auf Funktionen und Dialoge abgebildet werden
- **Technischer Systementwurf** wo die technische Realisierung entworfen wird (System wird in Komponente unterteilt, Schnittstellen werden definiert)
- **Komponentenspezifikation**, wo jedes Teilsystem im Detail beschrieben wird
- **Programmierung**, wo jeder Baustein (Modul, Klasse, etc.) in einer Programmiersprache programmiert wird

## Test Typen
- **Komponententest** prüft, ob jeder elementare Softwarebaustein seine Vorgaben erfüllt.
- **Integrationstest** prüft, ob Gruppen von Komponenten korrekt zusammenspielen
- **Systemtest** prüft, ob das System als Ganzes die Anforderungen erfüllt.
- **Abnahmetest** prüft, ob das System vom Kunden als korrekt akzeptiert wird.

## Teststrategie
- Testobjekte mit einer kurzen Auflistung aus welchen Teilen die Software besteht
- Auflistung was genau getestet wird (welche Funktionen zu testen sind, bzw. Und welche nicht getestet werden
- Testmethode auswählen
- Welche Testinfrastruktur verwendet wird

## Testobjekte
Hier handelt es sich um die Komponente oder Teil der Applikation, welches getestet wird. Typische Testobjekte sind Programmmodule oder Units (z.Bsp. eine Klasse). Aber auch Kommandozeilenskripte des Betriebssystems, DB-Skripte oder Datenkonvertierungsprozeduren können Testobjekte sein.

## Testfälle
- **Funktionale Testfälle**: Beschreiben die Funktionen einer Software, welche vom Kunden ursprünglich als Anforderung definiert worden sind.
- **Nicht-funktionale Testfälle**: Testfälle welche nicht generell mit der Applikation zutun haben. (Performance etc.)
- **Wir werden uns in diesem Modul nur auf funktionales Testing beschränken.**
- **Abstrakte Testfälle**: keine konkreten Ein- und Ausgabewerte, sondern wir verwenden logische Operatoren
- **Konkrete Testfälle**: konkreten Wertangaben für die Ein- und Ausgabe

## Testmethoden
- **Whitebox**: Code sichtbar; Code-Pfad Testing
- **Blackbox**: Kennen den Code nicht, schon kompliliert/deployed.
- **Automatisierte Testfälle**: automatisiert Test Case Suiten (ganze Reihen von Tests) auszuführen.

## Testlevels
![[Pasted image 20231216104827.png]]

## Unittest
- Wird manchmal zum Unit Testing Level dazu gezählt
- Von Entwickler geschrieben und ausgeführt
- White-Box-Test
- Hier wird das Zusammenspiel zwischen mehreren Komponenten getestet
- Schnittstellen jedoch wie z.B. zu einer Datenbank werden hier gemockt
    - Andere Beispiele von Schnittstellen:
        - Externe APIs
        - Message queues

## Component Testing
- Wird manchmal zum Unit Testing Level dazu gezählt
- Von Entwickler geschrieben und ausgeführt
- White-Box-Test
- Hier wird das Zusammenspiel zwischen mehreren Komponenten getestet
- Schnittstellen jedoch wie z.B. zu einer Datenbank werden hier gemockt
    - Andere Beispiele von Schnittstellen:
        - Externe APIs
        - Message queues

## Intergration Testing
- Wird von einem Tester (oder ganzes QA Team) ausgeführt
- Black-Box-Test
- Hier werden Integration wie z.B. zu einer Datenbank (oder APIs / Message queues) nicht mehr gemockt sondern aktiv benutzt
- Beispiel: Der Tester ruft eine API auf welche dann eine Datenbank einen Zugriff macht (der Tester kennt das innere der API jedoch nicht)

## System Testing
- Wird von den gleichen Team, welche die Integrations Tests gemacht haben, getestet
- Black-Box-Test
- Hier wird die Software als ganzes getestet, um sicherzustellen, dass alle Requirements erfüllt sind
- Eine Umgebung die Möglichst nahe an der **Live** Umgebung ist, wird hier benutzt
- Funktionale und Nichtfunktionale Anforderungen werden hier getestet
- Nichtfunktionale Tests wären hier zum Beispiel:
    - Performance Testing um [Bottlenecks](https://en.wikipedia.org/wiki/Bottleneck_(software)) bezüglich Performanz zu finden. Hier kann nochmals zwischen folgenden unterschieden werden:
        - Load Testing -> Um zu verstehen wie sich die Software z.B. bei einer gesetzten Anzahl an Requests verhält
        - Stress Testing -> Um ein Limit der Software zu wissen
    - Usability Testing um Fehler oder Verbesserungen zu finden, in dem man den Benutzer beobachtet wie er die Software bedient
    - Security Testing um z.B. zu Testen ob die Authentifizierung sicher ist

## Acceptance Testing
- Wird in der Regel vom Business / Kunden getestet
- Black-Box-Test
- Hier wird vom Kunden sichergestellt, ob das System die Akzeptanz Kriterien erfüllt

![[Pasted image 20231216104955.png]]


| Automation Testing                                                                                             | Manual Testing                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Zuverlässig, jeder Test ist programmiert / scripted                                                            | Unzuverlässig, Menschliche Fehler passieren schnell                                                                         |
| Riesiger Initial Aufwand, Billiger auf lange Zeit                                                              | Initialer Aufwand ist kleiner. [ROI](https://en.wikipedia.org/wiki/Return_on_investment) ist kleiner auf lange Zeit gesehen |
| Ist eine sehr zeitsparende Option für Regression Testing (Tests welche mehrere Male ausgeführt werden sollen). | Eher eine Option wenn die gleichen Tests nicht laufend wieder ausgeführt werden müssen.                                     |
| Ausführung durch einen einzigen Knopfdruck (oder automatisiert durch einen Trigger)                            | Ausführung braucht sehr viel Ressourcen (Mitarbeiter multipliziert mit den Anzahl Stunden)                                  |
| Exploratives Testen nicht möglich                                                                              | Exploratives Testen möglich                                                                                                 |
| Performanz Testing ist möglich                                                                                 | Performanz Testing ist nicht möglich                                                                                        |
| Tests können parallelisiert ausgeführt werden                                                                  | Braucht mehr Ressourcen um parallel zu Testen                                                                               |
| Braucht Programmier/Scripting Skills um Tests zu erstellen                                                     | Brauch sehr wenig Wissen um einen Test auszuführen                                                                          |
| Professionelle Testing Tools können sehr schnell teuer werden                                                  | -                                                                                                                           |

### Schritte um Automatisiertes Testing aufzusetzen
- Geeignetes Test Tool auswählen
- Den Scope (Anwendungsbereich) der Automation definieren
- Test Cases
    - Planen
    - Definieren
    - Implementieren
- Tests ausführen
- Tests warten (Maintenance)

### Auto-Test Typen
**Funktionstests:**
- Konzentriert sich darauf, ob die Software für einen bestimmten Eingabeaufforderung den richtigen Ausgabewert liefert.
- Beispiel: Überprüfung, ob ein Benutzer sich erfolgreich auf einer Webseite anmelden kann.

**Nicht-funktionale Tests:**
- Beziehen sich auf Aspekte der Software, die nicht unbedingt mit einer bestimmten Funktion oder Benutzeraktion zusammenhängen.
- Beispiele sind Skalierbarkeit, Verhalten unter Stressbedingungen und Sicherheit.

**Smoke-Tests (Sanity-Tests):**
- Enthalten minimale Tests, um festzustellen, ob grundlegende Probleme vorhanden sind, die das Funktionieren der Software verhindern.
- Es werden nur die essenziellsten Funktionen getestet.

**Regressionstests:**
- Zielen darauf ab, Fehler nach einer größeren Code-Änderung zu finden.
- Identifizieren Software-Regressionen, bei denen zuvor funktionierende Funktionen nicht mehr wie beabsichtigt arbeiten.
- Werden üblicherweise nach neuen Code-Änderungen durchgeführt, um unbeabsichtigte Konsequenzen zu entdecken.

**Schlüsselwortgesteuertes Testen:**
- Testansatz, bei dem Schlüsselwörter oder Aktionen verwendet werden, um verschiedene Funktionen eines Systems zu testen.

**Datengetriebenes Testen:**
- Testansatz, bei dem Testfälle auf der Grundlage von Eingabedatensätzen entworfen werden.
- Tests werden mit verschiedenen Datensätzen ausgeführt, um verschiedene Szenarien zu validieren.


## Test Doubles
- **Definition:**
    - Objekte oder Systeme, die anstelle anderer Elemente in Tests verwendet werden.
- **Kategorien:**
    - Mocks (mock, spy)
    - Stubs (stub, dummy, fake)

## **Mocks vs. Stubs:**
- **Zweck:**
    - Beseitigung von Testabhängigkeiten, um sich auf die Überprüfung bestimmter Funktionalitäten zu konzentrieren.
- **Mocks:**
    - Überprüfen Interaktionen zwischen dem zu testenden System (SUT) und seinen Kollaborateuren.
    - Überprüfen, ob Methoden korrekt aufgerufen werden.
- **Stubs:**
    - Liefern vordefinierte Daten an das SUT.
    - Direkte Überprüfung, ob das SUT das richtige Ergebnis mit den bereitgestellten Daten produziert.

## **Lebenszyklus:**
1. **Setup:**
    - Vorbereitung des SUT und seiner Stub-Kollaborateure.
    - Erwartungen für Mocks festlegen.
2. **Anwenden:**
    - Testen der Funktionalität.
    - Methodenaufrufe auf Mocks auslösen oder Daten an Stubs bereitstellen.
3. **Überprüfen:**
    - Überprüfen des Zustands des Objekts oder Überprüfen von Erwartungen für Mocks.
4. **Aufräumen:**
    - Ressourcen bereinigen.

## **Arten von Test Doubles:**
- **Mock:**
    - Erwartet bestimmte Aufrufe und überprüft Interaktionen.
- **Spy:**
    - Protokolliert und stellt Daten für die Analyse bereit, ähnlich wie ein Spion.
- **Dummy:**
    - Einfache Objekte, häufig für die Initialisierung von Konstruktoren verwendet.
- **Stub:**
    - Bietet vordefinierte Daten für Tests, nützlich, um unerwünschte Nebenwirkungen zu vermeiden.
- **Fake:**
    - Hat funktionale Implementierungen, die sich von der Produktionscode unterscheiden.

## **Mockito:**
- Ein umfassendes Mocking-Framework, das Dummies, Mocks, Spys und Stubs unterstützt.

## **Zusätzliche Anwendungsfälle:**
- Frameworks wie WireMock initialisieren HTTP-Mock-Server, um APIs zu mocken und HTTP-Antworten zu stubben.

## Teststrategie und Testkonzept

Teststrategie und Testkonzept sind wesentliche Komponenten für erfolgreiches Testen. Die Teststrategie beschreibt den Testansatz, während das Testkonzept diesen Ansatz definiert. Ein Testkonzept, oft auch als Testplan bezeichnet, umfasst Elemente wie:

## Testkonzept nach IEEE 829

Der IEEE 829 Standard dient als Empfehlung für ein Testkonzept und bietet eine detaillierte Liste aller notwendigen Elemente. Diese Elemente können als Checkliste betrachtet werden. Die wichtigsten Elemente sind:
### Introduction
- Kurze Beschreibung der Applikation für ein gemeinsames Verständnis.
### Test Items
- Auflistung und Beschreibung der zu testenden Elemente mit einer Architekturskizze.
### Features to be tested
- Detaillierte Liste der zu testenden Funktionalitäten, abgeleitet von den Test Items.
### Features not to be tested
- Beschreibung der Funktionalitäten, die nicht getestet werden, wie z.B. nicht-funktionale Aspekte.
### Approach
- Beschreibung der angewandten Testmethode, z.B., durch TDD im Entwicklerteam.
### Item pass / fail criteria
- Festlegung der Kriterien für erfolgreiche und nicht erfolgreiche Tests.
### Test Deliverables
- Beschreibung der Test-Artefakte, einschließlich Dokumente und Tools wie das Testkonzept oder Testwerkzeuge wie Postman.
### Testing Tasks
- Beschreibung der Teststufen, von Unit-Tests bis zu möglichen Integrationstests.
### Environmental Needs
- Beschreibung der für das Testing benötigten Testumgebungen (Hardware und Software).
### Schedule
- Zeitplan für die Durchführung der Tests, angepasst an den gewählten Entwicklungsansatz.

# Test Driven Development (TDD)
Test Driven Development, kurz TDD, existiert seit etwa 2003 und ist ein wesentlicher Bestandteil von Agile Programming. Ron Jeffries, ein Coach von Extreme Programming, verspricht "Clean code that works", wenn TDD regelmäßig trainiert und konsequent angewendet wird. Extreme Programming folgt dem Agile Manifest, daher ergibt die Anwendung von TDD in agilen Teams Sinn. Es kann jedoch herausfordernd sein, TDD in Projekten zu implementieren, die nicht von Anfang an darauf ausgerichtet waren.

## Was ist TDD?
TDD bedeutet, Tests zu verwenden, die das Schreiben des Codes antreiben. Der TDD-Workflow besteht aus den Schritten Red, Green und Refactor:

- **Red:** Tests für die erwartete Business-Logik schreiben, die zu diesem Zeitpunkt fehlschlagen werden, da noch kein Code vorhanden ist.
- **Green:** Code schreiben oder korrigieren, um die Tests erfolgreich zu machen.
- **Refactor:** Nach erfolgreichem Testen von Code und Tests, den Code und die Tests verbessern, um sie effizienter zu gestalten. Dieser Prozess wiederholt sich iterativ, beginnend mit dem Schritt Red.

**TDD-Mantra:** Immer zuerst einen fehlschlagenden Test schreiben, bevor auch nur eine Zeile "richtigen" Codes erstellt wird. Jeder Test sollte nur eine identifizierbare Logik oder Verhaltenseinheit überprüfen - also handelt es sich um Unit Tests.

## Best Practices für Test Driven Development
TDD betont das Schreiben von Tests vor dem eigentlichen Code und folgt einem zyklischen Prozess. Hier sind bewährte Verfahren:

1. **Klares Verständnis der Anforderungen:**
    - Verstehen Sie die Anforderungen oder Spezifikationen der zu entwickelnden Funktion, um gezielte Tests zu schreiben.
2. **Atomare Tests schreiben:**
    - Jeder Test sollte sich auf ein spezifisches Verhalten oder eine bestimmte Funktionalität konzentrieren, um die Lesbarkeit und Wartbarkeit zu verbessern.
3. **Einfachsten Testfall zuerst schreiben:**
    - Beginnen Sie mit dem einfachsten Testfall, der fehlschlagen wird, um sich auf die unmittelbare Aufgabe zu konzentrieren.
4. **Tests für Randfälle einbeziehen:**
    - Berücksichtigen Sie Randbedingungen und Randfälle, um potenzielle Fehler oder unerwartetes Verhalten aufzudecken.
5. **Regelmäßiges Refactoring:**
    - Nach einem bestandenen Test Zeit nehmen, den Code zu refaktorieren und das Design zu verbessern, ohne das Verhalten zu ändern.
6. **Schnelle Feedbackschleife beibehalten:**
    - Testsuite sollte schnell ausgeführt werden, um sofortiges Feedback über den Zustand des Codes zu erhalten.
7. **Automatisierung der Tests:**
    - Nutzen Sie Testautomatisierungs-Frameworks und -Tools, um Tests zu automatisieren und konsistente Ergebnisse sicherzustellen.
8. **Red-Green-Refactor-Zyklus befolgen:**
    - Halten Sie sich an den TDD-Zyklus: Schreiben Sie einen fehlgeschlagenen Test (Red), implementieren Sie den minimalen Code, um den Test zu bestehen (Green), und überarbeiten Sie dann den Code (Refactor). Wiederholen Sie diesen Zyklus für jedes neue Verhalten oder jede Funktion.
9. **Kontinuierliche Ausführung von Tests:**
    - Integrieren Sie die Testsuite in Ihre Entwicklungsumgebung, richten Sie Pipelines für die kontinuierliche Integration (CI) ein und führen Sie Tests automatisch aus, wenn Codeänderungen vorgenommen werden.

## Vorteile von TDD
- Kostenreduktion
- Schnelleres Refactoring und Neuschreiben von Code
- Vereinfachtes Onboarding neuer Teammitglieder
- Vermeidung von Bugs und Kopplung
- Verbesserte Teamzusammenarbeit
- Erhöhtes Vertrauen in die Code-Funktionalität
- Verbesserte Coding Patterns
- Beseitigung der Angst vor Veränderungen

# Automatisiertes Testen und Deployen
- **Pipeline:** Die Top-Level Komponente, in der "Stages" und "Jobs" deklariert werden können.
- **Stage:** Beschreibt die einzelne Phase in der Pipeline. Eine Stage besteht aus einem oder mehreren Jobs.
- **Job:** Ein einzelner Prozess innerhalb einer Stage. Ein Job könnte beispielsweise das Kompilieren von Code sein.
- **Runner:** Eine Open-Source-Anwendung, die die einzelnen Jobs ausführt. Die App kann lokal installiert oder in einer Cloud-Umgebung verwendet werden (Shared Runners werden auf GitLab gehostet).

## CI/CD
```yaml
stages:          # List of stages for jobs, and their order of execution
  - build
  - test
  - deploy

build-job:       # This job runs in the build stage, which runs first.
  stage: build
  script:
    - echo "Compiling the code..."
    - echo "Compile complete."

unit-test-job:   # This job runs in the test stage.
  stage: test    # It only starts when the job in the build stage completes successfully.
  script:
    - echo "Running unit tests... This will take about 60 seconds."
    - sleep 60
    - echo "Code coverage is 90%"

# Optional
lint-test-job:   # This job also runs in the test stage.
  stage: test    # It can run at the same time as unit-test-job (in parallel).
  script:
    - echo "Linting code... This will take about 10 seconds."
    - sleep 10
    - echo "No lint issues found."

deploy-job:      # This job runs in the deploy stage.
  stage: deploy  # It only runs when *both* jobs in the test stage complete successfully.
  environment: production
  script:
    - echo "Deploying application..."
    - echo "Application successfully deployed."
```

## Deployment Enviroment
![[Pasted image 20231216111737.png]]

- **Entwicklungsumgebung (Dev):** Hier entwickeln Entwickler neuen Code auf ihren Workstations. Unterscheidet sich von der Produktionsumgebung durch Entwicklertools.
- **Testumgebung:** Hier testen menschliche Tester neuen Code, entweder durch automatisierte oder manuelle Tests. Nach erfolgreichen Tests erfolgt die automatische Übertragung in die nächste Umgebung.
- **Staging-Umgebung:** Testumgebung, die der Produktionsumgebung entspricht. Hier werden Installations-/Konfigurations-/Migrations-Skripte getestet. Auch für Leistungs- und Lasttests sowie Vorschauen für Kunden genutzt.
- **Produktionsumgebung (Live):** Die Umgebung, mit der Benutzer direkt interagieren. Hier wird der Code live bereitgestellt. Der heikelste Schritt in der Softwareentwicklung.

##### Good to know
- **Patch:** Sofortige Softwareupdates zur Behebung von Problemen, meist im laufenden Betrieb.
- **Update:** Aktualisiert die Software, behebt Fehler, verbessert die Performance. Kleine Erweiterungen können enthalten sein, aber keine substantiellen Veränderungen.
- **Upgrade:** Erweitert die Software auf verschiedenen Ebenen, mit neuen Funktionen und möglicherweise einer neuen Struktur. Die Software rückt in eine neue Produktklasse.

## Code Review
### Beispiel Ablauf per GitLab
1. Entwickler erstellt Feature Branch.
2. Feature wird implementiert und committet.
3. Durch Push wird automatisch ein Link für einen Merge Request (PR) erstellt.
4. PR-Titel und -Beschreibung werden festgelegt.
5. Reviewer prüfen den Code und kommentieren.
6. Nach Diskussionen wird der PR genehmigt und der Code gemerged.
### Aufgaben eines Prüfers
- Überprüfung von Funktionalität und Implementierungsqualität.
- Kommentare zu Änderungen.
- Idealerweise kleinere PRs für effiziente Reviews.
- Code-Qualität anhand von Checklisten und Best Practices beurteilen.
### Qualität des Codes (ein paar Beispiele)
- Kommentare, Naming, Logik-Fehler, Typos.
- Verständlichkeit, Einhaltung von Prinzipien (YAGNI, DRY, KISS, SRP).
- Existenz und Abdeckung von Tests.
- Gepflegtheit des Codes.
### Ressourcen
- Verwendung von Checklisten und Kenntnis von Best Practices.
- Bezugnahme auf bewährte Prinzipien aus Büchern wie "Clean Code" und "Effective Java".
### Soziale Aspekte eines Prüfers
- Respektvoller Umgang mit dem persönlichen Beitrag jedes Entwicklers.
- Professionelles Verhalten und konstruktive Kritik.
- Detaillierte Antworten und Vorschläge.
- Separate Anmerkungen für übergeordnete Vorschläge.
### Abschluss und Merge Varianten
- Genehmigte PRs werden in den Master Branch gemerged.
- Default ist ein Merge-Commit.
- Beachtung alternativer Merge-Varianten, je nach Projektanforderungen.