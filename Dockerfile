# Python 3.9 kullanıyoruz
FROM python:3.9-slim

# Çalışma dizini oluşturuyoruz
WORKDIR /app

# Gereksinim dosyasını kopyalıyoruz
COPY requirements.txt /app/

# Gereksinimleri yüklüyoruz
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyalıyoruz
COPY . /app/

# Flask uygulamasını çalıştırıyoruz
CMD ["python", "app.py"]
