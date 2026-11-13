# Information and Network Security (INS) -- Practical Experiments


## Experiment 1 -- Classical Encryption Techniques

### 1(a) Caesar Cipher

**Aim:** To develop a Python program that performs encryption and
decryption of text using the Caesar Cipher technique with a specified
shift key.

**Description:** Caesar Cipher is a substitution cipher that shifts each
character by a fixed key. During encryption, the key is added to the
character value; during decryption, the same key is subtracted. In the
alphabet-based implementation, uppercase and lowercase letters are
shifted separately while other characters remain unchanged.

### 1(b) Playfair Cipher

**Aim:** To develop a Python program that performs encryption of text
using the Playfair Cipher technique with a specific key.

**Description:** Playfair Cipher is a symmetric-key encryption technique
that encrypts pairs of letters (digraphs) instead of individual letters.
It uses a 5 × 5 key matrix generated from a keyword. The letters I and J
are treated as the same character. Letter pairs are encrypted according
to their positions in the matrix.

### 1(c) Hill Cipher

**Aim:** To develop a Python program that performs encryption of text
using the Hill Cipher technique with a specified key.

**Description:** Hill Cipher is a symmetric-key encryption technique
based on matrix multiplication. Letters are converted into numerical
values (A = 0, B = 1, ..., Z = 25), grouped into blocks, and multiplied
by a key matrix. The results are reduced modulo 26 and converted back
into letters. The practical program demonstrates encryption.

## Experiment 2 -- Transposition Techniques

### 2(a) Rail Fence Cipher

**Aim:** To perform encryption and decryption using the Rail Fence
technique.

**Description:** Rail Fence Cipher is a transposition cipher. It
arranges plaintext characters in a zigzag pattern across a specified
number of rails. The ciphertext is obtained by reading the rows.
Decryption reconstructs the zigzag pattern to recover the plaintext.

### 2(b) Row Transformation

**Aim:** To perform encryption and decryption using Row Transformation.

**Description:** Row Transformation is a transposition cipher in which
plaintext is written into a table row by row. The characters are then
read column by column to form the ciphertext. The characters themselves
are not changed; only their positions are rearranged. Padding characters
may be added to complete the matrix.

### 2(c) Column Transformation

**Aim:** To perform encryption and decryption using Column
Transformation.

**Description:** Column Transformation is a transposition cipher in
which plaintext is arranged in a matrix row by row. The columns are read
in an order determined by the key to produce the ciphertext. Decryption
places the ciphertext back into the corresponding columns and reads the
rows.

## Experiment 3 -- Data Encryption Standard (DES)

**Aim:** To implement the DES algorithm for symmetric-key encryption and
decryption of data using an 8-byte secret key.

**Description:** DES is a symmetric-key block cipher that uses the same
key for encryption and decryption. It operates on 64-bit (8-byte) data
blocks. In the practical program, PyCryptodome performs encryption in
ECB mode. The plaintext is converted to bytes and padded to the required
block size. The ciphertext is displayed in hexadecimal form and then
decrypted using the same key.

## Experiment 4 -- Advanced Encryption Standard (AES)

**Aim:** To implement the AES algorithm for symmetric encryption.

**Description:** AES is a symmetric block cipher that uses the same
secret key for encryption and decryption. It operates on 128-bit blocks
and supports key sizes of 128, 192, and 256 bits. In the practical
program, PyCryptodome is used to pad and encrypt the plaintext in ECB
mode. The encrypted data is displayed in hexadecimal form and decrypted
using the same key.

## Experiment 5 -- RSA Algorithm

**Aim:** To implement the RSA algorithm for asymmetric-key encryption
and decryption using a public key and a private key.

**Description:** RSA is an asymmetric cryptographic algorithm that uses
two different keys: a public key for encryption and a private key for
decryption. The keys are generated using two prime numbers, p and q. The
program calculates n = p × q and Euler's totient φ(n) = (p − 1)(q − 1),
chooses e relatively prime to φ(n), and calculates its modular inverse
d. Encryption uses C = M\^e mod n, and decryption uses M = C\^d mod n.

## Experiment 6 -- Diffie-Hellman Key Exchange

**Aim:** To demonstrate how two parties can securely exchange secret
keys over an insecure communication channel using the Diffie-Hellman key
exchange algorithm.

**Description:** Diffie-Hellman is a key-agreement technique that allows
two parties to establish a common secret without directly transmitting
the secret key. Both parties publicly agree on a prime number p and a
base g. Each party selects a private value, computes a public value, and
exchanges only the public values. Both parties independently calculate
the same shared secret.

## Experiment 7 -- SHA-256 Hash Function

**Aim:** To implement the SHA-256 cryptographic hash function.

**Description:** SHA-256 belongs to the SHA-2 family of cryptographic
hash functions. It accepts input data of arbitrary length and produces a
256-bit (32-byte) hash value, normally represented as 64 hexadecimal
characters. The hash function is one-way: the original input is not
practically recovered from the digest. The same input produces the same
hash, while a small change in input produces a significantly different
digest.

## Experiment 8 -- Digital Signature Standard (DSS / DSA)

**Aim:** To implement Digital Signature Standard techniques for
generating and verifying digital signatures.

**Description:** Digital signatures use public-key cryptography. A hash
of the message is generated first. The signer uses a private key and a
per-signature value to generate a signature pair (r, s). The verifier
uses the corresponding public key, the message hash, and the signature
pair to check validity. A valid signature provides message
authentication, integrity, and non-repudiation, assuming the private key
is protected.

## Experiment 9 -- Secure Socket Layer (SSL) / Transport Layer Security (TLS)

**Aim:** To implement a secure client-server communication demonstration
using SSL/TLS.

**Description:** SSL is the predecessor of modern TLS. TLS protects data
exchanged over an insecure network by providing encryption, integrity,
and server authentication. In this practical, a local TLS server is
created using Python's `ssl` and `socket` modules and a
certificate/private-key pair. A client establishes a TLS connection,
sends a message, and receives a response from the server.

## Experiment 10 -- Intrusion Detection System (IDS) using Snort

**Aim:** To demonstrate an Intrusion Detection System using Snort and a
custom detection rule.

**Description:** An Intrusion Detection System monitors network traffic
or host activity and generates alerts when traffic matches known
suspicious patterns. Snort is a network IDS/IPS tool that inspects
packets and applies rule-based signatures. In this practical, a custom
ICMP rule is used to detect ping traffic in a controlled, authorized
laboratory network. When matching traffic is observed, Snort generates
an alert.


