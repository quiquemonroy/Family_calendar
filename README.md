# Calendario Familiar para Pantalla eInk

## Descripción

Este proyecto es un calendario familiar diseñado para mostrarse en una pantalla eInk, utilizando una Raspberry Pi como servidor local. El sistema muestra:

- Un calendario semanal con eventos destacados
- Información meteorológica actualizada
- Eventos familiares importados desde un calendario iCal
- Un diseño visual simple y legible, optimizado para pantallas eInk

## Características principales

- **Visualización de calendario**: Muestra dos semanas completas (actual y siguiente)
- **Eventos familiares**: Importa eventos desde un calendario iCal externo
- **Información meteorológica**: Muestra temperatura, condiciones climáticas y horas de salida/puesta del sol
- **Diseño responsive**: Adaptado para pantallas eInk
- **Toques personales**: Incluye emojis diarios y una imagen aleatoria de animal

## Requisitos del sistema

- Raspberry Pi (cualquier modelo reciente)
- Pantalla eInk compatible
- Python 3.x
- Conexión a Internet para:
  - Obtener datos meteorológicos
  - Sincronizar el calendario iCal

## Dependencias

Las principales dependencias de Python son:

- Flask
- requests
- ics (para manejar calendarios iCal)
- python-dotenv (para variables de entorno)

Instalar con:
```bash
pip install flask requests ics python-dotenv
```

## Configuración

1. Crear un archivo `LOCAL.py` con las siguientes variables:
   ```python
   CALENDAR_URL = "URL_DEL_CALENDARIO_ICAL"
   API_KEY = "TU_API_KEY_DE_OPENWEATHERMAP"
   lat = TU_LATITUD
   lon = TU_LONGITUD
   ```

2. Para el calendario iCal, puedes usar:
   - Google Calendar (exportar como iCal)
   - Cualquier otro servicio que ofrezca exportación iCal

3. Para la API meteorológica:
   - Registrarse en [OpenWeatherMap](https://openweathermap.org/) para obtener una API key

## Estructura de archivos

- `main.py`: Aplicación Flask principal
- `calendario.py`: Lógica para generar las semanas del calendario
- `ical.py`: Manejo de eventos desde el calendario iCal
- `weather.py`: Obtención de datos meteorológicos
- `templates/`: Plantillas HTML
  - `base.html`: Plantilla base
  - `calendar.html`: Vista principal del calendario
  - `footer.html`: Pie de página

## Ejecución

Para iniciar el servidor:

```bash
python main.py
```

El servidor estará disponible en `http://localhost:8000`

## Configuración para arranque automático (Opcional)

Para que la aplicación se inicie automáticamente al arrancar la Raspberry Pi:

1. Crear un servicio systemd:
   ```bash
   sudo nano /etc/systemd/system/calendario.service
   ```

2. Añadir este contenido (ajustar rutas según sea necesario):
   ```ini
   [Unit]
   Description=Calendario Familiar Service
   After=network.target

   [Service]
   ExecStart=/usr/bin/python3 /ruta/al/proyecto/main.py
   WorkingDirectory=/ruta/al/proyecto/
   StandardOutput=inherit
   StandardError=inherit
   Restart=always
   User=pi

   [Install]
   WantedBy=multi-user.target
   ```

3. Habilitar e iniciar el servicio:
   ```bash
   sudo systemctl enable calendario.service
   sudo systemctl start calendario.service
   ```

## Personalización

- **Emojis diarios**: Modificar la lista `WEEK` en `main.py`
- **Imágenes de animales**: Añadir imágenes PNG numeradas (1-31) en `static/img/`
- **Estilos CSS**: Editar las plantillas HTML o añadir un archivo CSS personalizado

