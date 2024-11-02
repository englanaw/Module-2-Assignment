
Cubic_inches_in_cubic_feet = 1728


def Calculate_the_refridgerator():
    Model = input('refridgerator model')
    Height = float(input('Height in inches'))
    width = float(input('width in inches'))
    Depth = float(input('Depth in inches'))

    Cubic_inches = (Height * width * Depth)

    Cubic_feet = (Cubic_inches / Cubic_inches_in_cubic_feet)

    print(Model)
    print(Cubic_feet)
Calculate_the_refridgerator()
