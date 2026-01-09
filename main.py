import streamlit as st

# ==========================================
# 1. KONFIGURASI PONDASI (HEADER)
# ==========================================
st.set_page_config(
    page_title="LOGIC WORLD - PRASANTI ADIKALA",
    layout="wide",
    page_icon="🏛️"
)

# ==========================================
# 2. SISTEM KEAMANAN GERBANG (AUTHENTICATION)
# ==========================================
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def login_gerbang():
    st.sidebar.title("🏛️ Gerbang Prasanti")
    st.sidebar.markdown("---")
    st.sidebar.markdown("*“Hanya nalar yang jernih yang mampu menyentuh akar waktu.”*")
    
    # Identitas & Kunci sesuai nilai Sansekerta Hilmi Mulazaman
    user_input = st.sidebar.text_input("Identitas Sansekerta (Username)")
    pw_input = st.sidebar.text_input("Kunci Adikala (Password)", type="password")
    
    if st.sidebar.button("Buka Gerbang Peradaban"):
        # Username: PRASANTI_ADIKALA | Password: prasanti_adikala24
        if user_input == "PRASANTI_ADIKALA" and pw_input == "prasanti_adikala24":
            st.session_state['logged_in'] = True
            st.rerun()
        else:
            st.sidebar.error("Kunci tidak berjodoh dengan pintu. Selaraskan kembali nalar Anda.")

# Cek Status Login
if not st.session_state['logged_in']:
    st.title("🏛️ LOKAGATRA: LOGIC WORLD")
    st.markdown("### *Peta Peradaban Digital: Menata Masa Depan dari Akar Waktu*")
    st.info("Selamat datang di ambang pintu ilmu. Silakan masukkan identitas Anda pada gerbang di sebelah kiri.")
    login_gerbang()
    st.stop()

# ==========================================
# 3. NAVIGASI PETA PERADABAN (SIDEBAR)
# ==========================================
with st.sidebar:
    st.success("Rahayu, Sang Adikala.")
    st.markdown("---")
    ruang = st.radio("Pilih Ruang Peradaban:", [
        "📚 Ruang Baitul Hikmah",
        "🛠️ Ruang Balai Kerja",
        "🤝 Ruang Majelis Ilmu",
        "🎭 Ruang Sastra & Budaya",
        "🧮 Ruang Alat Bedah & Kalkulator"
    ])
    st.markdown("---")
    if st.button("Tutup Gerbang (Log Out)"):
        st.session_state['logged_in'] = False
        st.rerun()

# ==========================================
# 4. IMPLEMENTASI RUANG-RUANG
# ==========================================

# --- RUANG 1: BAITUL HIKMAH ---
if ruang == "📚 Ruang Baitul Hikmah":
    st.header("📚 Baitul Hikmah (Perpustakaan Abadi)")
    st.markdown("> *Tempat buku-buku yang 'dibakar' bangkit kembali dalam bentuk digital.*")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        with st.expander("📖 Manuskrip Utama (Pustaka Klasik)"):
            st.write("1. **Al-Qanun fit-Tibb** (Ibnu Sina) – Kedokteran")
            st.write("2. **Muqaddimah** (Ibnu Khaldun) – Sosiologi & Sejarah")
            st.write("3. **Al-Jabr** (Al-Khwarizmi) – Matematika & Koding")
            st.write("4. **Ar-Risalah** (Imam Syafi'i) – Logika Hukum")
            st.button("🔄 Aktifkan Fitur 'Indonesiakan' (Translasi AI)")
    
    with col2:
        st.subheader("🔓 Akses Kitab")
        st.caption("Biografi & Ringkasan: Gratis")
        st.info("Download PDF & Analisa: Akses Berbayar (QRIS/Midtrans)")
        st.button("Beli Akses Penuh")

# --- RUANG 2: BALAI KERJA ---
elif ruang == "🛠️ Ruang Balai Kerja":
    st.header("🛠️ Balai Kerja (Freelance & Creative Hub)")
    tab1, tab2, tab3 = st.tabs(["🖋️ Copywriter & Penulis", "🔍 Peneliti & Akademisi", "📊 Data Analyst"])
    
    with tab1:
        st.write("Mode Gelap & Musik Lo-Fi Aktif.")
        st.text_area("Meja Tulis:", placeholder="Tuangkan gagasan Anda di sini...")
        st.button("Hitung Efisiensi Kata")
        
    with tab2:
        st.write("Validasi Sastrawi & Cek Plagiasi.")
        st.file_uploader("Unggah naskah (Dokumen/PDF)")
        
    with tab3:
        st.write("Kalkulator Cerdas & Pemrosesan Data Mentah.")
        st.number_input("Input Data Numerik:")

# --- RUANG 3: MAJELIS ILMU ---
elif ruang == "🤝 Ruang Majelis Ilmu":
    st.header("🤝 Majelis Ilmu (Meeting & Interaksi)")
    st.warning("Aturan Main: Gratis maks. 3 orang (40 menit). Premium via Webhook Midtrans.")
    
    if st.button("Hubungkan ke Jitsi Meet (Video Conference)"):
        st.info("Mengintegrasikan Pintu Meeting...")
        st.markdown("[Klik di Sini untuk Masuk Ruang Rapat]")

# --- RUANG 4: RUANG SASTRA & BUDAYA ---
elif ruang == "🎭 Ruang Sastra & Budaya":
    st.header("🎭 Sastra & Hiburan (Ruang Budaya)")
    st.write("Menghaluskan budi pekerti melalui karya anak bangsa.")
    
    with st.container():
        st.subheader("Koleksi Pilihan")
        c1, c2 = st.columns(2)
        with c1:
            st.write("**📖 Cerpen & Puisi**")
            st.caption("Baca Bab 1-3 Gratis")
            st.button("Buka Lanjutannya (Sedekah Digital/Saweria)")
        with c2:
            st.write("**🎨 Komik Anak Bangsa**")
            st.caption("Sistem Bagi Hasil 70/30")

# --- RUANG 5: ALAT BEDAH ---
elif ruang == "🧮 Ruang Alat Bedah & Kalkulator":
    st.header("🧮 Alat Bedah & Kalkulator Utility")
    tool = st.selectbox("Pilih Alat Bantu:", ["Kalkulator Zakat & Waris", "Cek Plagiasi (Gratis 1x/hari)", "Analisa Narasi (Reading Ease)"])
    
    if tool == "Kalkulator Zakat & Waris":
        st.number_input("Masukkan Nominal Harta:", step=1000)
        st.button("Hitung Distribusi")

# ==========================================
# 5. PENUTUP & FILOSOFI (FOOTER)
# ==========================================
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center;'>
        <p><i>"Apa yang dulu dihancurkan oleh musuh karena rasa takut, hari ini Mas bangun kembali karena rasa cinta pada ilmu."</i></p>
        <small><b>LOGIC WORLD</b> - Khalifah: Hilmi Mulazaman (Prasanti Adikala)</small>
    </div>
    """, 
    unsafe_allow_html=True
)
