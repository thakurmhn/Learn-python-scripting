#!/usr/bin/env python3.7

import os
import socket
import platform
import netifaces
import re

class Hostinfo():

    def get_basic_info(self):
    
        hostname=socket.gethostname()
        FQDN=socket.getfqdn()
        print(f"Hostname: {hostname}")
        print(f"FQDN: {socket.getfqdn()}")

        netiface=netifaces.interfaces()
        for each_iface in netiface: 
            if each_iface.startswith('e'):
                addrs=netifaces.ifaddresses(each_iface)
                list_addrs=addrs[netifaces.AF_INET]				# https://pypi.org/project/netifaces/
                for each_addr in list_addrs:
                    print("IP Address:",each_addr['addr'])


        return None

def main():
    
    host_obj=Hostinfo()
    host_obj.get_basic_info()


if __name__=="__main__":
    main()
