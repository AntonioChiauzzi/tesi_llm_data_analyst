# Large Language Models a supporto del Data Analyst: analisi e confronto di strumenti

Repository associato alla tesi di laurea **"Large Language Models a supporto del Data Analyst: analisi e confronto di strumenti"**.

Il repository raccoglie i materiali utilizzati durante la sperimentazione descritta nella tesi, con riferimento ai dataset, agli script per la preparazione dei dati e alle risposte complete generate dagli strumenti basati su Large Language Models (LLM).

## Struttura del repository

### `dataset_iscritti/`

Contiene i materiali relativi al dataset utilizzato nel primo caso di studio.

La cartella comprende:

- i file di dati originali nella cartella `data/raw/`;
- il file `classi_laurea.csv` nella cartella `data/lookup/`;
- lo script Python `merge_iscritti.py` utilizzato per preparare il dataset;
- il dataset finale `iscritticorsi20102025.csv` nella cartella `data/processed/`;
- il file `README.md` con le informazioni relative ai dati e alle operazioni effettuate.

### `risposte_ai/`

Contiene le risposte complete ottenute durante la sperimentazione con i quattro strumenti selezionati:

- Perplexity
- Microsoft Copilot
- Claude
- Gemini

Le risposte sono organizzate in base ai casi di studio e alle prove effettuate.

## Strumenti utilizzati

La sperimentazione è stata svolta utilizzando le seguenti configurazioni:

| Strumento | Configurazione |
|---|---|
| Perplexity | Sonar 2 derivante da Llama 3.3 70B |
| Microsoft Copilot | Automatico |
| Claude | Sonnet 5, Medio |
| Gemini | 3.6 Flash |

## Finalità

Il repository rende disponibili i materiali utilizzati durante la sperimentazione e permette di consultare le risposte complete degli strumenti.