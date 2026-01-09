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

# --- RUANG 1: BAITUL HIKMAH (MURNI NAVIGASI GLOBAL) ---
if ruang == "📚 Ruang Baitul Hikmah":
    st.header("📚 Baitul Hikmah - Navigator Ilmu Merdeka")
    st.markdown("> *Akses terbuka menuju warisan peradaban tanpa sekat.*")
    
    # 1. JALUR BAROKAH (DOMAIN PUBLIK / GRATIS)
    st.subheader("🍃 Jalur Barokah (Naskah Warisan Publik)")
    st.write("Naskah-naskah ini adalah milik peradaban manusia, tersedia gratis melalui lembaga legal dunia.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("**Al-Munqidh min al-Dalal** (Imam Al-Ghazali)")
        st.caption("Status: Domain Publik")
        st.link_button("🌐 Akses via Archive.org", "https://archive.org/details/al-ghazali-deliverance-from-error")
        
        st.info("**Siddharta** (Hermann Hesse)")
        st.caption("Status: Creative Commons")
        st.link_button("🌐 Akses via Project Gutenberg", "https://www.gutenberg.org/ebooks/500")

        st.info("**Tadbir an-Nafs** (Ibnu Sina)")
        st.caption("Status: Manuskrip Klasik")
        st.link_button("🌐 Akses Digital Library", "https://www.google.com/search?q=Tadbir+an-Nafs+Ibnu+Sina+manuscript+digital+library")

    with col2:
        st.info("**Man's Search for Meaning** (Viktor E. Frankl)")
        st.caption("Status: E-book Terbuka")
        st.link_button("🌐 Akses Repository Ilmu", "https://archive.org/details/manssearchformeaning_202001")

        st.info("**Muqaddimah** (Ibnu Khaldun)")
        st.caption("Status: Domain Publik")
        st.link_button("🌐 Akses Perpustakaan Dunia", "https://archive.org/details/MuqaddimahIbnuKhaldun")

    st.markdown("---")

    # 2. JALUR KEDAULATAN (PENCARIAN SHOPPING OTOMATIS)
    st.subheader("🛒 Jalur Kedaulatan (Navigator Belanja Resmi)")
    st.write("Untuk karya modern dengan hak cipta, sistem akan mencarikan gerai resmi dengan harga terbaik.")
    
    cari_buku = st.text_input("Ketik Judul Buku (Harari, Musashi, Sapardi, Haemin Sunim, dll):")
    
    if cari_buku:
        c1, c2 = st.columns(2)
        with c1:
            st.link_button(f"🛍️ Cari '{cari_buku}' di Gramedia", f"https://www.gramedia.com/search?q={cari_buku}")
        with c2:
            st.link_button(f"🔍 Cek Harga '{cari_buku}' di Google Shopping", f"https://www.google.com/search?tbm=shop&q=buku+original+{cari_buku}")
    else:
        st.caption("Masukkan judul untuk mulai berburu naskah resmi.")

# --- RUANG-RUANG LAINNYA (TETAP PADA POLA RITME MAS) ---
elif ruang == "🛠️ Ruang Balai Kerja":
    st.header("🛠️ Balai Kerja")
    st.write("Fokus pada nalar eksekusi.")
    st.text_area("Meja Tulis:", placeholder="Gunakan nalar The Book of Executor di sini...")

elif ruang == "🧮 Ruang Alat Bedah & Kalkulator":
    st.header("🧮 Laboratorium Alat Bedah")
    st.write("Bedah historiografi dan arkeologi secara saintifik.")
    st.button("Mulai Analisa Triangulasi")

# ==========================================
# 5. PENUTUP & FILOSOFI (FOOTER)
# ==========================================
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center;'>
        <p><i>"Nalar tidak boleh dipenjara. Ilmu harus menemukan jalannya sendiri ke tangan para pencarinya."</i></p>
        <small><b>LOGIC WORLD</b> - Khalifah: Hilmi Mulazaman (Prasanti Adikala)</small>
    </div>
    """, 
    unsafe_allow_html=True
)
