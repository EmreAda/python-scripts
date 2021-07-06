#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def isin(checkfrom: str, checkto: str):
    count = 0
    for a in range(len(checkfrom)):
        for b in range(len(checkto)):
            if checkfrom[a] == checkto[b]:
                count += 1
    if count == 0:
        print("Geçersiz karakterler barındırıyor.")
        exit(-1)


def emailslicer(email: str):
    try:
        allowedchars = "abcdefghijklmnoprstuvyzxwABCDEFGHIJKLMNOPRSTUVYZXW._-"
        mail = email.split("@")
        isin(allowedchars, mail[0])
        isin(allowedchars, mail[1])
        provider = ""
        for i in range(len(mail[1])):
            if (mail[1])[i] == ".":
                break
            provider = provider + (mail[1])[i]
        print(f"Mail servisi sağlayıcısı {provider}")
        print(f"Mailin kullanıcı adı: {mail[0]}")
    except AttributeError:
        print("Bozuk e-mail.")


def main():
    emailslicer("recep.azm@gmail.com")


if __name__ == '__main__':
    main()
