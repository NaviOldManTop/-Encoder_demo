def encrypt(open_mess: str, key: int) -> str:
    buff = ""
    for a in open_mess:
        x = ord(a)
        y = x + key
        b = chr(y)
        buff += b
    print(" Повідомлення успішно зашифроване!")
    return buff


def decrypt(secret_mess: str, key: int) -> str:
    buff = ""
    for a in secret_mess:
        x = ord(a)
        y = x - key
        b = chr(y)
        buff += b
    print("  Повідомлення готове")
    return buff
