Süper 👍 O zaman **lisans kısmını çıkarıp** sana güncel README.md veriyorum:

---

```markdown
# ⚡ Energy Prediction API

Bu proje, **FastAPI** tabanlı bir REST API uygulamasıdır.  
Kullanıcı kimlik doğrulama, enerji verilerinin yönetimi ve tahmin servisleri sunar.  

## 🚀 Özellikler
- JWT tabanlı kimlik doğrulama
- Kullanıcı kaydı ve oturum açma
- Enerji verilerinin kaydı ve yönetimi
- Tahmin servisi (ML modeli veya iş mantığı ile)

## 🛠️ Kullanılan Teknolojiler
- [Python 3.11+](https://www.python.org/)  
- [FastAPI](https://fastapi.tiangolo.com/)  
- [Pydantic](https://docs.pydantic.dev/)  
- [SQLAlchemy](https://www.sqlalchemy.org/)  
- [JWT (JSON Web Tokens)](https://jwt.io/)  

## 📂 Proje Yapısı
```

app/
├── main.py          # Uygulama giriş noktası
├── database.py      # Veritabanı bağlantısı
├── security.py      # Kimlik doğrulama & JWT
├── routes/          # API endpointleri (auth, data, predict)
├── models/          # SQLAlchemy modelleri
├── schemas/         # Pydantic şemaları
└── services/        # İş mantığı katmanı

````

## ⚙️ Kurulum

1. Depoyu klonla:
   ```bash
   git clone https://github.com/<kullanici-adi>/<repo-adi>.git
   cd <repo-adi>
````

2. Sanal ortam oluştur ve etkinleştir:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / Mac
   venv\Scripts\activate      # Windows
   ```

3. Bağımlılıkları yükle:

   ```bash
   pip install -r requirements.txt
   ```

4. Uygulamayı başlat:

   ```bash
   uvicorn app.main:app --reload
   ```

## ▶️ Kullanım

* Sunucu çalıştıktan sonra API dokümantasyonuna göz atabilirsin:

  * Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
  * ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Örnek endpointler:

* `POST /auth/register` → Yeni kullanıcı oluştur
* `POST /auth/login` → JWT token al
* `GET /data/` → Enerji verilerini listele
* `POST /predict/` → Tahmin sonucu al

```
