from imports.manipulator import Manipulator
import sys


def main():
    if len(sys.argv) < 3:
        err_code = '0C'  # C stands for custom
        err_mess = 'NOT ENOUGH INPUT ARGUMENTS'
        err_details = 'please pass the name of both input and output directory'
        raise ValueError(err_code, err_mess, err_details)

    manipulator= Manipulator()
    res = manipulator.performManipulation()

    #this case is never reached, since performManipulation() throws errors if fails, it is just the skeleton
    if res[0] != 0:
        print('Error occurred while performing data manipulation')

    else:
        if res[1]:
            print('Termination: SUCCESS')
        else:
            print('Termination FAILURE')







if __name__ == "__main__":
    main()