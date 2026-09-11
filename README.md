Nama: Hafizh Zuhdi Hartanto
NPM: 2506656785
Kelas: PBP D
Latihan Branching Git

Tugas 1

1. Penggunaan Elemen Semantik HTML5
Ya, saya menggunakan elemen semantik HTML5 seperti `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<dl>`, dan `<footer>`. Elemen-elemen ini sangat membantu dalam menyusun struktur kode yang bersih, terorganisir, serta mudah dibaca oleh developer maupun browser. Mengelompokkan konten ke dalam `<section>` dan kartu individual ke dalam `<article>` membuat penerapan styling CSS jauh lebih konsisten tanpa ketergantungan berlebihan pada tag `<div>`.

2. Tantangan Tata Letak & Responsivitas CSS
Tantangan utama yang dihadapi adalah menjaga keterbacaan serta kerapihan tata letak elemen saat berpindah dari layar desktop ke mobile. Saya mengatasinya dengan menerapkan CSS Grid `repeat(auto-fit, minmax(280px, 1fr))` pada section *Skills* dan *Projects*, serta mengatur alur flexbox pada header. Pada layar mobile, komponen secara otomatis menyesuaikan ukurannya menjadi satu kolom vertikal sehingga konten tetap nyaman dibaca.

3. Batasan Static Web & Rencana Fungsionalitas Dinamis
Sebagai web statis murni, batasan utama yang dirasakan adalah semua informasi bersifat *hardcoded*, sehingga setiap penambahan data harus mengedit berkas HTML secara langsung. Selain itu, belum ada interaksi dinamis seperti pengelolaan database atau otentikasi. Pada iterasi selanjutnya, saya ingin mengintegrasikan arsitektur MVT Django dan database PostgreSQL agar data portofolio dapat dikelola dan ditampilkan secara dinamis.

AI Disclosure
* Tools yang Digunakan: AI Collaboration Tool (Gemini).
* Penggunaan AI: AI digunakan sebagai sarana diskusi, membantu menyusun ide layout CSS Grid responsif, serta memvalidasi struktur penulisan HTML agar sesuai dengan standar kriteria tugas.
* Proses Mandiri: Seluruh pengkodean akhir, pengujian di server lokal, penyusunan konten pribadi, serta penyesuaian gaya tampilan dilakukan dan diverifikasi secara mandiri oleh penulis.

Tugas 2
1. Alur Permintaan Pengguna
Ketika pengguna membuka halaman portofolio baru seperti rute education, browser mengirimkan permintaan HTTP GET ke server. Django pertama kali menerima permintaan tersebut melalui urls.py tingkat proyek, yang kemudian mengarahkannya ke urls.py milik aplikasi main. Berkas urls.py aplikasi mencocokkan rute URL dan memanggil fungsi view show_education di views.py. Fungsi view ini bertugas mengambil seluruh objek data dari model Education yang tersimpan di database. Data tersebut dimasukkan ke dalam variabel context berformat dictionary lalu dikirimkan ke berkas template education.html. Django Template Language kemudian memproses data dari context untuk mencetak elemen HTML secara dinamis dan mengembalikan tampilan akhir ke browser pengguna.

2. Alasan Data Disimpan di Model
Penyimpanan data pada model diterapkan untuk memenuhi prinsip pemisahan tanggung jawab (Separation of Concerns). Dengan memisahkan antara struktur tampilan visual dan logika data bisnis, pengelolaan aplikasi menjadi jauh lebih rapi. Jika data perlu ditambah, diubah, atau dihapus, perubahan cukup dilakukan melalui database atau dashboard admin tanpa perlu menyentuh baris kode pada berkas template HTML. Hal ini meningkatkan efisiensi pemeliharaan kode serta memudahkan pengembangan aplikasi dalam skala yang lebih besar di masa depan.

3. Perbedaan makemigrations dan migrate
Perintah makemigrations berfungsi untuk mencatat setiap perubahan yang dilakukan pada berkas models.py dan mengemasnya menjadi berkas draf instruksi migrasi baru di dalam folder migrations. Sementara itu, perintah migrate berfungsi untuk mengeksekusi draf instruksi tersebut dan mengaplikasikannya secara nyata ke dalam skema tabel database. Sebagai contoh, ketika model Education ditambahkan ke models.py, perintah makemigrations dijalankan untuk membuat berkas draf migrasi 0002_education.py. Setelah itu, perintah migrate dieksekusi agar Django membuat tabel baru bernama main_education pada database.