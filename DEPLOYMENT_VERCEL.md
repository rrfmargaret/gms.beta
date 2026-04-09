# Gate System Deployment Guide (Vercel & Google Apps Script)

Panduan ini berisi tahapan lengkap untuk mengangkat aplikasi Gate Monitoring System ini ke Vercel agar dapat diakses oleh browser darimanapun di dunia, lengkap dengan rute yang rapi tanpa perlu ekstensi `.html`.

## Part 1: Persiapan File (Local)
Sistem sekarang dirancang agar sangat siap-deploy (*production-ready*).
Saya telah men-generate 2 file krusial khusus untuk Anda:
- `index.html`: Sebuah portal "Home" pendaratan (landing page) dengan desain estetika P&G, berfungsi untuk mengarahkan pengguna ke **POST 7** atau **POST 1**.
- `vercel.json`: Konfigurasi *rewrite* resmi Vercel yang otomatis mengubah URL memanjang menjadi sangat bersih (contoh: `domain.com/post7-entry.html` diubah menjadi path bersih `domain.com/entry`).

## Part 2: Konfigurasi Database Utama (Google Sheets)
Sebagaimana desain arsitekturnya, sistem ini menggunakan Google Sheets sebagai log utamanya.

1. Buka Google Sheets Anda (Buat baru jika belum).
2. Buat Sheet ber-tab nama **`Entry Log`**.
3. Pastikan Kolom di Baris Pertama membentang A hingga V secara berurutan sesuai pembaruan kita:
    - `ID`, `Date`, `Time In`, `Time Out`, `Duration`, `License Plate`, `Driver Name`, `Company`, `SIM Type`, `ID Number`, `Driver Card`, `Vehicle Type`, `Destination`, `Annotations`, `Approver`, `Shipments`, `Products`, `Details`, `Post In`, `Post Out`, `Status`, `Full Time In`
4. Copy/Ambil URL Spreadsheets tersebut dari atas browser Anda.

## Part 3: Eksekusi Backend (Google Apps Script)
1. Pergi ke menu **Extensions > Apps Script** di Google Sheets Anda.
2. Salin keseluruhan teks kode dari file `Code.gs` yang ada di laptop ke dalam antarmuka Apps Script tersebut (Timpa apapun isi bawaannya).
3. Cari properti ini pada baris atas: `var SHEET_ID = 'YOUR_GOOGLE_SHEET_ID_HERE';`
4. Ubah kode di dalam tanda kutip menjadi ID asli Spreadsheets Anda (Kumpulan huruf/angka acak sesudah `/d/` di URL Google sheet Anda).
5. Klik tombol biru **Deploy > New Deployment** di bagian kanan atas layar.
6. Pilih lambang mur/roda gigi, jadikan bertipe **Web App**.
   - *Execute as: Me*
   - *Who has access: Anyone*
7. Tekan Deploy. Google akan meminta izin (Authorize access), klik setujui melalui konfirmasi email/advance.
8. Anda akan diberikan satu buah link executable URL dengan bentuk seperti `https://script.google.com/macros/s/xxxx/exec`. **SALIN DAN SIMPAN URL INI SECARA HATI-HATI.**

## Part 4: Tautkan Frontend ke API
URL yang tadi disalin adalah jembatan *backend* Anda!
1. Buka file `post7-entry.html` menggunakan Code Editor, dan cari baris `const SHEET_URL =`. Tempel (Paste) URL Apps Script rahasia Anda ke dalam tanda kutip tersebut.
2. Buka `post1-exit.html` menggunakan Code Editor, dan cari baris `const SHEET_URL =`. Tempel (Paste) URL Apps Script rahasia Anda juga ke dalam sini.
*(Aplikasi Entry dan Exit kini saling terhubung ke database yang sama!)*

## Part 5: Go-Live (Deployment via Vercel)
Kini seluruh kode Frontend telah matang, direkonstruksi, dan siap online.

1. Buka akun GitHub Anda dan buatlah repositori kosong (Repository) baru.
2. Unggah (push/commit) seluruh file dari folder `/Gate Monitoring System` ini ke repositori Github tersebut. *(Jangan lupa index.html dan vercel.json juga disertakan).*
3. Buka website **https://vercel.com** dan login menggunakan akun GitHub Anda tersebut.
4. Di dashboard Vercel, klik tulisan **Add New > Project**.
5. Muncul daftar repositori Anda. Klik tombol **Import** di sebelah nama repositori Gate System.
6. Pada kolom Framework Preset, tidak perlu repot menyetel apapun (biarkan saja otomatis mendeteksi konfigurasi `Other`).
7. Klik **DEPLOY**.
8. Setelah kurang dari 1 menit kompilasi berjalan, layar akan dihujani *confetti* tanda sukses. **Sistem Mengudara Sempurna!** 

Coba akses domain yang diberikan dari Vercel (contoh: `https://gate-system-x.vercel.app`). Saat diklik, portal `index.html` elegan akan memunculkan opsi navigasi Gate Anda secara rapi. Jika Anda menambahkan path `/entry`, URL tetap cantik. 

Saran pengoperasian: Karena PWA dan Service Worker telah disematkan, jangan lupa akses situs ini langsung di *browser Tablet/Smartphone* Gate 7 & 1, bagikan, dan klik **"Add to Home Screen"** agar muncul seperti aplikasi native Android biasa, tanpa antarmuka URL di atasnya!
