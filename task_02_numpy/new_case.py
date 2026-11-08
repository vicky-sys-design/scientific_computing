import numpy as np

t = np.array([16.0,15.5,15.2,15.0,15.4,17.0,20.5,24.0,27.5,30.2,32.8,34.5,
              35.6,35.1,33.9,31.4,28.7,25.6,23.0,21.0,19.5,18.4,17.4,16.7])

print(f"Mean: {t.mean():.2f} C, Min: {t.min():.1f} C, Max: {t.max():.1f} C")
print("Hours above 30 C:", int(np.sum(t > 30)))
print("Hours below 18 C:", int(np.sum(t < 18)))
print("Max in F:", round(1.8*t.max()+32, 1))