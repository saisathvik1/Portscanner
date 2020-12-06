import nmap

target = input("Enter Target IP: ")
scan_target = nmap.PortScanner()
ports = [21,22,80,139,443,445,8080]

for port in ports:
  portscanner = scan_target.scan(target,str(port))
  if portscanner!='closed':
    print(f"Port {port} on {target} is {portscanner['scan'][target]['tcp'][port]['state']}")
