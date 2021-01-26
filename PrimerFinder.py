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

t_min = 58
t_max = 62

sequence_length = len(sequence)
total_primer_counter = 0
correct_primer_counter = 0

for primer_length in range(20, 25):
    for position in range(0, sequence_length - primer_length + 1):
        primer = sequence[position:position + primer_length]
        result = calculate_tm(primer)
        if result > t_min and result < t_max:
            print(primer)
            print(result)
            correct_primer_counter += 1
        total_primer_counter += 1

end = time.time()

print("Total primer counter: " + str(total_primer_counter))
print("Correct primer counter: " + str(correct_primer_counter))
print(end - start)

#test: AGTCGATCGATACGTACCTGATCGTATCGATCGATCGATCGATGCATGACGTACGATCGTAGTAGCGTAGCTGATCGATCGTGATCGATGCTAGCTAGCGATCGATGCTAGCTAGCTAGCTAGCTCATCAG