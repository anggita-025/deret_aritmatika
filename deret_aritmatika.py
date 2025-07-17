import streamlit as st
import time

def aritmatika_calculator():
    st.title("Kalkulator Deret Aritmatika 🧮")
    st.write("Temukan nilai suku ke-$n$ dari deret aritmatika!")

    st.sidebar.header("Pengaturan Deret")
    a = st.sidebar.number_input("Suku Pertama (a):", value=1, step=1)
    b = st.sidebar.number_input("Beda (b):", value=1, step=1)

    st.header("Menghitung Suku ke-$n$ ($U_n$)")
    n_un = st.number_input("Masukkan nilai $n$ untuk suku ke-$n$:", min_value=1, value=5, step=1)

    if st.button("Hitung Suku ke-$n$"):
        st.write("Menganalisis deret...")
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            progress_bar.progress(percent_complete + 1)
        st.success("Analisis selesai!")

        un_value = a + (n_un - 1) * b
        st.subheader(f"Suku ke-{n_un} ($U_n$) adalah:")
        st.info(f"**$U_n$ = {un_value}**")

        st.markdown("---")

    st.write("Terima kasih telah menggunakan kalkulator deret aritmatika ini!")
    st.balloons() # Animasi balon saat selesai

if __name__ == "__main__":
    aritmatika_calculator()
