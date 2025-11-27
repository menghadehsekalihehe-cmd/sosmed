# Flask REST API - Dokumentasi Proyek

## Ikhtisar
Ini adalah aplikasi REST API lengkap yang dibangun dengan Flask, menggunakan ORM SQLAlchemy dan database MySQL/MariaDB. Proyek ini mengikuti pola arsitektur MVC (Model-View-Controller).

## Struktur Proyek
```
├── app/
│   ├── __init__.py           # Flask app factory
│   ├── models/
│   │   └── __init__.py       # Model basis data (ORM)
│   ├── controllers/
│   │   └── __init__.py       # Kontroler logika bisnis
│   └── views/
│       └── __init__.py       # Rute API dan blueprints
├── config/
│   └── config.py             # Pengaturan konfigurasi
├── venv/                      # Virtual environment
├── .env                       # Variabel lingkungan
├── run.py                     # Titik masuk aplikasi
├── init_db.py                # Skrip inisialisasi basis data
└── requirements.txt          # Dependensi Python
```

## Fitur

### Arsitektur
- **Pola MVC**: Pemisahan perhatian dengan Models, Controllers, dan Views
- **ORM (SQLAlchemy)**: Lapisan abstraksi basis data untuk MySQL/MariaDB
- **API RESTful**: Konvensi REST standar untuk semua endpoint
- **Blueprints**: Perutean terorganisir dengan blueprints Flask

### Tabel Basis Data (6 tabel)
1. **Users** - Akun pengguna dan autentikasi
2. **Posts** - Postingan blog/artikel
3. **Comments** - Komentar pada postingan
4. **Categories** - Kategori postingan
5. **Tags** - Tag postingan
6. **Likes** - Like postingan (tabel asosiasi)

### Endpoint API

#### Pengguna
- `POST /api/users` - Buat pengguna baru
- `GET /api/users` - Dapatkan semua pengguna (dipaginasi)
- `GET /api/users/<id>` - Dapatkan pengguna berdasarkan ID
- `PUT /api/users/<id>` - Perbarui pengguna
- `DELETE /api/users/<id>` - Hapus pengguna
- `POST /api/users/login` - Login pengguna

#### Postingan
- `POST /api/posts` - Buat postingan baru
- `GET /api/posts` - Dapatkan semua postingan (dipaginasi, difilter berdasarkan status)
- `GET /api/posts/<id>` - Dapatkan postingan berdasarkan ID
- `PUT /api/posts/<id>` - Perbarui postingan
- `DELETE /api/posts/<id>` - Hapus postingan

#### Komentar
- `POST /api/comments` - Buat komentar baru
- `GET /api/comments/<id>` - Dapatkan komentar berdasarkan ID
- `GET /api/comments/post/<post_id>` - Dapatkan komentar postingan
- `PUT /api/comments/<id>` - Perbarui komentar
- `DELETE /api/comments/<id>` - Hapus komentar

#### Kategori
- `POST /api/categories` - Buat kategori baru
- `GET /api/categories` - Dapatkan semua kategori
- `GET /api/categories/<id>` - Dapatkan kategori berdasarkan ID
- `PUT /api/categories/<id>` - Perbarui kategori
- `DELETE /api/categories/<id>` - Hapus kategori

#### Tag
- `POST /api/tags` - Buat tag baru
- `GET /api/tags` - Dapatkan semua tag
- `GET /api/tags/<id>` - Dapatkan tag berdasarkan ID
- `DELETE /api/tags/<id>` - Hapus tag

#### Like
- `POST /api/likes` - Like sebuah postingan
- `DELETE /api/likes` - Unlike sebuah postingan
- `GET /api/likes/post/<post_id>` - Dapatkan like postingan

#### Pemeriksaan Kesehatan
- `GET /api/health` - Status kesehatan API

## Instalasi & Setup

### 1. Buat Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # Di Windows: venv\Scripts\activate
```

### 2. Install Dependensi
```bash
pip install -r requirements.txt
```

### 3. Konfigurasi Basis Data
Edit file `.env` dengan kredensial MySQL/MariaDB Anda:
```
DATABASE_URL=mysql+pymysql://username:password@localhost:3306/database_name
```

### 4. Inisialisasi Basis Data
```bash
python init_db.py
```

Skrip ini akan:
- Membuat semua tabel basis data
- Menambahkan contoh pengguna, kategori, tag, postingan, komentar, dan like

### 5. Jalankan Aplikasi
```bash
python run.py
```

API akan tersedia di `http://localhost:5000`

## Contoh Penggunaan

### Buat Pengguna
```bash
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{
    "username": "newuser",
    "email": "user@example.com",
    "password": "secure_password",
    "full_name": "New User"
  }'
```

### Dapatkan Semua Pengguna
```bash
curl http://localhost:5000/api/users?page=1&per_page=10
```

### Buat Postingan
```bash
curl -X POST http://localhost:5000/api/posts \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My First Post",
    "content": "This is the content of my post",
    "user_id": 1,
    "category_id": 1,
    "status": "published"
  }'
```

### Like Postingan
```bash
curl -X POST http://localhost:5000/api/likes \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "post_id": 1
  }'
```

### Buat Komentar
```bash
curl -X POST http://localhost:5000/api/comments \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Great post!",
    "user_id": 2,
    "post_id": 1
  }'
```

## Model Basis Data

### Model Pengguna
- `id` (Integer, Primary Key)
- `username` (String, Unique)
- `email` (String, Unique)
- `password` (String, Hashed)
- `full_name` (String)
- `profile_picture` (String)
- `is_active` (Boolean)
- `created_at` (DateTime)
- `updated_at` (DateTime)

### Model Postingan
- `id` (Integer, Primary Key)
- `title` (String)
- `content` (Text)
- `user_id` (Foreign Key)
- `category_id` (Foreign Key)
- `status` (String: draft, published, archived)
- `views_count` (Integer)
- `created_at` (DateTime)
- `updated_at` (DateTime)
- `published_at` (DateTime)

### Model Komentar
- `id` (Integer, Primary Key)
- `content` (Text)
- `user_id` (Foreign Key)
- `post_id` (Foreign Key)
- `is_approved` (Boolean)
- `created_at` (DateTime)
- `updated_at` (DateTime)

### Model Kategori
- `id` (Integer, Primary Key)
- `name` (String, Unique)
- `description` (Text)
- `slug` (String, Unique)
- `created_at` (DateTime)
- `updated_at` (DateTime)

### Model Tag
- `id` (Integer, Primary Key)
- `name` (String, Unique)
- `slug` (String, Unique)
- `created_at` (DateTime)
- `updated_at` (DateTime)

### Model Like
- `id` (Integer, Primary Key)
- `user_id` (Foreign Key)
- `post_id` (Foreign Key)
- `created_at` (DateTime)
- Unique constraint on (user_id, post_id)

## Variabel Lingkungan
Konfigurasi ini di file `.env`:
- `FLASK_ENV` - Lingkungan (development/production)
- `FLASK_DEBUG` - Mode debug (True/False)
- `DATABASE_URL` - String koneksi MySQL
- `SECRET_KEY` - Kunci rahasia untuk sesi

## Kebutuhan
- Python 3.8+
- Flask 2.3.3
- Flask-SQLAlchemy 3.0.5
- PyMySQL 1.1.0
- python-dotenv 1.0.0
- cryptography 41.0.3
- PyJWT 2.8.1

## Fitur Utama

### 1. **Arsitektur MVC**
   - **Models**: Model basis data dengan relasi
   - **Controllers**: Logika bisnis dan pemrosesan data
   - **Views**: Endpoint API dan perutean

### 2. **ORM (SQLAlchemy)**
   - Pembuatan SQL otomatis
   - Keamanan tipe dan validasi
   - Manajemen relasi
   - Optimasi kueri

### 3. **Basis Data**
   - Dukungan MySQL/MariaDB
   - 6 tabel yang saling terhubung
   - Foreign key dan constraint
   - Kolom terindeks untuk performa

### 4. **Keamanan**
   - Password hashing dengan werkzeug
   - Autentikasi pengguna
   - Validasi data

### 5. **Fitur API**
   - Dukungan paginasi
   - Respon JSON
   - Penanganan kesalahan
   - Endpoint pemeriksaan kesehatan

## Penanganan Kesalahan
API mengembalikan kode status HTTP yang sesuai:
- `200` - OK
- `201` - Created
- `400` - Bad Request
- `401` - Unauthorized
- `403` - Forbidden
- `404` - Not Found
- `500` - Internal Server Error

## Perintah Development

### Buat Database
```bash
python init_db.py
```

### Flask Shell
```bash
export FLASK_APP=run.py
flask shell
```