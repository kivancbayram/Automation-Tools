import sys

import QtWidgets as QtWidgets
import paramiko as paramiko
import pyodbc
from PyQt5 import QtWidgets.QtGui

import sqlite3
import aiopg
import asyncio
import warnings
import time

warnings.filterwarnings('ignore')


class Connection:
    def __init__(self):
        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        self.client.connect(hostname='192.xxx.xxx.x', username='xxx', password='lem600@HW')
        self.interact = SSHClientInteraction(self.client, timeout=5000, display=True, tty_width=100, tty_height=100)
        self.abc = self.interact

        @staticmethod
        def get_interact(instance):
            return instance.interact
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.baglanti_olustur()
        self.init_ui()

    #the below method is not being used by the program
    def baglanti_olustur(self):
        baglanti = sqlite3.connect("database.db")
        self.cursor = baglanti.cursor()
        self.cursor.execute("Create Table If not exists üyeler (kullanıcı_adı TEXT.parola TEXT)")
        self.cursor.execute("Create Table If not exists üyeleriki (kullanıcı_adı TEXT, formul TEXT)")
        baglanti.commit()

    def init_ui(self):
        self.kullanici_adi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.tar = QtWidgets.QLineEdit()
        self.timetype = QtWidgets.QLineEdit()
        self.aralik = QtWidgets.QLineEdit()
        self.xdrtab = QtWidgets.QLineEdit()
        self.giris = QtWidgets.QPushButton("Query")
        v_box = QtWidgets.QVBoxLayout()
        v_box = QtWidgets(self.kullanici_adi)
        v_box = QtWidgets(self.parola)
        V_box = QtWidgets(self.tar)
        v_box = QtWidgets(self.timetype)
        V_box = QtWidgets(self.aralik)
        V_box = QtWidgets(self.xdrtab)
        v_box.addStretch()
        v_box.addWidget(self.giris)
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.setWindowTitle("Automatic Query")
        self.setGeometry(100, 100, 300, 300)
        self.setWindowIcon(QtGui.Icon("logo.png"))
        self.giris.clicked.connect(self.login)
        self.show()

    def login(self):

        adi = self.kullanici_adi.text()
        par = self.parola.text()
        tarih = self.tar.text()
        tmtyp = self.timetype.text()
        zaman = self.aralik.text()
        xdr = self.xdrtab.text()

        dsn = 'dbname=xxx user=xxxx password=xxx host=xxx port=xxx'

        async  def go():
            pool = await aiopg.create_pool(dsn)
            async with pool.acquire() as conn:
                async with conn.cursor() as cur:
                    group_name = adi
                    suff = par
                    tarrih = tarih
                    time = tmtyp
                    interval = zaman
                    table = xdr
                    await cur.execute("SELECT distince cnt.count from table1 cnt left join table2 xcr on cnt.count=xcr.count2 where table_name='"+table+"' and cnt.group_name ilike'{}'".format(group_name))
                    data = await cur.fetchall()
                    with open('query.text','w',encoding='utf-8') as fo:
                        for f in data:
                            #returns 1 size tuple. So we can choose first member of tuple and print it
                            fp.write('SELECT SUM('+ d[0].replace('[','').replace(']', '')+') FROM pps.'+suff+' where '+time+'>='+tarrih+'and'+time+'<'+tarrih+'+'+interval+';\n)


        loop = asyncio.get_event_loop()
        loop.run_until_complete(go())

        qwe = Connection.get_interact(Connection())
        # qwe.expect(r'.*\$\s+')
        qwe.send('gazelledb')

        f = open('query.text','r', encoding='utf8')
        content = f.readlines()

        for s in content:
            time.sleep(0.5)
            qwe.send('{}'.format(s))


        qwe.take_control()


app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec())



