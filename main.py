import streamlit as st

# ==========================================
# 1. KONFIGURASI PONDASI (HEADER)
# ==========================================
st.set_page_config(
    page_title="LOGIC WORLD - PRASANTI ADIKALA",
    layout="wide",
    page_icon="🏛️"
)

# CSS Custom untuk mempercantik tampilan agar lebih berwibawa
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #1e3d59;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. SISTEM KEAMANAN GERBANG (AUTHENTICATION)
# ==========================================
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def login_gerbang():
    st.sidebar.title("🏛️ Gerbang Prasanti")
    st.sidebar.markdown("---")
    st.sidebar.markdown("*“Hanya nalar yang jernih yang mampu menyentuh akar waktu.”*")
    
    user_input = st.sidebar.text_input("Identitas Sansekerta (Username)")
    pw_input = st.sidebar.text_input("Kunci Adikala (Password)", type="password")
    
    if st.sidebar.button("Buka Gerbang Peradaban"):
        # Username: PRASANTI_ADIKALA | Password: prasanti_adikala24
        if user_input == "PRASANTI_ADIKALA" and pw_input == "prasanti_adikala24":
            st.session_state['logged_in'] = True
            st.rerun()
        else:
            st.sidebar.error("Kunci tidak berjodoh. Selaraskan kembali nalar Anda.")

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
        "🧮 Ruang Alat Bedah & Kalkulator"
    ])
    st.markdown("---")
    if st.button("Tutup Gerbang (Log Out)"):
        st.session_state['logged_in'] = False
        st.rerun()

# ==========================================
# 4. IMPLEMENTASI RUANG-RUANG
# ==========================================

# --- RUANG 1: BAITUL HIKMAH (NAVIGATOR TERJEMAHAN) ---
if ruang == "📚 Ruang Baitul Hikmah":
    st.header("📚 Baitul Hikmah - Navigator Terjemahan Indonesia")
    st.markdown("> *Menemukan kembali nalar yang hilang dalam bahasa yang kita pahami.*")
    st.markdown("---")

    # DAFTAR NASKAH (OTOMATIS MENCARI VERSI INDONESIA)
    st.subheader("🍃 Jalur Pustaka Terjemahan (Warisan Publik)")
    st.write("Sistem akan melacak versi Bahasa Indonesia dari naskah-naskah maestro dunia:")

    naskah_data = {
        "Al-Munqidh min al-Dalal": ["Imam Al-Ghazali", "Terjemahan+Indonesia+Al-Munqidh+min+al-Dalal+PDF"],
        "Tadbir an-Nafs": ["Ibnu Sina (Avicenna)", "Terjemahan+Indonesia+Tadbir+an-Nafs+Ibnu+Sina+PDF"],
        "Muqaddimah": ["Ibnu Khaldun", "Terjemahan+Muqaddimah+Ibnu+Khaldun+PDF+Indonesia"],
        "Siddharta": ["Hermann Hesse", "Siddharta+Hermann+Hesse+Bahasa+Indonesia+PDF"],
        "Man's Search for Meaning": ["Viktor E. Frankl", "Man%27s+Search+for+Meaning+Bahasa+Indonesia+PDF"],
        "The Book of Five Rings": ["Miyamoto Musashi", "The+Book+of+Five+Rings+Bahasa+Indonesia+PDF"],
        "The Things You Can See...": ["Haemin Sunim", "Haemin+Sunim+The+Things+You+Can+See+Only+When+You+Slow+Down+Bahasa+Indonesia+PDF"]
    }

    for judul, info in naskah_data.items():
        with st.container():
            col_buku, col_tombol = st.columns([3, 1])
            with col_buku:
                st.markdown(f"📖 **{judul}**")
                st.caption(f"Karya: {info[0]}")
            with col_tombol:
                st.link_button("🇮🇩 Cari Terjemahan", f"https://www.google.com/search?q={info[1]}")
            st.markdown("---")

    # NAVIGATOR SHOPPING (BELANJA RESMI)
    st.subheader("🛒 Jalur Kedaulatan (Navigator Belanja Resmi)")
    st.write("Mencari gerai resmi untuk buku fisik asli (Harari, Musashi, Sapardi, Agustinus Wibowo, dll).")
    
    cari_belanja = st.text_input("Ketik Judul Buku untuk Cek Harga di Gramedia/Marketplace:")
    if cari_belanja:
        st.link_button(f"🔎 Cari Harga Terbaik '{cari_belanja}'", f"https://www.google.com/search?tbm=shop&q=buku+original+{cari_belanja}")

# --- RUANG 2: BALAI KERJA ---
elif ruang == "🛠️ Ruang Balai Kerja":
    st.header("🛠️ Balai Kerja (Creative & Freelance Hub)")
    st.write("Fokus pada nalar eksekusi dan karya.")
    
    tab_editor, tab_analisa = st.tabs(["🖋️ Meja Editor", "📊 Analisa Kerja"])
    with tab_editor:
        st.text_area("Meja Tulis:", placeholder="Tuangkan gagasan nalar Anda di sini...", height=300)
        st.button("Hitung Ritme Kata")
    with tab_analisa:
        st.file_uploader("Unggah draf untuk pengecekan pola nalar.")

# --- RUANG 3: ALAT BEDAH ---
elif ruang == "🧮 Ruang Alat Bedah & Kalkulator":
    st.header("🧮 Laboratorium Alat Bedah")
    st.write("Gunakan alat ini untuk membedah data dan sejarah secara presisi.")
    
    opsi_alat = st.selectbox("Pilih Alat:", ["Triangulasi Sumber Sejarah", "Analisa Aksara Arkeologi", "Kalkulator Zakat & Waris"])
    
    if opsi_alat == "Triangulasi Sumber Sejarah":
        st.subheader("Metode Triangulasi")
        st.text_area("Sumber A (Kolonial/Asing):")
        st.text_area("Sumber B (Lokal/Tradisi):")
        st.text_area("Sumber C (Data Arkeologi):")
        st.button("Bedah Korelasi")

# ==========================================
# 5. PENUTUP & FILOSOFI (FOOTER)
# ==========================================
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center;'>
        <p><i>"Nalar tidak boleh dipenjara. Ia harus menemukan jalannya sendiri dalam bahasa yang dimengerti oleh hati."</i></p>
        <small><b>LOGIC WORLD</b> - Khalifah: Hilmi Mulazaman (Prasanti Adikala)</small>
    </div>
    """, 
    unsafe_allow_html=True
)
