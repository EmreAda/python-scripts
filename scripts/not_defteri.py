#!/usr/bin/env python3
# -*- coding: utf8 -*-
import sqlite3 as sql
import sys

def removelastchar(string):
    str = ""
    for i in range(len(string)):
        if i == len(string)-1:
            pass
        else:
            str = str + string[i]
    return str

def concatnate_sysv_array(array):
    concatnated = ""
    for i in range(len(array)):
        if i == 0 or i == 1:
            pass
        else:
            concatnated = concatnated + array[i] + " "
    return removelastchar(concatnated)

def dbbaglan():
    """
    KULLANIM: python <script_ismi> [yardım|gir|getir|listele hepsi|sil] [gir: girilecek not|getir: getirilecek notun id'si|sil: silinecek notun id'si]
    """
    db = sql.connect("notdefteri.db")
    cs = db.cursor()

    cs.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, note TEXT)")

    if not len(sys.argv) >= 2:
        print("Eksik argüman miktarı")
    elif sys.argv[1] == "gir" and len(sys.argv) >= 3:
        cs.execute(f"INSERT INTO notes (note) VALUES ('{concatnate_sysv_array(sys.argv)}')")
    elif sys.argv[1] == "getir":
        try:
            cs.execute(f"SELECT * FROM notes WHERE id={int(sys.argv[2])}")
            data = cs.fetchall()
            db.commit()
            print(data)
        except ValueError:
            print("Değer hatası, getir'den sonra gelen argüman sayı dışı karakter içeremez.")
    elif sys.argv[1] == "listele" and sys.argv[2] == "hepsi":
        cs.execute(f"SELECT * FROM notes")
        data = cs.fetchall()
        db.commit()
        for i in data:
            print(i)
    elif sys.argv[1] == "yardım":
        print(dbbaglan.__doc__)
    elif sys.argv[1] == "sil" and len(sys.argv) == 3:
        cs.execute("SELECT * FROM notes")
        data = cs.fetchall()
        for i in data:
            print(i)
        db.commit()
    else:
        print(f"Eksik argüman. {dbbaglan.__doc__}")

dbbaglan()