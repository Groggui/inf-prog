import re


def identify_of_num(number):
    private_car_pattern = r'^[А,В,Е,К,М,Н,О,Р,С,Т,У,Х]{1}\d{3}[А-Я]{2}\d{2,3}$'
    taxi_pattern = r'^[А,В,Е,К,М,Н,О,Р,С,Т,У,Х]{2}\d{3}\d{2,3}$'

    if re.match(private_car_pattern, number):
        return "Частный"
    elif re.match(taxi_pattern, number):
        return "Такси"
    else:
        return "Не номер"


numbers = ["С227НА777", "КУ22777", "Т22В7477", "М227К19У9"]
for number in numbers:
    print(f"{number}: {identify_of_num(number)}")


def count_words(text):
    words = re.findall(r'[А-Яа-яA-Za-z-]+', text)
    return len(words)


text = "Он - серо-буро-малиновая редиска! А не кот"
word_count = count_words(text)
print(word_count)

def replace(text):
    time_pattern = r'\d{2}:\d{2}(:\d{2})?'
    replaced_text = re.sub(time_pattern, "(TBD)", text)
    return replaced_text


text = "Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю."
replaced_text = replace(text)
print(replaced_text)