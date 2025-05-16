# Identificare il tipo di applicazione
L'applicazione è una API REST che gestisce un database di utenti. Una API REST permette due applicazioni di comunicare tramite protocollo HTTP. Per essere RESTful deve rispettare diverse caratteristiche, tra cui:
- un webservice espone l’accesso a risorse di vario tipo (dati, procedure, dispositivi,sensori, ...) identificate mediante URL;
- le risorse sono rese disponibili mediante rappresentazioni che possono essere differenziate (per esempio: XML, JSON, ...);
- le operazioni che si effettuano sulle risorse sono quelle espresse dai metodi del protocollo HTTP (GET, POST, PUT, DELETE, ...) rispettandone la semantica;
- il webservice non memorizza lo stato dell’interazione con il client (stateless server) e, di conseguenza, ogni richiesta da parte del client deve contenere tutte le informazioni necessarie per essere servita;
- lo stato dell’interazione tra client e server è rappresentato e gestito mediante URL restituiti dal webservice al client, che identificano le rappresentazioni delle risorse: questo principio è definito HATEOAS (Hypermedia As The Engine Of ApplicationState).
Tutte queste proprietà sono rispettate dall'applicazione.
Questo software fa da middleware tra il client (es. sito web) e il server (contenente una istanza di un database come MongoDB che in questo caso è solo simulato da un dizionario di python). Utilizza quindi l'architettura client-server a 3 livelli, con il client che gestirà la User Interface, il middleware che gestirà la logica di business e il server che gestirà i dati.

RIspettando le regole delle API REST, le operazioni da eseguire sulle risorse sono specificate dal metodo HTTP e non nell'url, come di seguito dimostrato.
## Operazioni GET
### Lista di tutti gli utenti del database
![[Screenshot 2025-05-16 alle 12.53.39.png]]
### Richiesta di un utente specifico
![[Screenshot 2025-05-16 alle 12.56.49.png]]
## Operazioni POST
### Aggiunta di un nuovo utente
![[Screenshot 2025-05-16 alle 12.59.37.png]]
![[Screenshot 2025-05-16 alle 12.59.48.png]]
## Operazioni PUT
### Aggiornamento di un utente
![[Screenshot 2025-05-16 alle 13.02.23.png]]
![[Screenshot 2025-05-16 alle 13.02.58.png]]
## Operazioni DELETE
### Eliminazione di un utente
![[Screenshot 2025-05-16 alle 13.04.54.png]]
![[Screenshot 2025-05-16 alle 13.05.06.png]]
# Docker
È possibile far girare l'applicazione in un docker container per una migliore portabilità e scalabilità.
Di seguito un esempio di DockerFile. (utilizzerò poetry per la gestione del virtuall environment)
``` DockerFile
# Use an official Python image
FROM python:3.13-slim

# Install Poetry
RUN python -m pip install poetry

# Set working directory
WORKDIR /app

# Copy Poetry files
COPY poetry.lock pyproject.toml ./

# Install dependencies
RUN poetry install --no-interaction --no-ansi --no-root

# Copy the application
COPY . .

# Install the application
RUN poetry install --no-interaction --no-ansi

# Expose the port Flask runs on
EXPOSE 8000

# Start the FastAPI server
CMD ["poetry", "run", "python", "applicazione.py"]
```
Per creare l'immagine:
``` bash
sudo docker build .
```
Per runnare il container:
``` bash
sudo docker run -d -p 5000:5000 <container_id> 
```
### Docker compose
``` yml
version: "3.8"

services:
  app:
    build: .
    ports:
      - "5000:5000"
      - .:/app       
    restart: unless-stopped
```
Per runnarlo:
``` bash
sudo docker compose up --build -d
```
#### Ulteriori possibilità
Volendo automatizzare la scalabilità dell'applicazione potrei creare un cluster di docker container con docker swarm.
# Framework
Il framework utilizzato per l'implementazione delle API è `flask`.
**Flask** è un **micro web framework** scritto in Python, utilizzato per sviluppare applicazioni web in modo semplice e veloce.
[Fonte][https://en.wikipedia.org/wiki/Flask_(web_framework)]
## Caratteristiche principali:
- **Leggero e minimalista:** fornisce solo gli strumenti essenziali, lasciandoti la libertà di scegliere librerie e componenti aggiuntivi.
- **Routing facile:** permette di associare facilmente URL a funzioni Python.
- **Supporta JSON, form HTML, richieste HTTP…**
- **Modulare:** puoi espanderlo con estensioni (es. per database, login, ecc.).
- **Perfetto per piccoli progetti e REST API.**
## Utilizzi
Flask viene utilizzato negli ambiti della sanità, dei viaggi e della finanza.
### Viaggi
Flask è l'ideale per applicazioni basate sull'intelligenza artificiale, come motori di ricerca, route planners, e sistemi di pricing dinamici.
### Sanità
Flask è utilizzato in applicazioni che usano l'IA per le diagnosi mediche, chatbot medici e piattaforme di sanità telematica. Un solido esempio di questa applicazione è [FlaskData.io][_FlaskData.io_].
### Finanza
Flask è ideale per applicazione di tracking delle spese e applicazioni di rilevamento delle truffe che usano l'IA.
[Fonte][https://embarkingonvoyage.com/blog/technologies/how-python-flask-django-for-enterprise-applications-are-powering-digital-innovation/]
## Alternative
Una valida alternativa a flask è il framework `FastAPI`.
