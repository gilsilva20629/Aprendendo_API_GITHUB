from secp256k1 import PrivateKey

class KeyPair:
	def __init__(self, str_random: str):
		self.secret_key = PrivateKey(bytes.fromhex(str_random))

	def sign(self, message: str):
		message_bytes = bytes.fromhex(message)

		return self.secret_key.schnorr_sign(
			message_bytes, 
			bip340tag=None, 
			raw=True
			).hex()

	def verify(self, message: str, signature: str):
		message_bytes = bytes.fromhex(message)
		signature_bytes = bytes.fromhex(signature)

		return self.secret_key.pubkey.schnorr_verify(
			message_bytes,
			signature_bytes,
			bip340tag=None, 
			raw=True
			)

	def getPubkey(self):
		return self.secret_key.pubkey.serialize()[1:].hex()

	def getbytes(self):
		return self.secret_key.private_key

	def serialize(self):
		return self.secret_key.serialize()


