import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv("tumor-data.csv")

def getDataInformation():
    """
    Fungsi ini berguna untuk mem-print berbagai macam informasi soal data yang dimiliki ke terminal
    """
    print("="*25)
    print("OUTPUT INFO() FILE CSV")
    print("="*25)
    print(df.info())
    print("="*25)
    print("OUTPUT DESCRIBE() FILE CSV")
    print("="*25)
    print(df.describe())

def getGraphBeforePreProcessing():
    print("[I] Memulai pembuatan grafik sebelum preprocessing...")

    # Membuat grafik histogram
    plt.figure(figsize=(8,5))
    sns.histplot(df["mean area"], color="red", alpha=0.5, label="Mean Area")
    sns.histplot(df["mean smoothness"], color="blue", alpha=0.5, label="Mean Smoothness")
    sns.histplot(df["mean radius"], color="green", alpha=0.5, label="Mean Radius")
    plt.legend()
    plt.title("Perbedaan Skala Angka Pada Data Tumor")
    plt.savefig("Histogram-Pre-EDA.png", dpi=300)
    plt.close()

    # Membuat grafik heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.iloc[:, :10].corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Heatmap Korelasi 10 Fitur Pertama Data Tumor")
    plt.savefig("Heatmap-Pre-EDA.png", dpi=300)
    plt.close()

    # Membuat grafik boxplot
    plt.figure(figsize=(10, 6))
    # 4 fitur ini dipilih biar buuktikan rentang angka yang berbeda dan mendeteksi outlier
    sns.boxplot(data=df[["mean radius", "mean texture", "mean perimeter", "mean area"]])
    plt.title("Boxplot Deteksi Outlier (Sebelum Preprocessing)")
    plt.savefig("Boxplot-Pre-EDA.png", dpi=300)
    plt.close()

    # Bikin grafik scatter plot
    plt.figure(figsize=(8, 5))
    # Cek apakah ada tanda-tanda pengelompokan dari perbandingan jari-jari dan tekstur
    sns.scatterplot(x=df["mean radius"], y=df["mean texture"], color="purple", alpha=0.7)
    plt.title("Persebaran Data: Mean Radius vs Mean Texture")
    plt.savefig("Scatter-Pre-EDA.png", dpi=300)
    plt.close()

    print("[I] Semua grafik Pre-EDA berhasil disimpan!")

def getGraphAfterPreProcessing():
    print("[I] Memulai pembuatan grafik SESUDAH preprocessing (Data Scaled)...")

    # =======================
    # PERBAIKAN DARI GEMINI: Kembalikan hasil Numpy Array ke bentuk Pandas DataFrame
    array_scaled = StandardScaler().fit_transform(df)
    df_scaled = pd.DataFrame(array_scaled, columns=df.columns)
    # =======================

    # Buat grafik histogram
    plt.figure(figsize=(8,5))
    sns.histplot(df_scaled["mean area"], color="red", alpha=0.5, label="Mean Area")
    sns.histplot(df_scaled["mean smoothness"], color="blue", alpha=0.5, label="Mean Smoothness")
    sns.histplot(df_scaled["mean radius"], color="green", alpha=0.5, label="Mean Radius")
    plt.legend()
    plt.title("Distribusi Skala Data Tumor (Sesudah StandardScaler)")
    plt.savefig("Histogram-Post-EDA.png", dpi=300)
    plt.close()

    # Buat grafik boxplot
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df_scaled[["mean radius", "mean texture", "mean perimeter", "mean area"]])
    plt.title("Boxplot Deteksi Outlier (Sesudah StandardScaler)")
    plt.savefig("Boxplot-Post-EDA.png", dpi=300)
    plt.close()

    print("[I] Grafik Post-EDA berhasil disimpan!")

def elbowMethod():
    df_scaled = StandardScaler().fit_transform(df)
    inertia = []
    for i in range(1,11):
        kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
        kmeans.fit(df_scaled)
        inertia.append(kmeans.inertia_)

    plt.figure(figsize=(8,5))
    plt.plot(range(1,11), inertia, marker="o", linestyle="--", color="green")
    plt.title("Metode Elbow")
    plt.xlabel("Group Counts(I)")
    plt.ylabel("Error Level")
    plt.xticks(range(1,11))
    plt.grid(True)
    plt.savefig("Elbow-Post-EDA.png", dpi=300)
    plt.close()

def finalClustering():
    print("[I] Memulai proses Clustering Final dengan K=2...")
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    group_label = kmeans.fit_predict(df_scaled)
    df["malignant"] = group_label
    df.to_csv("clustered.csv", index=False)
    print("[I] Total anggota masing-masing kelompok:\n", df["malignant"].value_counts())

def clusterProfile():
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)
    kmeans = KMeans(n_clusters=2, random_state=42)
    clusters = kmeans.fit_predict(df_scaled)
    df['cluster'] = clusters
    print(df.head())
    print("="*25)
    df.to_csv('clustered.csv', index=False)
    print("[I] Berhasil menyimpan data beserta clusternya ke 'clustered.csv'")
    print("="*25)
    print("[I] Profil karakteristik dari masing-masing cluster (rata-rata):")
    cluster_profile = df.groupby('cluster').mean()
    print(cluster_profile)

if __name__ == "__main__":
    getDataInformation()
    getGraphBeforePreProcessing()
    getGraphAfterPreProcessing()
    elbowMethod()
    finalClustering()
    clusterProfile()
