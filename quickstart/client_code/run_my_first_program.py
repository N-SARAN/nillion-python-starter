from nada_dsl import *

def nada_main():
    # Define parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")

    # Inputs for party1
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Inputs for party2
    my_int3 = SecretInteger(Input(name="my_int3", party=party2))

    # Define additional constants using PublicInteger for simplicity
    my_int4 = PublicInteger(40)
    my_int5 = PublicInteger(50)

    # Perform operations
    sum_ints = my_int1 + my_int2
    product_ints = sum_ints * my_int3

    # Additional computations
    complex_operation = (my_int1 * my_int2) + (my_int3 * my_int4) - my_int5

    # Outputs
    return [
        Output(sum_ints, "sum_output", party1),
        Output(product_ints, "product_output", party2),
        Output(complex_operation, "complex_output", party3)
    ]
