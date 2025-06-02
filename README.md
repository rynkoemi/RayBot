🧠💬 Proyek RayBot – Chatbot AI Offline Tanpa API 🧠💬  
Selamat datang di repositori **RayBot**, chatbot AI offline yang berjalan tanpa API eksternal! 🚀  
Proyek ini mendemonstrasikan bagaimana membangun chatbot interaktif berbasis **model open-source** (BlenderBot dari HuggingFace) yang dapat dijalankan **sepenuhnya lokal**, tanpa koneksi internet atau API dari OpenAI.

---

🧱 Arsitektur Aplikasi  
Arsitektur RayBot dirancang sederhana namun modular, dengan tiga komponen utama:

- **Model AI Lokal:** Menggunakan model `facebook/blenderbot-400M-distill` dari HuggingFace untuk percakapan responsif dan natural.
- **Backend:** Server ringan berbasis Python Flask untuk menangani permintaan dan respons AI.
- **Frontend:** Antarmuka pengguna berbasis HTML, CSS, dan JavaScript yang intuitif dan modern.

---

📖 Gambaran Umum Proyek  

Proyek ini melibatkan:

- 🎯 **Penerapan Model AI Lokal:** Memanfaatkan model BlenderBot agar chatbot bisa berjalan offline, tanpa ketergantungan pada API pihak ketiga.
- 🧰 **Pengembangan Frontend & Backend:** Flask digunakan untuk backend, dan HTML/CSS modern untuk frontend.
- 🌐 **Integrasi Chatbot Web:** Chatbot dapat diakses melalui browser dengan percakapan real-time menggunakan AJAX.
- 🖼️ **Tampilan Estetis:** UI ringan dan ramah pengguna, dapat disesuaikan sesuai kebutuhan branding.

---

🎯 Repositori ini cocok untuk:

- Pelajar & mahasiswa yang ingin memahami penerapan chatbot AI tanpa API.
- Developer yang ingin membangun asisten AI lokal (tanpa biaya langganan).
- Siapa pun yang ingin mengembangkan prototipe chatbot pribadi/offline.

---

🛠️ Resources:

- HuggingFace Transformers + BlenderBot
- Python 3.12
- Flask (Web Framework)
- HTML + CSS + JS
- Browser modern (Chrome, Firefox, Edge)

---

🚀 Cara Menjalankan Proyek  

1. **Install dependensi:**

```bash
pip install flask transformers torch
```

2. **Tulis kode di main.py dan index.html**

3. **Jalankan aplikasi**

```bash
python app.py
```

4. Buka browser ke:

```bash
http://127.0.0.1:5000
```
---

📂 Struktur Repositori

```bash
raybot-offline/
├── templates/
│   └── index.html              # Tampilan frontend chatbot
├── app.py                     # Backend Flask + integrasi model BlenderBot
├── README.md                  # Dokumentasi ini
└── requirements.txt (opsional)
```
---

🛡️ Lisensi
Proyek ini dilisensikan di bawah MIT License. Anda bebas menggunakan, memodifikasi, dan membagikan proyek ini dengan atribusi yang sesuai.

---

