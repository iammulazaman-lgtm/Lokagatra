import streamlit as st

st.set_page_config(page_title="LOKAGATRA", layout="wide")

st.title("🏛️ LOKAGATRA")
st.markdown("---")

with st.sidebar:
    st.header("Peta Ruang")
    pilihan = st.radio("Pilih Ruang:", ["Baitul Hikmah", "Workspace", "Finance"])

if pilihan == "Baitul Hikmah":
    st.subheader("📚 Ruang Baitul Hikmah")
    if st.button("Buka Folder Buku"):
        st.info("Menampilkan daftar manuskrip...")
        st.write("- Sejarah Peradaban Dunia")
        st.write("- Logika Nalar dan Rasa")
            
elif pilihan == "Workspace":
    st.subheader("🛠️ Ruang Kerja")
    if st.button("Buka Meja Kerja"):
        st.success("Meja kerja digital telah disiapkan.")

elif pilihan == "Finance":
    st.subheader("💰 Manajemen Finance")
    if st.button("Lihat Laporan"):
        st.table({"Kategori": ["Operasional"], "Status": ["Aman"]})

st.markdown("---")
st.caption("Lokagatra - Mengalirkan Ilmu, Menata Peradaban.")
