class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = None
        self._humidity = None
        self._pressure = None
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)
    
    def set_measurements(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify()

class Observer:
    def update(self, temperature, humidity, pressure):
        raise NotImplementedError("Subclass must implement abstract method")

class PhoneDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print(f"Phone Display: Temperature: {temperature}*C, Humidity: {humidity}%, Pressure: {pressure} hPa")

class DashboardDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print(f"Dashboard Display: Temperature: {temperature}*C, Humidity: {humidity}%, Pressure: {pressure} hPa")


if __name__ == "__main__":
    weather_station = WeatherStation()

    phone_display = PhoneDisplay()
    dashboard_display = DashboardDisplay()

    weather_station.attach(phone_display)
    weather_station.attach(dashboard_display)

    # Simulate new weather measurements
    weather_station.set_measurements(25, 65, 1013)
    weather_station.set_measurements(28, 70, 1009)

    # Detach one observer and simulate new measurements
    weather_station.detach(phone_display)
    weather_station.set_measurements(22, 60, 1011)
