import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt


fungsi_integrasi = lambda x: x**2 * np.cos(x) + 3 * np.sin(2 * x)


x_awal = 0
x_akhir = np.pi


nilai_integral, _ = integrate.quad(fungsi_integrasi, x_awal, x_akhir)
print("Nilai Integral:", nilai_integral)


x_values = np.linspace(x_awal, x_akhir, 1000)
y_values = x_values**2 * np.cos(x_values) + 3 * np.sin(2 * x_values)


plt.plot(x_values, y_values, label=r'$f(x) = x^2 \cos(x) + 3 \sin(2x)$', color='skyblue')
plt.fill_between(x_values, y_values, where=(y_values > 0), color='skyblue', alpha=0.3)


plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(r'Grafik Fungsi $f(x) = x^2 \cos(x) + 3 \sin(2x)$ dan Area di Bawah Kurva')
plt.legend()

plt.show()
