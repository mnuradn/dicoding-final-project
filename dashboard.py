# import library yang dibutuhkan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Membuat beberapa helper function
def create_bystate_df(df):
    bystate_df = df.groupby(by="customer_state").customer_id.nunique().sort_values(ascending=False).reset_index().head(5)
    bystate_df.rename(columns={
        "customer_id":"customer_count"
    }, inplace=True)
    
    return bystate_df

def create_bycity_df(df):
    bycity_df = df.groupby(by="customer_city").customer_id.nunique().sort_values(ascending=False).reset_index().head(5)
    bycity_df.rename(columns={
    "customer_id":"customer_count"
    }, inplace=True)
    
    return bycity_df

def create_bymethod_df(df):
    bymethod_df = df.groupby(by="payment_type").customer_id.nunique().sort_values(ascending=False).reset_index()
    bymethod_df.rename(columns={
    "customer_id":"customer_count"
}, inplace=True)
    
    return bymethod_df

def create_sum_order_products_df(df):
    sum_order_products_df = df.groupby("product_category").order_id.nunique().sort_values(ascending=False).reset_index()
    return sum_order_products_df


# load data yang akan digunakan
all_df = pd.read_csv("all_data.csv")


# memanggil helper function
bycity_df = create_bycity_df(all_df)
bystate_df = create_bystate_df(all_df)
bymethod_df = create_bymethod_df(all_df)
sum_order_products_df = create_sum_order_products_df(all_df)


st.header(":sparkles: E-Commerce Dataset Dashboard 2016 - 2018")

# menampilkan best & worst performing product
st.subheader("Penjualan Produk Terbaik & Terburuk")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(60,20))

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x="order_id", y = "product_category", data=sum_order_products_df.head(5), palette = colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("Number of Sales", fontsize=30)
ax[0].set_title("Penjualan Produk Terbaik", loc="center", fontsize=50)
ax[0].tick_params(axis='x', labelsize=30)
ax[0].tick_params(axis='y', labelsize=25)

sns.barplot(x="order_id", y="product_category", data = sum_order_products_df.sort_values(by="order_id", ascending = True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("Number of Sales", fontsize=30)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("left")
ax[1].set_title("Penjualan Produk Terburuk", loc="center", fontsize=50)
ax[1].tick_params(axis="x", labelsize=30)
ax[1].tick_params(axis="y", labelsize=25)

plt.suptitle("Penjualan Produk Terbaik dan Terburuk Bedasarkan Jumlah Order ID",fontsize=35)
plt.show()

st.pyplot(fig)

# menampilkan jumlah pelanggan berdasarkan kota dan negara bagian
st.subheader("Jumlah Pelanggan Berdasarkan Kota dan Negara Bagian")

fig, ax = plt.subplots(figsize=(20, 10))
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    x="customer_count", 
    y="customer_city",
    data=bycity_df.sort_values(by="customer_count", ascending=False),
    palette=colors,
    ax=ax
)
ax.set_title("Jumlah Pelanggan Berdasarkan Kota", loc="center", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(20, 10))
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    x="customer_count", 
    y="customer_state",
    data=bystate_df.sort_values(by="customer_count", ascending=False),
    palette=colors,
    ax=ax
)
ax.set_title("Jumlah Pelanggan Berdasarkan Negara Bagian", loc="center", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

# Menampilkan penggunaan metode pembayaran yang sering digunakan pelanggan
st.subheader("Metode Pembayaran yang Sering Digunakan Pelanggan")

fig, ax = plt.subplots(figsize=(20, 10))
colors_= ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    x="customer_count",
    y="payment_type",
    data=bymethod_df.sort_values(by="customer_count", ascending=False),
    palette=colors_
)
ax.set_title("Metode Pembayaran yang Sering Digunakan Pelanggan", loc="center", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

st.caption("Dibuat oleh: Muhammad Nur Adnan | Garut, 23 Agustus 2023")
st.caption("Sumber dataset: https://www.dicoding.com/academies/555/tutorials/31230/submission-guidance")