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
    
    user_input = st.sidebar.text_input("Identitas Sansekerta (Username)")
    pw_input = st.sidebar.text_input("Kunci Adikala (Password)", type="password")
    
    if st.sidebar.button("Buka Gerbang Peradaban"):
        if user_input == "PRASANTI_ADIKALA" and pw_input == "prasanti_adikala24":
            st.session_state['logged_in'] = True
            st.rerun()
        else:
            st.sidebar.error("Kunci tidak berjodoh dengan pintu. Selaraskan kembali nalar Anda.")

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

# --- RUANG 1: BAITUL HIKMAH (GLOBAL NAVIGATOR) ---
if ruang == "📚 Ruang Baitul Hikmah":
    st.header("📚 Baitul Hikmah - Global Navigator")
    st.markdown("> *Menghubungkan nalar ke seluruh samudera ilmu di jagat digital.*")
    
    # FITUR PENCARIAN OTOMATIS GLOBAL
    st.subheader("🔍 Navigator Pengetahuan")
    query = st.text_input("Masukkan Judul Buku, Jurnal, atau Nama Ilmuwan:", placeholder="Contoh: Ibnu Sina, Harari, Musashi...")
    
    if query:
        st.markdown(f"### Hasil Navigasi untuk: *{query}*")
        col_search1, col_search2 = st.columns(2)
        
        with col_search1:
            st.info("🍃 Jalur Pustaka & Naskah (Gratis/Publik)")
            st.write("Mencari di Perpustakaan Digital, Archive.org, dan Repository Ilmiah.")
            st.link_button(f"Cari PDF '{query}' di Dunia", f"https://www.google.com/search?q={query}+filetype:pdf+manuscript+archive")
            
        with col_search2:
            st.warning("🛒 Jalur Gerai Resmi (Berbayar/Shopping)")
            st.write("Mencari di Toko Buku Resmi, Gramedia, Mizan, dan Google Shopping.")
            st.link_button(f"Cek Harga '{query}' di Shopping", f"https://www.google.com/search?tbm=shop&q={query}+buku+original")

    st.divider()

    tab_pustaka, tab_premium = st.tabs(["🍃 Koleksi Barokah (Locked)", "💎 Manuskrip & Bundle Khusus"])

    with tab_pustaka:
        st.subheader("Pustaka Terpilih (Mahar Data Diri)")
        buku_gratis = {
            "Man's Search For Meaning - Viktor Frankl": "https://archive.org/details/manssearchformeaning_202001",
            "Siddharta - Hermann Hesse": "https://www.gutenberg.org/ebooks/500",
            "The Things You Can See Only When You Slow Down - Haemin Sunim": "https://www.google.com/search?q=Haemin+Sunim+PDF+Public",
            "Al-Munqidh min al-Dalal - Al-Ghazali": "https://archive.org/details/al-ghazali-deliverance-from-error",
            "Muqaddimah - Ibnu Khaldun": "https://archive.org/details/MuqaddimahIbnuKhaldun"
        }
        pilihan_gratis = st.selectbox("Pilih Kitab Gratis:", list(buku_gratis.keys()))
        
        with st.form("form_santri"):
            st.write("### 📝 Form Mahar Data")
            nama = st.text_input("Nama Lengkap")
            wa = st.text_input("Nomor WhatsApp (Aktif)")
            if st.form_submit_button("Buka Kunci Naskah"):
                if nama and wa:
                    st.success(f"Rahayu, {nama}. Kunci telah dibuka.")
                    st.link_button(f"📥 Unduh {pilihan_gratis}", buku_gratis[pilihan_gratis])
                else:
                    st.warning("Mohon isi data diri untuk menghargai nalar penulis.")

    with tab_premium:
        st.subheader("Manuskrip Langka & Produk Kedaulatan")
        st.info("Naskah modern dengan hak cipta ketat dan produk spesialisasi.")
        
        c_a, c_b = st.columns(2)
        with c_a:
            st.markdown("**🏛️ Nalar Strategi & Masa Depan**")
            st.caption("Akses langsung ke Shopping & Shopping Navigator")
            st.write("- 21 Lessons (Harari)")
            st.write("- Five Rings (Musashi)")
            st.write("- Tadbir an-Nafs (Ibnu Sina)")
            st.link_button("🛒 Cari Harga Terbaik di Gramedia", "https://www.gramedia.com/search?q=harari+musashi")

        with c_b:
            st.markdown("**🌸 Bundle Navigasi Jiwa (Poppy's Dream)**")
            st.caption("Produk Teruji & Jurnal Spesialis")
            st.write("- The Book of Twenties, Dreams, & Executor")
            st.link_button("🛍️ Tebus Mahar di Ruang Arti", "https://lynk.id/ruangarti")

# --- RUANG 2: BALAI KERJA ---
elif ruang == "🛠️ Ruang Balai Kerja":
    st.header("🛠️ Balai Kerja (Freelance & Creative Hub)")
    tab1, tab2, tab3 = st.tabs(["🖋️ Editor & Copywriter", "🔍 Peneliti & Akademisi", "📊 Data Analyst"])
    with tab1:
        st.text_area("Meja Tulis Editor:", placeholder="Masukkan draf buku Anda...")
        st.button("Cek Kerapihan Bahasa (AIDA Structure)")
    with tab2:
        st.file_uploader("Unggah naskah untuk cek Plagiasi/Turnitin")
    with tab3:
        st.write("Kalkulator Cerdas Peradaban.")
        st.number_input("Input Data Numerik:")

# --- RUANG 3: MAJELIS ILMU ---
elif ruang == "🤝 Ruang Majelis Ilmu":
    st.header("🤝 Majelis Ilmu (Meeting & Interaksi)")
    if st.button("Hubungkan ke Jitsi Meet"):
        st.markdown("[Masuk Ruang Rapat]")

# --- RUANG 4: RUANG SASTRA & BUDAYA ---
elif ruang == "🎭 Ruang Sastra & Budaya":
    st.header("🎭 Sastra & Hiburan (Ruang Budaya)")
    st.write("Karya terpilih yang menyentuh akar rasa.")
    st.write("- Titik Nol (Agustinus Wibowo)")
    st.write("- Hujan Bulan Juni (Sapardi Djoko Damono)")
    st.link_button("🔍 Cari Karya Sastra Lainnya", "https://www.google.com/search?tbm=shop&q=buku+sastra+indonesia")

# --- RUANG 5: ALAT BEDAH ---
elif ruang == "🧮 Ruang Alat Bedah & Kalkulator":
    st.header("🧮 Laboratorium Alat Bedah")
    tool = st.selectbox("Pilih Alat Bantu:", ["Kalkulator Zakat & Waris", "Triangulasi Sumber Sejarah", "Analisa Aksara Arkeologi"])
    if tool == "Kalkulator Zakat & Waris":
        st.number_input("Masukkan Nominal Harta:", step=1000)
        st.button("Hitung Distribusi")
    elif tool == "Triangulasi Sumber Sejarah":
        st.text_area("Input Sumber Primer:")
        st.button("Bedah Historiografi")

# ==========================================
# 5. PENUTUP & FILOSOFI (FOOTER)
# ==========================================
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center;'>
        <p><i>"Apa yang dulu dihancurkan karena rasa takut, hari ini dibangun kembali karena cinta pada ilmu."</i></p>
        <small><b>LOGIC WORLD</b> - Khalifah: Hilmi Mulazaman (Prasanti Adikala)</small>
    </div>
    """, 
    unsafe_allow_html=True
)
