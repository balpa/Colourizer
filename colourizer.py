# @author: Berke Altıparmak
# You may use, distribute and modify this code under the
# terms of the Beerware license, which unfortunately won't be
# written for another century.
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <berkealtiparmak@outlook.com> wrote this file.  As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return.   Berke Altıparmak
# ----------------------------------------------------------------------------

import time
import random
from rgb2hex import RGBtoHEX

class Colourizer:
    def __init__(self, rgb_value, hex_value):
        self.rgb_value = rgb_value
        self.rgba_value = rgba_value
        self.hex_value = hex_value
        self.hsl_value = hsl_value
        self.hsla_value = hsla_value

    def randContinuously(speed: int = 1, console: bool = False):
        """
        The first argument is the speed of the loop. The second argument decides whether it will print the data on the console or not.
        Speed is in seconds and the default value is defined as 1 second.
                 
        """
        count = 0
        while True:
            count += 1
            for x in range(0, 10000, 10):
                if count == x:
                    print(f"Iterated {count} times! ")
                    
            RED = random.randint(0,255)
            GREEN = random.randint(0,255)
            BLUE = random.randint(0,255)
            
            Colourizer.rgb_value = f"({RED},{GREEN},{BLUE})"
            Colourizer.hex_value = RGBtoHEX(RED, GREEN, BLUE)

            print(
                f"""
            ************************************
            * RGB: {Colourizer.rgb_value} \r
            * Hex Value: {Colourizer.hex_value}
            ************************************
            """
            )
            time.sleep(speed)

    def randRGB(console: bool = False):
        """
        The first argument of this function decides whether it will print the data on the console or not.
        True = print, False or None = dont print.
        """
        color = {
            "RGB Value": "",
            "Hex Value": ""
        }
        
        RED = random.randint(0,255)
        GREEN = random.randint(0,255)
        BLUE = random.randint(0,255)

        Colourizer.rgb_value = f"({RED},{GREEN},{BLUE})"
        Colourizer.hex_value = RGBtoHEX(RED, GREEN, BLUE)

        color["RGB Value"] = Colourizer.rgb_value
        color["Hex Value"] = Colourizer.hex_value

        if console == True:
            print(
                f'''
            ************************************
            * RGB: {Colourizer.rgb_value} \r
            * Hex Value: {Colourizer.hex_value}
            ************************************
            '''
            )
        elif console == False:
            pass
        else:
            raise ValueError("The first argument of this function must be True or False.")

        return color
    
    
    

