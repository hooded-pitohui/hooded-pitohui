#!/usr/bin/env python3

import sys, requests, json, os

var vt_key = config.VT_KEY

def banner():
    print("." * 70)

def geo():
    curl = "curl https://ipvigilante.com/" + request
    d = os.popen(curl).read()
    fkegr = json.loads(d)
    naps = fkegr.get("data")
    print("Location is: " + naps.get("city_name") + " in " + naps.get("subdivision_1_name") + ", " + naps.get("country_name"))

def whois_scan():
    banner()
    print("WHOIS scan: ")
    banner()
    whois = "whois " + request
    os.system(whois)

def nmap_scan():
    banner()   
    print("NMAP scan: ")
    banner()   
    nmap = "nmap -T4 -Pn -sV " + request
    os.system(nmap)

def nikto_scan():
    banner()   
    print("NIKTO scan: ")
    banner()   
    nikto = "nikto -h " + request
    os.system(nikto)

def dirb_scan():
    banner()  
    print("DIRB scan: ")
    banner()  
    dirb = "dirb https://" + request
    os.system(dirb)

def virus_total_scan():
    banner()    
    print("VIRUSTOTAL scan")
    banner()    
    url = 'https://www.virustotal.com/vtapi/v2/url/report'
    params = {'apikey': vt_key, 'resource': request}
    response = requests.get(url, params=params)
    virus_total = response.json()
    scans = virus_total.pop("scans")
    for k, v in virus_total.items():
        print(k, ":" , v)
    print("\n")
    for k, v in scans.items():
        alp_scan = sorted(scans.items(), key=lambda key_value : key_value[0])
        #print(alp_scan) 
    value = input("Would you like to see the scans? y/n:\n")
    if value == "y":
        # Alphabetical scan
        for k, v in alp_scan:
            print(k, "||", "detected :", v["detected"], "||", "result", ":",  v["result"])
    else:
        banner()
        print("Thank you for using hooded-pitohui\nExiting program")
        banner()
        sys.exit()

def firewall():
    firewall = "iptables -A INPUT -s " + request + " -j REJECT"
    display = "iptables -L"
    os.system(firewall)
    print("-" * 70)
    os.system(display)
    print("-" * 70)

print("Which IP would you like to scan:")
request = input()

geo()

count = 0

print("\nWould you like to do a whois scan? y/n ")

while True:
    wi_scan = input()
    if wi_scan == "y":
        whois_scan()
        break
    elif wi_scan == "n":
        print("\npitohui will not run the whois scan\n")   
        break
    elif count == 2:
        print("\npitohui will not run a whois scan\n")
        break
    else:
        count += 1
        print("Please enter y or n:")

banner()
print("\nWould you like to do an nmap scan? y/n ")

count = 0

while True:
    nm_scan = input()
    if nm_scan == "y":
        nmap_scan()
        break
    elif nm_scan == "n":
        print("\npitohui will not run an nmap scan\n")   
        break
    elif count == 2:
        print("\npitohui will not run an nmap scan\n")
        break
    else:
        count += 1
        print("Please enter y or n:")

banner()
print("\nWould you like to do a nikto scan? y/n ")

count = 0

while True:
    nko_scan = input()
    if nko_scan == "y":
        nikto_scan()
        break
    elif nko_scan == "n":
        print("\npitohui will not run a nikto scan\n")   
        break
    elif count == 2:
        print("\npitohui will not run a nikto scan\n")
        break
    else:
        count += 1
        print("Please enter y or n:")


banner()
print("\nWould you like to run dirb on this IP address? y/n ")

count = 0

while True:
    db_scan = input()
    if db_scan == "y":
        dirb_scan()
        break
    elif db_scan == "n":
        print("\npitohui will not run dirb\n")   
        break
    elif count == 2:
        print("\npitohui will not run dirb\n")
        break
    else:
        count += 1
        print("Please enter y or n:")


print("-" * 50)           
print("Would you like to use the Virus Total scan? y/n ")

count = 0

while True:
    vt_scan = input()
    if vt_scan == "y":
        virus_total_scan()
        break
    elif vt_scan == "n":
        print("\npitohui will not do the virustotal scan\nExiting hooded-pitohui")   
        break
    elif count == 2:
        print("\npitohui will not run a virostotal scan\nExiting hooded-pitohui")
        break
    else:
        count += 1
        print("Please enter y or n:")

banner()
print("\nWould you like to block " + request + "  y/n ")

count = 0

while True:
    f_wall = input()
    if f_wall == "y":
        firewall()
        break
    elif f_wall == "n":
        print("\npitohui will not block " + request +"\n")   
        break
    elif count == 2:
        print("\npitohui will not block " + request +"\n")
        break
    else:
        count += 1
        print("Please enter y or n:")

print("\nThank you for using hooded-pitohui for your scans\nExiting hooded-pitohui")
 
