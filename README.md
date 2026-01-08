# Solidity Security Scanner 🛡️

Bu proje, Solidity akıllı sözleşmelerindeki (Smart Contracts) yaygın güvenlik açıklarını ve riskli kod kullanım kalıplarını tespit etmek için geliştirilmiş Python tabanlı bir **Statik Analiz (Static Analysis)** aracıdır.

## 📌 Proje Amacı / Project Purpose
Blockchain ekosisteminde güvenlik, geri döndürülemez hataların önlenmesi için hayati önem taşır. Bu araç, geliştiricilerin veya denetçilerin (auditors) manuel inceleme öncesinde kod içerisindeki "tehlikeli" fonksiyonları ve hatalı mantık kurgularını hızlıca tespit etmesini sağlar.

## 🚀 Öne Çıkan Özellikler / Key Features
- **Hızlı Tarama:** `.sol` dosyalarını saniyeler içinde analiz eder.
- **Kritik Zafiyet Tespiti:** Hackerların en çok kullandığı giriş noktalarını tarar.
- **Eğitsel Yaklaşım:** Bulunan her risk için açıklayıcı uyarılar sunar.

## 🔍 Tespit Edilen Güvenlik Riskleri / Detected Risks
Tarayıcı şu an aşağıdaki kritik başlıkları kontrol etmektedir:
- **tx.origin:** Phishing saldırılarına davetiye çıkaran hatalı kimlik doğrulama yöntemi.
- **selfdestruct:** Kontratın yetkisiz kişilerce imha edilme riski.
- **delegatecall:** Dış kaynaklı kodların kontrat yetkisiyle çalıştırılması tehlikesi.
- **.call{value:...}:** Reentrancy (Yeniden Giriş) saldırılarına karşı potansiyel zayıflık.
- **abi.encodePacked:** Hash çakışması (collision) riski taşıyan veri kodlama yöntemi.

## 🛠 Kurulum ve Kullanım / Installation & Usage

1. Sisteminizde Python yüklü olduğundan emin olun.
2. `scanner.py` dosyasını indirin.
3. Terminal (CMD) üzerinden aşağıdaki komutla taramayı başlatın:

 bash
python scanner.py 

.sol uzantılı dosyanızın adını girin


 ⚖️ Yasal Uyarı / Disclaimer

Bu araç sadece eğitim amaçlıdır. Profesyonel projelerde tek başına yeterli değildir; manuel denetim ve Slither/Mythril gibi araçlarla desteklenmelidir. Kullanım sorumluluğu kullanıcıya aittir.

 This tool is for educational purposes only. It should be used alongside professional audit tools. Use at your own risk.
