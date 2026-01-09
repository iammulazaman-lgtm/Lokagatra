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

# --- TAHAP 1: IMPLEMENTASI BAITUL HIKMAH (DETAILED) ---
if ruang == "📚 Ruang Baitul Hikmah":
    st.header("📚 Baitul Hikmah (Perpustakaan Abadi)")
    st.markdown("> *Menyatukan Akar Klasik dan Nalar Modern untuk Kesembuhan Jiwa.*")
    
    tab_pustaka, tab_premium = st.tabs(["🍃 Jalur Barokah (Gratis)", "💎 Jalur Kedaulatan (Berbayar)"])

    with tab_pustaka:
        st.subheader("Pustaka Umum (Mahar Data Diri)")
        st.write("Silakan pilih kitab untuk dipelajari. Akses dibuka setelah menyetor data diri.")
        
        # Daftar Buku Gratis yang Sudah Dikunci
        buku_gratis = {
            "Man's Search For Meaning - Viktor Frankl": "LINK_GD_FRANKL",
            "Siddharta - Hermann Hesse": "LINK_GD_HESSE",
            "Hujan Bulan Juni - Sapardi Djoko Damono": "LINK_GD_SAPARDI",
            "The Things You Can See Only When You Slow Down - Haemin Sunim": "LINK_GD_HAEMIN",
            "Al-Munqidh min al-Dalal - Al-Ghazali": "LINK_GD_GHAZALI"
        }
        
        pilihan_gratis = st.selectbox("Pilih Kitab Gratis:", list(buku_gratis.keys()))
        
        with st.form("form_santri"):
            st.write("### 📝 Form Mahar Data")
            nama = st.text_input("Nama Lengkap")
            wa = st.text_input("Nomor WhatsApp (Aktif)")
            
            if st.form_submit_button("Buka Kunci Naskah"):
                if nama and wa:
                    st.success(f"Rahayu, {nama}. Data Anda telah tersimpan di lumbung. Silakan unduh melalui tombol di bawah.")
                    st.link_button(f"📥 Unduh {pilihan_gratis}", "https://google.com") # Ganti dengan link Drive asli nanti
                else:
                    st.warning("Mohon isi data diri untuk menghargai nalar penulis.")

    with tab_premium:
        st.subheader("Manuskrip Langka & Bundle Solusi")
        st.info("Naskah ini didapatkan melalui jalur perburuan khusus. Mahar digunakan untuk kedaulatan operasional.")
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown("**📁 Nalar Strategi & Masa Depan**")
            st.write("- 21 Lessons for 21st Century (Harari)")
            st.write("- The Book of Five Rings (Musashi)")
            st.write("- Kitab Tadbir an-Nafs (Ibnu Sina)")
            st.link_button("🔓 Tebus Mahar Naskah", "https://lynk.id/ruangarti")

        with col_b:
            st.markdown("**📁 Bundle Navigasi Jiwa (Poppy's Dream)**")
            st.write("- The Book of Twenties (Anxiety Solution)")
            st.write("- The Book of Dreams (Identity Mapping)")
            st.write("- The Book of Executor (Action Plan)")
            st.link_button("🛍️ Beli Bundle (Rp249rb - Rp349rb)", "https://lynk.id/ruangarti")

# --- RUANG 2: BALAI KERJA ---
elif ruang == "🛠️ Ruang Balai Kerja":
    st.header("🛠️ Balai Kerja (Freelance & Creative Hub)")
    tab1, tab2, tab3 = st.tabs(["🖋️ Editor & Copywriter", "🔍 Peneliti & Akademisi", "📊 Data Analyst"])
    
    with tab1:
        st.write("Alat penyunting naskah dan mesin AIDA.")
        st.text_area("Meja Tulis Editor:", placeholder="Masukkan draf buku Anda...")
        st.button("Cek Kerapihan Bahasa (Readability Index)")
        
    with tab2:
        st.write("Validasi Sastrawi & Cek Plagiasi.")
        st.file_uploader("Unggah naskah untuk cek Turnitin")
        
    with tab3:
        st.write("Kalkulator Cerdas Peradaban.")
        st.number_input("Input Data Numerik:")

# --- RUANG 3: MAJELIS ILMU ---
elif ruang == "🤝 Ruang Majelis Ilmu":
    st.header("🤝 Majelis Ilmu (Meeting & Interaksi)")
    st.warning("Pintu interaksi langsung antar Khalifah.")
    if st.button("Hubungkan ke Jitsi Meet"):
        st.markdown("[Masuk Ruang Rapat]")

# --- RUANG 4: RUANG SASTRA & BUDAYA ---
elif ruang == "🎭 Ruang Sastra & Budaya":
    st.header("🎭 Sastra & Hiburan (Ruang Budaya)")
    st.write("Pencarian Jati Diri melalui Rasa.")
    st.write("- Titik Nol (Agustinus Wibowo)")
    st.button("Buka Koleksi Sastra")

# --- RUANG 5: ALAT BEDAH ---
elif ruang == "🧮 Ruang Alat Bedah & Kalkulator":
    st.header("🧮 Laboratorium Alat Bedah")
    tool = st.selectbox("Pilih Alat Bantu:", ["Kalkulator Zakat & Waris", "Triangulasi Sumber Sejarah", "Analisa Aksara Arkeologi"])
    
    if tool == "Kalkulator Zakat & Waris":
        st.number_input("Masukkan Nominal Harta:", step=1000)
        st.button("Hitung Distribusi")
    elif tool == "Triangulasi Sumber Sejarah":
        st.text_area("Input Sumber Primer:")
        st.text_area("Input Sumber Sekunder:")
        st.button("Bedah Historiografi")

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
