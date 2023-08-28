from assets.menu import *
from assets.files import *
from assets.crypt import *
from assets.dialog import *

SECRET_FILE = 'data/secret.txt'

if __name__ == '__main__':
    # 1

    # 2
    while True:
        # ->
        try:
            start_program()
            k = get_choise()

            if k == 1:
                mess, key = input_encrypt_data()
                secret = encrypt(mess, key)
                write_mess(SECRET_FILE, secret)


            elif k == 2:
                v = input("  Ви вже зашифрували якесь повідомленя? (y/n) ")
                if v == "y":
                    secret_mess = read_mess(SECRET_FILE)
                    key = input_decrypt_data()
                    de_mess = decrypt(secret_mess, key)
                    print(f"  Ваш розшифрований текст - {de_mess}")
                else:
                    print("  Зашифруйте спочатку якийсь текст.")

            elif k == 3:
                break
            else:
                print("  Ви обрали неіснуючий варіант!")

        except ValueError as mess:
            print("  ValueError:", mess)

        if not allow_continue():
            finish_program()
            break
