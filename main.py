import streamlit as st

# ==========================================
# I. ESTETIKA: REPOSITORY PERADABAN (GITHUB MODE)
# ==========================================
st.set_page_config(page_title="LOKAGATRA.id / Repository", page_icon="💠", layout="wide")

st.markdown("""
    <style>
    /* Karakter Visual Minimalis & Berwibawa */
    .main { background-color: #ffffff; color: #1F2328; font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif; }
    .repo-header { background-color: #F6F8FA; border-bottom: 1px solid #D0D7DE; padding: 20px 40px; margin: -60px -40px 20px -40px; }
    
    /* Navigasi Tab Ala GitHub */
    .stTabs [data-baseweb="tab-list"] { gap: 24px; border-bottom: 1px solid #D0D7DE; background-color: #F6F8FA; padding: 0 40px; }
    .stTabs [data-baseweb="tab"] { height: 45px; font-weight: 600; color: #57606A; border: none; }
    .stTabs [aria-selected="true"] { color: #1F2328; border-bottom: 2px solid #FD8C73 !important; }
    
    /* Kartu & Tombol */
    .neumorph-card { border: 1px solid #D0D7DE; border-radius: 6px; padding: 20px; background-color: #ffffff; margin-bottom: 15px; }
    .stButton>button { background-color: #2DA44E; color: white; border-radius: 6px; border: 1px solid rgba(27,31,36,0.15); font-weight: 600; transition: 0.2s; }
    .stButton>button:hover { background-color: #2C974B; border-color: rgba(27,31,36,0.15); }
    
    /* Tombol Hapus (Danger Zone) */
    div[data-testid="stColumn"]:nth-child(2) .stButton>button { background-color: #CF222E; }
    div[data-testid="stColumn"]:nth-child(2) .stButton>button:hover { background-color: #A40E26; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# II. SISTEM MEMORI & IDENTITAS (SSO SIMULASI)
# ==========================================
if 'user' not in st.session_state: st.session_state.user = None
if 'lumbung_ide' not in st.session_state: st.session_state.lumbung_ide = []

# Pintu Masuk Google (Simulasi Logic)
if not st.session_state.user:
    st.markdown("<div style='text-align:center; padding:100px 0;'><h1>💠 LOKAGATRA.id</h1><p style='color:#57606A;'>Pusat Data & Nalar Peradaban Digital</p></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Masuk dengan Akun Google", use_container_width=True):
            st.session_state.user = "Khalifah_User"
            st.rerun()
    st.stop()

# ==========================================
# III. HEADER REPOSITORY (KEDAULATAN)
# ==========================================
st.markdown(f"""<div class="repo-header"><span style="color: #0969DA;">iammulazaman-lgtm / </span><b>Lokagatra.id</b> <span style="border: 1px solid #D0D7DE; padding: 2px 8px; border-radius: 20px; font-size: 12px; vertical-align:middle; margin-left:10px;">Public</span></div>""", unsafe_allow_html=True)

# ==========================================
# IV. STRUKTUR PINTU BERKELANA (TABS)
# ==========================================
tab_code, tab_work, tab_finance = st.tabs(["📁 Ruang Ilmu (Library)", "📝 Workspace (Lumbung Ide)", "💰 Finance (Kedaulatan)"])

# --- TAB 1: EKSPLORASI BUKU & ANALISA ---
with tab_code:
    st.markdown("### **Repository / Peradaban / Peta Ilmu**")
    st.write("Jelajahi folder-folder hikmah di bawah ini:")
    
    col_a, col_b = st.columns(2)
    with col_a:
        with st.container():
            st.markdown("<div class='neumorph-card'><b>📚 Baitul Hikmah</b><br>Manuskrip Klasik, Sejarah Dunia, & Pola Nasib.</div>", unsafe_allow_html=True)
            if st.button("Buka Folder Buku"):
                st.info("Membuka Pintu Baitul Hikmah... (Daftar PDF akan muncul di sini)")
    
    with col_b:
        with st.container():
            st.markdown("<div class='neumorph-card'><b>🔬 Alat Bedah Data</b><br>Kalkulator presisi dan validasi narasi.</div>", unsafe_allow_html=True)
            if st.button("Aktifkan Alat Bedah"):
                st.info("Mesin Analisa siap digunakan.")

# --- TAB 2: TEMPAT PENYIMPANAN IDE & HAPUS SAMPAH ---
with tab_work:
    st.header("Baitul Mal Ide")
    st.write("Simpan lintasan pikiran atau hasil analisa data Mas di bawah ini.")
    
    # Input Area
    with st.container():
        input_ide = st.text_area("Tulis ide atau catatan analisa:", placeholder="Ketik di sini...", height=150)
        if st.button("Simpan ke Memori Repository"):
            if input_ide:
                st.session_state.lumbung_ide.append(input_ide)
                st.success("Ide berhasil dikunci dalam lumbung.")
                st.rerun()

    st.markdown("---")
    st.subheader("Manajemen Catatan (Pembersihan Sampah)")
    
    if not st.session_state.lumbung_ide:
        st.caption("Belum ada ide yang disimpan. Ruang kerja masih bersih.")
    else:
        for i, ide in enumerate(st.session_state.lumbung_ide):
            c1, c2 = st.columns([6, 1])
            c1.markdown(f"<div class='neumorph-card'>{ide}</div>", unsafe_allow_html=True)
            if c2.button("🗑️ Hapus", key=f"hapus_{i}"):
                st.session_state.lumbung_ide.pop(i)
                st.rerun()

# --- TAB 3: KABEL KEUANGAN ---
with tab_finance:
    st.header("Kedaulatan Ekonomi")
    st.markdown("""
        <div class='neumorph-card'>
        <b>Kemandirian Adalah Kunci.</b><br>
        Dukung pengembangan LOKAGATRA untuk membuka lebih banyak akses manuskrip langka.
        </div>
    """, unsafe_allow_html=True)
    st.link_button("💖 Sponsori via QRIS / Midtrans", "https://link-pembayaran-mas-hilmi.com")

# ==========================================
# V. PUNGKASAN (SIDEBAR INFO)
# ==========================================
st.sidebar.markdown(f"Status: **Connected**")
st.sidebar.write(f"Sesi: **{st.session_state.user}**")
st.sidebar.markdown("---")
if st.sidebar.button("Keluar (Logout)"):
    st.session_state.user = None
    st.rerun()
