from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# -----------------------------------------------------------------------------
# FUNZIONI PER LA GENERAZIONE DEI GRAFICI
# -----------------------------------------------------------------------------


def genera_scheda_1_media_mediana(
    df: pd.DataFrame, media: float, mediana: float, output_dir: Path
):
    """Scheda 1: Grafico dell'andamento con linee di Media e Mediana."""
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(
        df["Mese"],
        df["Entrate"],
        marker="o",
        linewidth=2,
        color="#1f77b4",
        label="Entrate Mensili (€)",
    )
    ax.axhline(
        media,
        color="red",
        linestyle="--",
        linewidth=1.5,
        label=f"Media ({media:.2f} €)",
    )
    ax.axhline(
        mediana,
        color="green",
        linestyle=":",
        linewidth=2,
        label=f"Mediana ({mediana:.2f} €)",
    )

    ax.set_title(
        "Scheda 1: Andamento Entrate e Confronto Media vs Mediana",
        fontsize=12,
        pad=15,
    )
    ax.set_ylabel("Entrate (€)")
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend(loc="upper left")
    plt.xticks(rotation=45)
    plt.tight_layout()

    path_salvataggio = output_dir / "scheda_1_media_vs_mediana.png"
    plt.savefig(path_salvataggio, dpi=300)
    plt.close()
    print(f" Grafico Scheda 1 salvato in: {path_salvataggio}")


def genera_scheda_2_outlier(
    df: pd.DataFrame, media: float, dev_std: float, output_dir: Path
):
    """Scheda 2: Istogramma/Bar chart per evidenziare l'outlier di Giugno."""
    fig, ax = plt.subplots(figsize=(10, 5))

    soglia_ucl = media + (2 * dev_std)
    colori = ["#d62728" if m == "Giugno" else "#aec7e8" for m in df["Mese"]]

    ax.bar(df["Mese"], df["Entrate"], color=colori)
    ax.axhline(
        soglia_ucl,
        color="darkred",
        linestyle="--",
        linewidth=1.5,
        label=f"Soglia Tolleranza (+2σ = {soglia_ucl:.2f} €)",
    )

    ax.set_title(
        "Scheda 2: Identificazione Outlier di Giugno (Soglia 2 Dev.Std)",
        fontsize=12,
        pad=15,
    )
    ax.set_ylabel("Entrate (€)")
    ax.grid(axis="y", linestyle="--", alpha=0.5)
    ax.legend(loc="upper left")
    plt.xticks(rotation=45)
    plt.tight_layout()

    path_salvataggio = output_dir / "scheda_2_outlier_giugno.png"
    plt.savefig(path_salvataggio, dpi=300)
    plt.close()
    print(f" Grafico Scheda 2 salvato in: {path_salvataggio}")


def genera_scheda_3_carta_controllo(df_senza_giugno: pd.DataFrame, output_dir: Path):
    """Scheda 3: Carta di Controllo (UCL / LCL) escludendo l'outlier di Giugno."""
    media_nj = df_senza_giugno["Entrate"].mean()
    std_nj = df_senza_giugno["Entrate"].std()
    ucl = media_nj + (2 * std_nj)
    lcl = media_nj - (2 * std_nj)

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(
        df_senza_giugno["Mese"],
        df_senza_giugno["Entrate"],
        marker="o",
        color="#2ca02c",
        linewidth=2,
        label="Entrate (Ordinario)",
    )
    ax.axhline(
        media_nj,
        color="black",
        linestyle="-",
        linewidth=1.5,
        label=f"Media Ordinaria ({media_nj:.2f} €)",
    )
    ax.axhline(
        ucl,
        color="red",
        linestyle="--",
        linewidth=1.5,
        label=f"UCL ({ucl:.2f} €)",
    )
    ax.axhline(
        lcl,
        color="red",
        linestyle="--",
        linewidth=1.5,
        label=f"LCL ({lcl:.2f} €)",
    )

    ax.set_title(
        "Scheda 3: Carta di Controllo del Processo dei Ricavi (Escluso Giugno)",
        fontsize=12,
        pad=15,
    )
    ax.set_ylabel("Entrate (€)")
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend(loc="upper right")
    plt.xticks(rotation=45)
    plt.tight_layout()

    path_salvataggio = output_dir / "scheda_3_carta_controllo.png"
    plt.savefig(path_salvataggio, dpi=300)
    plt.close()
    print(f" Grafico Scheda 3 salvato in: {path_salvataggio}")


# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------


def main() -> int:
    print("Hello from PixelNova Data Analyst!")

    # 1. PERCORSI FILE E CARTELLE
    project_root = Path(__file__).parents[2]
    file_path = (
        project_root
        / "data"
        / "ITS ICT Academy_Lezione 1_Rivelazione delle Performance_Dataset studenti.xlsx"
    )
    output_dir = project_root / "output"
    output_dir.mkdir(exist_ok=True)

    # 2. CARICAMENTO E PULIZIA DATI
    df_pixelnova = pd.read_excel(
        file_path, sheet_name="PixelNova", usecols="B:C", header=5
    ).dropna(how="all")
    df_pixelnova.columns = ["Mese", "Entrate"]
    df_pixelnova = df_pixelnova.dropna(subset=["Entrate"]).reset_index(drop=True)
    df_pixelnova["Entrate"] = pd.to_numeric(df_pixelnova["Entrate"])

    print("\n==================================================")
    print(" 1. MEDIA E MEDIANA")
    print("==================================================")

    totale_entrate = df_pixelnova["Entrate"].sum()
    media_entrate = df_pixelnova["Entrate"].mean()
    mediana_entrate = df_pixelnova["Entrate"].median()
    diff_media_mediana = media_entrate - mediana_entrate

    print(f"Totale Entrate Annue: {totale_entrate:.2f} €")
    print(f"Media mensile:       {media_entrate:.2f} €")
    print(f"Mediana mensile:     {mediana_entrate:.2f} €")
    print(f"Differenza:          {diff_media_mediana:.2f} €")
    print(
        "Spiegazione: La media è superiore alla mediana perché gonfiata dall'outlier di Giugno."
    )

    print("\n==================================================")
    print(" 2. DISPERSIONE ED EVENTUALE OUTLIER (GIUGNO)")
    print("==================================================")

    # Calcolo manuale devianza e varianza per completezza
    devianza = ((df_pixelnova["Entrate"] - media_entrate) ** 2).sum()
    varianza = devianza / (len(df_pixelnova) - 1)
    dev_std = df_pixelnova["Entrate"].std()

    entrate_giugno = df_pixelnova.loc[
        df_pixelnova["Mese"] == "Giugno", "Entrate"
    ].values[0]
    z_score_giugno = (entrate_giugno - media_entrate) / dev_std
    soglia_ucl_semplificata = media_entrate + (2 * dev_std)
    is_outlier = entrate_giugno > soglia_ucl_semplificata

    print(f"Devianza (SS):               {devianza:.2f} €²")
    print(f"Varianza (s²):               {varianza:.2f} €²")
    print(f"Deviazione Standard (s):     {dev_std:.2f} €")
    print(f"Entrate Giugno:              {entrate_giugno:.2f} €")
    print(f"Z-Score di Giugno:           {z_score_giugno:.2f}")
    print(f"UCL Semplificato (Media+2σ): {soglia_ucl_semplificata:.2f} €")
    print(f"Giugno è un Outlier?:        {is_outlier}")

    print("\n==================================================")
    print(" 3. ANALISI DEL PROCESSO (ESCLUSO GIUGNO)")
    print("==================================================")

    df_senza_giugno = df_pixelnova[df_pixelnova["Mese"] != "Giugno"].copy()

    media_nj = df_senza_giugno["Entrate"].mean()
    devianza_nj = ((df_senza_giugno["Entrate"] - media_nj) ** 2).sum()
    varianza_nj = devianza_nj / (len(df_senza_giugno) - 1)
    std_nj = df_senza_giugno["Entrate"].std()

    ucl = media_nj + (2 * std_nj)
    lcl = media_nj - (2 * std_nj)

    sotto_controllo = (
        (df_senza_giugno["Entrate"] >= lcl) & (df_senza_giugno["Entrate"] <= ucl)
    ).all()

    print(f"Media (11 mesi):             {media_nj:.2f} €")
    print(f"Devianza (11 mesi):          {devianza_nj:.2f} €²")
    print(f"Varianza (11 mesi):          {varianza_nj:.2f} €²")
    print(f"Deviazione Standard (11 mesi):{std_nj:.2f} €")
    print(f"UCL (Limite Superiore):      {ucl:.2f} €")
    print(f"LCL (Limite Inferiore):      {lcl:.2f} €")
    print(f"Processo Sotto Controllo?:   {sotto_controllo}")

    # 3. GENERAZIONE SCHEDE GRAFICHE
    print("\n==================================================")
    print(" GENERAZIONE SCHEDE GRAFICHE")
    print("==================================================")

    genera_scheda_1_media_mediana(
        df_pixelnova, media_entrate, mediana_entrate, output_dir
    )
    genera_scheda_2_outlier(df_pixelnova, media_entrate, dev_std, output_dir)
    genera_scheda_3_carta_controllo(df_senza_giugno, output_dir)

    print("\nTutte le schede e i report sono stati completati con successo!")
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
