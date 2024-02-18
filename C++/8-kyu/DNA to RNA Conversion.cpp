#include <string>

std::string DNAtoRNA(const std::string& dna) {
    std::string rna = dna;

    for (char& nucleotide : rna) {
        if (nucleotide == 'T') {
            nucleotide = 'U';
        }
    }

    return rna;
}
