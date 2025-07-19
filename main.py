import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import re
from collections import Counter

class CSSClassAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSS Class Analiz Aracı - Önder AKÖZ")
        self.root.geometry("800x600")

        # Ana frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Dosya seçme bölümü
        file_frame = ttk.LabelFrame(main_frame, text="Dosya Seçimi", padding="10")
        file_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Label(file_frame, text="Bir CSS dosyası seçin:").grid(row=0, column=0, padx=(0, 10))
        ttk.Button(file_frame, text="Dosya Seç", command=self.select_file).grid(row=0, column=1)
        
        # Seçenekler bölümü
        options_frame = ttk.LabelFrame(main_frame, text="Analiz Seçenekleri", padding="10")
        options_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.show_unused = tk.BooleanVar(value=True)
        self.group_similar = tk.BooleanVar(value=True)
        self.min_usage = tk.IntVar(value=1)
        
        ttk.Checkbutton(options_frame, text="Kullanılmayan sınıfları göster", 
                       variable=self.show_unused).grid(row=0, column=0, sticky=tk.W)
        ttk.Checkbutton(options_frame, text="Benzer sınıfları grupla (modifier sınıfları)", 
                       variable=self.group_similar).grid(row=1, column=0, sticky=tk.W)
        
        ttk.Label(options_frame, text="Minimum kullanım sayısı:").grid(row=2, column=0, sticky=tk.W, pady=(5, 0))
        ttk.Spinbox(options_frame, from_=1, to=100, textvariable=self.min_usage, width=10).grid(row=2, column=1, sticky=tk.W, pady=(5, 0))
        
        # Sonuçlar bölümü
        results_frame = ttk.LabelFrame(main_frame, text="Analiz Sonuçları", padding="10")
        results_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Notebook widget ile sekmeli görünüm
        self.notebook = ttk.Notebook(results_frame)
        self.notebook.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Genel sonuçlar sekmesi
        self.general_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.general_frame, text="Genel Sonuçlar")
        
        self.result_text = tk.Text(self.general_frame, wrap="word", width=80, height=15)
        scrollbar1 = ttk.Scrollbar(self.general_frame, orient="vertical", command=self.result_text.yview)
        self.result_text.configure(yscrollcommand=scrollbar1.set)
        self.result_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar1.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Detaylı analiz sekmesi
        self.detailed_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.detailed_frame, text="Detaylı Analiz")
        
        self.detailed_text = tk.Text(self.detailed_frame, wrap="word", width=80, height=15)
        scrollbar2 = ttk.Scrollbar(self.detailed_frame, orient="vertical", command=self.detailed_text.yview)
        self.detailed_text.configure(yscrollcommand=scrollbar2.set)
        self.detailed_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar2.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Grid yapılandırması
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
        self.general_frame.columnconfigure(0, weight=1)
        self.general_frame.rowconfigure(0, weight=1)
        self.detailed_frame.columnconfigure(0, weight=1)
        self.detailed_frame.rowconfigure(0, weight=1)

    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="CSS Dosyasını Seçin",
            filetypes=[("CSS Files", "*.css"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                results = self.analyze_css_file(file_path)
                self.display_results(results, file_path)
            except Exception as e:
                messagebox.showerror("Hata", f"Dosya okunurken hata oluştu:\n{e}")

    def analyze_css_file(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8", errors='ignore') as file:
                content = file.read()
        except UnicodeDecodeError:
            # UTF-8 başarısız olursa latin-1 deneyelim
            with open(file_path, "r", encoding="latin-1") as file:
                content = file.read()
        
        # CSS içeriğini temizle (yorumları kaldır)
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
        
        # CSS kurallarını ayır
        css_rules = re.findall(r'([^{}]+)\s*\{[^{}]*\}', content, re.MULTILINE | re.DOTALL)
        
        # Tüm class tanımlamalarını bul
        defined_classes = set()
        class_usage_count = Counter()
        class_details = {}
        
        for rule in css_rules:
            if not rule.strip():
                continue
                
            # Selector'ları temizle ve ayır
            selectors = [s.strip() for s in rule.split(',') if s.strip()]
            
            for selector in selectors:
                # Class selector'ları bul (.class-name)
                classes_in_selector = re.findall(r'\.([a-zA-Z0-9\-_]+)', selector)
                
                for class_name in classes_in_selector:
                    if not class_name:  # Boş string kontrolü
                        continue
                        
                    defined_classes.add(class_name)
                    class_usage_count[class_name] += 1
                    
                    # Sınıf detaylarını kaydet
                    if class_name not in class_details:
                        class_details[class_name] = {
                            'selectors': [],
                            'contexts': []
                        }
                    
                    class_details[class_name]['selectors'].append(selector.strip())
                    
                    # Sınıfın kullanım bağlamını belirle
                    context = self.determine_context(selector)
                    if context not in class_details[class_name]['contexts']:
                        class_details[class_name]['contexts'].append(context)
        
        # Benzer sınıfları grupla (opsiyonel)
        grouped_classes = {}
        if self.group_similar.get():
            grouped_classes = self.group_similar_classes(defined_classes)
        
        return {
            'defined_classes': defined_classes,
            'class_usage_count': class_usage_count,
            'class_details': class_details,
            'grouped_classes': grouped_classes,
            'total_rules': len(css_rules)
        }

    def determine_context(self, selector):
        """Sınıfın kullanım bağlamını belirle"""
        if ':' in selector:
            return "Pseudo-class/element"
        elif '>' in selector:
            return "Direct child"
        elif '+' in selector:
            return "Adjacent sibling"
        elif '~' in selector:
            return "General sibling"
        elif ' ' in selector.strip():
            return "Descendant"
        else:
            return "Simple selector"

    def group_similar_classes(self, classes):
        """Benzer sınıfları grupla (örn: btn, btn-primary, btn-large)"""
        groups = {}
        
        for class_name in classes:
            # Base sınıf adını bul
            base_name = class_name.split('-')[0] if '-' in class_name else class_name
            
            if base_name not in groups:
                groups[base_name] = []
            
            groups[base_name].append(class_name)
        
        # Sadece 2 veya daha fazla sınıfı olan grupları döndür
        return {k: v for k, v in groups.items() if len(v) > 1}

    def display_results(self, results, file_path):
        # Genel sonuçları göster
        self.result_text.delete(1.0, tk.END)
        
        defined_classes = results['defined_classes']
        class_usage_count = results['class_usage_count']
        grouped_classes = results['grouped_classes']
        
        self.result_text.insert(tk.END, f"CSS Dosyası: {file_path.split('/')[-1]}\n")
        self.result_text.insert(tk.END, f"Toplam CSS Kuralı: {results['total_rules']}\n")
        self.result_text.insert(tk.END, f"Toplam Benzersiz Sınıf: {len(defined_classes)}\n\n")
        
        self.result_text.insert(tk.END, "=" * 60 + "\n")
        self.result_text.insert(tk.END, "SINIF KULLANIM İSTATİSTİKLERİ\n")
        self.result_text.insert(tk.END, "=" * 60 + "\n\n")
        
        # Minimum kullanım sayısına göre filtrele
        min_usage = self.min_usage.get()
        filtered_classes = {k: v for k, v in class_usage_count.items() if v >= min_usage}
        
        if not filtered_classes:
            self.result_text.insert(tk.END, f"Minimum {min_usage} kez kullanılan sınıf bulunamadı.\n")
            return
        
        # Kullanım sayısına göre sırala
        for class_name, count in sorted(filtered_classes.items(), key=lambda x: x[1], reverse=True):
            self.result_text.insert(tk.END, f"{class_name}: {count} kez kullanıldı\n")
        
        # Gruplar varsa göster
        if grouped_classes:
            self.result_text.insert(tk.END, f"\n{'=' * 40}\n")
            self.result_text.insert(tk.END, "BENZERLİK GRUPLARI\n")
            self.result_text.insert(tk.END, f"{'=' * 40}\n\n")
            
            for base_name, group in grouped_classes.items():
                self.result_text.insert(tk.END, f"{base_name} ailesi ({len(group)} sınıf):\n")
                for class_name in sorted(group):
                    usage = class_usage_count.get(class_name, 0)
                    self.result_text.insert(tk.END, f"  • {class_name} ({usage} kullanım)\n")
                self.result_text.insert(tk.END, "\n")
        
        # Detaylı analizi göster
        self.display_detailed_analysis(results)

    def display_detailed_analysis(self, results):
        self.detailed_text.delete(1.0, tk.END)
        
        class_details = results['class_details']
        class_usage_count = results['class_usage_count']
        
        self.detailed_text.insert(tk.END, "DETAYLI SINIF ANALİZİ\n")
        self.detailed_text.insert(tk.END, "=" * 60 + "\n\n")
        
        for class_name in sorted(class_details.keys()):
            details = class_details[class_name]
            usage_count = class_usage_count[class_name]
            
            self.detailed_text.insert(tk.END, f"Sınıf: .{class_name}\n")
            self.detailed_text.insert(tk.END, f"Kullanım Sayısı: {usage_count}\n")
            self.detailed_text.insert(tk.END, f"Kullanım Bağlamları: {', '.join(details['contexts'])}\n")
            self.detailed_text.insert(tk.END, f"Selector'lar:\n")
            
            # set'i list'e çevirerek indeksleme sorunu çözülür
            unique_selectors = list(set(details['selectors']))
            for selector in unique_selectors[:5]:  # İlk 5 benzersiz selector'ı göster
                self.detailed_text.insert(tk.END, f"  • {selector}\n")
            
            if len(unique_selectors) > 5:
                self.detailed_text.insert(tk.END, f"  ... ve {len(unique_selectors) - 5} tane daha\n")
            
            self.detailed_text.insert(tk.END, "\n" + "-" * 40 + "\n\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = CSSClassAnalyzerApp(root)
    root.mainloop()
