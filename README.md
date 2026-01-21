# Solidity Security Scanner 🛡️ (v2.0)

[English](#english) | [Türkçe](#türkçe)

---

## English

Python-based static analysis tool designed to detect common vulnerabilities and risky patterns in Solidity smart contracts.

### 🚀 Key Features
- **Deep Scan:** Analyzes `.sol` files for 7+ critical vulnerability patterns.
- **Automated Reporting:** Generates a detailed `.txt` report for every scan with timestamps.
- **Smart Filtering:** Ignores comment blocks to reduce false positives.

### 🔍 Detected Risks
- **Critical:** `tx.origin` (Phishing), `delegatecall` (External Code Execution)
- **High:** `selfdestruct` (Contract Destruction), `Reentrancy` (.call value usage)
- **Medium/Low:** `abi.encodePacked` (Hash Collision), `block.timestamp` (Miner Manipulation)

### 🛠️ Usage
1. Run `python scanner.py`
2. Enter the name of your `.sol` file.
3. Check the generated `report_[filename].txt`.

---

## Türkçe

Solidity akıllı sözleşmelerindeki güvenlik açıklarını tespit etmek için geliştirilmiş Python tabanlı **Statik Analiz** aracıdır.

### 🚀 Öne Çıkan Özellikler
- **Derinlemesine Tarama:** `.sol` dosyalarını 7'den fazla kritik zafiyet türüne karşı analiz eder.
- **Otomatik Raporlama:** Her tarama sonrası sonuçları tarih damgalı bir `.txt` dosyasına kaydeder.
- **Akıllı Filtreleme:** Yorum satırlarını tarama dışı bırakarak yanlış alarmları önler.

### 🔍 Tespit Edilen Güvenlik Riskleri
- **Kritik:** `tx.origin` (Oltalama), `delegatecall` (Dış Kod Çalıştırma)
- **Yüksek:** `selfdestruct` (Kontrat İmhası), `Reentrancy` (Yeniden Giriş Saldırıları)
- **Orta/Düşük:** `abi.encodePacked` (Hash Çakışması), `block.timestamp` (Zaman Damgası Bağımlılığı)

### 🛠️ Kullanım
1. `python scanner.py` komutunu çalıştırın.
2. Taramak istediğiniz `.sol` dosyasının adını girin.
3. Oluşturulan `report_[dosya_adi].txt` raporunu inceleyin.

---

### ⚖️ Disclaimer / Yasal Uyarı
English: This tool is for educational purposes only. Automated scans may have false positives/negatives. Always conduct a manual audit and use professional tools deploying to mainnet.

Türkçe: Bu araç sadece eğitim amaçlıdır. Otomatik taramalar hatalı sonuçlar verebilir. Ana ağ (mainnet) dağıtımı öncesinde mutlaka manuel denetim yapılmalı ve profesyonel araçlar kullanılmalıdır.
