import datetime
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID

# Genera una chiave privata RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Genera un certificato autofirmato
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

# Esporta la chiave privata e il certificato
private_key_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

certificate_pem = certificate.public_bytes(
    encoding=serialization.Encoding.PEM
)

# Salva la chiave privata e il certificato su file
with open("ca_private_key.pem", "wb") as key_file:
    key_file.write(private_key_pem)

with open("ca_certificate.pem", "wb") as cert_file:
    cert_file.write(certificate_pem)