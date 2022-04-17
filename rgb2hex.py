

def RGBtoHEX(RED: int, GREEN: int, BLUE: int):
    
        if RED > 255 or GREEN > 255 or BLUE > 255:
            raise ValueError("RGB values must be between 0 and 255.")
        if RED < 0 or GREEN < 0 or BLUE < 0:
            raise ValueError("RGB values must be between 0 and 255.")

        hex_value = "#{:02x}{:02x}{:02x}".format(RED, GREEN, BLUE).upper()
        return hex_value