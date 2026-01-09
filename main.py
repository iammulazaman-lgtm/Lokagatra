import streamlit as st

# Pengaturan Judul Halaman
st.set_page_config(page_title="LOKAGATRA", layout="wide")

# Header Utama
st.title("🏛️ LOKAGATRA")
st.markdown("---")

# Area Navigasi Utama (Sidebar)
with st.sidebar:
    st.header("Peta Ruang")
    pilihan = st.radio("Pilih Ruang:", ["Baitul Hikmah", "Workspace", "Finance"])

# Logika Konten Berdasarkan Pilihan
if pilihan == "Baitul Hikmah":
    st.subheader("📚 Ruang Baitul Hikmah (Perpustakaan)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Buka Folder Buku"):
            st.info("Menampilkan daftar manuskrip...")
            st.write("- Sejarah Peradaban Dunia")
            st.write("- Logika Nalar dan Rasa")
            st.write("- Arsip Pemikiran Global")
            
    with col2:
        if st.button("Aktifkan Alat Bedah"):
            st.warning("Alat analisis teks sedang diinisialisasi...")
            st.write("Status: Siap digunakan untuk membedah data.")

elif pilihan == "Workspace":
    st.subheader("🛠️ Ruang Kerja (Workspace)")
    
    if st.button("Buka Meja Kerja"):
        st.success("Meja kerja digital telah disiapkan.")
        st.write("Daftar Proyek Aktif:")
        st.checkbox("Penyusunan Kurikulum")
        st.checkbox("Analisis Data Wilayah")

elif pilihan == "Finance":
    st.subheader("💰 Manajemen Finance")
    
    if st.button("Lihat Laporan"):
        st.table({
            "Kategori": ["Operasional", "Pengembangan", "Cadangan"],
            "Status": ["Aman", "Berjalan", "Tersedia"]
        })

# Footer
st.markdown("---")
st.caption("Lokagatra - Mengalirkan Ilmu, Menata Peradaban.")
