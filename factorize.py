from os import cpu_count
import concurrent.futures


def fact(number):
    result = list()
    for i in range(1, number + 1):
        if number % i == 0:
            result.append(i)
    return result


def factorize(*number):
    with concurrent.futures.ProcessPoolExecutor(cpu_count()) as executor:
        result = list(executor.map(fact, number))
    return result


if __name__ == '__main__':
    a, b, c, d, e, f = factorize(128, 255, 99999, 10651060, 78764544, 48997487)
    print(a, b, c, d, e, f, sep='\n')
