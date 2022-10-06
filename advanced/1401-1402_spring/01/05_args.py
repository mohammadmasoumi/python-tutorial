
# func_unlimited_args(*args)
# arguments
# *inputs = [1, 2, 3, 4, 4]
def func_unlimited_args(*inputs):
    print(f"inputs: {inputs}, type: {type(inputs)}")


# a, *b, c = [1, 2, 3, 4 ,5]
func_unlimited_args()
func_unlimited_args(1, 2, 3, 4, 4)
func_unlimited_args(1, 2, 3, 4, 4, 5)
func_unlimited_args(1, 2, 3, 4, 4, 5, 6)
