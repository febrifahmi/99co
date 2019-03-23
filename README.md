# 99co
Scraper data listing properti di situs jual beli properti online 

Usage:

<code>scrapy runspider scraperumah.py -o <outputfile.csv></code>

Data yang didapat meliputi:
- id property
- judul properti
- nama komplek
- lokasi
- provinsi
- jumlah kamar
- jumlah km
- luas lahan
- luas bangunan
- dijual/disewakan
- nego/fixed
- harga
- nama agen
- nama perusahaan property agen
- username
- nomor telepon
- whether premium agent atau tidak
- link send whatsapp message
- tipe properti
- tipe listing dijual atau disewakan
- url properti

Analisis yang bisa dilakukan:
- Distribusi properti dan berbagai atributnya (luas lahan, luas bangunan, jumlah kamar, harga, dsb) secara spasial
- Perbandingan harga properti yang ada di pasar properti online di berbagai daerah
- Geocoding dapat dilakukan untuk data yang detail untuk analisis kedekatan dengan fasilitas publik
- dsb.
