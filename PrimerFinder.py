import math
import time

def calculate_tm(sequence):
    A = sequence.count("A")
    T = sequence.count("T")
    C = sequence.count("C")
    G = sequence.count("G")

    result = 100.5 + (41 * ((G+C)/(A+T+G+C))) - (820 / (A+T+G+C)) + 16.6 * math.log10(0.05)

    return result

sequence = input("enter the sequence: ")

start = time.time()

result = calculate_tm(sequence)

end = time.time()

print(result)
print(end - start)

#test: AGTCGATCGATACGTACCTGATCGTATCGATCGATCGATCGATGCATGACGTACGATCGTAGTAGCGTAGCTGATCGATCGTGATCGATGCTAGCTAGCGATCGATGCTAGCTAGCTAGCTAGCTCATCAG