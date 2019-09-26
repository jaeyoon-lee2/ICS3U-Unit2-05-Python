#!/user/bin/env python3

# Created by: Jaeyoon
# Created on: Sept 2019
# This program shows local and global variables work

#global variable
variable_X = 25


def local_wariable():
    # this show what happens with local variables

    variable_X = 10
    variable_Y = 30
    variable_Z = variable_Y + variable_X
    print("Local variable_X, variable_Y, variable_Z: {0} + {1} = {2}".
    format(variable_X, variable_Y, variable_Z))


def global_variable():
    # this show what happens with global variables

    global variable_X
    variable_X = variable_X + 1
    variable_Y = 30
    variable_Z = variable_X + variable_Y
    print("Global variable_X, variable_Y, variable_Z: {0} + {1} = {2}".
    format(variable_X, variable_Y, variable_Z))


def main():
    # this function show how local and globalvariabls work
    
    local_wariable()
    global_variable()


if __name__ == "__main__":
    main()
