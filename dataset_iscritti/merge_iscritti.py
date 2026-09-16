from pathlib import Path
import pandas as pd

# =====================================================
# CARTELLE
# =====================================================

BASE_DIR = Path(__file__).parent
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

# =====================================================
# CERCA I CSV DEL MUR
# =====================================================

FILES = sorted(RAW_DIR.glob("*iscrittixcorso*.csv"))
if not FILES:
    raise FileNotFoundError(
        f"Nessun file trovato nella cartella:\n{RAW_DIR}"
    )
print("=====================================")
print("File trovati:")
for f in FILES:
    print(" -", f.name)
print("=====================================\n")

# =====================================================
# LETTURA FILE
# =====================================================

dfs = []
for file in FILES:
    print(f"Lettura {file.name}")
    try:
        df = pd.read_csv(
            file,
            sep=";",
            encoding="utf-8",
            low_memory=False
        )
    except UnicodeDecodeError:
        df = pd.read_csv(
            file,
            sep=";",
            encoding="latin1",
            low_memory=False
        )
    dfs.append(df)

# =====================================================
# UNIONE
# =====================================================

df = pd.concat(dfs, ignore_index=True)
print(f"\nRighe lette: {len(df):,}")

# =====================================================
# ELIMINA COLONNE
# =====================================================

drop_cols = [
    "AteneoCOD",
    "SedeP",
    "SedeC"
]
df = df.drop(
    columns=[c for c in drop_cols if c in df.columns],
    errors="ignore"
)

# =====================================================
# RINOMINA
# =====================================================

df = df.rename(columns={
    "AnnoA": "Anno",
    "AteneoNOME": "Ateneo",
    "ClasseNUMERO": "Classe",
    "CorsoNOME": "Corso",
    "GruppoCODICE": "GruppoCodice",
    "Sesso": "Sesso",
    "Isc": "Iscritti"
})

# =====================================================
# ORDINA
# =====================================================

df = df.sort_values(
    ["Anno", "Ateneo", "Corso", "Sesso"]
)

# =====================================================
# DUPLICATI
# =====================================================

prima = len(df)
df = df.drop_duplicates()
dopo = len(df)
print(f"Duplicati rimossi: {prima - dopo:,}")

# =====================================================
# ESPORTA
# =====================================================

output = PROCESSED_DIR / "iscritti_corsi20102025.csv"
df.to_csv(
    output,
    index=False,
    encoding="utf-8-sig"
)

# =====================================================
# FINE
# =====================================================

print("\n=====================================")
print("CSV creato correttamente!")
print(output)
print(f"Righe: {len(df):,}")
print(f"Colonne: {len(df.columns)}")
print("=====================================")