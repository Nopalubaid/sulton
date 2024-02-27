import streamlit as st
import pandas as pd

def main():
    st.title("Sulton")

    def var3(a):
        return a * 3
    def var5(a):
        return a * 5
    def var10(a):
        return a * 10
    def blnkt(a):
        return 10 * a
    def bln(a):
        return 20 * a
    
    # Meminta pengguna untuk memasukkan nomor
    a = st.text_input("Masukkan nomor:")
    
    if a:  # Jika a tidak kosong (pengguna telah memasukkan nomor)
        x = var3(int(a))
        xx = var5(int(a))
        xxx = var10(int(a))
        
        data = {'Unit': [int(a), int(a), int(a), int(a), int(a), int(a)],
                'Hari': ['3', '3', '5', '5','10', '10'],
                'Dikirim': [x, x, xx, xx, xxx, xxx],
                'persen': ['10%', '20%', '10%', '20%', '10%', '20%'],
                'Blangket': [blnkt(x), bln(xx), blnkt(xx), bln(xx), blnkt(xxx), bln(xxx)]}
        df = pd.DataFrame(data)

        # Menampilkan tabel di Streamlit
        st.table(df)

if __name__ == "__main__":
    main()
