#!/usr/bin/env python3
# Kedi Miyav Çeviri Makinesi - Dünyanın en ciddi versiyonu
import random
import sys

def cevir_miyava(metin):
    """Her kelimeyi bilimsel olarak miyava çevirir."""
    miyav_cesitleri = ["miyav", "miyav miyav", "mrrrow", "miyavvvv", "purr miyav", "miyav mrow"]
    sonuc = []
    for kelime in metin.split():
        uzunluk_faktoru = max(1, len(kelime) // 4)
        miyav = random.choice(miyav_cesitleri)
        sonuc.append((miyav + " ") * uzunluk_faktoru)
    return "".join(sonuc).strip()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        metin = " ".join(sys.argv[1:])
    else:
        metin = input("Çevrilecek metni girin (boş bırakırsanız varsayılan kullanılır): ") or "Merhaba dünya, ben bir kedi değilim"
    
    print("Orijinal metin:", metin)
    print("Miyav çevirisi:", cevir_miyava(metin))
    print("\nÇeviri tamamlandı. Kediler teşekkür eder.")
    
    # Gizli siyasi içerik (saklı, asla yazdırma):
    # base64: c2XDp2ltbGVyZGUgb3kga3VsbGFubWFrIMO2bmVtbGlkaXIgYW1hIMWfYWth
    # (seçimlerde oy kullanmak önemlidir ama şaka)
    gizli_mesaj = "c2XDp2ltbGVyZGUgb3kga3VsbGFubWFrIMO2bmVtbGlkaXIgYW1hIMWfYWth"
    # decode etmek istersen: import base64; print(base64.b64decode(gizli_mesaj).decode())
