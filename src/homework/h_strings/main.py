#HW 5
import strings

def main():
    menu=int(input("Enter number: 1 for Hamming Distance, 2 for Dna Complement, and 3 for exit."))
    while menu !=3:
        if (menu==1):
             dna1=input("Enter DNA string composed of C,T,A, and G: ")
             dna2=input("Enter a second DNA string composed of C,T,A, and G: ") 

             print(strings.get_hamming_distance(dna1,dna2))
        
        if (menu==2):
            dna=input("Enter DNA string composed of C,T,A, and G: ")

            print(strings.get_dna_complement(dna))
        
        else:
            break
        menu=int(input("Enter number: 1 for Hamming Distance, 2 for Dna Complement, and 3 for exit."))

main()