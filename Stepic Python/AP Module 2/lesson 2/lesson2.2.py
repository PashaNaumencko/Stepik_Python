from simplecrypt import decrypt, DecryptionException
with open("passwords.txt", "r", encoding="utf-8") as stream_for_passwords:
    with open("encrypted.bin", "rb") as stream_for_encrypt:
        encrypted_text = stream_for_encrypt.read()
        for password in stream_for_passwords.read().strip().splitlines():
            try:
                print("Encrypted message:", decrypt(password, encrypted_text).decode("utf-8"))
                break
            except DecryptionException:
                print(password, "is wrong")
