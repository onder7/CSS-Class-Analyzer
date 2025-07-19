# CSS Sınıf Analiz Aracı

CSS dosyalarını analiz etmek ve sınıf kullanım istatistiklerini takip etmek için güçlü bir Python GUI uygulaması.

## 🚀 Özellikler

- **Akıllı CSS Ayrıştırma**: CSS dosyalarını doğru şekilde ayrıştırır ve tüm sınıf tanımlarını tespit eder
- **Kullanım İstatistikleri**: Her CSS sınıfının kaç kez kullanıldığını sayar
- **Tekrar Tespiti**: Karmaşık seçicilerde aynı sınıfın birden fazla sayılmasını önler
- **Sınıf Gruplandırma**: Benzer sınıfları gruplar (örn: `btn`, `btn-primary`, `btn-large`)
- **Bağlam Analizi**: Sınıfların nasıl kullanıldığını belirler (pseudo-class, child selector, vb.)
- **Detaylı Raporlar**: Hem genel hem de detaylı analiz görünümleri sunar
- **Filtreleme Seçenekleri**: Minimum kullanım sayısına göre sonuçları filtreler
- **Modern Arayüz**: Sekmeli görünümler ve seçeneklerle kullanıcı dostu arayüz

## 📋 Gereksinimler

- Python 3.6+
- tkinter (genellikle Python ile birlikte gelir)
- Ek bağımlılık gerektirmez!

## 🛠️ Kurulum

1. Bu repoyu klonlayın:
```bash
git clone https://github.com/kullaniciadi/css-sinif-analiz-araci.git
cd css-sinif-analiz-araci
```

2. Uygulamayı çalıştırın:
```bash
python css_analyzer.py
```

## 💻 Kullanım

1. **Uygulamayı başlatın**
2. **"Dosya Seç" butonu** ile bir CSS dosyası seçin
3. **Analiz seçeneklerini yapılandırın**:
   - Kullanılmayan sınıfları göster
   - Benzer sınıfları grupla
   - Minimum kullanım sayısını ayarla
4. **Sonuçları görüntüleyin** iki sekmede:
   - **Genel Sonuçlar**: Genel bakış ve istatistikler
   - **Detaylı Analiz**: Sınıf bazında ayrıntılı bilgiler

## 📊 Elde Edeceğiniz Bilgiler

### Genel Sonuçlar
- Toplam CSS kuralı sayısı
- Benzersiz sınıf sayısı
- Sıklığa göre sıralanmış kullanım istatistikleri
- Sınıf ailesi gruplandırmaları

### Detaylı Analiz
- Bireysel sınıf analizi
- Seçici bağlamları (pseudo-class, child, descendant, vb.)
- Her sınıf için tam seçici listesi
- Kullanım desenleri

## 🎯 Kullanım Alanları

- **Kod Optimizasyonu**: Kullanılmayan CSS sınıflarını bulun
- **Refaktöring**: Yaygın kullanılan desenleri tespit edin
- **Dokümantasyon**: Sınıf kullanım raporları oluşturun
- **Kod İncelemesi**: CSS yapısını ve organizasyonunu analiz edin
- **Performans**: Kullanılmayan sınıfları kaldırarak CSS'i optimize edin

## 📝 Örnek Çıktı

```
CSS Dosyası: styles.css
Toplam CSS Kuralı: 245
Toplam Benzersiz Sınıf: 78

SINIF KULLANIM İSTATİSTİKLERİ
========================================
container: 15 kez kullanıldı
btn: 12 kez kullanıldı
nav-item: 8 kez kullanıldı
...

BENZERLİK GRUPLARI
========================================
btn ailesi (4 sınıf):
  • btn (12 kullanım)
  • btn-primary (5 kullanım)
  • btn-secondary (3 kullanım)
  • btn-large (2 kullanım)
```

## 🔧 Teknik Detaylar

Analiz aracı:
- Ayrıştırmadan önce CSS yorumlarını kaldırır
- Sınıf seçicilerini tespit etmek için regex desenleri kullanır
- Karmaşık seçicileri işler (kombinatörler, pseudo-class'lar)
- Bileşik seçicilerde çift sayımı önler
- Çeşitli CSS formatlama stillerini destekler

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Pull Request göndermekten çekinmeyin.

1. Projeyi fork edin
2. Özellik dalınızı oluşturun (`git checkout -b feature/HarikaBirOzellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Harika bir özellik ekle'`)
4. Dalınıza push edin (`git push origin feature/HarikaBirOzellik`)
5. Pull Request açın

## 📄 Lisans

Bu proje MIT Lisansı ile lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 🐛 Hata Bildirimi

Bir hata bulursanız, lütfen aşağıdaki bilgilerle bir issue açın:
- Python sürümü
- İşletim sistemi
- Soruna neden olan CSS dosyası (mümkünse)
- Hata mesajı

## ⭐ Destek

Bu aracı yararlı bulduysanız, lütfen yıldız verin! ⭐

## 🌍 Dil Desteği

- [English README](README.md)
- [Türkçe README](README_TR.md)

## 📞 İletişim

Sorularınız için GitHub Issues kullanabilirsiniz.
