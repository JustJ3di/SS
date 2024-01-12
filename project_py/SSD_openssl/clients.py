import socket
import ssl

# Funzione per creare e connettersi a una socket SSL
def create_ssl_socket():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="ca_certificate.pem", keyfile="ca_private_key.pem")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = context.wrap_socket(sock, server_side=False, server_hostname="myserver.com")
    ssl_sock.connect(("localhost", 12345))

    return ssl_sock

# Client 1
def client1():
    ssl_sock = create_ssl_socket()

    # Invia una richiesta al server
    ssl_sock.sendall(b"Client 1 requesting certificate")

    # Ricevi il certificato dal server
    received_data = ssl_sock.recv(4096)
    certificate = ssl.DER_cert_to_PEM_cert(received_data)

    # Utilizza il certificato per la comunicazione sicura
    # ...

    ssl_sock.close()

# Client 2
def client2():
    ssl_sock = create_ssl_socket()

    # Invia una richiesta al server
    ssl_sock.sendall(b"Client 2 requesting certificate")

    # Ricevi il certificato dal server
    received_data = ssl_sock.recv(4096)
    certificate = ssl.DER_cert_to_PEM_cert(received_data)

    # Utilizza il certificato per la comunicazione sicura
    # ...

    ssl_sock.close()

# Esecuzione dei client
client1()
client2()