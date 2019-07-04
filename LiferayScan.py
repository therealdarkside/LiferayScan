#/usr/bin/python3
import os, requests, sys, time
from time import sleep

os.system("clear")
print ("////////////////////////////////////////////////////////////")
print ("///////////////////     LiferayScan      //////////////////")
print ("//////////////////////////////////////////////////////////\n\n")
print ("Created by Darkside\n")


def get_list():
    if len(sys.argv) > 1:
         
        return sys.argv[1]
    else:
        print ("[-] Usage: python3 LiferayScan dictionary.lst\n")
        exit()

#The read the domains or IP's from a file
def get_data(filename):
        print ("[+] Scanning...")
        #f = open("rangoIPs", "r")
        f = open(filename, "r")
        data = []
        for line in f:
              data.append(line)
        return data

#the TCP connection to test the target.
def tcp_connection(argu, domain):
    fname = ("LifeRay-Founds"+time.strftime("%Y%m%d-%H%M%S")+".txt")
    fd = open(fname, "a")
    for ip in domain:
        for line in argu:
            query = str("http://"+ip.rstrip("\n")+line)
            query_ssl = str("https://"+ip.rstrip("\n")+line)
            try:
                message = str("[+] Trying "+ip.rstrip("\n")+line)
                print (message)
                r = requests.get(query, allow_redirects=True, timeout=3)
                r = requests.get(query_ssl, allow_redirects= True, timeout=3)
            except requests.exceptions.ConnectionError:
                continue

            try:
                print (query+" or "+query_ssl+" exist!\n")
                fd.write(ip.rstrip("\n")+line)
            except:
                continue
    fd.close()
    print ("[+] Report saved in "+fname)
    print ("Good bye!!!")
    return

if __name__ == '__main__':

    Get_Arg = get_list()
    ips = get_data("rangoIPs")
    argu = get_data(Get_Arg)
    tcp_connection(argu, ips)
