def start_program() -> None:
    print("===============================================")
    print("  Універсальна програма шифрування повідомлень ")
    print("===============================================")
    print("   1 - Зашифрувати повідомлення                ")
    print("   2 - Розшифрувати повідомлення               ")
    print("   3 - Вийти із програми                       ")
    print("===============================================")


def finish_program() -> None:
    print("\nПрограму завершено", end="")


def allow_continue() -> bool:
    allow = input("\n> Продовжити? (y/n) ? - ")
    return allow == 'y'


def get_choise() -> int:
    choise = int(input("  > Виберіть потрібну інформацію: "))
    return choise