
| Özellik | Standart Hash Fonksiyonu (örn. SHA-256) | MAC / HMAC |
| --- | --- | --- |
| **Girdi** | Yalnızca Mesaj | Mesaj + **Gizli Anahtar** |
| **Bütünlük (Integrity)** | Var (kaza sonucu veri bozulmalarını yakalar) | Var (kötü niyetli değişiklikleri yakalar) |
| **Kimlik Doğrulama (Authenticity)** | **Yok** | **Var** |
| **Saldırıya Karşı Koruma** | Saldırgan yeni hash hesaplayabilir | Anahtarsız geçerli bir etiket üretilemez |
