from imports.manipulator import Manipulator
import sys


def main():
    if len(sys.argv) < 3:
        err_code = '0C'  # C stands for custom
        err_mess = 'NOT ENOUGH INPUT ARGUMENTS'
        err_details = 'please pass the name of both input and output directory'
        raise ValueError(err_code, err_mess, err_details)

    manipulator= Manipulator()
    manipulator.performManipulation()
    print('END')







if __name__ == "__main__":
    main()