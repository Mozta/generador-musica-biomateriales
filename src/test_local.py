import time
import random
from pythonosc.udp_client import SimpleUDPClient

# Configurar el cliente OSC para SuperCollider
osc_client = SimpleUDPClient("127.0.0.1", 57120)

# Listas de frecuencias mapeadas a los sensores
frequencies_cuenco = [136.1, 176, 194, 214, 242, 262, 286, 330, 360, 392]
frequencies_piano = [261, 293, 329, 349, 392, 440, 493, 523, 587, 659]  # Notas de piano
frequencies_synth = [136, 176, 220, 261, 330, 392, 440, 494, 523, 587]  # Pads etéreos

print("Enviando datos aleatorios a SuperCollider (Cuencos, Piano, Synth)...")

# Iniciar grabación en SuperCollider
osc_client.send_message("/startRecording", [1])
print("Grabación iniciada...")

try:
    while True:
        # Generar valores aleatorios para simular sensores
        values = [
            random.randint(0, 1000),  # Capacitancia 1
            random.randint(0, 1000),  # Capacitancia 2
            random.randint(0, 1000),  # Capacitancia 3
            random.uniform(10, 40),   # Temperatura (10-40°C)
            random.randint(0, 1000)   # Luz
        ]

        # Mapeo de capacitancia a frecuencias
        index_cuenco = min(len(frequencies_cuenco) - 1, int((values[0] / 1000) * len(frequencies_cuenco)))
        freq_cuenco = frequencies_cuenco[index_cuenco]

        index_piano = min(len(frequencies_piano) - 1, int((values[1] / 1000) * len(frequencies_piano)))
        freq_piano = frequencies_piano[index_piano]

        index_synth = min(len(frequencies_synth) - 1, int((values[2] / 1000) * len(frequencies_synth)))
        freq_synth = frequencies_synth[index_synth]

        # Temperatura afecta el volumen del sintetizador
        temp = values[3] / 50  # Normalizamos temperatura (0-50°C)
        amp_synth = max(0.2, min(temp, 1.0))

        # Luz afecta la reverb del piano
        luz = values[4] / 1000  # Normalizamos luz (0-1000)
        reverb_piano = max(0.3, min(luz, 0.9))

        # Enviar a SuperCollider
        osc_client.send_message("/sensor1", freq_cuenco)
        osc_client.send_message("/sensor2", [freq_piano, reverb_piano])
        osc_client.send_message("/sensor3", [freq_synth, amp_synth])

        print(f"Cuenco: {values[0]} -> {freq_cuenco} Hz | Piano: {values[1]} -> {freq_piano} Hz | Synth: {values[2]} -> {freq_synth} Hz | Temp: {values[3]:.2f}°C | Luz: {values[4]}")

        time.sleep(0.2)  # Pequeño delay para evitar repeticiones excesivas

except KeyboardInterrupt:
    print("\nDeteniendo lectura y liberando recursos.")
    # Detener grabación en SuperCollider
    osc_client.send_message("/stopRecording", [1])
    print("Grabación detenida.")
