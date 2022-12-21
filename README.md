# genes


2.2 Genes. In cells, DNA contains fundamental information so that the organism provides all the functions useful to live. To support the cell functions, instructions in DNA are first transcribed into RNA molecules. Later, RNA molecules get translated into proteins. Translation from RNA to messenger RNA (mRNA) to proteins is based on genetic code, which is the set of rules in which a sequence of nucleotides ('A', 'C', 'U' and 'G') gets translated in a sequence of amino acids for proteic synthesis. Each amino acid corresponds to one or more sequences of 3 nucleotides, called codons. The following table shows the codon that in mRNA code the 20 ordinary amino acids.

Amino acid	Codons	Amino acid	Codons
Ala	GCU, GCC, GCA, GCG	Leu	UUA, UUG, CUU, CUC, CUA, CUG
Arg	CGU, CGC, CGA, CGG, AGA, AGG	Lys	AAA, AAG
Asn	AAU, AAC	Met	AUG
Asp	GAU, GAC	Phe	UUU, UUC
Cys	UGU, UGC	Pro	CCU, CCC, CCA, CCG
Gln	CAA, CAG	Ser	UCU, UCC, UCA, UCG, AGU, AGC
Glu	GAA, GAG	Thr	ACU, ACC, ACA, ACG
Gly	GGU, GGC, GGA, GGG	Trp	UGG
His	CAU, CAC	Tyr	UAU, UAC
Ile	AUU, AUC, AUA	Val	GUU, GUC, GUA, GUG
Following codons indicate the start and the end of the translation process. Note, start codon also codificates Methionine ('Met').

Instruction	Codons
start	AUG, GUG
stop	UAG, UGA, UAA
Write a program elaborating a sequence of mRNA inserted as an input from the user, showing the sequence of amino acid translated. To simulate the translation problem, use a dictionary genetic_code, which, reading all info reported as a table in genetic_code.csv, memorizes codons and amino acids codified by those codons, choosing opportune keys and values. Then, iterate through the sequence inserted by the user until you find a 'start'. Iterate through the next part memorizing the result of the translation in a list called protein. Translation shall stop when the 'stop' sequence is found. Example: starting from the sequence ('start' and 'stop' are underlined), GUAUGCACGUGACUUUCCUCAUGAGCUGAU, the program shall output: MetHisValThrPheLeuMetSerstop. If no codon of 'start' and 'stop' is found, then output an error.
