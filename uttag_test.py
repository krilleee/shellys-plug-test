from InquirerPy import inquirer
import ShellyPy

VPplug = ShellyPy.Shelly("***REMOVED***")

while(True):
    lamp_on = inquirer.select(
        message="Vill du trycka på lampan?:",
        choices=["Ja", "Nej", "Ta mig härifrån!"],
    ).execute()

    if lamp_on == "Ja":
        VPplug.relay(0, turn=True)
    if lamp_on == "Ta mig härifrån!":
        break
        