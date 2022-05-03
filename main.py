from fileauth import FileAuth

filename = input("Enter filename: ")
block_size = int(input("Enter block size: "))
file_auth = FileAuth(filename, block_size)
print("Hash (sha256): ", file_auth.auth().hex())
file_auth.__del__()
