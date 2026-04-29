import sys
import nmap

def scan_local_ports(ports: str = "1-1024") -> dict:
    """
    Escanea los puertos abiertos en localhost.
    """
    scanner = nmap.PortScanner()
    results = {"host": "127.0.0.1", "open_ports": []}

    try:
        scanner.scan(hosts="127.0.0.1", ports=ports, arguments="-sT")
    except nmap.PortScannerError as e:
        print(f"Error al ejecutar nmap: {e}")
        sys.exit(1)

    if "127.0.0.1" in scanner.all_hosts():
        for port, info in scanner["127.0.0.1"].get("tcp", {}).items():
            if info["state"] == "open":
                results["open_ports"].append({
                    "port": port,
                    "service": info.get("name", "desconocido")
                })
    return results
