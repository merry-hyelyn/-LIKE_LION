def plus(num1, num2):
    result = {
        "real" : num1["real"] + num2["real"],
        "image" : num1["image"] + num2["image"],
    }

    return result


complex1 = {
    "real" : 5.0,
    "image" : 6.0,
}

complex2 = {
    "real" : 2.0,
    "image" : 4.0,
}

result = plus(complex1, complex2)
print(complex1, complex2, result)
