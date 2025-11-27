# Panduan Testing REST API

## Testing API dengan curl

### 1. Health Check
```bash
curl http://localhost:5000/api/health
```

### 2. Manajemen User

#### Buat User
```bash
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "password123",
    "full_name": "Test User"
  }'
```

#### Login
```bash
curl -X POST http://localhost:5000/api/users/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john",
    "password": "password123"
  }'
```

#### Dapatkan Semua User
```bash
curl http://localhost:5000/api/users?page=1&per_page=10
```

#### Dapatkan User Berdasarkan ID
```bash
curl http://localhost:5000/api/users/1
```

#### Update User
```bash
curl -X PUT http://localhost:5000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{
    "full_name": "Updated Name",
    "email": "newemail@example.com"
  }'
```

#### Hapus User
```bash
curl -X DELETE http://localhost:5000/api/users/1
```

### 3. Manajemen Posts

#### Buat Post
```bash
curl -X POST http://localhost:5000/api/posts \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My First Post",
    "content": "This is amazing content",
    "user_id": 1,
    "category_id": 1,
    "status": "published"
  }'
```

#### Dapatkan Semua Posts
```bash
curl http://localhost:5000/api/posts?page=1&per_page=10&status=published
```

#### Dapatkan Post Berdasarkan ID
```bash
curl http://localhost:5000/api/posts/1
```

#### Update Post
```bash
curl -X PUT http://localhost:5000/api/posts/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated Title",
    "content": "Updated content",
    "user_id": 1
  }'
```

#### Hapus Post
```bash
curl -X DELETE http://localhost:5000/api/posts/1 \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1
  }'
```

### 4. Manajemen Komentar

#### Buat Komentar
```bash
curl -X POST http://localhost:5000/api/comments \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Great post!",
    "user_id": 2,
    "post_id": 1
  }'
```

#### Dapatkan Komentar Post
```bash
curl http://localhost:5000/api/comments/post/1?page=1&per_page=10
```

#### Dapatkan Komentar Berdasarkan ID
```bash
curl http://localhost:5000/api/comments/1
```

#### Update Komentar
```bash
curl -X PUT http://localhost:5000/api/comments/1 \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Updated comment",
    "user_id": 2
  }'
```

#### Hapus Komentar
```bash
curl -X DELETE http://localhost:5000/api/comments/1 \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 2
  }'
```

### 5. Manajemen Kategori

#### Buat Kategori
```bash
curl -X POST http://localhost:5000/api/categories \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Programming",
    "slug": "programming",
    "description": "Programming related posts"
  }'
```

#### Dapatkan Semua Kategori
```bash
curl http://localhost:5000/api/categories
```

#### Dapatkan Kategori Berdasarkan ID
```bash
curl http://localhost:5000/api/categories/1
```

#### Update Kategori
```bash
curl -X PUT http://localhost:5000/api/categories/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Web Development",
    "description": "Web development posts"
  }'
```

#### Hapus Kategori
```bash
curl -X DELETE http://localhost:5000/api/categories/1
```

### 6. Manajemen Tags

#### Buat Tag
```bash
curl -X POST http://localhost:5000/api/tags \
  -H "Content-Type: application/json" \
  -d '{
    "name": "JavaScript",
    "slug": "javascript"
  }'
```

#### Dapatkan Semua Tags
```bash
curl http://localhost:5000/api/tags
```

#### Dapatkan Tag Berdasarkan ID
```bash
curl http://localhost:5000/api/tags/1
```

#### Hapus Tag
```bash
curl -X DELETE http://localhost:5000/api/tags/1
```

### 7. Manajemen Likes

#### Like Post
```bash
curl -X POST http://localhost:5000/api/likes \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "post_id": 1
  }'
```

#### Unlike Post
```bash
curl -X DELETE http://localhost:5000/api/likes \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "post_id": 1
  }'
```

#### Dapatkan Likes Post
```bash
curl http://localhost:5000/api/likes/post/1?page=1&per_page=10
```

## Contoh Response API

### Response Sukses (200/201)
```json
{
  "id": 1,
  "username": "john",
  "email": "john@example.com",
  "full_name": "John Doe",
  "is_active": true,
  "created_at": "2024-11-27T10:00:00",
  "updated_at": "2024-11-27T10:00:00"
}
```

### Response Error (400/404/500)
```json
{
  "error": "Kolom yang diperlukan tidak ada"
}
```

## Checklist Testing

- [ ] Endpoint health check
- [ ] Buat user
- [ ] Login user
- [ ] Dapatkan semua user (dengan pagination)
- [ ] Dapatkan user berdasarkan ID
- [ ] Update user
- [ ] Hapus user
- [ ] Buat post
- [ ] Dapatkan semua posts
- [ ] Dapatkan post berdasarkan ID
- [ ] Update post
- [ ] Hapus post
- [ ] Buat kategori
- [ ] Dapatkan semua kategori
- [ ] Buat tag
- [ ] Dapatkan semua tags
- [ ] Buat komentar
- [ ] Dapatkan komentar post
- [ ] Update komentar
- [ ] Hapus komentar
- [ ] Like post
- [ ] Unlike post
- [ ] Dapatkan likes post

## Verifikasi Database

### Perintah MySQL/MariaDB
```bash
# Terhubung ke database
mysql -u username -p database_name

# Tampilkan tabel
SHOW TABLES;

# Tampilkan struktur tabel
DESCRIBE users;
DESCRIBE posts;
DESCRIBE comments;
DESCRIBE categories;
DESCRIBE tags;
DESCRIBE likes;
DESCRIBE post_tags;

# Lihat data
SELECT * FROM users;
SELECT * FROM posts;
SELECT * FROM comments;
```
