from InquirerPy import inquirer
import ShellyPy
import time

VPplug = ShellyPy.Shelly("<ipadress-to-plug")

while (True):
    lamp_on = inquirer.select(
        message="Vad vill du göra?:",
        choices=["Tända", "Släcka", "Morse", "Ta mig härifrån!"],
    ).execute()

    if lamp_on == "Tända":
        VPplug.relay(0, turn=True)
    if lamp_on == "Släcka":
        VPplug.relay(0, turn=False)
    if lamp_on == "Ta mig härifrån!":
        break

    if lamp_on == "Morse":
        morse_kod = "-*.-.*.*...-*.-..*..*--./....*.*.-..*--." #Trevlig helg

        morse = []
        for char in morse_kod:
            VPplug.relay(0, turn=False)
            time.sleep(0.5)
            if char == ".":
                VPplug.relay(0, turn=True)
                time.sleep(0.5)
            elif char == "-":
                VPplug.relay(0, turn=True)
                time.sleep(1.5)
            elif char == "*":
                VPplug.relay(0, turn=False)
                time.sleep(1)
            elif char == "/":
                VPplug.relay(0, turn=False)
                time.sleep(3)