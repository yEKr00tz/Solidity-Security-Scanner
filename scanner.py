import re
import os
from datetime import datetime

def solidity_scanner():
    file_path = input("Taramak istediğiniz .sol dosyasının adını yazın: ").strip()

    if not os.path.exists(file_path):
        print(f"Hata: '{file_path}' dosyası bulunamadı!")
        return

  
    risk_patterns = {
        r"tx\.origin": "KRİTİK: Phishing saldırısı riski (tx.origin kullanımı).",
        r"selfdestruct": "YÜKSEK: Yetkisiz kontrat imhası riski (selfdestruct).",
        r"delegatecall": "KRİTİK: Dış kaynaklı kod çalıştırma tehlikesi (delegatecall).",
        r"\.call\s*\{.*value": "YÜKSEK: Reentrancy (Yeniden Giriş) riski.",
        r"abi\.encodePacked": "ORTA: Hash çakışması (collision) riski.",
        r"block\.timestamp": "DÜŞÜK: Madenci manipülasyonu riski (Timestamp Dependency).",
        r"assert\(.*==.*\s*this\.balance\)": "YÜKSEK: Zorunlu Ether gönderimi ile kilitlenme riski."
    }

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            lines = file.readlines()

        report_content = [f"--- Analiz Raporu: {file_path} ---", f"Tarih: {datetime.now()}\n"]
        
        print(f"\n[+] {file_path} üzerinde derin tarama başlatılıyor...")
        
        found_any = False
        for line_num, line in enumerate(lines, 1):
            clean_line = line.strip()
            
          
            if clean_line.startswith("//") or clean_line.startswith("/*"):
                continue

            for pattern, message in risk_patterns.items():
                if re.search(pattern, clean_line):
                    output = f"[SATIR {line_num}] {message}"
                    print(output)
                    report_content.append(output)
                    found_any = True
        
        if not found_any:
            msg = "\nTemiz! Belirlenen standart riskler bulunamadı."
            print(msg)
            report_content.append(msg)
        
       
        report_file = f"report_{file_path}.txt"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("\n".join(report_content))
        
        print(f"\n[!] Tarama tamamlandı. Detaylı rapor oluşturuldu: {report_file}")
            
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    solidity_scanner()
