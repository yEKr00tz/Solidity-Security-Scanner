# -*- coding: utf-8 -*-
import re
import os

def solidity_scanner():
    # Kullanıcıdan dosya adını alır
    file_path = input("Taramak istediğiniz .sol dosyasının adını yazın): ")

    # Dosyanın var olup olmadığını kontrol eder
    if not os.path.exists(file_path):
        print(f"Hata: '{file_path}' dosyası bulunamadı!")
        return

    risks = {
        "tx.origin": "Kritik: Phishing saldırısına yol açabilir.",
        "selfdestruct": "Uyarı: Yetkisiz kontrat imhası riski.",
        "delegatecall": "Kritik: Dış kod çalıştırma tehlikesi.",
        ".call{value:": "Uyarı: Reentrancy (Yeniden Giriş) riski.",
        "abi.encodePacked": "Uyarı: Hash çakışması riski."
    }

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()

        print(f"\n--- {file_path} Analiz Ediliyor ---\n")
        
        found_any = False
        for line_num, line in enumerate(content, 1):
            for key, message in risks.items():
                if key in line:
                    print(f"[SATIR {line_num}] {message} -> Bulunan: {key}")
                    found_any = True
        
        if not found_any:
            print("Temiz! Kritik bir risk bulunamadı.")
            
    except Exception as e:
        print(f"Dosya okunurken bir hata oluştu: {e}")

if __name__ == "__main__":
    solidity_scanner()
