#include <string>

std::string DNAStrand(const std::string& dna) {
    std::string complementary;

    for (char nucleotide : dna) {
        switch (nucleotide) {
            case 'A':
                complementary += 'T';
                break;
            case 'T':
                complementary += 'A';
                break;
            case 'C':
                complementary += 'G';
                break;
            case 'G':
                complementary += 'C';
                break;
            default:
                break;
        }
    }

    return complementary;
}
