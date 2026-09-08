# Observer Class
class DisplayDevice:
    def __init__(self, name):
        self.name = name

    def update(self, temperature):
        print(self.name, "received update: Temperature =", temperature, "°C")


# Subject Class
class WeatherStation:
    def __init__(self):
        self.observers = []
        self.temperature = 0

    # Register observer
    def register(self, observer):
        self.observers.append(observer)

    # Notify all observers
    def notify(self):
        for observer in self.observers:
            observer.update(self.temperature)

    # Change temperature
    def set_temperature(self, temperature):
        self.temperature = temperature
        print("\nWeather Station: Temperature changed to", temperature, "°C")
        self.notify()


# Main Program
station = WeatherStation()

display1 = DisplayDevice("Mobile Display")
display2 = DisplayDevice("LED Display")
display3 = DisplayDevice("Computer Display")

# Register devices
station.register(display1)
station.register(display2)
station.register(display3)

# Update temperature
station.set_temperature(30)
station.set_temperature(35)