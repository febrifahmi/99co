# 99co

<img src="https://cdn.pixabay.com/photo/2017/09/07/08/53/money-2724237_960_720.jpg"></img>

Scraper data listing properti di situs jual beli properti online.

<b>Usage:</b>

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

<b>Contoh:</b>

<img src="https://github.com/febrifahmi/99co/blob/master/data.png"></img>

Analisis yang bisa dilakukan:
- Distribusi properti dan berbagai atributnya (luas lahan, luas bangunan, jumlah kamar, harga, dsb) secara spasial dan dibandingkan dengan NJOP
- Perbandingan harga properti yang ada di pasar properti online di berbagai daerah
- Geocoding dapat dilakukan untuk data yang detail untuk analisis kedekatan dengan fasilitas publik
- dsb.



<i>Disclaimer: for research/educational purpose only please!</i> Silahkan baca <a href="https://www.99.co/id/terms?ref=footer">ketentuan layanan</a> situs 99co!
