import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from colorama import Fore, Style

# Baca file CSV
data_csv = pd.read_csv("tumor-data.csv")

# Men-Generate Gambar Yang Membuktikan Kalau Data Kita Berantakan
def getHistogram():
    data_kosong = data_csv.isnull().sum().sum()
    print(Fore.BLUE + f"[I] Jumlah nilai kolom yang kosong: {data_kosong}" + Style.RESET_ALL)
    if data_kosong == 0:
        print(Fore.GREEN + "[I] Data bersih" + Style.RESET_ALL)
    else:
        None
    # Membuat Histogram (Melihan perbedaan rentang angka)
    plt.figure(figsize=(8,5))
    sns.histplot(data_csv["mean area"], color="red", alpha=0.5, label="Mean Area (Luas)")
    sns.histplot(data_csv["mean smoothness"], color="blue", alpha=0.5, label="Mean Smoothness (Kehalusan)")
    plt.legend()
    plt.title("Perbedaan Skala Angka Pada Data Tumor")
    plt.savefig("Histogram-Pre-EDA.png", dpi=300)
    plt.close()

def getHeatmap():
    plt.figure(figsize=(10, 8))
    sns.heatmap(data_csv.iloc[:, :10].corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Heatmap Korelasi Data Tumor")
    plt.savefig("Heatmap-Pre-EDA.png")
    plt.close()

def getElbow():
    # Menyamakan semua skala angka AI bisa menghitung dengan adil
    data_csv_scaled = StandardScaler().fit_transform(data_csv)
    # Mencari jumlah Cluster yang pas pakai Elbow Method
    inertia = []
    for i in range(1,11):
        kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
        kmeans.fit(data_csv_scaled)
        inertia.append(kmeans.inertia_)

    plt.figure(figsize=(8,5))
    plt.plot(range(1,11), inertia, marker="o", linestyle="--", color="green")
    plt.title("Metode Elbow")
    plt.xlabel("Jumlah Kelompok (I)")
    plt.ylabel("Tingkat Error")
    plt.xticks(range(1,11))
    plt.grid(True)
    plt.savefig("Elbow-Post-EDA.png", dpi=300)
    plt.close()

def doClustering():
    print(Fore.BLUE + "[I] Memulai proses Clustering Final dengan K=2..." + Style.RESET_ALL)
    scaler = StandardScaler()
    data_csv_scaled = scaler.fit_transform(data_csv)
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    label_kelompok = kmeans.fit_predict(data_csv_scaled)
    data_csv["malignant"] = label_kelompok
    data_csv.to_csv("hasil_clustering.csv", index=False)
    print(Fore.BLUE + "[I] Total anggota masing-masing kelompok:" + Style.RESET_ALL)
    print(data_csv["malignant"].value_counts())

if __name__ == "__main__":
    getHistogram()
    getHeatmap()
    getElbow()
    doClustering()
