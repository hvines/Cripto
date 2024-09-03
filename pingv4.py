from scapy.all import *
import time
import struct

def send_icmp_requests(message, ip_chain):
    seq_number = 0  # Inicializa el número de secuencia

    for i, char in enumerate(message):
        # Generar el timestamp actual en milisegundos y limitarlo a los últimos 4 bytes
        timestamp = int(time.time() * 1000) & 0xFFFFFFFF  # Timestamp en milisegundos, limitado a 4 bytes
        timestamp_le = struct.pack('<I', timestamp)  # Convertir a Little-Endian (4 bytes)

        # Define la IP de origen y destino basándote en la cadena de IPs
        src_ip = ip_chain[i % len(ip_chain)]
        dst_ip = ip_chain[(i + 1) % len(ip_chain)]

        # Crear la carga útil para tener 48 bytes en total
        padding = b'\x00' * (48 - len(timestamp_le) - 1)  # Rellenar con ceros para alcanzar 48 bytes
        payload = timestamp_le + char.encode() + padding

        # Crear la solicitud de eco (Echo Request)
        request_packet = (
            Ether() / 
            IP(src=src_ip, dst=dst_ip) / 
            ICMP(type=8, code=0, seq=seq_number) / 
            Raw(load=payload)
        )

        # Calcular la suma de verificación manualmente
        del request_packet[ICMP].chksum  # Elimina cualquier valor preexistente de checksum
        request_packet = request_packet.__class__(bytes(request_packet))  # Fuerza el recálculo del checksum

        # Enviar la solicitud de eco
        sendp(request_packet)
        print(f"Sent ICMP Request with seq: {seq_number} and payload size: {len(payload)} bytes")

        # Incrementar el número de secuencia para el siguiente paquete
        seq_number += 1

        # Esperar un poco antes de enviar el siguiente paquete
        time.sleep(1)

if __name__ == "__main__":
    message = "larycxpajorj h bnpdarmjm nw anmnb"
    
    # Define la cadena de direcciones IP a utilizar
    ip_chain = ["192.168.0.1", "192.168.0.2", "192.168.0.3", "192.168.0.4"]
    
    send_icmp_requests(message, ip_chain)
