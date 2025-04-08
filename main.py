import pandas as pd


def phone_to_hash(phone: str) -> str:
    """Функция преобразования номера в хэш"""
    phone = phone.replace("+7985", "+7985-").replace("8985", "+7985-")
    return phone


def process_csv(input_file: str) -> None:
    """Функция чтения файла и его обработки"""
    with open(input_csv, "r") as f:
        format_encode = f.encoding
        if f.read().strip() == "":
            print("Пустой файл")
            return
        data = pd.read_csv(input_file, encoding=format_encode, sep=";")
        result_list = []
        if "Номер телефона" not in data:
            print("Нет нужного заголовка")
            return

        for number in data["Номер телефона"]:
            hash = phone_to_hash(str(number))
            result_list.append(hash)
        result_df = pd.DataFrame(result_list)
        print(result_df)


input_csv = 'input.csv'

process_csv(input_csv)

