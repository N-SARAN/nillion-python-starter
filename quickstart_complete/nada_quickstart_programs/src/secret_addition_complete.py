from nada_dsl import *

def nada_main():
    # Define parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    # Inputs for party1
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Inputs for party2
    my_int3 = SecretInteger(Input(name="my_int3", party=party2))

    # Perform operations
    sum_ints = my_int1 + my_int2
    product_ints = sum_ints * my_int3

    # Outputs
    return [
        Output(sum_ints, "sum_output", party1),
        Output(product_ints, "product_output", party2)
    ]
