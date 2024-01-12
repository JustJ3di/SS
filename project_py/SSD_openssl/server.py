import socket
import ssl
import datetime
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
import threading

# Funzione per generare un certificato autofirmato
def generate_self_signed_certificate():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096
    )

    builder = x509.CertificateBuilder()
    builder = builder.subject_name(x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"IT"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My CA"),
        x509.NameAttribute(NameOID.COMMON_NAME, u"My CA"),
    ]))
    builder = builder.issuer_name(x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"IT"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My CA"),
        x509.NameAttribute(NameOID.COMMON_NAME, u"My CA"),
    ]))
    builder = builder.not_valid_before(datetime.datetime.utcnow())
    builder = builder.not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365))
    builder = builder.serial_number(x509.random_serial_number())
    builder = builder.public_key(private_key.public_key())

    builder = builder.add_extension(
        x509.BasicConstraints(ca=True, path_length=None), critical=True,
    )

    certificate = builder.sign(
        private_key=private_key, algorithm=hashes.SHA256()
    )

    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    certificate_pem = certificate.public_bytes(
        encoding=serialization.Encoding.PEM
    )

    return private_key_pem, certificate_pem

# Funzione per gestire le richieste dei client
def handle_client(sock):
    # Genera un certificato autofirmato per il client
    private_key_pem, certificate_pem = generate_self_signed_certificate()

    # Invia il certificato al client
    sock.sendall(certificate_pem)

    # Utilizza il certificato per la comunicazione sicura con il client
    # ...

    sock.close()

# Funzione principale del server
def server():
    # Crea una socket TCP/IP
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Associa la socket all'indirizzo e alla porta desiderati
    server_address = ('localhost', 12345)
    server_sock.bind(server_address)

    # Inizia ad ascoltare le connessioni in arrivo
    server_sock.listen(1)
    print("Server avviato. In attesa di connessioni...")

    while True:
        # Accetta una connessione
        client_sock, client_address = server_sock.accept()
        print("Connessione accettata da:", client_address)

        # Avvia un thread per gestire la connessione con il client
        client_thread = threading.Thread(target=handle_client, args=(client_sock,))
        client_thread.start()

# Esecuzione del server
server()