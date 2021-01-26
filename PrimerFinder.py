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

sequence_length = len(sequence)
primer_counter = 0

for primer_length in range(20, 25):
    for position in range(0, sequence_length - primer_length + 1):
        primer = sequence[position:position + primer_length]
        result = calculate_tm(primer)
        print(primer)
        print(result)
        primer_counter += 1

end = time.time()

print("Primer counter: " + str(primer_counter))
print(end - start)

#test: AGTCGATCGATACGTACCTGATCGTATCGATCGATCGATCGATGCATGACGTACGATCGTAGTAGCGTAGCTGATCGATCGTGATCGATGCTAGCTAGCGATCGATGCTAGCTAGCTAGCTAGCTCATCAG