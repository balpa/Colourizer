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

import requests
import time

URL = "https://random-data-api.com/api/color/random_color"


class Colourizer:
    def __init__(self, id, uid, hex_value, color_name, hsl_value, hsla_value):
        self.id = id
        self.uid = uid
        self.hex_value = hex_value
        self.color_name = color_name
        self.hsl_value = hsl_value
        self.hsla_value = hsla_value

    def randContinuously():
        count = 0
        while True:
            response = requests.get(URL)
            page = response.json()

            # DATA FETCH COUNT
            count += 1
            for x in range(0, 10000, 10):
                if count == x:
                    print(f"Data fetched {count} times! ")

            Colourizer.id = page["id"]
            Colourizer.uid = page["uid"]
            Colourizer.hex_value = page["hex_value"]
            Colourizer.color_name = page["color_name"]
            Colourizer.hsl_value = page["hsl_value"]
            Colourizer.hsla_value = page["hsla_value"]

            print(
                f"""
            ************************************
            * ID: {Colourizer.id} \r
            * UID: {Colourizer.uid}
            * Hex Value: {Colourizer.hex_value}
            * Color Name: {Colourizer.color_name}
            * HSL Value: {Colourizer.hsl_value}
            * HSLA Value: {Colourizer.hsla_value}
            ************************************
            """
            )
            time.sleep(1)

    def rand(console: bool = False) -> dict:
        """
        The first argument of this function decides whether it will print the data on the console or not.
        True = print, False or None = don't print.
        """
        color = {
            "Id": "",
            "UID": "",
            "Hex Value": "",
            "Color Name": "",
            "HSL Value": "",
            "HSLA Value": "",
        }
        response = requests.get(URL)
        page = response.json()

        Colourizer.id = page["id"]
        Colourizer.uid = page["uid"]
        Colourizer.hex_value = page["hex_value"]
        Colourizer.color_name = page["color_name"]
        Colourizer.hsl_value = page["hsl_value"]
        Colourizer.hsla_value = page["hsla_value"]

        color["Id"] = Colourizer.id
        color["UID"] = Colourizer.uid
        color["Hex Value"] = Colourizer.hex_value
        color["Color Name"] = Colourizer.color_name
        color["HSL Value"] = Colourizer.hsl_value
        color["HSLA Value"] = Colourizer.hsla_value

        if console == True:
            print(
                f"""
            ************************************
            * ID: {Colourizer.id} \r
            * UID: {Colourizer.uid}
            * Hex Value: {Colourizer.hex_value}
            * Color Name: {Colourizer.color_name}
            * HSL Value: {Colourizer.hsl_value}
            * HSLA Value: {Colourizer.hsla_value}
            ************************************
            """
            )
        elif console == False:
            pass
        else:
            raise ValueError(
                "The first argument of this function must be True or False."
            )

        return color

    def RGBtoHEX(RED: int, GREEN: int, BLUE: int) -> str:

        if RED > 255 or GREEN > 255 or BLUE > 255:
            raise ValueError("RGB values must be between 0 and 255.")
        if RED < 0 or GREEN < 0 or BLUE < 0:
            raise ValueError("RGB values must be between 0 and 255.")

        hex_value = "#{:02x}{:02x}{:02x}".format(RED, GREEN, BLUE).upper()
        return hex_value


final = Colourizer.RGBtoHEX(54, 244, 222)
print(final)
