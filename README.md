# Examen Final: Agente de Análisis Conversacional con BigQuery y Cloud Run

## Descripción
Solución web para responder preguntas en lenguaje natural sobre datasets en BigQuery usando un Data Agent y una Cloud Run Function.

## Estructura del Proyecto
- fase-1-bigquery/: Configuración del agente en BigQuery.
- fase-2-backend/: Cloud Run Function (Python + Flask).
- fase-3-despliegue/: Scripts para despliegue y logs.
- fase-4-frontend/: Interfaz web (HTML + CSS + JS).
- entregables/: URL del endpoint e informe de evidencias.

## Despliegue
1. Habilitar APIs en GCP.
2. Crear el Data Agent en BigQuery Studio.
3. Desplegar la Cloud Run Function:
   ```bash
   gcloud functions deploy analista-arboles-sf --gen2 --runtime=python311 --region=us-central1 --source=. --entry-point=app --trigger-http --allow-unauthenticated