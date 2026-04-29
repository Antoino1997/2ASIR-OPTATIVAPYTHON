import socket
import ipaddress
def get_local_ip() -> str:
    """Devuelve la IP local del equipo."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
def get_network_cidr(ip: str, prefix: int = 24) -> str:
    """Construye el rango CIDR de la red local."""
    return str(ipaddress.IPv4Network(f"{ip}/{prefix}", strict=False))