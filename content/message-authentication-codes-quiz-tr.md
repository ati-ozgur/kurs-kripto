## Quiz

** Soru 1**

Mesaj Kimlik Doğrulama Kodları (MAC) kullanımı ile ilgili olarak, bir MAC algoritmasının sunduğu temel güvenlik garantileri aşağıdakilerden hangisidir?

A. Yalnızca iletim sırasında oluşabilecek kaza sonucu gürültü hatalarını tespit eder, kötü niyetli müdahalelere karşı koruma sağlamaz.

B. Mesajın boyutunu sıkıştırarak ağ üzerinde daha hızlı iletilmesini sağlar ve gizlilik sunar.

C. Mesajın yolda bozulmadığını (bütünsellik) ve kaynağının doğruluğunu (kimlik doğrulama) garanti eder.

D. Mesajın içeriğinin üçüncü şahıslar tarafından okunmasını (gizlilik) ve gönderenin bunu inkar edememesini garanti eder.

** Soru 2**

Standart bir kriptografik hash fonksiyonu (ör. SHA-256) ile MAC/HMAC arasındaki en temel fark aşağıdakilerden hangisidir?

A.
Hash fonksiyonu yalnızca mesajı girdi olarak alırken, MAC girdisine paylaşılan bir gizli anahtar dahil eder.

B.
Hash fonksiyonları kötü niyetli saldırıları engellerken, MAC sadece kaza sonucu oluşan bozulmaları yakalar.

C.
Hash fonksiyonları yalnızca blok şifreleyicilerle çalışırken, MAC yapısı sadece akış şifreleyicileriyle çalışır.

D.
Hash fonksiyonları değişken uzunlukta çıktı üretirken, MAC her zaman sabit 32-bit çıktı üretir.

** Soru 3**

NIST tarafından resmi olarak onaylanmış genel amaçlı (Approved) MAC algoritmaları arasında aşağıdakilerden hangileri yer almaktadır?

A. CRC32, MD5 ve DES

B. HMAC, KMAC ve CMAC

C. ECC, Diffie-Hellman ve DSA

D. SHA-256, AES ve RSA


** Soru 4**

Cipher-based MAC (CMAC) algoritmasının temel yapısal özelliği hakkında aşağıda verilen ifadelerden hangisi doğrudur?

A.
Yalnızca mesaj uzunluğu blok boyutunun tam katı olduğunda çalışabilir ve dolgu (padding) mekanizmasını desteklemez.
CMAC, mesaj uzunluğu blok boyutunun katı olmadığında alt anahtar türetimi ve dolgu mekanizmalarıyla esnek mesaj uzunluklarını destekler.

B.
İki aşamalı iç/dış dolgulama (inner/outer padding) yapısına sahip hash tabanlı bir algoritmadır.
İki aşamalı iç/dış dolgulama yapısı CMAC'e değil, HMAC algoritmasına ait bir özelliktir.

C.
Hash fonksiyonları yerine AES gibi onaylı bir blok şifreleme algoritmasını kullanarak MAC etiketleri üretir.

D.
Özetleme adımlarında yalnızca MD5 ve SHA-1 hash algoritmalarının kombinasyonunu kullanır.
CMAC hash fonksiyonlarını değil, simetrik blok şifreleme algoritmalarını kullanır.

** Soru 5**

HMAC (Hash-based MAC) yapısının teknik özellikleri ile ilgili aşağıdakilerden hangisi doğrudur?

A. Bir özetleme algoritması (SHA-256 vb.) ile gizli bir anahtarın özel yapılandırılmış iki aşamalı (inner/outer padding) kombinasyonudur.

B. Mesaj bütünlüğünü korumak için simetrik şifreleme yerine asimetrik (açık anahtarlı) kriptografi prensiplerini uygular.

C. Gizli anahtar kullanmadan doğrudan mesajın çift katlı hash değerini alarak doğrulama etiketi oluşturur.

D. Yalnızca TLS/SSL protokollerinde kullanılabilir, IPsec veya OAuth gibi diğer sistemlerde desteklenmez.

** Soru 6**

Aşağıdakilerden hangisi bir MAC sisteminin kullanımından kaynaklanan temel sınırlamalardan (limitations) biridir?

A.
Her zaman mesajın tamamını şifreleyerek yüksek işlemci yükü oluşturması.

B.
Taraflar arasında güvenli bir anahtar paylaşım ve yönetim mekanizmasına gereksinim duyması.

C.
Açık anahtarlı dijital imzalara kıyasla hesaplama hızının çok daha yavaş olması.

D.
Kaza sonucu oluşan iletim hatalarını tespit edememesi.

** Soru 7**

Ağ güvenliği protokollerinde mesajların hem gizliliğini hem de bütünlük ve kaynağını aynı anda korumak amacıyla kullanılan genel kriptografik yaklaşım aşağıdakilerden hangisidir?

A.
Yalnızca CRC32 gibi anahtarsız hata denetim kodlarının kullanılması.
CRC32 anahtarsız bir yapı olduğu için kötü niyetli değişikliklere veya gizlilik ihlallerine karşı koruma sağlayamaz.

B.
Mesajın hiçbir şifreleme yapılmadan sadece düz metin ve anahtarsız SHA-256 hash'i ile gönderilmesi.
Anahtarsız hash değerleri ortadaki adam (MitM) tarafından mesajla birlikte kolayca değiştirilebildiği için ne gizlilik ne de kimlik doğrulaması sağlar.

C.
Her ağ paketi için yeni bir asimetrik anahtar çifti oluşturularak doğrudan RSA ile şifreleme yapılması.
Her paket için asimetrik şifreleme kullanmak aşırı yüksek işlem yükü oluşturduğu için pratik değildir.

D.
CPA-güvenli bir şifreleyici ile güvenli bir MAC yapısını birleştiren Kimlik Doğrulamalı Şifreleme (Authenticated Encryption / örn. Encrypt-then-MAC veya GCM).



### Quiz Cevaplar

1. C
2. A
3. B
4. C
5. A
6. B
7. D