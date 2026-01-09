import streamlit as st
import os

# --- 1. KEAMANAN RAHASIA (Environment Variables) ---
# Mengambil kunci gaib dari fitur Secrets Replit
SECRET_KEY = os.environ.get('SECRET_KEY')

# --- 2. PENGATURAN GERBANG UTAMA ---
st.set_page_config(page_title="LOGIC WORLD - Peta Peradaban Digital", layout="wide", page_icon="🌐")

# --- 3. SISTEM KEAMANAN PINTU MASUK (Authentication) ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def login():
    st.sidebar.title("🔑 Penjaga Gerbang")
    user = st.sidebar.text_input("Username")
    pw = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Masuk ke Logic World"):
        if pw == SECRET_KEY: # Validasi kunci dari Secrets
            st.session_state['logged_in'] = True
            st.rerun()
        else:
            st.sidebar.error("Kunci Salah!")

if not st.session_state['logged_in']:
    st.title("🏛️ LOGIC WORLD")
    st.info("Silakan masukkan kunci akses di Sidebar untuk masuk ke Peta Peradaban.")
    login()
    st.stop()

# --- 4. NAVIGASI RUANG (PETA PERADABAN) ---
with st.sidebar:
    st.title("🗺️ PETA PERADABAN")
    ruang = st.radio("Pilih Ruang:", [
        "1. Baitul Hikmah (Perpustakaan)",
        "2. Balai Kerja (Creative Hub)",
        "3. Majelis Ilmu (Meeting)",
        "4. Sastra & Hiburan (Budaya)",
        "5. Alat Bedah & Kalkulator"
    ])
    if st.button("Keluar (Log Out)"):
        st.session_state['logged_in'] = False
        st.rerun()

# --- 5. IMPLEMENTASI RUANG ---

# RUANG 1: BAITUL HIKMAH
if ruang == "1. Baitul Hikmah (Perpustakaan)":
    st.header("📚 Ruang Baitul Hikmah (Perpustakaan Abadi)")
    st.write("Tempat buku-buku yang 'dibakar' bangkit kembali.")
    
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("📖 Koleksi Manuskrip Klasik"):
            st.write("- **Al-Qanun fit-Tibb** (Kedokteran)")
            st.write("- **Muqaddimah** (Sosiologi & Sejarah)")
            st.write("- **Al-Jabr** (Matematika & Koding)")
            st.button("Terjemahkan (Indonesiakan) 🔄")
    
    with col2:
        st.subheader("🔓 Akses Kitab")
        st.write("Status: *Premium Content*")
        st.button("Buka PDF Lengkap (Scan QRIS/Midtrans)")

# RUANG 2: BALAI KERJA
elif ruang == "2. Balai Kerja (Creative Hub)":
    st.header("🛠️ Ruang Balai Kerja")
    sub_kerja = st.tabs(["Copywriter", "Peneliti", "Data Analyst"])
    
    with sub_kerja[0]:
        st.write("Mode Gelap Aktif 🌙 | Musik Lo-Fi 🎧")
        st.text_area("Tulis Narasi Anda di sini...")
        st.button("Hitung Efisiensi Kata")
        
    with sub_kerja[1]:
        st.write("Akses Jurnal & Validasi Sastrawi")
        st.file_uploader("Upload Jurnal untuk Cek Plagiasi")

# RUANG 3: MAJELIS ILMU
elif ruang == "3. Majelis Ilmu (Meeting)":
    st.header("🤝 Majelis Ilmu (Virtual Meeting)")
    st.warning("Syarat: Gratis max 3 orang (40 menit). Selebihnya otomatis via Webhook.")
    if st.button("Mulai Pertemuan (Jitsi Integration)"):
        st.info("Menghubungkan ke Jitsi Meet API...")
        st.write("[Ruang Virtual Anda Siap - Klik di Sini]")

# RUANG 4: SASTRA & HIBURAN
elif ruang == "4. Sastra & Hiburan (Ruang Budaya)":
    st.header("🎭 Ruang Sastra & Budaya")
    st.write("Sistem Sedekah Digital: Baca Bab 1-3 Gratis.")
    with st.expander("📚 Cerpen: Kebangkitan Nalar"):
        st.write("Bab 1: Cahaya dari Timur...")
        st.button("Buka Bab Selanjutnya (Saweria)")

# RUANG 5: ALAT BEDAH
elif ruang == "5. Alat Bedah & Kalkulator":
    st.header("🧮 Alat Bedah & Kalkulator Utility")
    opsi_tool = st.selectbox("Pilih Alat:", ["Cek Plagiasi", "Kalkulator Zakat/Waris", "Analisa Narasi"])
    if opsi_tool == "Kalkulator Zakat/Waris":
        st.number_input("Masukkan Nominal Harta:", step=100000)
        st.button("Hitung Hak Waris")

# --- 6. FOOTER & FILOSOFI ---
st.markdown("---")
st.caption("Mas Hilmi sebagai Khalifah | Logic World: Guru, Kantor, dan Pasar.")
