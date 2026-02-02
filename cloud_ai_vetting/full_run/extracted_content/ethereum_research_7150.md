# Ethereum Research
**URL:** https://ethresear.ch/t/fhe-dksap-fully-homomorphic-encryption-based-dual-key-stealth-address-protocol/16213
**Page Title:** FHE-DKSAP: Fully Homomorphic Encryption based Dual Key Stealth Address Protocol - Cryptography - Ethereum Research
--------------------


## FHE-DKSAP: Fully Homomorphic Encryption based Dual Key Stealth Address Protocol

You have selected 0 posts.
select all
cancel selecting
This research is a joint effort from Ethereum Fellows: @Mason-Mind @georgesheth @dennis @AshelyYan

## 1. Introduction

The Stealth Address (SA) prevents the public association of a blockchain transaction with the recipient’s wallet address. SA effectively conceals the actual destination address of the transaction. It is critical to protect privacy of recipients and cut off social engineering attack on transaction flow.
@vbuterin @Nero_eth proposed EIP-5564 as the first SA design, and developed BasedSAP as a implementation of SA on Ethereum by utilising the Secp256k1 elliptic curve (EC).  However, @vbuterin also highlighted the current limitations in Open problem: improving stealth addresses to demand a (Fully Homomorphic Encryption) FHE solution:
Based on BaseSAP, we contribute further to propose FHE-DKSAP : a SA protocol with Fully Homomorphic Encryption (FHE). FHE-DKSAP has bellow primary advantages:
- FHE-DKSAP replace EC with FHE to improve security level. FHE constructs the lattice cryptographic, and born to equip FHE-DKSAP to prevents quantum computing attacks.
- Therefore, SA in FHE-DKSAP is secured to be reused and no need to generate large amount of SA to reduce the complexity and difficulty of SA adoption.
- Comparing to the dual-key design in EIP-5564, our design in FHE-DKSAP, can help the receiver outsource the computation of checking the entire chain for SA containing assets without revealing his view key.

## 2. Background

One of the key focus of privacy protection in the Ethereum is to cut off the public association of the receipt’s address. SA is proposed to require the sender to create a random one-time address for every transaction on behalf of the recipient so that different payments are made to the same payee unlinkable.
We systematically studied on previous publications, and found Dual-Key Stealth Address Protocols (Courtois, N. T., & Mercer, R. 2017) is the most appreciated design. However, it is still vulnerable to key leakage attacks and quantum computing attacks. To prevent these attacks, we propose to implement SA with FHE, an application of lattices.
Others research can be summarised as bellow:
- The development of Stealth Address (SA) technology began with its initial invention by a user named ‘bytecoin’ in the Bitcoin forum on April 17, 2011. This technique introduced the concept of untraceable transactions capable of carrying secure messages, paving the way for enhanced privacy and security in blockchain systems.
- In 2013, Nicolas van Saberhagen took the concept further in the CryptoNote white paper, providing more insights and advancements in Stealth Address technology. His contribution expanded the understanding of how Stealth Addresses could be integrated into cryptographic protocols. Subsequent years saw several researchers making strides in the realm of Stealth Address technology.
- In 2017, Nicolas T. Courtois and Rebekah Mercer introduced the Robust Multi-Key Stealth Address, which enhanced the robustness and security of the SA technique.
- The year 2018 saw Fan Xinxin and his team presenting a faster dual-key Stealth Address protocol, specifically designed for blockchain-based Internet of Things (IoT) systems. Their protocol introduced an increasing counter, enabling quicker parsing and improving overall efficiency.
- In 2019, Fan Jia and his team tackled the issue of key length in Stealth Addresses by utilizing bilinear maps, thereby making significant advancements in enhancing the protocol’s security and practicality.
- The same year, researchers introduced a lattice-based linkable ring signature supporting Stealth Addresses. This innovation was aimed at countering adversarially-chosen-key attacks, further reinforcing the security aspect. However, this paper is not leveraging multi-keys.
- As technology progressed, EIP-5564 was proposed to implement SA on Ethereum and on June 25, 2023, the paper, BasedSAP emerged as a fully open and reusable Stealth Address protocol.
Based on our knowledge, all research did not resolve to meet overall requirements on 1) protect privacy on Ethereum, 2) prevent quantum computing attacks, 3) reuse SA rather than creating many.

## 3. Our Design: FHE-DKSAP

We resolve challenges by adopting FHE into DKSAP, and name our new design as FHE-DKSAP:
We present FHE-DKSAP with details as bellow. It requires preliminary knowledge on DKSAP and FHE, and you may read Chapter 6 first to have these knowledge ready:
- Bob (receiver) creates two key pairs: (sk_2, PK_2) ( s k 2 , P K 2 ) and (sk_b, PK_b) ( s k b , P K b ) . 1.1. sk_2 s k 2 is a randomly generated Ethereum wallet private key for SA spending purpose. It does not need to register on Ethereum before use and is not Bob’s wallet private key. 1.2. A SA spending wallet address public key PK_2 P K 2 is generated using sk_2 s k 2 . It follows standard Ethereum address conversion from sk_2 s k 2 to PK_2 P K 2 . As said, the final wallet address by PK_2 P K 2 does not need to register on Ethereum before use. 1.3. sk_b s k b is the FHE private key for SA encryption and decryption. 1.4. PK_b P K b is used to encrypt the value of sk_2 s k 2 to get the ciphertext C_2 C 2 . Because FHE prevents quantum computing attacks, it is safe to encrypt sk_2 s k 2 into C_2 C 2 . 1.5. Bob publicly shares PK_2 P K 2 , PK_b P K b , and the ciphertext C_2 C 2 .
Bob (receiver) creates two key pairs: (sk_2, PK_2) ( s k 2 , P K 2 ) and (sk_b, PK_b) ( s k b , P K b ) . 1.1. sk_2 s k 2 is a randomly generated Ethereum wallet private key for SA spending purpose. It does not need to register on Ethereum before use and is not Bob’s wallet private key. 1.2. A SA spending wallet address public key PK_2 P K 2 is generated using sk_2 s k 2 . It follows standard Ethereum address conversion from sk_2 s k 2 to PK_2 P K 2 . As said, the final wallet address by PK_2 P K 2 does not need to register on Ethereum before use. 1.3. sk_b s k b is the FHE private key for SA encryption and decryption. 1.4. PK_b P K b is used to encrypt the value of sk_2 s k 2 to get the ciphertext C_2 C 2 . Because FHE prevents quantum computing attacks, it is safe to encrypt sk_2 s k 2 into C_2 C 2 . 1.5. Bob publicly shares PK_2 P K 2 , PK_b P K b , and the ciphertext C_2 C 2 .
- Alice (sender) generates a key pair (sk_1, PK_1) ( s k 1 , P K 1 ) randomly for each SA transaction. 2.1. sk_1 s k 1 is Ethereum ephemeral and the public key or wallet address does not need to register on Ethereum before use. 2.2. She combines the two public keys for Ethereum wallet generation, PK_1 P K 1 and PK_b P K b , to obtain PK_z P K z . 2.3. The Stealth Address (SA) is generated based on PK_z P K z by following standard Ethereum address conversion. 2.4. Alice encrypts the secret key sk_1 s k 1 using Bob’s FHE public key PK_b P K b , resulting in the ciphertext C_1 C 1 . Alice then broadcast C1, so that Bob is able to get it in an untrackable manner. 2.5. Alice can not know SA’s private key, as nobody can guess private key from public key PK_z P K z . It means Alice only knows where to send SA transaction, but never be able to login to this SA wallet.
Alice (sender) generates a key pair (sk_1, PK_1) ( s k 1 , P K 1 ) randomly for each SA transaction. 2.1. sk_1 s k 1 is Ethereum ephemeral and the public key or wallet address does not need to register on Ethereum before use. 2.2. She combines the two public keys for Ethereum wallet generation, PK_1 P K 1 and PK_b P K b , to obtain PK_z P K z . 2.3. The Stealth Address (SA) is generated based on PK_z P K z by following standard Ethereum address conversion. 2.4. Alice encrypts the secret key sk_1 s k 1 using Bob’s FHE public key PK_b P K b , resulting in the ciphertext C_1 C 1 . Alice then broadcast C1, so that Bob is able to get it in an untrackable manner. 2.5. Alice can not know SA’s private key, as nobody can guess private key from public key PK_z P K z . It means Alice only knows where to send SA transaction, but never be able to login to this SA wallet.
- Bob receives the ciphertext C_1 C 1 and adds two ciphertexts ( C_1 C 1 , C_2 C 2 ) together to get the C C . 3.1 With the additive homomorphism, he can decrypt the ciphertext C C with his FHE private key sk_b s k b . The FHE decryption result is the private key sk_z s k z to the wallet that receives the sent from Alice. 3.3. Then, he can generate the stealth address with sk_z s k z and decrypt it with the private key, which only bob owns.So Bob is capable of transferring its balance with the private key sk_z s k z for SA wallet .
Bob receives the ciphertext C_1 C 1 and adds two ciphertexts ( C_1 C 1 , C_2 C 2 ) together to get the C C . 3.1 With the additive homomorphism, he can decrypt the ciphertext C C with his FHE private key sk_b s k b . The FHE decryption result is the private key sk_z s k z to the wallet that receives the sent from Alice. 3.3. Then, he can generate the stealth address with sk_z s k z and decrypt it with the private key, which only bob owns.So Bob is capable of transferring its balance with the private key sk_z s k z for SA wallet .
Based BasedSAP, FHE-DKSAP has bellow improvement:
- It protects privacy of stealth address by computing over ciphertext.
- Compared to DKSAP and BasedSAP, our design remove the risk of leakages on keys and personal information.
- Meanwhile, it can prevent quantum computing attacks as well.

## 4. Our Implementation: FHE-DKSAP

We have implement FHE-DKSAP in Python and we will provide code here soon.

## 5. Our Evaluation: FHE-DKSAP

We have tested FHE-DKSAP and comparing to BaseSAP and we will provide evaluation here soon.

## 6. Other reading

## 6.1 Recap of Dual-key Stealth Address Protocol (DKSAP)

DKSAP builds on the Diffie-Hellman (DH) key exchange protocol in elliptic curve (EC). When a sender (A) would like to send a transaction to a receiver (B) in stealth mode, DKSAP works as follows:
Definitions:
- A “stealth meta-address” is a set of one or two public keys that can be used to compute a stealth address for a given recipient.
A “stealth meta-address” is a set of one or two public keys that can be used to compute a stealth address for a given recipient.
- A “spending key” is a private key that can be used to spend funds sent to a stealth address. A “spending public key” is the corresponding public key.
A “spending key” is a private key that can be used to spend funds sent to a stealth address. A “spending public key” is the corresponding public key.
- A “viewing key” is a private key that can be used to determine if funds sent to a stealth address belong to the recipient who controls the corresponding spending key. A “viewing public key” is the corresponding public key.
A “viewing key” is a private key that can be used to determine if funds sent to a stealth address belong to the recipient who controls the corresponding spending key. A “viewing public key” is the corresponding public key.
- The receiver B has a pair of private/public keys (v_B, V_B) ( v B , V B ) and (s_B, S_B) ( s B , S B ) , where v_B v B and s_B s B are called B’s ‘viewing private key’ and ‘spending private key’, respectively, whereas V_B = v_BG V B = v B G and S_B = s_BG S B = s B G are the corresponding public keys. Note that none of V_B V B and S_B S B ever appear in the blockchain and only the sender A and the receiver B know those keys.
- The sender A generates an ephemeral key pair (r_A, R_A) ( r A , R A ) with R_A = r_AG R A = r A G and 0 < r_A r A < n, and sends R_A R A to the receiver B.
- Both the sender A and the receiver B can perform the ECDH protocol to compute a shared secret: c_{AB} = H(r_A*v_B G) = H(r_A*V_B) = H(v_B*R_A) c A B = H ( r A ∗ v B G ) = H ( r A ∗ V B ) = H ( v B ∗ R A ) , where H(·) H ( ⋅ ) is a cryptographic hash function.
- The sender A can now generate the destination address of the receiver B to which A should send the payment: T_A = c_{AB}G + S_B T A = c A B G + S B . Note that the one-time destination address TA is publicly visible and appears on the blockchain.
- Depending on whether the wallet is encrypted, the receiver B can compute the same destination address in two different ways: T_A = c_{AB}G + S_B = (c_{AB} + s_B)G T A = c A B G + S B = ( c A B + s B ) G . The corresponding ephemeral private key is t_A = c_{AB} + s_B t A = c A B + s B , which can only be computed by the receiver B, thereby enabling B to spend the payment received from A later on.

## 6.2 Fully Homomorphic Encryption

Homomorphic Encryption (HE) refers to a special type of encryption technique that allows computations to be done on encrypted data, without requiring access to a secret (decryption) key. The results of the computations remain encrypted, and can be revealed only by the owner of the secret key. There are additive homomorphism and multiplicative homomorphism as below:
Additive homomorphism: E(m_1) + E(m_2) = E(m_1+m_2) E ( m 1 ) + E ( m 2 ) = E ( m 1 + m 2 )
Multiplicative homomorphism: E(m_1) * E(m_2) = E(m_1*m_2) E ( m 1 ) ∗ E ( m 2 ) = E ( m 1 ∗ m 2 )
A homomorphic encryption scheme consists of four procedures, E = ( KeyGen, Encrypt, Decrypt, Evaluate) E = ( K e y G e n , E n c r y p t , D e c r y p t , E v a l u a t e ) :
- (sk, pk) ← KeyGen (1^λ, 1^τ ) ( s k , p k ) ← K e y G e n ( 1 λ , 1 τ ) . Takes the security parameter λ λ and another parameter τ τ and outputs a secret/public key-pair.
(sk, pk) ← KeyGen (1^λ, 1^τ ) ( s k , p k ) ← K e y G e n ( 1 λ , 1 τ ) . Takes the security parameter λ λ and another parameter τ τ and outputs a secret/public key-pair.
- c ← Encrypt(pk, b) c ← E n c r y p t ( p k , b ) . Given the public key and a plaintext bit, outputs a ciphertext.
c ← Encrypt(pk, b) c ← E n c r y p t ( p k , b ) . Given the public key and a plaintext bit, outputs a ciphertext.
- b ← Decrypt(sk, c) b ← D e c r y p t ( s k , c ) . Given the secret key and a ciphertext, outputs a plaintext bit.
b ← Decrypt(sk, c) b ← D e c r y p t ( s k , c ) . Given the secret key and a ciphertext, outputs a plaintext bit.
- c ← Evaluate(pk, Π, c ) c ← E v a l u a t e ( p k , Π , c ) . Takes a public key pk, a circuit Π Π , a vector of ciphertexts, one for every input bit of Π Π , and outputs another vector of ciphertexts, one for every output bit of Π Π .
c ← Evaluate(pk, Π, c ) c ← E v a l u a t e ( p k , Π , c ) . Takes a public key pk, a circuit Π Π , a vector of ciphertexts, one for every input bit of Π Π , and outputs another vector of ciphertexts, one for every output bit of Π Π .
Currently, numerous fully homomorphic encryption (FHE) algorithms exist. Gentry was the pioneer in proposing a homomorphic encryption algorithm capable of performing both multiplication and addition operations. However, its practical implementation has been limited. Another significant advancement is the BGV scheme, which introduces a novel homomorphic encryption construction technology.

## 7. Conclusion

Motivated by the DKSAP and BaseSAP, we propose the FHE-DKSAP to help the receiver outsource the computation of checking the entire chain for stealth addresses containing assets without revealing his view key, and prevent quantum computing attacks.
- Ethereum Magicians

--------------------