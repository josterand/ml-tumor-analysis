import pandas as pd

def main():
    global df
    df = pd.read_csv('tumor-data.csv')

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

if __name__ == "__main__":
    main() # Biarin aja di paling pertama!
    checkDataSetInfo()
