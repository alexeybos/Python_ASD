import random

from ASD1.test.lesson11.bloom_with_delete import BloomFilter

def bloom_recovery():
    '''
    только брутфорс.
    Знаем размер фильтра. Знаем ограниченное значение символов, из которых состоят строки, сохраненные в фильтре
    результат
    '''
    bfilter = BloomFilter(32)
    bfilter.add("0123456789")
    bfilter.add("2345678901")
    bfilter.add("4567890123")
    bfilter.add("6789012345")
    bfilter.add("8901234567")

    bloom_real = bin(bfilter.bloom)
    eq = False
    interation = 0
    bfilter_new = BloomFilter(32)
    vals = []
    while not eq or interation < 100000:
        vals = []
        for i in range(5):
            str1 = ''
            for j in range(10):
                str1 = str1 + str(random.randint(0,9))
            bfilter_new.add(str1)
            vals.append(str1)
        eq = bloom_real == bin(bfilter_new.bloom)
        interation = interation + 1
    print(eq)
    for v in vals:
        print(v)