import nmap
from .utils import get_local_ip, get_network_cidr

def scan_local_network(ports: str = "22,80,443,8080") -> list:
    """
    Descubre hosts activos y escanea los puertos indicados sin errores de clave.
    """
    scanner = nmap.PortScanner()
    local_ip = get_local_ip()
    network_cidr = get_network_cidr(local_ip)

    try:
        print(f"\nEscaneando red {network_cidr}...")
        # -sn: Escaneo de descubrimiento (ping scan)
        scanner.scan(hosts=network_cidr, arguments="-sn")
    except nmap.PortScannerError as e:
        print(f"Error en escaneo de red: {e}")
        return []

    resultados = []
    # Guardamos la lista de hosts descubiertos para no perder el rastro
    hosts_descubiertos = scanner.all_hosts()

    for host in hosts_descubiertos:
        try:
            # Escaneo de puertos específico para el host encontrado
            scanner.scan(hosts=host, ports=ports, arguments="-sT -T4")

            # Verificamos que el host siga en el diccionario de resultados
            if host not in scanner.all_hosts():
                continue

            # Usamos .get() con diccionarios vacíos por seguridad absoluta
            datos_tcp = scanner[host].get("tcp", {})

            abiertos = []
            for p, d in datos_tcp.items():
                if d.get("state") == "open":
                    abiertos.append({
                        "port": p,
                        "service": d.get("name", "unknown")
                    })

            # Solo lo añadimos si nos interesa reportar hosts con puertos abiertos
            if abiertos:
                resultados.append({"ip": host, "open_ports": abiertos})

        except Exception as e:
            print(f"Error al escanear {host}: {e}")
            continue

    return resultados