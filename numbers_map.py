numbers_map = {
    "zero": "0",
    "um": "1",
    "dois": "2",
    "três": "3",
    "quatro": "4",
    "cinco": "5",
    "seis": "6",
    "sete": "7",
    "oito": "8",
    "nove": "9",
    "dez": "10",
    "onze": "11",
    "doze": "12",
    "treze": "13",
    "quatorze": "14",
    "quinze": "15",
    "dezesseis": "16",
    "dezessete": "17",
    "dezoito": "18",
    "dezenove": "19",
    "vinte": "20",
    "trinta": "30",
    "quarenta": "40",
    "cinquenta": "50",
    "sessenta": "60",
    "setenta": "70",
    "oitenta": "80",
    "noventa": "90",
    "cem": "100"
}

# Adicionando números de 21 a 99
for tens in ["vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]:
    for unit in ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]:
        if unit:
            numbers_map[f"{tens} e {unit}"] = f"{numbers_map[tens]}{numbers_map[unit]}"
        else:
            numbers_map[tens] = numbers_map[tens]

# Adicionando números de 101 a 999
hundreds = ["cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

for i, hundred in enumerate(hundreds, 1):
    # Adicionando centenas exatas
    numbers_map[hundred] = f"{i}00"

    # Adicionando números de 101 a 199, 201 a 299, ..., 901 a 999
    for remainder in range(1, 100):
        if remainder <= 19:
            numbers_map[f"{hundred} e {list(numbers_map.keys())[remainder]}"] = f"{i}00{remainder}"
        else:
            ten_part = remainder // 10 * 10
            unit_part = remainder % 10
            if unit_part == 0:
                numbers_map[f"{hundred} e {list(numbers_map.keys())[ten_part]}"] = f"{i}00{ten_part}"
            else:
                numbers_map[f"{hundred} e {list(numbers_map.keys())[ten_part]} e {list(numbers_map.keys())[unit_part]}"] = f"{i}00{ten_part}{unit_part}"
