class RNA(str):
    '''
    class for RNA sequence parsing
        assigned first as have common with DNA options
        differs from DNA in transcription,
                            reverse complementation
    :param: sequence
    :return: 
        self.gc_content - GC proportion 
        self.reverse_complement - reverse complement sequence
    '''
    def __init__(self, seq_data):
        self.seq_data = seq_data.upper()
        # check validity of sequence
        if set('AGTCU') >= set(self.seq_data):
            pass
        else:
            raise ValueError('The query is not a valid sequence - check for inappropriate nucleotides')
    
    def gc_cont(self):
        self.GC_c = (sum([self.seq_data.count('G'), self.seq_data.count('C')])/len(self.seq_data)) * 100
        return self.GC_c
    
    def reverse_complement(self):
        self.complementary = self.maketrans('AGUTC', 'UCAAG')
        return self.seq_data.translate(self.complementary)[::-1]
    
    # check if sequences of two equal
    def __eq__(self, other):
        return self.seq_data == other.seq_data
    
    def __hash__(self):
        return hash(self.seq_data)
    
class DNA(RNA):
    '''
    class for DNA sequence parsing
        inherit gc_content and reverse_complement from RNA class
        differs from RNA in transcription,
                            reverse complementation
    :param: sequence
    :return: 
        self.gc_content - GC proportion 
        self.reverse_complement - reverse complement sequence
        self.transcription - transcribed sequence (DNA only)
    '''
    def reverse_complement(self):
        self.complementary = self.maketrans('AGTC', 'TCAG')
        return self.seq_data.translate(self.complementary)[::-1]
    
    def transcription(self):
        templ = RNA.reverse_complement(self)
        return templ.replace('T','U')
