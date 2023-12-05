from mage_ai.data_preparation.variable_manager import set_global_variable

@custom
def transform_custom(seq, *args, **kwargs):
    
    seq.append(seq[-2] + seq[-1])
    print(seq)
    
    return seq