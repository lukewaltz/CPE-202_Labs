def weight_on_planets():
    # write your code here
    weight = float(input('What do you weigh on earth? '))
    marsWeight = weight * 0.38
    jupiterWeight = weight * 2.34
    print("\nOn Mars you would weigh", marsWeight, "pounds.\nOn Jupiter you would weigh", jupiterWeight, "pounds.\n")


if __name__ == '__main__':
    weight_on_planets()
