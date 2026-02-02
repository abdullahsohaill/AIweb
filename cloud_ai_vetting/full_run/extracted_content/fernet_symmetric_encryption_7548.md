# Fernet symmetric encryption
**URL:** https://cryptography.io/en/latest/fernet
**Page Title:** Fernet (symmetric encryption) — Cryptography 47.0.0.dev1 documentation
--------------------

- Fernet (symmetric encryption)
- View page source

## Fernet (symmetric encryption) 

Fernet guarantees that a message encrypted using it cannot be
manipulated or read without the key. Fernet is an implementation of
symmetric (also known as “secret key”) authenticated cryptography. Fernet also
has support for implementing key rotation via MultiFernet .
[LINK: Fernet](https://github.com/fernet/spec/)
[LINK: [source]](https://github.com/pyca/cryptography/blob/main/src/cryptography/fernet.py#L28-L168)
This class provides both encryption and decryption facilities. This class
exhibits thread safety .
key ( bytes or str ) – A URL-safe base64-encoded 32-byte key. This must be
kept secret. Anyone with this key is able to create and
read messages.
[LINK: bytes](https://docs.python.org/3/library/stdtypes.html#bytes)
[LINK: str](https://docs.python.org/3/library/stdtypes.html#str)
[LINK: [source]](https://github.com/pyca/cryptography/blob/main/src/cryptography/fernet.py#L48-L50)
Generates a fresh fernet key. Keep this some place safe! If you lose it
you’ll no longer be able to decrypt messages; if anyone else gains
access to it, they’ll be able to decrypt all of your messages, and
they’ll also be able to forge arbitrary messages that will be
authenticated and decrypted.
[LINK: [source]](https://github.com/pyca/cryptography/blob/main/src/cryptography/fernet.py#L52-L53)
Encrypts data passed. The result of this encryption is known as a
“Fernet token” and has strong privacy and authenticity guarantees.
data ( bytes ) – The message you would like to encrypt.
[LINK: bytes](https://docs.python.org/3/library/stdtypes.html#bytes)
A secure message that cannot be read or altered
without the key. It is URL-safe base64-encoded. This is
referred to as a “Fernet token”.
TypeError – This exception is raised if data is not bytes .
[LINK: TypeError](https://docs.python.org/3/library/exceptions.html#TypeError)
Note
The encrypted message contains the current time when it was
generated in plaintext , the time a message was created will
therefore be visible to a possible attacker.
[LINK: [source]](https://github.com/pyca/cryptography/blob/main/src/cryptography/fernet.py#L55-L57)
Added in version 3.0.
Encrypts data passed using explicitly passed current time. See encrypt() for the documentation of the data parameter, the
return type and the exceptions raised.
The motivation behind this method is for the client code to be able to
test token expiration. Since this method can be used in an insecure
manner one should make sure the correct time ( int(time.time()) )
is passed as current_time outside testing.
current_time ( int ) – The current time.
[LINK: int](https://docs.python.org/3/library/functions.html#int)
Note
Similarly to encrypt() the encrypted message contains the
timestamp in plaintext , in this case the timestamp is the value
of the current_time parameter.
[LINK: [source]](https://github.com/pyca/cryptography/blob/main/src/cryptography/fernet.py#L84-L90)
Decrypts a Fernet token. If successfully decrypted you will receive the
original plaintext as the result, otherwise an exception will be
raised. It is safe to use this data immediately as Fernet verifies
that the data has not been tampered with prior to returning it.
- token ( bytes or str ) – The Fernet token. This is the result of
calling encrypt() .
token ( bytes or str ) – The Fernet token. This is the result of
calling encrypt() .
[LINK: bytes](https://docs.python.org/3/library/stdtypes.html#bytes)
[LINK: str](https://docs.python.org/3/library/stdtypes.html#str)
- ttl ( int ) – Optionally, the number of seconds old a message may be
for it to be valid. If the message is older than ttl seconds (from the time it was originally
created) an exception will be raised. If ttl is not
provided (or is None ), the age of the message is
not considered.
ttl ( int ) – Optionally, the number of seconds old a message may be
for it to be valid. If the message is older than ttl seconds (from the time it was originally
created) an exception will be raised. If ttl is not
provided (or is None ), the age of the message is
not considered.
[LINK: int](https://docs.python.org/3/library/functions.html#int)
The original plaintext.
- cryptography.fernet.InvalidToken – If the token is in any
way invalid, this exception
is raised. A token may be
invalid for a number of
reasons: it is older than the ttl , it is malformed, or
it does not have a valid
signature.
cryptography.fernet.InvalidToken – If the token is in any
way invalid, this exception
is raised. A token may be
invalid for a number of
reasons: it is older than the ttl , it is malformed, or
it does not have a valid
signature.
- TypeError – This exception is raised if token is not bytes or str .
TypeError – This exception is raised if token is not bytes or str .
[LINK: TypeError](https://docs.python.org/3/library/exceptions.html#TypeError)
[LINK: [source]](https://github.com/pyca/cryptography/blob/main/src/cryptography/fernet.py#L92-L100)
Added in version 3.0.
Decrypts a token using explicitly passed current time. See decrypt() for the documentation of the token and ttl parameters ( ttl is required here), the return type and the exceptions
raised.
The motivation behind this method is for the client code to be able to
test token expiration. Since this method can be used in an insecure
manner one should make sure the correct time ( int(time.time()) )
is passed as current_time outside testing.
current_time ( int ) – The current time.
[LINK: int](https://docs.python.org/3/library/functions.html#int)
[LINK: [source]](https://github.com/pyca/cryptography/blob/main/src/cryptography/fernet.py#L102-L106)
Added in version 2.3.
Returns the timestamp for the token. The caller can then decide if
the token is about to expire and, for example, issue a new token.
token ( bytes or str ) – The Fernet token. This is the result of
calling encrypt() .
[LINK: bytes](https://docs.python.org/3/library/stdtypes.html#bytes)
[LINK: str](https://docs.python.org/3/library/stdtypes.html#str)
The Unix timestamp of the token.
- cryptography.fernet.InvalidToken – If the token ’s signature
is invalid this exception
is raised.
cryptography.fernet.InvalidToken – If the token ’s signature
is invalid this exception
is raised.
- TypeError – This exception is raised if token is not bytes or str .
TypeError – This exception is raised if token is not bytes or str .
[LINK: TypeError](https://docs.python.org/3/library/exceptions.html#TypeError)
[LINK: [source]](https://github.com/pyca/cryptography/blob/main/src/cryptography/fernet.py#L171-L224)
Added in version 0.7.
This class implements key rotation for Fernet. It takes a list of Fernet instances and implements the same API with the exception
of one additional method: MultiFernet.rotate() :
MultiFernet performs all encryption options using the first key in the list provided. MultiFernet attempts to decrypt tokens with each key in
turn. A cryptography.fernet.InvalidToken exception is raised if
the correct key is not found in the list provided.
Key rotation makes it easy to replace old keys. You can add your new key at
the front of the list to start encrypting new messages, and remove old keys
as they are no longer needed.
Token rotation as offered by MultiFernet.rotate() is a best practice
and manner of cryptographic hygiene designed to limit damage in the event of
an undetected event and to increase the difficulty of attacks. For example,
if an employee who had access to your company’s fernet keys leaves, you’ll
want to generate new fernet key, rotate all of the tokens currently deployed
using that new key, and then retire the old fernet key(s) to which the
employee had access.
[LINK: [source]](https://github.com/pyca/cryptography/blob/main/src/cryptography/fernet.py#L186-L198)
Added in version 2.2.
Rotates a token by re-encrypting it under the MultiFernet instance’s primary key. This preserves the timestamp that was originally
saved with the token. If a token has successfully been rotated then the
rotated token will be returned. If rotation fails this will raise an
exception.
msg ( bytes or str ) – The token to re-encrypt.
[LINK: bytes](https://docs.python.org/3/library/stdtypes.html#bytes)
[LINK: str](https://docs.python.org/3/library/stdtypes.html#str)
A secure message that cannot be read or altered without
the key. This is URL-safe base64-encoded. This is referred to as a
“Fernet token”.
- cryptography.fernet.InvalidToken – If a token is in any
way invalid this exception is raised.
cryptography.fernet.InvalidToken – If a token is in any
way invalid this exception is raised.
- TypeError – This exception is raised if the msg is not bytes or str .
TypeError – This exception is raised if the msg is not bytes or str .
[LINK: TypeError](https://docs.python.org/3/library/exceptions.html#TypeError)
[LINK: [source]](https://github.com/pyca/cryptography/blob/main/src/cryptography/fernet.py#L21-L22)
See Fernet.decrypt() for more information.

## Using passwords with Fernet 

It is possible to use passwords with Fernet. To do this, you need to run the
password through a key derivation function such as PBKDF2HMAC , Argon2id or Scrypt .
In this scheme, the salt has to be stored in a retrievable location in order
to derive the same key from the password in the future.
The iteration count used should be adjusted to be as high as your server can
tolerate. A good default is at least 1,200,000 iterations, which is what Django
recommends as of January 2025 .
[LINK: Django
recommends as of January 2025](https://github.com/django/django/blob/main/django/contrib/auth/hashers.py)

## Implementation 

Fernet is built on top of a number of standard cryptographic primitives.
Specifically it uses:
- AES in CBC mode with a
128-bit key for encryption; using PKCS7 padding.
AES in CBC mode with a
128-bit key for encryption; using PKCS7 padding.
- HMAC using SHA256 for authentication.
HMAC using SHA256 for authentication.
- Initialization vectors are generated using os.urandom() .
Initialization vectors are generated using os.urandom() .
For complete details consult the specification .
[LINK: specification](https://github.com/fernet/spec/blob/master/Spec.md)

## Limitations 

Fernet is ideal for encrypting data that easily fits in memory. As a design
feature it does not expose unauthenticated bytes. This means that the complete
message contents must be available in memory, making Fernet generally
unsuitable for very large files at this time.

--------------------