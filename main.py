import pandas as pd


def phone_to_hash(phone: str) -> str:
    """Функция преобразования номера в хэш"""
    phone = phone.replace("8985", "+7985-").replace("+7985", "+7985-")
    return phone


def process_csv(input_file: str, output_file: str) -> None:
    """Функция чтения файла и его обработки"""
    with open(input_csv, "r") as f:
        format_encode = f.encoding

        data = pd.read_csv(input_file, encoding=format_encode, sep=";")
        result_list = []

        for number in data["Номер телефона"]:
            hash = phone_to_hash(str(number))
            result_list.append(hash)
        result_df = pd.DataFrame(result_list)
        print(result_df)


input_csv = 'input.csv'
output_csv = 'output.csv'

process_csv(input_csv, output_csv)
