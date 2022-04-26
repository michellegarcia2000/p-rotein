#RNN model 
import numpy as np 

def encode_aa(seq): 
    """
    :param: (str) an amino acid sequence 
    """
    seq_len = len(seq)
    encoded = np.zeros((seq_len, 20), dtype=int)
    # encode based on nonpolar, polar, and charge amino acids: 
    #  G, A, V, C, P, L, I, M, W, F, S, T, Y, N, Q, H, K, R, D, E 
    encode_dict = {}
    for i, a in enumerate(["G", "A", "V", "C", "P", "L", "I", "M", "W", "F", "S", "T", "Y", "N", "Q", "H", "K", "R", "D", "E"]):
        encode_dict[a] = i 
    
    for i, a in enumerate(seq): 
        encoded[i] = encode_dict[a]
    
    return encoded 
