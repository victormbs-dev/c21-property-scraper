# Century21 México Property Scraper 🏠

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

Web scraper para extracción automatizada de datos de propiedades en venta/renta de [Century21 México](https://century21mexico.com). Diseñado para alimentar sistemas de análisis inmobiliario con datos estructurados y actualizados.

## Características Principales

- Extracción robusta de 20+ campos por propiedad (incluyendo precios, amenidades, datos de contacto)
- Resistente a variaciones en la estructura de las páginas
- Exportación a CSV listo para análisis
- Manejo elegante de datos faltantes
- Documentación clara para mantenimiento

## Datos Extraídos

✅ **Campos obligatorios**  
📊 Campos opcionales

- ✅ Título del anuncio
- ✅ Precio del inmueble
- ✅ Tipo de inmueble (Casa, Departamento, Terreno, etc.)
- ✅ Tipo de Operación (Venta/Renta)
- ✅ Agente inmobiliario (nombre, teléfono, correo)
- ✅ Agencia (nombre, teléfono, correo)
- ✅ Enlace de la propiedad
- 📊 Metraje (terreno/construcción)
- 📊 Amenidades (piscina, jardín, etc.)
- 📊 Año de construcción
- ...y [15+ campos más](docs/DATA_FIELDS.md)

## Requisitos

- Python 3.8+
- Librerías (instalables via `requirements.txt`):
  - `requests`, `beautifulsoup4` (scraping)
  - `pandas` (manejo de datos)
  - `tqdm` (barra de progreso)

## Instalación

```bash
git clone https://github.com/tu-usuario/c21-property-scraper.git
cd c21-property-scraper
pip install -r requirements.txt
