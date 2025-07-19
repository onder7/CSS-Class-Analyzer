# CSS Class Analyzer
- [English README](README.md)
- [Türkçe README](README_TR.md)

<img width="800" height="632" alt="image" src="https://github.com/user-attachments/assets/3de41dfb-1bca-4646-b582-43840f9e6ec0" />

A powerful Python GUI application for analyzing CSS files and tracking class usage statistics.

## 🚀 Features

- **Smart CSS Parsing**: Accurately parses CSS files and identifies all class definitions
- **Usage Statistics**: Counts how many times each CSS class is used
- **Duplicate Detection**: Prevents counting the same class multiple times in complex selectors
- **Class Grouping**: Groups similar classes (e.g., `btn`, `btn-primary`, `btn-large`)
- **Context Analysis**: Determines how classes are used (pseudo-classes, child selectors, etc.)
- **Detailed Reports**: Provides both general and detailed analysis views
- **Filtering Options**: Filter results by minimum usage count
- **Modern GUI**: User-friendly interface with tabbed views and options

## 📋 Requirements

- Python 3.6+
- tkinter (usually comes with Python)
- No additional dependencies required!

## 🛠️ Installation

1. Clone this repository:
```bash
git clone https://github.com/onder7/CSS-Class-Analyzer.git
cd CSS-Class-Analyzer
```

2. Run the application:
```bash
python css_analyzer.py
```

## 💻 Usage

1. **Launch the application**
2. **Select a CSS file** using the "Select File" button
3. **Configure analysis options**:
   - Show unused classes
   - Group similar classes
   - Set minimum usage count
4. **View results** in two tabs:
   - **General Results**: Overview and statistics
   - **Detailed Analysis**: Per-class breakdown with selectors

## 📊 What You'll Get

### General Results
- Total CSS rules count
- Unique classes count
- Usage statistics sorted by frequency
- Class family groupings

### Detailed Analysis
- Individual class analysis
- Selector contexts (pseudo-class, child, descendant, etc.)
- Complete selector list for each class
- Usage patterns

## 🎯 Use Cases

- **Code Optimization**: Find unused CSS classes
- **Refactoring**: Identify commonly used patterns
- **Documentation**: Generate class usage reports
- **Code Review**: Analyze CSS structure and organization
- **Performance**: Optimize CSS by removing unused classes

## 📝 Example Output

```
CSS File: styles.css
Total CSS Rules: 245
Total Unique Classes: 78

CLASS USAGE STATISTICS
========================================
container: 15 times used
btn: 12 times used
nav-item: 8 times used
...

SIMILARITY GROUPS
========================================
btn family (4 classes):
  • btn (12 uses)
  • btn-primary (5 uses)
  • btn-secondary (3 uses)
  • btn-large (2 uses)
```

## 🔧 Technical Details

The analyzer:
- Removes CSS comments before parsing
- Uses regex patterns to identify class selectors
- Handles complex selectors (combinators, pseudo-classes)
- Prevents double-counting in compound selectors
- Supports various CSS formatting styles

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Bug Reports

If you find a bug, please open an issue with:
- Python version
- Operating system
- CSS file that caused the issue (if possible)
- Error message

## ⭐ Support

If you found this tool helpful, please give it a star! ⭐

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
git clone https://github.com/onder7/CSS-Class-Analyzer.git
cd CSS-Class-Analyzer
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
