# -*- coding: utf-8 -*-
__author__ = 'yijingping'
import paramiko
import threading

IP_LIST = []
ACCOUNT_LIST = []


def get_ip_list():
    global IP_LIST
    if not IP_LIST:
        f = open('IpText.txt')
        for item in f.readlines():
            item = item.strip()
            if item and not item.startswith('#'):
                IP_LIST.append(item)
        f.close()
    return IP_LIST


def get_account_list():
    global ACCOUNT_LIST
    if not ACCOUNT_LIST:
        f = open('Accounts.txt')
        for item in f.readlines():
            item = item.strip()
            if item and not item.startswith('#'):
                arr = item.strip().split()
                if len(arr) == 2:
                    ACCOUNT_LIST.append((arr[0], arr[1]))
        f.close()
    return ACCOUNT_LIST


def scan_all():
    ip_list = get_ip_list()
    for item in ip_list:
        th = threading.Thread(target=scan, args=(item,))
        th.start()


def scan(ip):
    accounts = get_account_list()
    for user, password in accounts:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, 22, user, password, timeout=5)
            print "%s user is: %s, password is: %s" % (ip, user, password)
        except Exception as e:
            print e
            print "%s unknown" % ip
            pass

if __name__ == '__main__':
    scan_all()