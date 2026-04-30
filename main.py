import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def checkDataSetInfo():
    """
    # Memeriksa Isi File CSV
    Print informasi teknis mengenai file data dan memeriksa adakah nilai yang kosong."""
    print("\n" + "="*50 + "\n", "Informasi dasar file CSV:", "\n" + "="*50 + "\n")
    print(df.info())

    print("\n" + "="*50 + "\n", "Jumlah nilai yang kosong di setiap kolom file CSV", "\n" + "="*50 + "\n")
    print(df.isnull().sum())

    print("\n" + "="*50 + "\n", "Sekilas isi file CSV", "\n" + "="*50 + "\n")
    print(df.describe())

def getGraph():
    print("Memproses visualisasi Data")
    fig, axes = plt.subplots(1,2,figsize=(12,5))

    # Grafik kiri: Mean Smoothness
    sns.histplot(df["mean smoothness"], kde=True, color="blue", ax=axes[0])
    axes[0].set_title("Distribusi Mean Smoothness")

    sns.histplot(df["mean area"], kde=True, color="red", ax=axes[1])
    axes[1].set_title("Distribusi Mean Area")

    plt.tight_layout()
    plt.show()

def main():
    global df
    df = pd.read_csv('tumor-data.csv')

if __name__ == "__main__":
    main() # Biarin aja di paling pertama!
    # checkDataSetInfo()
    getGraph()
