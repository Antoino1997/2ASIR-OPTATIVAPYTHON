import sys
from network_scanner.local_ports import scan_local_ports
from network_scanner.network_scan import scan_local_network
from network_scanner.utils import get_local_ip

def menu():
    print("\n=== Escáner de Red y Puertos Locales ===")
    print("1. Escanear puertos locales")
    print("2. Escanear red local")
    print("3. Escaneo COMPLETO (Local + Red)")
    print("4. Salir")
    return input("Selecciona una opción: ").strip()

def main():
    while True:
        opcion = menu()

        # --- OPCIÓN 1: LOCAL ---
        if opcion == "1":
            ports = input("Introduce rango o lista de puertos (ej: 1-1024): ").strip()
            if not ports: ports = "1-1024"
            resultados = scan_local_ports(ports)
            print("\n--- Puertos Locales Abiertos ---")
            if resultados["open_ports"]:
                for p in resultados["open_ports"]:
                    print(f"  {p['port']}/tcp - {p['service']}")
            else:
                print("  No se encontraron puertos abiertos.")

        # --- OPCIÓN 2: RED ---
        elif opcion == "2":
            ports = input("Introduce puertos a escanear (ej: 22,80,443): ").strip()
            if not ports: ports = "22,80,443,8080"
            resultados = scan_local_network(ports)
            print("\n--- Dispositivos Detectados en Red ---")
            if resultados:
                for r in resultados:
                    print(f"\nHost: {r['ip']}")
                    for p in r["open_ports"]:
                        print(f"  {p['port']}/tcp - {p['service']}")
            else:
                print("  No se detectaron hosts con esos puertos abiertos.")

        # --- OPCIÓN 3: TODO (LOCAL Y RED) ---
        elif opcion == "3":
            print("\nIniciando escaneo global (esto puede tardar)...")
            rango_todo = "1-1024,3306,8080,8888"

            # 1. Escaneo Local
            print("\n[1/2] Escaneando puertos locales...")
            res_local = scan_local_ports(rango_todo)

            # 2. Escaneo de Red
            print("[2/2] Escaneando red completa...")
            res_red = scan_local_network(rango_todo)

            # Resumen unificado
            print("\n" + "="*40)
            print("        RESULTADOS GLOBALES")
            print("="*40)

            print(f"\n[+] localhost (Tú):")
            for p in res_local["open_ports"]:
                print(f"    {p['port']}/tcp - {p['service']}")

            for r in res_red:
                mi_ip = get_local_ip()
                if r['ip'] != "127.0.0.1" and r['ip'] != mi_ip:
                    print(f"\n[+] Host en red: {r['ip']}")
                    for p in r["open_ports"]:
                        print(f"    {p['port']}/tcp - {p['service']}")
            print("\n" + "="*40)

        # --- OPCIÓN 4: SALIR ---
        elif opcion == "4":
            print("Saliendo del programa...")
            sys.exit(0)

        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()