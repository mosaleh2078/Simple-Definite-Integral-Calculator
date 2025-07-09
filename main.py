import numpy as np
import colorama
import typing
import math
import os

# Custom type: allows int or None for return type
T1 = typing.Union[int, None]

class Function:
    def __init__(self,_max:int, _min:int) -> None:
        """
        Initializes a Function object with a given integration range.

        Parameters:
            _max (int): Upper limit of the integral.
            _min (int): Lower limit of the integral.

        Initializes:
            self.n: number of intervals (set later).
            self.func: the function expression as a string (to be read from a file).
        """
        self.n = 0
        self.func = None
        self.max = _max
        self.min = _min

    def function_read(self, file:str) -> T1:
        """
        Reads a single-line function string from a given text file.

        Parameters:
            file (str): The filename containing the function definition.

        Returns:
            1 if the file doesn't exist or contains more than one line,
            Otherwise, None and sets self.func to the read function string.
        """
        path = os.path.join(os.getcwd(), file)
        if not os.path.exists(path):
            io_handler(f"File {file} doesn't exist!", 1)
            return 1
        with open(path, 'r') as source:
            func: str = [source.read().strip()]
            if len(func) != 1:
                io_handler("Multiple line of equation is not supported!", 1)
                return 1
            else:
                io_handler("Function read successfully", 0)
                self.func = func[0]

    def _function_cal(self, x) -> float:
        """
        Evaluates the stored function expression at a given x.

        Parameters:
            x (float): The value at which to evaluate the function.

        Returns:
            The result of evaluating the function at x.

        Warning:
            Uses eval() directly on self.func. Assumes self.func is a valid expression.
        """
        return eval(self.func)

    def error_bound(self, k:int) -> int:
        """
        Computes the required number of intervals (self.n) for integration
        based on the maximum second derivative bound `k`, and sets self.n.

        Parameters:
            k (int): Upper bound for the second derivative of the function.

        Formula used:
            n = ceil( sqrt( (k * (b - a)) / 0.00024 ) )
        """
        self.n = math.ceil(math.sqrt((k * (self.max - self.min)) / 0.00024))

    def calculate(self) -> float:
        """
        Numerically integrates the stored function over [min, max] using
        the Midpoint Riemann Sum with `self.n` intervals.

        Returns:
            The approximate value of the definite integral.
        """
        delta_x: float = (self.max - self.min) / self.n
        arr = np.arange(self.min, self.max + delta_x, delta_x)
        ranges: list = np.column_stack((arr[:-1], arr[1:])).tolist()
        _sum:float = 0.0
        for r in ranges:
            mid = (r[0] + r[1]) / 2
            _sum += self._function_cal(mid)
        else:
            return _sum * delta_x

def io_handler(message:str, status:int) -> int:
    """
    Displays a formatted message in the terminal using the colorama color scheme.

    Parameters:
        message (str): The text to display.
        status (int): Determines message type:
            0 = success (green),
            1 = error (red),
            2 = warning (yellow),
            3 = info (light blue)

    Returns:
        0 on success, 1 on unknown status.
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
    """
    Main program logic:
    - Displays an ASCII welcome screen.
    - Takes user input for integral range [a, b], bound k, and filename.
    - Loads the function from a file.
    - Computes the required number of intervals for the desired accuracy.
    - Approximates the integral using the midpoint rule.
    - Displays the result.
    """
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
            io_handler(f"Range set from {a} to {b}", 0)
            io_handler("Using this equation, first calculate the k and then enter it (|f''(x)| <= k)", 3)
            k = int(input("-> "))
            io_handler(f"K set to {k}", 0)
            io_handler("Enter the name of equation file", 3)
            file = input("-> ")
            io_handler(f"File set to {file}", 0)
        except Exception as e:
            io_handler(f"Error: {e}, please enter again ...", 1)
        else:
            break
    func = Function(_max=b, _min=a)
    r = func.function_read(file)
    if r == 1:
        exit(1)
    func.error_bound(k)
    result:float = func.calculate()
    io_handler(f"Result: {result}", 0)
