from datetime import datetime

daftar_harga = [
    ("Laptop ASUS", 15000000),
    ("Smartphone Samsung", 8500000),
    ("Headphone Sony", 2500000),
    ("Keyboard Mechanical", 1200000),
    ("Mouse Gaming", 750000),
    ("Monitor LG 24 inci", 3200000),
    ("SSD 1TB", 1800000),
    ("RAM 16GB", 1400000),
    ("Printer Canon", 2200000),
    ("Kamera Mirrorless", 9500000),
    ("Smartwatch Apple", 6000000),
    ("Tablet Lenovo", 5000000),
    ("Harddisk Eksternal 2TB", 2100000),
    ("Power Bank 20000mAh", 550000),
    ("Laptop HP", 13500000),
    ("Speaker Bluetooth JBL", 1800000),
    ("Smartphone iPhone", 14000000),
    ("Router WiFi 6", 2000000),
    ("Keyboard Wireless", 900000),
    ("Webcam HD", 1300000)
]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x[1] < pivot[1]]
    middle = [x for x in arr if x[1] == pivot[1]]
    right = [x for x in arr if x[1] > pivot[1]]
    return quick_sort(left) + middle + quick_sort(right)

print("Daftar harga sebelum diurutkan:")
for barang, harga in daftar_harga:
    print(f"{barang} - Rp{harga:,}")

sorted_harga = quick_sort(daftar_harga)

print("\nDaftar harga setelah diurutkan:")
for barang, harga in sorted_harga:
    print(f"{barang} - Rp{harga:,}")
