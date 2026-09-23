# Tumor Data Clustering Analysis

[ English Version ](#english) | [ Versi Bahasa Indonesia ](#bahasa-indonesia)

---

<a name="english"></a>
## English

### Project Overview
An Unsupervised Machine Learning project to analyze and cluster breast cancer tumor morphology data. The project standardizes high-dimensional cell features using StandardScaler, optimizes cluster count via the Elbow Method, and executes K-Means clustering to distinguish underlying tumor groupings.

### Team Members (Group 2)
- Azis Al Risal
- Bagas Dwi Saputra
- Desta Ega Fatima
- Jonathan Steve Roland
- Nayla Khairusyi Shabrina

### Dataset & Methodology
- **Dataset**: `tumor-data.csv` (569 records, 30 continuous features capturing nuclear characteristics from FNA biopsies).
- **Target Analysis**: Unsupervised partitioning into natural diagnostic groups (benign vs. malignant indications).
- **Pipeline**:
  1. **Pre-EDA**: Feature scale inspection, 10-feature correlation heatmap, outlier detection boxplots, and scatter distribution plots.
  2. **Preprocessing**: Feature scaling using `StandardScaler` to ensure uniform scale contribution across all 30 features.
  3. **Hyperparameter Tuning**: Inertia evaluation across $K=1$ to $K=10$ using the Elbow Method (`Elbow-Post-EDA.png`).
  4. **Clustering & Profiling**: K-Means clustering ($K=2$), export of cluster assignments to `clustered.csv`, and feature mean profiling across clusters.

### Results
- The Elbow Method clearly identified an optimal inflection point at $K=2$.
- The two resulting clusters align with distinct morphological profiles: one cluster exhibits substantially higher values for radius, perimeter, area, and concavity (indicative of malignant characteristics), while the other displays smaller, more uniform cell parameters (indicative of benign characteristics).
- Outputs are saved to `clustered.csv` and visualization charts are generated in the project root.

### Project Structure
```text
├── INSTRUCTION.md          # Assignment instructions and requirements
├── main.ipynb              # Interactive analysis notebook (EDA, scaling, clustering)
├── main.py                 # Main execution script (EDA, scaling, clustering, profiling)
├── requirements.txt        # Python dependencies
├── tumor-data.csv          # Breast cancer tumor dataset
└── README.md               # Project documentation
```

### Setup & Local Execution

1. **Clone the repository:**
   ```bash
   git clone https://github.com/josterand/ml-tumor-analysis.git
   cd ml-tumor-analysis
   ```

2. **Create and activate a virtual environment:**
   - Linux / macOS:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - Windows:
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the project:**
   - Run Python script:
     ```bash
     python main.py
     ```
   - Or open Jupyter Notebook:
     ```bash
     jupyter notebook main.ipynb
     ```

---

<a name="bahasa-indonesia"></a>
## Bahasa Indonesia

### Gambaran Proyek
Proyek Machine Learning (Unsupervised Learning) untuk menganalisis dan mengelompokkan data morfologi tumor payudara. Proyek ini melakukan standarisasi data berdimensi tinggi menggunakan StandardScaler, mencari jumlah kluster optimal dengan Metode Elbow, dan mengelompokkan data menggunakan K-Means Clustering.

### Anggota Kelompok (Kelompok 2)
- Azis Al Risal
- Bagas Dwi Saputra
- Desta Ega Fatima
- Jonathan Steve Roland
- Nayla Khairusyi Shabrina

### Dataset & Metodologi
- **Dataset**: `tumor-data.csv` (569 baris data, 30 fitur kontinu karakteristik inti sel hasil biopsi FNA).
- **Tujuan Analisis**: Pengelompokan data tanpa label ke dalam pola kluster alami (indikasi jinak / ganas).
- **Alur Kerja**:
  1. **Pre-EDA**: Analisis disparitas skala fitur, heatmap matriks korelasi 10 fitur pertama, boxplot outlier, dan scatter plot persebaran data.
  2. **Preprocessing**: Standarisasi seluruh fitur menggunakan `StandardScaler` agar tiap fitur memiliki bobot seimbang.
  3. **Tuning Hyperparameter**: Evaluasi nilai inertia untuk $K=1$ hingga $K=10$ menggunakan Metode Elbow (`Elbow-Post-EDA.png`).
  4. **Clustering & Profiling**: Pemodelan final K-Means dengan $K=2$, ekspor data berlabel ke `clustered.csv`, dan profiling karakteristik rata-rata fitur pada tiap kluster.

### Hasil Analisis
- Metode Elbow menunjukkan titik siku optimal pada $K=2$.
- Kluster yang terbentuk berhasil memisahkan dua profil morfologi yang kontras: kluster dengan nilai rata-rata radius, perimeter, luas, dan konkavitas yang lebih tinggi (mengindikasikan sifat tumor ganas / *malignant*), serta kluster dengan nilai yang lebih kecil dan stabil (mengindikasikan sifat tumor jinak / *benign*).
- Hasil kluster disimpan ke dalam berkas `clustered.csv` serta grafik visualisasi disimpan di direktori proyek.

### Struktur Berkas
```text
├── INSTRUCTION.md          # Petunjuk dan spesifikasi pengerjaan tugas
├── main.ipynb              # Notebook analisis interaktif (EDA, standarisasi, klusterisasi)
├── main.py                 # Skrip utama (EDA, standarisasi, klusterisasi, profiling)
├── requirements.txt        # Daftar dependensi modul Python
├── tumor-data.csv          # Dataset karakteristik tumor payudara
└── README.md               # Dokumentasi lengkap proyek
```

### Panduan Instalasi & Menjalankan Lokal

1. **Klon repositori:**
   ```bash
   git clone https://github.com/josterand/ml-tumor-analysis.git
   cd ml-tumor-analysis
   ```

2. **Buat dan aktifkan virtual environment:**
   - Linux / macOS:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - Windows:
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\activate
     ```

3. **Pasang dependensi:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan program:**
   - Melalui skrip Python:
     ```bash
     python main.py
     ```
   - Melalui Jupyter Notebook:
     ```bash
     jupyter notebook main.ipynb
     ```
