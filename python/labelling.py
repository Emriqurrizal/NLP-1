import pandas as pd

# Load dataset
df = pd.read_csv('csv/stockbit_preprocessing_id.csv')

# Ambil 100 baris pertama untuk sentimen positif
df_positif = df[df['sentiment'] == 'positif'].head(100)

# Ambil 100 baris pertama untuk sentimen negatif
df_negatif = df[df['sentiment'] == 'negatif'].head(100)

# Gabungkan keduanya
df_hasil = pd.concat([df_positif, df_negatif], ignore_index=True)

# Simpan ke file baru
df_hasil.to_csv('csv/stockbit_sampled_200.csv', index=False)