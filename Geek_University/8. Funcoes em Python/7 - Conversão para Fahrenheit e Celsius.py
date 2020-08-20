def conversao_fahrenheit(celcius):
    c = celcius
    f = c * (9 / 5) + 32
    return f

def conversao_celcius(fahrenheit):
    f = fahrenheit
    c = 5 * (f - 32) / 9
    return c