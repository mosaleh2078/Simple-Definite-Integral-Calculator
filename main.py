import math
import os
import colorama
import typing
import numpy as np

# Custom type: allows int or None for return type
T1 = typing.Union[int, None]

class Function:
    def __init__(self,_max:int, _min:int) -> None:
        """
            Initializes a Function object with a max and min range for integration.
            Sets self.func to None initially.
        """
        self.func = None
        self.max = _max
        self.min = _min

    def function_read(self, file:str) -> T1:
        """
            Reads a function from a text file (single-line equation).
            If successful, stores the function as a string in self.func.
            Returns 1 if the file doesn't exist or contains multiple lines.
        """
        path = os.path.join(os.getcwd(), file)
        if not os.path.exists(path):
            io_handler(f"File {file} doesn't exist!", 1)
            return 1
        with open(path, 'r') as source:
            func: str = list(source.read().strip())
            if len(list) != 1:
                io_handler("Multiple line of equation is not supported!", 1)
                return 1
            io_handler("Function read successfully", 0)
            self.func = func

    def _function_cal(self, x) -> float:
        """
            Returns a lambda function that evaluates the stored function string with the given x.
            This method is intended to be used inside calculate().
        """
        return lambda x: eval(self.func)

    def calculate(self) -> float:
        """
            Approximates the definite integral of the stored function using the midpoint Riemann sum.
            The range is divided into 2 intervals, then evaluated at midpoints.
            Returns the numerical result of the integration.
        """
        delta_x = (self.max - self.min) / 2
        arr = np.arange(self.min, self.max + delta_x, delta_x)
        ranges = np.column_stack((arr[:-1], arr[1:])).tolist()
        _sum:float = 0.0
        for r in ranges:
            mid = (r[0] + r[1]) / 2
            _sum += self._function_cal(mid)
        else:
            return _sum * delta_x

def io_handler(message:str, status:int) -> int:
    """
        Prints a formatted message to the terminal using colorama, based on the status code:
        0 → success (green),
        1 → error (red),
        2 → warning (yellow),
        3 → info (light blue),
        Any other value → returns 1 (invalid).
    """
    if status == 0: # Good
        print(f"[ {colorama.Fore.GREEN}+{colorama.Fore.RESET} ] {message}")
    elif status == 1: # Bad
        print(f"[ {colorama.Fore.RED}-{colorama.Fore.RESET} ] {message}")
    elif status == 2: # Warning
        print(f"[ {colorama.Fore.YELLOW}?{colorama.Fore.RESET} ] {message}")
    elif status == 3:
        print(f"[ {colorama.Fore.LIGHTBLUE_EX}.{colorama.Fore.RESET} ] {message}")
    else:
        return 1
    return 0

if __name__ == "__main__":
    os.system("clear")
    welcome:str = """
                                                                                    
_______                                                                                      
\  ___ `'.        __.....__             .--.  _..._  .--.             __.....__              
 ' |--.\  \   .-''         '.       _.._|__|.'     '.|__|         .-''         '.            
 | |    \  ' /     .-''"'-.  `.   .' .._.--.   .-.   .--.    .|  /     .-''"'-.  `.          
 | |     |  /     /________\   \  | '   |  |  '   '  |  |  .' |_/     /________\   \         
 | |     |  |                  |__| |__ |  |  |   |  |  |.'     |                  |         
 | |     ' .\    .-------------|__   __||  |  |   |  |  '--.  .-\    .-------------'         
 | |___.' /' \    '-.____...---.  | |   |  |  |   |  |  |  |  |  \    '-.____...---.         
/_______.'/   `.             .'   | |   |__|  |   |  |__|  |  |   `.             .'          
\_______|/      `''-...... -'     | |      |  |   |  |     |  '.'   `''-...... -'            
                                  | |      |  |   |  |     |   /                             
                                  |_|      '--'   '--'     `'-'  .---.                       
.--.  _..._                __.....__                             |   |                       
|__|.'     '.          .-''         '.    .--./)                 |   |                       
.--.   .-.   .    .|  /     .-''"'-.  `. /.''\\  .-,.--.         |   |                       
|  |  '   '  |  .' |_/     /________\   | |  | | |  .-. |   __   |   |                       
|  |  |   |  |.'     |                  |\`-' /  | |  | |.:--.'. |   |                       
|  |  |   |  '--.  .-\    .-------------'/("'`   | |  | / |   \ ||   |                       
|  |  |   |  |  |  |  \    '-.____...---.\ '---. | |  '-`" __ | ||   |                       
|__|  |   |  |  |  |   `.             .'  /'""'.\| |     .'.''| ||   |                       
   |  |   |  |  |  '.'   `''-...... -'   ||     || |    / /   | |'---'                       
   |  |   |  |  |   /                    \'. __//|_|    \ \._,\ '/                           
   '--'   '--'  `'-'                      `'---'         `--'  `"                            
       _..._                       _..._                                  .-'''-.            
    .-'_..._''.         .---.   .-'_..._''.        .---.                 '   _    \          
  .' .'      '.\        |   | .' .'      '.\       |   |               /   /` '.   \         
 / .'                   |   |/ .'                  |   |              .   |     \  '         
. '                     |   . '                    |   |            .||   '      |  .-,.--.  
| |                __   |   | |                    |   |   __     .' |\    \     / /|  .-. | 
| |             .:--.'. |   | |              _    _|   |.:--.'. .'     `.   ` ..' / | |  | | 
. '            / |   \ ||   . '             | '  / |   / |   \ '--.  .-'  '-...-'`  | |  | | 
 \ '.          `" __ | ||   |\ '.          .' | .' |   `" __ | |  |  |              | |  '-  
  '. `._____.-'/.'.''| ||   | '. `._____.-'/  | /  |   |.'.''| |  |  |              | |      
    `-.______ // /   | |'---'   `-.______ |   `'.  '---/ /   | |_ |  '.'            | |      
             ` \ \._,\ '/                `'   .'|  '/  \ \._,\ '/ |   /             |_|      
                `--'  `"                   `-'  `--'    `--'  `"  `'-'                       
"""
    print(welcome)
    while True:
        try:
            io_handler("Enter the range of integral:", 3)
            a, b = map(int, input("-> ").split(" ")) # a:min b:max
            io_handler("Using this equation, first calculate the k and then enter it (|f''(x)| <= k)", 3)
            k = int(input("-> "))
            io_handler("Enter the name of equation file", 3)
            file = input("-> ")
        except Exception as e:
            io_handler(f"Error: {e}, please enter again ...", 1)
        else:
            break
    func = Function(_max=b, _min=a)
    r = func.function_read(file)
    if r == 1:
        exit(1)
    result:float = func.calculate()
    io_handler(f"Result: {result}", 0)