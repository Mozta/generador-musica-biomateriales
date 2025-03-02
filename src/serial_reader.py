import serial

class SerialReader:
    def __init__(self, port: str, baudrate: int = 9600, timeout: int = 1):
        """
        Inicializa el lector serial.

        :param port: Nombre del puerto serial (ej. "/dev/ttyUSB0" o "COM3")
        :param baudrate: Velocidad de transmisión (default: 9600)
        :param timeout: Tiempo de espera para lectura (default: 1 segundo)
        """
        try:
            self.device = serial.Serial(port, baudrate, timeout=timeout)
            print(f"Conectado a {port} con {baudrate} baudios")
        except serial.SerialException as e:
            print(f"Error al conectar con {port}: {e}")
            self.device = None

    def read_data(self):
        """
        Lee una línea del puerto serial y la devuelve como una cadena de texto.
        """
        if self.device and self.device.is_open:
            try:
                data = self.device.readline().decode('utf-8').strip()
                return data
            except Exception as e:
                print(f"Error al leer datos: {e}")
                return None
        return None

    def close(self):
        """ Cierra la conexión serial. """
        if self.device and self.device.is_open:
            self.device.close()
            print("Conexión serial cerrada.")

# Uso del lector serial
if __name__ == "__main__":
    serial_reader = SerialReader("/dev/tty.usbmodem1414101")  # Cambia el puerto según tu sistema

    try:
        while True:
            data = serial_reader.read_data()
            if data:
                print(f"Datos recibidos: {data}")
    except KeyboardInterrupt:
        print("\nDeteniendo lectura serial.")
    finally:
        serial_reader.close()
