import pandas as pd
import matplotlib.pyplot as plt

# Antalya'nın 2023 yılı aylık yağış verileri (örnek)
data = {
    "Ay": ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"],
    "Yağış (mm)": [150, 130, 120, 80, 40, 20, 10, 5, 30, 70, 110, 140]  # Aylık yağış miktarları
}

# Veriyi DataFrame'e dönüştürme
df = pd.DataFrame(data)

# Grafik oluşturma
plt.figure(figsize=(10, 6))
plt.plot(df["Ay"], df["Yağış (mm)"], marker='o', color='b', linestyle='-', linewidth=2, markersize=6)

# Grafik başlık ve etiketler
plt.title("2023 Yılı Antalya Aylık Yağış Miktarı", fontsize=14)
plt.xlabel("Aylar", fontsize=12)
plt.ylabel("Yağış (mm)", fontsize=12)

# Grafik gösterme
plt.xticks(rotation=45)  # Ay isimlerini daha rahat okuyabilmek için döndürme
plt.grid(True)
plt.tight_layout()  # Düzenleme
plt.show()
