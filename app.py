import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Interface import dept_con
from Interface import Jenis_Kelamin
from Interface import Jenis_Kulit
from Interface import Masalah_Kulit
from Interface import Harga
import streamlit as st
from streamlit_option_menu import option_menu

# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
EXAMPLE_NO = 1


def streamlit_menu(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="Menu Utama",  # required
                options=["BERANDA", "PREDIKSI"],  # required
                icons=["house", "search"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected

    if example == 2:
        # 2. horizontal menu w/o custom style
        selected2 = option_menu(
            menu_title=None,  # required
            options=["BERANDA", "PREDIKSI"],  # required
            icons=["house", "search"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected2



selected = streamlit_menu(example=EXAMPLE_NO)

if selected == "BERANDA":
    st.title(f"WEDYA Rekomendasi Skincare")

    col1, col2 = st.columns(2)

    with col1:
        st.image("img/6.png")

    with col2:
        st.image("img/4.png")

    st.write(f"Kulit merupakan organ tubuh terbesar yang menutupi seluruh permukaan tubuh manusia. Merawat kesehatan kulit merupakan salah satu bagian dari menjaga kesehatan tubuh yang sangat penting untuk dilakukan. Setiap orang memiliki tipe/jenis kulit wajah yang berbeda-beda, tergantung pada jenis kelamin, usia hingga genetik. Banyak orang yang belum mengenal dan mengetahui apa tipe/jenis kulit yang dimiliki. Padahal mengetahui tipe/jenis kulit itu sangat penting,sebab ini akan menentukan jenis perawatan dan produk skincare yang dibutuhkan. Sehingga sistem ini dibuat untuk memprediksi jenis skincare berdasarkan survey masyarakat.")


if selected == "PREDIKSI":
    st.title(f"WEDYA ")
    st.image("img/2.png")

    model = pickle.load(open('model_ds.pkl', 'rb'))

    df_rec = pd.read_csv("Data_Skincare.csv")
    df_rec = df_rec.drop(['Jenis Kelamin','Usia/Umur','Jenis Kulit','Harga '],axis = 1)
    df_rec = df_rec.rename(columns={'Jenis Skincare': 'JenisSkincare'})
    df_rec = df_rec.rename(columns={'Produk/Merk': 'Merk'})

# Inisialisasi objek tfidf
    tfidf = TfidfVectorizer(max_features=5000)

# Transform data
    vectorized_data = tfidf.fit_transform(df_rec['Masalah Kulit'].values)

    vectorized_dataframe = pd.DataFrame(vectorized_data.toarray(), index=df_rec['Masalah Kulit'].index.tolist())

    similarity = cosine_similarity(vectorized_dataframe)
    def recommendation(position1,position2):
        id_of_position1 = df_rec[df_rec['JenisSkincare']==position1].index[0]
        distances1 = similarity[id_of_position1]
        position_list1 = sorted(list(enumerate(distances1)), reverse=True, key=lambda x:x[1])[1:10]
        id_of_position2 = df_rec[df_rec['Merk']==position2].index[0]
        distances2 = similarity[id_of_position2]
        position_list2 = sorted(list(enumerate(distances2)), reverse=True, key=lambda x:x[1])[1:10]

        for i in position_list1:
            a = df_rec.iloc[i[0]].JenisSkincare

        for i in position_list2:
            b = df_rec.iloc[i[0]].Merk

        st.write(f'recomendation Skin Care lain: {a} {b}', end='')


    st.title('Rekomendasi Skincare Wajah')

# input data baru
    Sex = st.selectbox('Apa Jenis Kelamin Anda? ',
                  ('Laki-Laki','Perempuan'))
    Usia = st.number_input('Berapa Usia Anda? ',min_value = 15, max_value = 100, value = 20,step=1)
    jenis = st.selectbox('Jenis Kulit yang Anda Miliki? ',
                           ('Berminyak','Kombinasi','Normal','Kering'))
    masalah = st.selectbox('Masalah Kulit Yang Dialami? ',
                             ('Komedo','Dark Spot (Bekas Jerawat)','Kusam','Jerawat','Beruntusan','Kerutan','Dark Circle (Mata Panda)','Flek Hitam','Milia'))
    rupiah = st.selectbox('Budget Anda Untuk Perawatan? ',
                     ('Murah','Sedang','Mahal'))
    Merk = st.selectbox('Pilih Produk Yang Cocok^^ ',
                   ('MsGlow','Skintific','Acnes','Wardah','Nivea','Avoskin','Garnier','Hanasui','Benings','BioAqua','Biore','Ponds','Loreal','Scarlett','Emina','Himalaya','Mustika,Ratu','Cetaphil','Clear & Clean','Safi','WhiteLab','Citra','Azarine','St.Ives'))


    JenisKelamin = Jenis_Kelamin(Sex)
    JenisKulit = Jenis_Kulit(jenis)
    MasalahKulit = Masalah_Kulit(masalah)
    harga = Harga(rupiah)
    ProdukMerk = dept_con(Merk)

# initialize list of lists
    data = [[JenisKelamin,Usia,JenisKulit,MasalahKulit,harga,ProdukMerk]]

# Create the pandas DataFrame
    New_Data = pd.DataFrame(data, columns=['Jenis Kelamin','Usia/Umur','Jenis Kulit','Masalah Kulit','Harga ','Produk/Merk'])

    if st.button('Rekomen Skin Care'):
        Prediction = model.predict(New_Data)
        pred = Prediction
        rec_str = pred.item()[:]

        st.success('Jenis Skincare yang cocok adalah:')
        st.subheader(rec_str,Merk)
        rec = recommendation(rec_str,Merk)
