def input_encrypt_data() -> list:
    message = input("  Введіть ваше повідомлення:\n")
    secret_key = int(input("  Введіть ключ шифрування: "))
    return [message, secret_key]


def input_decrypt_data() -> int:
    key = int(input("  Введіть ваш ключ шифрування: "))
    return key


