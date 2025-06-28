# aritmatika_app.py
import streamlit as st
import time

def aritmatika_calculator():
    st.title("Kalkulator Deret Aritmatika 🧮")
    st.write("Temukan nilai suku ke-n atau jumlah n suku pertama dari deret aritmatika!")

    st.sidebar.header("Pengaturan Deret")
    a = st.sidebar.number_input("Suku Pertama (a):", value=1, step=1)
    b = st.sidebar.number_input("Beda (b):", value=1, step=1)

    st.header("1. Menghitung Suku ke-n (Un)")
    n_un = st.number_input("Masukkan nilai n untuk suku ke-n:", min_value=1, value=5, step=1)

    if st.button("Hitung Suku ke-n"):
        st.write("Menganalisis deret...")
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            progress_bar.progress(percent_complete + 1)
        st.success("Analisis selesai!")

        un_value = a + (n_un - 1) * b
        st.subheader(f"Suku ke-{n_un} (Un) adalah:")
        st.info(f"**Un = {un_value}**")

        st.markdown("---")

    st.header("2. Menghitung Jumlah n Suku Pertama (Sn)")
    n_sn = st.number_input("Masukkan nilai n untuk jumlah n suku pertama:", min_value=1, value=5, step=1)

    if st.button("Hitung Jumlah n Suku Pertama"):
        st.write("Menghitung total jumlah...")
        with st.spinner('Sedang menghitung...'):
            time.sleep(2) # Simulasi perhitungan yang memakan waktu
        st.success("Perhitungan selesai!")

        sn_value = (n_sn / 2) * (2 * a + (n_sn - 1) * b)
        st.subheader(f"Jumlah {n_sn} suku pertama (Sn) adalah:")
        st.info(f"**Sn = {sn_value}**")

        st.markdown("---")

    st.write("Terima kasih telah menggunakan kalkulator deret aritmatika ini!")
    st.balloons() # Animasi balon saat selesai

if __name__ == "__main__":
    aritmatika_calculator()
