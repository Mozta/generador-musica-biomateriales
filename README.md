# generador-musica-biomateriales
# **Generador de música con biomateriales** 🎶🌿

Sistema de generación musical basado en biomateriales y sensores ambientales, diseñado para crear música tranquila, melódica y armónica

---

## **🚀 Características principales**
✅ **Sonidos generados**: Cuencos tibetanos, piano etéreo y sintetizador atmosférico.  
✅ **Interacción con el entorno**: Modificado en tiempo real por **capacitancia, luz y temperatura**.
✅ **SuperCollider & Python**: Comunicación mediante **OSC** para control preciso del sonido.  
✅ **Grabación en tiempo real**: Guarda la sesión en formato **WAV**.

---

## **📌 Tecnologías**
- **Hardware**:
  - Adafruit Circuit Playground Bluefruit (sensores capacitivos, temperatura y luz).
- **Software**:
  - **SuperCollider** (Síntesis y generación de sonido).
  - **Python** (Lectura de sensores y comunicación OSC).
  - **CircuitPython** (Captura y procesamiento de datos).
  - **OSC (Open Sound Control)** (Comunicación entre Python y SuperCollider).

---

## **📂 Estructura del proyecto**
```
📂 generador-musica-biomateriales
│── 📁 src
│   ├── serial_reader.py  # Clase para lectura de sensores
│   ├── main.py  # Script principal en Python
│── 📁 supercollider
│   ├── sound_generator.scd  # Código de SuperCollider
│── README.md 
```

---

## **🎼 Sonidos generados**
### **1️⃣ Cuencos tibetanos** 🥣
   - Basado en resonancias armónicas naturales.
   - Se activa con sensores capacitivos.
   - Procesado con **GVerb** para mayor profundidad.

### **2️⃣ Piano etéreo** 🎹
   - Melodías basadas en la **escala pentatónica mayor**.
   - La **luz ambiental** ajusta la reverberación.
   - Generado con **SinOsc y FreeVerb** en SuperCollider.

### **3️⃣ Synth atmosférico** 🌌
   - Armonía base con ondas **LFSaw y SinOsc**.
   - La **temperatura** modifica la calidez del sonido.
   - Filtro dinámico y chorus para mayor riqueza sonora.

---

## **⚡ Instalación y ejecución**
### **1️⃣ Requisitos**
- **Python 3.x**
- **SuperCollider**
- **Adafruit Circuit Playground Bluefruit**

### **2️⃣ Instalación**
```bash
# Clonar el repositorio
git clone https://github.com/usuario/generador-musica-biomateriales.git
cd generador-musica-biomateriales

# Instalar dependencias
pip install -r requirements.txt
```

### **3️⃣ Ejecución**
1. **Ejecutar SuperCollider y cargar `sound_generator.scd`**.
2. **Ejecutar el script de Python** para leer los sensores:
   ```bash
   python src/main.py
   ```
3. **Interactuar con los sensores para generar música en tiempo real**.

---

## **📌 Controles de sensores**
| Sensor        | Modificación |
|--------------|-------------|
| **Capacitancia** | Controla el tono de los cuencos tibetanos. |
| **Luz** | Modifica la reverberación y brillo armónico del piano. |
| **Temperatura** | Afecta la calidez del sintetizador atmosférico. |

---

## **📡 Comunicación OSC**
Los datos de sensores se envían desde **Python → SuperCollider** usando OSC:
- `/sensor1` → Controla los **cuencos tibetanos**.
- `/sensor2` → Modifica el **piano etéreo**.
- `/sensor3` → Controla el **synth atmosférico**.
- `/sensor_temp` → Ajusta la **calidez** del sonido.
- `/sensor_light` → Modifica la **reverberación**.

---

## **🎤 Grabación en tiempo real**
El sistema permite grabar la sesión musical y guardarla en **WAV**.

### **Comandos OSC**:
- `'/startRecording'` → Inicia la grabación.
- `'/stopRecording'` → Detiene y guarda el archivo.

---

## **💡 Créditos y agradecimientos**
Desarrollado por Rafael, basado en la idea original y esencia de **María José**

---

