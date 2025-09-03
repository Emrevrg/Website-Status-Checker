# 🌐 Website Status Checker

Bu Python scripti, girilen web sitelerinin aktif olup olmadığını kontrol eder.  
Sitenin durumunu HTTP isteği göndererek test eder ve sonucu ekrana yazar.

## 🚀 Özellikler
- Bir veya birden fazla URL kontrol edilebilir
- HTTP durum kodunu gösterir
- Hızlı ve basit kullanım

## 🔧 Kurulum
1. Depoyu klonla:
   ```bash
   git clone https://github.com/kullaniciadi/website-status-checker.git
   cd website-status-checker
   ```

2. Gerekli paketleri yükle:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Kullanım
```bash
python status_checker.py https://google.com https://github.com
```

📌 Çıktı:
```
[+] https://google.com --> Çalışıyor (200)
[+] https://github.com --> Çalışıyor (200)
```

## 📄 Lisans
MIT License
