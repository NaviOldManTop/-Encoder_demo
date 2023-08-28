def read_mess(file: str) -> str:
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()
    return text


def write_mess(file_path: str, mess: str) -> None:
    with open(file_path, "w", encoding="utf-8") as file_stream:
        file_stream.write(mess)
        print("  Повідомлення успішно збережено!")
