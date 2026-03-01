# ================================================================
#  AKILLI KABLO YANGIN RİSKİ TESPİT SİSTEMİ
#  Python Termal + Harmonik + Risk Simülasyonu
# ================================================================

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ------------------------------------------------
# Zaman ekseni
# ------------------------------------------------
t = np.linspace(0, 10, 2000)

# ------------------------------------------------
# Kablo kesitine göre izin verilen maksimum akımlar (A)
# ------------------------------------------------
cable_table = {
    1.5: 10,
    2.5: 16,
    4: 25,
    6: 32,
    10: 40
}

def get_max_current(cross_section):
    return cable_table.get(cross_section, 16)


# ------------------------------------------------
# Risk seviyesi mesajı
# ------------------------------------------------
def risk_message(value):
    if value < 0.30:
        return "GÜVENLİ ÇALIŞMA"
    elif value < 0.60:
        return "DİKKAT: Risk Artıyor"
    else:
        return "ALARM: YÜKSEK YANGIN RİSKİ!"


# ------------------------------------------------
# Senaryo raporu
# ------------------------------------------------
def system_report(name, current, temp, risk):
    print(f"\n=== {name} ===")
    print(f"RMS Akım: {np.sqrt(np.mean(current**2)):.2f} A")
    print(f"Maksimum Akım: {np.max(np.abs(current)):.2f} A")
    print(f"Ortalama Sıcaklık: {np.mean(temp):.2f} °C")
    print(f"Son Sıcaklık: {temp[-1]:.2f} °C")
    print(f"Ortalama Risk Skoru: {np.mean(risk):.3f}")
    print("Durum:", risk_message(np.mean(risk)))


# ------------------------------------------------
# ANA SİMÜLASYON FONKSİYONU
# ------------------------------------------------
def simulate(thd_level, load_level, cross_section, length):

    max_current = get_max_current(cross_section)

    # Akım sinyali (temel + harmonik)
    fundamental = 5 * load_level * np.sin(2*np.pi*50*t)
    harmonic = thd_level * np.sin(2*np.pi*150*t)
    current = fundamental + harmonic

    # Bakır kablo direnci (Ω)
    rho = 0.0175
    R = rho * length / cross_section

    # Joule kaybı
    power_loss = (current**2) * R

    # ---------------- TERMAL MODEL ----------------
    temperature = np.zeros(len(t))
    temperature[0] = 25

    heating_coeff = 0.025
    cooling_coeff = 0.008

    for i in range(1, len(t)):
        temperature[i] = temperature[i-1] + \
                         heating_coeff * power_loss[i] - \
                         cooling_coeff * (temperature[i-1] - 25)

    temperature += np.random.normal(0, 0.4, len(t))

    # ---------------- RİSK HESABI ----------------
    overload_ratio = np.maximum(0, np.abs(current) - max_current) / max_current

    risk = 0.5 * (np.abs(current) / max_current) + \
           0.3 * thd_level + \
           0.4 * (temperature / 80) + \
           0.6 * overload_ratio

    risk = np.clip(risk, 0, 1)

    return current, temperature, risk


# =================================================
# SİSTEM PARAMETRELERİ
# =================================================
cross_section = 2.5
length = 20


# =================================================
# SENARYOLAR
# =================================================
i1, t1, r1 = simulate(0.10, 1.0, cross_section, length)
i2, t2, r2 = simulate(0.40, 1.8, cross_section, length)
i3, t3, r3 = simulate(0.80, 3.2, cross_section, length)


# =================================================
# RAPOR
# =================================================
system_report("NORMAL YÜK", i1, t1, r1)
system_report("HARMONİKLİ YÜK", i2, t2, r2)
system_report("AŞIRI YÜK", i3, t3, r3)


# =================================================
# GRAFİKLER
# =================================================
plt.figure()
plt.plot(t, t1, label="Normal")
plt.plot(t, t2, label="Harmonikli")
plt.plot(t, t3, label="Aşırı")
plt.title("Kablo Sıcaklık Değişimi")
plt.xlabel("Zaman (s)")
plt.ylabel("Sıcaklık (°C)")
plt.legend()
plt.show()

plt.figure()
plt.plot(r1, label="Normal")
plt.plot(r2, label="Harmonikli")
plt.plot(r3, label="Aşırı")
plt.title("Yangın Risk Skoru")
plt.xlabel("Örnek")
plt.ylabel("Risk")
plt.legend()
plt.show()


# =================================================
# MATLAB için CSV çıktı
# =================================================
df = pd.DataFrame({
    'Zaman': t,
    'Akim': i3,
    'Sicaklik': t3,
    'Risk': r3
})

df.to_csv('proje_verileri.csv', index=False)
print("Veriler MATLAB için hazır!")
