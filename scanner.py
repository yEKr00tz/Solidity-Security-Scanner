# -*- coding: utf-8 -*-
import re
import os

def solidity_scanner():
    file_path = input("Taramak istediğiniz .sol dosyasının adını yazın: ").strip()

    if not os.path.exists(file_path):
        print(f"Hata: '{file_path}' dosyası bulunamadı! Lütfen dosya adını ve uzantısını kontrol edin.")
        return

    
    risk_patterns = {
        r"tx\.origin": "KRİTİK: Phishing saldırısına yol açabilir (tx.origin kullanımı).",
        r"selfdestruct": "UYARI: Yetkisiz kontrat imhası riski (selfdestruct).",
        r"delegatecall": "KRİTİK: Dış kod çalıştırma tehlikesi (delegatecall).",
        r"\.call\s*\{.*value": "UYARI: Reentrancy (Yeniden Giriş) riski (.call kullanımı).",
        r"abi\.encodePacked": "UYARI: Hash çakışması riski (abi.encodePacked)."
    }

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            lines = file.readlines()

        print(f"\n--- {file_path} Analiz Ediliyor ---")
        print("-" * 40)
        
        found_any = False
        for line_num, line in enumerate(lines, 1):
            clean_line = line.strip()
          
            if clean_line.startswith("//") or clean_line.startswith("/*"):
                continue

            for pattern, message in risk_patterns.items():
                if re.search(pattern, clean_line):
                    print(f"[SATIR {line_num}] {message}")
                    found_any = True
        
        if not found_any:
            print("\nTemiz! Belirlenen kritik riskler bulunamadı.")
        else:
            print("\nTarama tamamlandı. Yukarıdaki riskleri inceleyin.")
            
    except Exception as e:
        print(f"Dosya okunurken bir hata oluştu: {e}")

if __name__ == "__main__":
    solidity_scanner()
