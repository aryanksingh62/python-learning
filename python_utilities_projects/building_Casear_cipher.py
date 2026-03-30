def encrypt(messg,key):
    encrypt_messg=""
    for ch in messg:
        if ch.isalpha():
            base= ord("A") if ch.isupper() else ord("a")
            shifted=chr((ord(ch)-base+key)% 26 + base)
            encrypt_messg+=shifted
        else:
            encrypt_messg+=ch
    return encrypt_messg

def decrypt(messg,key):
    return encrypt(messg,-key)

text=input("what you want to do encrpt(E)/decrypt(D) a messge:E/D?").strip().upper()

if text=="E":
    try:
        messg=input("enter message you want to encrypt:")
        key=int(input("enter the key:"))
        print("your encrypted message is:",encrypt(messg,key))
    except ValueError:
        print("Invalid Key")
else:
    try:
        messg=input("enter message you want to decrypt:")
        key=int(input("enter the key:"))
        print("your decrypted message is:",decrypt(messg,key))
    except ValueError:
        print("Invalid key")