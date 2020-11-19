class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

try:
    assert sum([1,2])==3, "Sum of [1,2] should be 3"
    print(f"{bcolors.OKGREEN}Passed: Sum of [1,2] is 3{bcolors.ENDC}") 
    assert sum([1,2,3])==5, "Sum of [1,2,3] should be 6"
    print(f"{bcolors.OKGREEN}Passed: Sum of [1,2,3] is 6{bcolors.ENDC}")
except AssertionError as msg:  
    print(f"{bcolors.FAIL}Failed: {msg}{bcolors.ENDC}")