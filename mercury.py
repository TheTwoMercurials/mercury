import rsa
import sys
import pickle

if len(sys.argv) < 2:
    print('usage: python mercury.py <options>')
    exit()

if sys.argv[1] == 'generate keys':
    public_key, private_key = rsa.newkeys(512)
    with open('public_key', 'wb') as f:
        pickle.dump(public_key, f)
    with open('private_key', 'wb') as f:
        pickle.dump(private_key, f)

elif sys.argv[1] == 'encrypt':
    with open('public_key', 'rb') as f:
        public_key = pickle.load(f)
    encrypted = rsa.encrypt(sys.argv[3].encode(), public_key)
    with open(sys.argv[2], 'wb') as f:
        f.write(encrypted)

elif sys.argv[1] == 'decrypt':
    with open('private_key', 'rb') as f:
        private_key = pickle.load(f)
    with open(sys.argv[2], 'rb') as f:
        decrypted = rsa.decrypt(f.read(), private_key)
        print(decrypted.decode())
