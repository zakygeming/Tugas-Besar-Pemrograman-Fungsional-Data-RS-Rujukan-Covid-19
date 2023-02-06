import requests
from waitress import serve
#import json
from flask import Flask, render_template, url_for, request, json

app = Flask(__name__)
data = requests.get('https://dekontaminasi.com/api/id/covid19/hospitals').json() #ambil data asli

#data-data provinsi yang di dapat dari url json akan disimpan /append ke dalam prov
prov = []
for i in data:
    prov.append(i['province'])

@app.route('/')
def home():
    return render_template('home1.html',rs = data, judul = 'Home')

@app.route('/cari-data/')
def caridata():
    q = set(prov)
    # mep sebagai penerapan fungsi pada semua elemen
    #lambda(membuat fungsi jadi sebuah ekspresi)
    # beberapa provinsi akan disortir sesuai nama provinsi, jika ditemukan datanya akan masuk ke dalam p
    p = list(map(lambda x:'Provinsi'+ x, sorted(q))) 
    return render_template('cariutama.html',x=p, judul = 'Cari Data')

@app.route('/cari',methods = ['POST','GET']) #saat "serch", akan tampil dengan metode pos & get
def cari():
    if request.method == 'POST':
        cari = request.form['cari']
        #list data provinsi di filter sesuai dengan fungsi definisi sebelumnya (hasil pencarian), disimpan sebagai list baru
        new_list = list(filter(lambda x: (x['province'] == cari), data))
        return render_template('cari.html', rs = new_list, judul='Cari Data')
    else:
        cari=request.args.get['cari']
  
if __name__ == "__main__":
    app.run(debug=True)

