import secrets

def metni_bitlere_cevir(metin: str) -> str:
    """Metindeki her karakteri 8 bitlik (ASCII/UTF-8) binary dizisine dönüştürür."""
    return ''.join(f"{ord(c):08b}" for c in metin)

def bitleri_metne_cevir(bit_dizisi: str) -> str:
    """8'er bitlik parçaları tekrar karakterlere dönüştürür."""
    karakterler = [bit_dizisi[i:i+8] for i in range(0, len(bit_dizisi), 8)]
    return ''.join(chr(int(b, 2)) for b in karakterler)

def rastgele_anahtar_uret(bit_uzunlugu: int) -> str:
    """Kriptografik olarak güvenli 'True Random' bit dizisi üretir."""
    return ''.join(str(secrets.randbelow(2)) for _ in range(bit_uzunlugu))

def vernam_xor(veri_bitleri: str, anahtar_bitleri: str) -> str:
    """Iki bit dizisini XOR (Özel Veya) işlemine tabi tutar."""
    if len(veri_bitleri) != len(anahtar_bitleri):
        raise ValueError("Mesaj ve anahtar uzunluğu eşit olmalıdır!")
    
    # XOR Islemi: '1' ^ '1' -> '0', '0' ^ '0' -> '0', '1' ^ '0' -> '1'
    return ''.join(str(int(b1) ^ int(b2)) for b1, b2 in zip(veri_bitleri, anahtar_bitleri))


# --- UYGULAMA ORNEGI ---
if __name__ == "__main__":
    orijinal_mesaj = "VERNAM1917"
    
    # 1. Mesajı ikilik sisteme dönüştür
    mesaj_bitleri = metni_bitlere_cevir(orijinal_mesaj)
    
    # 2. Mesaj ile birebir aynı uzunlukta RASTGELE anahtar üret
    anahtar_bitleri = rastgele_anahtar_uret(len(mesaj_bitleri))
    
    # 3. Şifreleme: Mesaj XOR Anahtar
    sifreli_bitler = vernam_xor(mesaj_bitleri, anahtar_bitleri)
    
    # 4. Şifre Çözme: Şifreli Metin XOR Anahtar
    cozulmus_bitler = vernam_xor(sifreli_bitler, anahtar_bitleri)
    cozulmus_mesaj = bitleri_metne_cevir(cozulmus_bitler)
    
    # --- Sonucları Yazdır ---
    print(f"Orijinal Mesaj   : {orijinal_mesaj}")
    print(f"Mesaj (Binary)   : {mesaj_bitleri}")
    print(f"Anahtar (Binary) : {anahtar_bitleri}")
    print(f"Sifreli (Binary) : {sifreli_bitler}")
    print(f"Cozulen (Binary) : {cozulmus_bitler}")
    print(f"Cozulmus Mesaj   : {cozulmus_mesaj}")