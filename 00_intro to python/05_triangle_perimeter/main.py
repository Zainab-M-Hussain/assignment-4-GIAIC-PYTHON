def main():
    print ('this program calculate the perimeter of triangle')
    side1 = float(input('what is the lenght of side 1 ?'))
    side2 = float(input('what is the lenght of side 2 ?'))
    side3 = float(input('what is the lenght of side 3 ?'))
    perimeter = float(side1 + side2 + side3 )
    print ('the perimeter of a triangle is :' , perimeter)


if __name__ == '__main__':
    main()