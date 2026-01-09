import streamlit as st

# ==========================================
# 1. KONFIGURASI PONDASI (HEADER)
# ==========================================
st.set_page_config(
    page_title="LOGIC WORLD - PRASANTI ADIKALA",
    layout="wide",
    page_icon="🏛️"
)

# Custom Styling untuk Kewibawaan Visual
st.markdown("""
    <style>
    .stApp { background-color: #fcfcfc; }
    .kurasi-box {
        padding: 15px;
        border-left: 5px solid #1e3d59;
        background-color: #f0f4f7;
        margin-bottom: 10px;
        border-radius: 0px 10px 10px 0px;
    }
    .jurnal-card {
        padding: 15px;
        border: 1px solid #d1d1d1;
        border-radius: 10px;
        background-color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. SISTEM KEAMANAN GERBANG
# ==========================================
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def login_gerbang():
    st.sidebar.title("🏛️ Gerbang Prasanti")
    st.sidebar.markdown("---")
    user_input = st.sidebar.text_input("Identitas Sansekerta (Username)")
    pw_input = st.sidebar.text_input("Kunci Adikala (Password)", type="password")
    
    if st.sidebar.button("Buka Gerbang Peradaban"):
        if user_input == "PRASANTI_ADIKALA" and pw_input == "prasanti_adikala24":
            st.session_state['logged_in'] = True
            st.rerun()
        else:
            st.sidebar.error("Kunci tidak berjodoh dengan pintu.")

if not st.session_state['logged_in']:
    st.title("🏛️ LOKAGATRA: LOGIC WORLD")
    st.markdown("### *Menata Masa Depan dari Akar Waktu*")
    st.info("Silakan masukkan identitas Anda pada gerbang di sebelah kiri.")
    login_gerbang()
    st.stop()

# ==========================================
# 3. NAVIGASI PETA PERADABAN
# ==========================================
with st.sidebar:
    st.success("Rahayu, Sang Adikala.")
    st.markdown("---")
    ruang = st.radio("Pilih Ruang Peradaban:", [
        "📚 Baitul Hikmah (Rekomendasi Adikala)",
        "📊 Ruang Riset & Jurnal Ilmiah",
        "🛠️ Balai Kerja"
    ])
    st.markdown("---")
    if st.button("Log Out"):
        st.session_state['logged_in'] = False
        st.rerun()

# ==========================================
# 4. IMPLEMENTASI RUANG-RUANG
# ==========================================

# --- RUANG 1: BAITUL HIKMAH (KURASI REKOMENDASI) ---
if ruang == "📚 Baitul Hikmah (Rekomendasi Adikala)":
    st.header("📚 Baitul Hikmah - Kurasi Rekomendasi Sang Adikala")
    st.markdown("> *Ilmu bukan untuk dihafal, tapi untuk membedah realitas.*")
    st.markdown("---")

    # KATEGORI GOLDEN AGE
    st.subheader("🌙 Naskah Klasik Zaman Keemasan")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='kurasi-box'><b>📖 Al-Qanun fit-Thibb (Ibnu Sina)</b><br><small><i>Catatan Nalar:</i> Fokus pada bagaimana Ibnu Sina melakukan triangulasi antara logika dan observasi klinis.</small></div>", unsafe_allow_html=True)
        st.link_button("📄 Buka Naskah Otentik", "https://archive.org/details/al-qanun-fit-tibb-lengkap")

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("<div class='kurasi-box'><b>📖 Tahafut al-Falasifah (Al-Ghazali)</b><br><small><i>Catatan Nalar:</i> Bedah nalar kritik filosofis untuk menjaga kejernihan akidah dan logika.</small></div>", unsafe_allow_html=True)
        st.link_button("📄 Buka Naskah Otentik", "https://archive.org/details/TahafutAlFalasifahAlGhazaliTerjemah")

    with col2:
        st.markdown("<div class='kurasi-box'><b>📖 Kitab Al-Jabr (Al-Khwarizmi)</b><br><small><i>Catatan Nalar:</i> Dasar dari segala algoritma digital hari ini. Nalar matematika Islam.</small></div>", unsafe_allow_html=True)
        st.link_button("📄 Buka Naskah Otentik", "https://archive.org/details/TheAlgebraOfMohammedBenMusa")

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("<div class='kurasi-box'><b>📖 Muqaddimah (Ibnu Khaldun)</b><br><small><i>Catatan Nalar:</i> Memahami siklus peradaban dan sosiologi kekuasaan secara objektif.</small></div>", unsafe_allow_html=True)
        st.link_button("📄 Buka Naskah Otentik", "https://archive.org/download/BukuMuqaddimahIbnuKhaldun/Buku%20Muqaddimah%20Ibnu%20Khaldun.pdf")

    st.divider()

    # KATEGORI MODERN & PSIKOLOGI
    st.subheader("🌍 Nalar Modern & Fakta Teruji")
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("<div class='kurasi-box'><b>📖 Man's Search for Meaning (Viktor Frankl)</b><br><small><i>Catatan Nalar:</i> Fakta sejarah kamp konsentrasi yang melahirkan ilmu ketangguhan jiwa.</small></div>", unsafe_allow_html=True)
        st.link_button("📄 Buka Terjemahan Indo", "https://archive.org/download/mans-search-for-meaning-pdf-bahasa-indonesia/Viktor%20Frankl%20-%20Man%27s%20Search%20For%20Meaning.pdf")

    with c2:
        st.markdown("<div class='kurasi-box'><b>📖 Orientalism (Edward Said)</b><br><small><i>Catatan Nalar:</i> Kritik sejarah yang diakui dunia. Membedah cara Barat melihat Timur.</small></div>", unsafe_allow_html=True)
        st.link_button("📄 Buka Naskah", "https://archive.org/details/Orientalism_201710")

# --- RUANG 2: RUANG RISET (JURNAL ILMIAH) ---
elif ruang == "📊 Ruang Riset & Jurnal Ilmiah":
    st.header("📊 Navigator Riset & Fakta Dunia")
    st.write("Akses langsung ke hasil penelitian yang diakui dunia dan teruji fakta sejarahnya.")
    
    tab_search, tab_repo = st.tabs(["🔍 Pencarian Jurnal", "🏛️ Repository Pilihan"])
    
    with tab_search:
        topik = st.text_input("Ketik Bidang Keilmuan (Misal: Arkeologi Islam, Neuroains, Sejarah Ekonomi):")
        if topik:
            st.link_button(f"🌐 Cari Jurnal Ilmiah di CORE", f"https://core.ac.uk/search?q={topik}")
            st.link_button(f"🏛️ Cari Riset Terakreditasi di Google Scholar", f"https://scholar.google.com/scholar?q={topik}")

    with tab_repo:
        st.markdown("""
        <div class='jurnal-card'>
        <b>📌 Rekomendasi Sumber Riset:</b><br>
        1. <b>JSTOR:</b> Arsip jurnal sejarah dan kemanusiaan dunia.<br>
        2. <b>Nature Journal:</b> Fakta sains dan biologi teruji.<br>
        3. <b>UNESCO Silk Road Project:</b> Data otentik pertukaran ilmu lintas peradaban.
        </div>
        """, unsafe_allow_html=True)

# --- RUANG 3: BALAI KERJA ---
elif ruang == "🛠️ Balai Kerja":
    st.header("🛠️ Balai Kerja")
    st.text_area("Meja Tulis Adikala:", placeholder="Tuangkan analisis keilmuan Anda di sini...", height=400)

# ==========================================
# 5. FOOTER
# ==========================================
st.markdown("---")
st.markdown("<center><small>LOGIC WORLD - Kurasi & Rekomendasi: Hilmi Mulazaman (Prasanti Adikala)</small></center>", unsafe_allow_html=True)
