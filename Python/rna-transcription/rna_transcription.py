code = { "G" : "C" ,
		 "C" : "G" ,
		 "T" : "A" ,
		 "A" : "U"
		 }

def to_rna(dna_strand):
	translation = dna_strand.maketrans(code)
	return dna_strand.translate(translation)   

# """Turns DNA sequence into RNA sequence"""

# def to_rna(dna):
#     """Makes RNA sequence from DNA sequence"""
#     return dna.translate(dna.maketrans('GCTA','CGAU'))
