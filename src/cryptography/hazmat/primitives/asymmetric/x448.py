# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.


import abc

from cryptography.exceptions import UnsupportedAlgorithm, _Reasons


class X448PublicKey(metaclass=abc.ABCMeta):
    @classmethod
    def from_public_bytes(cls, data):
        from cryptography.hazmat.backends.openssl.backend import backend

        if not backend.x448_supported():
            raise UnsupportedAlgorithm(
                "X448 is not supported by this version of OpenSSL.",
                _Reasons.UNSUPPORTED_EXCHANGE_ALGORITHM,
            )

        return backend.x448_load_public_bytes(data)

    @abc.abstractmethod
    def public_bytes(self, encoding, format):
        """
        The serialized bytes of the public key.
        """


class X448PrivateKey(metaclass=abc.ABCMeta):
    @classmethod
    def generate(cls):
        from cryptography.hazmat.backends.openssl.backend import backend

        if not backend.x448_supported():
            raise UnsupportedAlgorithm(
                "X448 is not supported by this version of OpenSSL.",
                _Reasons.UNSUPPORTED_EXCHANGE_ALGORITHM,
            )
        return backend.x448_generate_key()

    @classmethod
    def from_private_bytes(cls, data):
        from cryptography.hazmat.backends.openssl.backend import backend

        if not backend.x448_supported():
            raise UnsupportedAlgorithm(
                "X448 is not supported by this version of OpenSSL.",
                _Reasons.UNSUPPORTED_EXCHANGE_ALGORITHM,
            )

        return backend.x448_load_private_bytes(data)

    @abc.abstractmethod
    def public_key(self):
        """
        The serialized bytes of the public key.
        """

    @abc.abstractmethod
    def private_bytes(self, encoding, format, encryption_algorithm):
        """
        The serialized bytes of the private key.
        """

    @abc.abstractmethod
    def exchange(self, peer_public_key):
        """
        Performs a key exchange operation using the provided peer's public key.
        """
