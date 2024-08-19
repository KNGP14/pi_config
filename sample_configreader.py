import configparser

config = configparser.ConfigParser()
config.read('pi_gpio.config')

def getGPIO(query_name, query_config):
    for section in query_config.sections():
        if "GPIO_" in section:
            name=query_config.get(section,"NAME", fallback="")
            if name==query_name:
                gpio=section[5:]
                mode=query_config.get(section,"MODE", fallback="")
                gpio_config = {
                    "gpio": gpio,
                    "mode": mode,
                    "name": name
                }
                return gpio_config

print(getGPIO("HAUPTSCHALTER_BEWAESSERUNG", config))
print(getGPIO("HAUPTSCHALTER_BEWAESSERUNG", config)["gpio"])
print(getGPIO("HAUPTSCHALTER_BEWAESSERUNG", config)["mode"])
print(getGPIO("HAUPTSCHALTER_BEWAESSERUNG", config)["name"]) 