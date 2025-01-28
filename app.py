import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Memuat data(csv)
data = pd.read_csv("supermarket_sales.csv")

# Judul dan deskripsi
st.title("Supermarket Sales Dashboard")
st.markdown("""
    **Dashboard ini membantu kamu menganalisis data penjualan supermarket.**
    
    Fitur yang tersedia:
    - Tabel data dengan opsi pencarian dan filter
    - Visualisasi data seperti distribusi penjualan dan pendapatan
""")

# Sidebar untuk filter
st.sidebar.header("Filter Data")
branch = st.sidebar.multiselect("Pilih Cabang:", options=data["Branch"].unique(), default=data["Branch"].unique())
city = st.sidebar.multiselect("Pilih Kota:", options=data["City"].unique(), default=data["City"].unique())
customer_type = st.sidebar.multiselect("Tipe Pelanggan:", options=data["Customer type"].unique(), default=data["Customer type"].unique())

# Terapkan filter
filtered_data = data[(data["Branch"].isin(branch)) &
                     (data["City"].isin(city)) &
                     (data["Customer type"].isin(customer_type))]

# Tampilkan data
tab1, tab2 = st.tabs(["Tabel Data", "Visualisasi"])

with tab1:
    st.subheader("Tabel Data")
    st.dataframe(filtered_data)

with tab2:
    st.subheader("Visualisasi")
    # Distribusi Total Penjualan
    st.markdown("### Distribusi Total Penjualan")
    fig, ax = plt.subplots()
    filtered_data['Total'].hist(bins=30, ax=ax, color='skyblue', edgecolor='black')
    ax.set_title("Distribusi Total Penjualan")
    ax.set_xlabel("Total Penjualan")
    ax.set_ylabel("Frekuensi")
    st.pyplot(fig)

    # Peringkat Rata-rata berdasarkan Lini Produk
    st.markdown("### Rata-rata Rating per Produk")
    avg_rating = filtered_data.groupby('Product line')['Rating'].mean().sort_values()
    fig, ax = plt.subplots()
    avg_rating.plot(kind='barh', ax=ax, color='salmon', edgecolor='black')
    ax.set_title("Rata-rata Rating per Produk")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Kategori Produk")
    st.pyplot(fig)

st.sidebar.markdown("---")
st.sidebar.write(f"Jumlah data setelah filter: {len(filtered_data)} dari {len(data)} total data.")
