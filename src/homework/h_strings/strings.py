#HW 5

def get_hamming_distance(dna1,dna2):
   count=0

   for i in range(0,len(dna1)):
      if dna1[i]!= dna2[i]:
         count+=1
   return count 

def get_dna_complement(dna):

   comp = ""
   for i in range(0,len(dna)):
      if dna[i]=="C":
         comp="G"+comp
      elif dna[i]=="G":
         comp="C"+comp
      elif dna[i]=="A":
         comp="T"+comp
      elif dna[i]=="T":
         comp="A"+comp
   return comp