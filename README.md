# MyPortofolio

<p align="center">This is my project for PBP course</p>

## Data
Nama : Vebian Francois Ariftya Manurung

NPM : 2506543363

Kelas : PBP D

## Pertanyaan Reflektif
### Tugas 1

1. Pada Tutorial dan Tugas satu ini dari antara `<section>`, `<article>`, dan `<aside>` yang saya gunakan hanyalah `<section>` untuk memisahkan bagian utama sepeti profile, skills dan lainnya. Sedangkan yang lain belum terlalu saya butuhkan dan saya juga belum punya ide untuk pemakaian mereka. Mungkin kedepannya akan saya pakai.
2. Tantangan untuk mengatur css agar tetap _responsive_ bagi saya tentu saja untuk mengatur agar ukurannya dapat mengecil/membesar sesuai kebutuhan. Dalam proses ini saya menggunakan _flex/flexbox_ dan tipe ukuran _rem_ yang banyak saya lihat ditutorial orang lain. Selain _flex_ saya juga belajar menggunakan _grid_ (pada bagian skills) untuk membuat kotak-kotak yang posisi _row_ dan _collum_ otomatis berubah. Saat ini masalah yang masih ada garis pemisah antar section yang tidak ujung ke ujung.
3. Saya ingin mencoba membuatnya lebih interaktif yang dimana banyak menggunakan _javascript_. Tapi tetap saya sendiri belum tau cara memakainya untuk menghasilkan Website yang lebih interaktif. Ide saya sementara adalah membuat _toggle_ navbar untuk layar mobile, informasi lanjutan terkait _skills_ seperti pop up ketika melihat gambar di _google_, dan beberapa animasi yang sebenarnya bisa saja pakai css tapi saya masih kurang paham juga :v

>Saya tidak menggunakan AI dalam mengerjakan tugas ini, tetapi saya banyak memakai tutorial dan mengikuti desain yang tersedia di Internet. Untuk lebih lengkap ada di bagian _Learning Source_.

### Tugas 2

1. Alur yang terjadi sekarang dimulai dari request oleh user misal /"" ke yang akan masuk ke `urls.py` proyek dan dari situ akan diarahkan ke `urls.py` aplikasi karena telah diinclude didalamnya (berbeda dengan /admin yang tidak masuk kesebuah aplikasi). Dari `urls.py` aplikasi barulah mengarahkan kita ke setiap view yang kita ingin atau jika ada. Dalam `views.py` menerima request lalu mengambil data dari database dan menyimpannya dalam suatu dictionary (`context`), lalu kemudian `views.py` mengembalikan hasil render sekalian dengan `.html` yang ingin dibuka. `models.py` Adalah tabel data itu sendiri yang diambil oleh `views.py` yang memiliki _field_ (kolom) dan _object_ (baris). `.html` Ini berada didalam `templates/` yang memiliki berbagai file `.html` yang dipakaikan Django Template Language (DTL).

2. Menyimpan data didalam sebuah model memudahkan kita untuk memelihara dan mengembangkan aplikasi, dibandingkan _hardcoded_ yang langsung ditulis datanya didalam `templates/` yang akan menyusahkan kita jika ingin menambah atau mengedit data. Penggunaan model memudahkanya karena kita jadi hanya perlu mengolah data yang didalam database dan otomatis akan berubah juga di `templates/`. Terlebih ini implementasi pemisahan logika antara pengatur tampilan dan data.

3. `makemigrations` dan `migrate` berbeda tapi saling berhubungan.
    * `makemigrations` dipakai untuk melihat dan mencatat perubahan pada `models.py` dan membuat berkas baru di dalam `/migrations`, tapi belum mengimplementasikannya di dalam database.
    * `migrate` memakai catatan didalam `/migrations` tadi dan mengimplementasikannya ke dalam database.
    ```
    # jadi urutannya
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

    Perlu diingat hal ini harus dilakukan setiap menambah atau mengedit sebuah model di dalam `models.py`.

>Saya menggunakan AI model _Gemini_ dalam mengerjakan tugas 2 ini,  saya gunakan untuk membantu saya menerapkan sistem toggle navbar di layar responsive karena tutorial youtube yang saya ikuti memiliki perbedaan struktur _header_ dan cara membuat struktur laman _Projects_ kiri-kanan tanpa javascript disarankan memakai _nth-child_. Contoh promt yang saya gunakan adalah file `.html` saya dan file `.html` dari contoh [tutorial](https://github.com/SnippetsDevelop/snippetsdevelop.github.io/blob/master/codes/Hamburger-Menu.html) dengan pesan "Saya ingin menerapkan desain ini dikode saya, tapi saya membuat navnya ada ditengah (divideo cuma ada logo dan nav), bagaimana agar bisa dipakai di kode saya". Selain itu saya juga mengikuti tutorial lain yang beberapa saya tambahkan di bagian _Learning Source_.

### Tugas 3

1. Penggunaan ModelForm dibanding membuat secara manual utamanya agar form tersebut dapat digunakan kembali dan tak perlu duplikasi lagi, terlebih menggunakan form ini kita dapat langsung mengambil field apa saja yang ada didalam model. Penggunaan `{% csrf_token %}` pada form agar penambahan yang dilakukan di web service mendapat izin otorisasi (misal di pws).

2. JSON lebih disukai dibandingkan XML karena lebih simpel dan cepat serta penggunaannya yang cocok dengan javascript karena memang bagian dari javascript itu sendiri.

3. Alurnya dimulai dari pengguna memberi *request* kepada *views* lalu mengakses data model (jika diperlukan, akan memfilter juga untuk kegunaan *search*). Setelah data object model didapatkan, dilakukan proses *serialization* untuk mengubahnya menjadi format JSON dan dikembalikan dalam bentuk HTTP response.

>Saya menggunakan AI model _Gemini_ pada pengerjaan tugas 2 ini, tepatnya dibagian kode rahasia untuk create, update dan delete (bagian project). Tapi saya tidak mengerti jadi tidak saya lanjut terapkan di model _experience_ dan berencana menggunakan metode autensifikasi saja sesuai materi minggu berikutnya.
Disisi lain sebenarnya saya masih binggung untuk update, saya menggabungkan logika create dan delete untuk buat fungsi update di `main/views`, semabri mengikuti contoh orang yang sedikit berbeda desainnya. Intinya saya mengetahui untuk bisa update butuh idnya seperti ketika mendelete, lalu saya copy sisa create dan menambahkan (contoh) instance=project, hal ini yang membuat inputnya langsung terisi dengan object model yang kita pilih. Lalu saya juga copy `project_form.html` untuk membuat `project_update_form.html` agar judulnya bisa saya ubah bukan "Add New Projects". Tapi ketika saya coba, malah terjadi error yang entah bagaimana saat saya hapus bagian `action="{% url 'main:update_project' %}"` (saya copy dan ubah dari yang sebelumnya `action="{% url 'main:create_project' %}"` di `project_form.html`), malah bisa berhasil. (saya juga lihat di contoh youtube action mereka kosong ""). Saya menjelaskan ini karena setelah saya melakukan ini baru saya bertanya kepada AI model _Gemini_ alasan hal tersebut bisa terjadi.

## Learning Source
Pada Tugas ini, banyak refrensi yang saya gunakan, dan refrensi utama saya untuk membuat website ini adalah desain dari web
>[ryoku.dev](https://ryoku.dev/)

Selain itu banyak juga tutorial dari Youtube yang saya tonton, seperti berikut:
* https://youtu.be/HGTJBPNC-Gw?si=8hMeXkslxpAXMm4u (banyak skip :v)
* https://youtu.be/wsTv9y931o8?si=JoY3rvTmjdhl1Mmn
* https://youtu.be/PwWHL3RyQgk?si=ekD2kZhbdC5Wik3E
* https://youtu.be/HmaQwuKUYTc?si=pkBRqAsr_e3WfQwG
* https://youtu.be/JYfiaSKeYhE?si=T5El_T_8qrcYsvF-
* https://youtu.be/l04dDYW-QaI?si=UraM26mqd1gKL-OV
* https://youtu.be/a8CwpGARAsQ?si=Lxe3hdQDHMu9MYzF (Edit Readme.md)
* https://youtu.be/aswRKAjjWuE?si=91_exOXhHZF1AgPp
* https://youtu.be/sDE34X8b6Ts?list=PLZS-MHyEIRo6p_RwsWntxMO5QAqIHHHld (Playlist django oleh **Kelas Terbuka** yang belum saya tonton semua karena agak berbeda :v)
* https://youtu.be/OnWTTUfBLMo?si=lDTH7QOPW62BeHeN (toggle menu)
* https://youtu.be/Rw1JeekTUVU?si=iO_lJC2dptWYQu1V (logic DTE)
* https://youtu.be/FtMsJ5qj6RY?si=btOM2cUwUFnjYpmU (Create, update, delete)
* https://youtu.be/EX6Tt-ZW0so?si=P96EONG3vRrVU9Cz
* Dan lainnya (Ada yang dari shorts Youtube juga)

Saya juga belajar pemakaian dan masalah git/github serta hal lainnya dengan bantuan paman saya. <br>
Lalu beberapa alat yang saya pakai:
* https://markdownlivepreview.com/ (Edit README)
* https://palettegenerator.com/ (Generate Palatte warna)
* https://paletton.com/
* https://glitchyimage.com/ (Belum terpakai :v)
* https://www.magicpattern.design/tools/css-backgrounds (background untuk tidak ada image)
* IbisPaint X
* Dan lainnya 

## See Myportofolio
Online access via **https://vebian-francois-myportofolio.pws.cs.ui.ac.id/**