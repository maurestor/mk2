# mk2 – Simulación de Mercados Tradicionales de México

**Estado:** Activamente en desarrollo
**Autor:** [maurestor](https://github.com/maurestor)

## Descripción

mk2 es un juego educativo que simula la dinámica de los mercados tradicionales de México, usando Python y la librería PyGame. El objetivo es crear una experiencia interactiva donde los jugadores puedan explorar, interactuar y aprender sobre el funcionamiento y la cultura de estos mercados.

## Características principales

- Simulación de tiendas y movimiento dentro del mercado.
- Sistema de botones y diálogos (en desarrollo).
- Generación y renderizado de mapas con sprites personalizados.
- Elementos y objetos coleccionables dentro del juego.
- Gestión de inventario para el jugador y las tiendas.
- Sistema de diálogos dinámicos (parcialmente implementado).
- Interfaz de usuario para estadísticas y notificaciones.
- Efectos de partículas.
- Manejo de assets como sprites, fuentes y música.
- Uso de `items.json` para la configuración de ítems.

## Capturas de pantalla

*(Próximamente se agregarán capturas de pantalla del juego.)*

## Instalación

1. **Requisitos previos**
   - Python 3.7 o superior ([Descargar Python](https://www.python.org/downloads/))
   - PyGame 2.1.2 o superior
     ```bash
     pip install pygame
     ```
   - Se recomienda usar un entorno virtual de Python.
   - Para instalar todas las dependencias (si se proporciona un archivo `requirements.txt`):
     ```bash
     pip install -r requirements.txt
     ```

2. **Clonar el repositorio**
   ```bash
   git clone https://github.com/maurestor/mk2.git
   cd mk2
   ```

3. **Ejecutar el juego**
   ```bash
   python main.py
   ```

## Controles

- Flechas de dirección / Teclas W, A, S, D: Mover al personaje.
- TAB: Abrir/Cerrar menú de ítems del jugador.
- F4: Activar/Desactivar modo debug (mostrar rectángulos de colisión, información adicional).
- ESC: Salir del menú actual o del juego.
- Click del mouse: Interactuar con botones en los menús. En modo debug, puede permitir mover elementos.

## Estructura del repositorio

```
mk2/
├── main.py             # Archivo principal para ejecutar el juego
├── libs/               # Módulos principales del juego (jugador, tiendas, etc.)
├── assets/             # Recursos gráficos, sonidos, fuentes, etc.
├── items.json          # Configuración de ítems del juego
├── savegame.json       # Archivo de guardado (ejemplo)
├── README.md
└── ...otros archivos y carpetas
```

## Contribuir

¡Las contribuciones son bienvenidas! Si deseas colaborar con el desarrollo de mk2, puedes:

1.  Reportar bugs o sugerir mejoras abriendo un "Issue" en GitHub.
2.  Hacer fork del repositorio y enviar "Pull Requests" con tus cambios.
3.  Ayudar a mejorar la documentación.

Por favor, sigue las guías de estilo del código existente y comenta tus cambios adecuadamente.

## Tareas pendientes / Roadmap

- [ ] Mejorar la modularidad del código (ej. menús, manejo de estados del juego).
- [ ] Optimizar la carga y gestión de assets.
- [ ] Integrar completamente `items.json` en la lógica de la clase `Items`.
- [ ] Implementar sistema de guardado y carga de progreso del juego (parcialmente iniciado con `savegame.json`).
- [ ] Expandir el sistema de diálogos.
- [ ] Añadir más variedad de tiendas e interacciones.
- [ ] Balancear la economía del juego.
- [ ] Completar sistema de diálogos.
- [ ] Mejorar interfaz de usuario y experiencia visual.
- [ ] Agregar sonidos y música.
- [ ] Publicar capturas de pantalla y demo.
- [ ] Documentar más el código.
- [ ] Internacionalización (soporte para otros idiomas).
- [ ] Crear archivo LICENSE si no existe.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más información (si existe, de lo contrario, se añadirá).
