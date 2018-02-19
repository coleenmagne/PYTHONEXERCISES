



dna = open("dna.txt").read()
D=len(dna)

perc = 0
perg = 0

for i in range(1,D):
    if dna[i]=='C':
        num=len(dna[i])
        perc=perc+num
    if dna[i]=='G':
        num1=len(dna[i])
        perg=perg+num1

sumcg=perc+perg
percg=(sumcg/18.0)*100

print("The percent of C+G is", percg,"%")

