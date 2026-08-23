from google.cloud import geminidataanalytics_v1alpha1 as gda

def crear_agente_bigquery(project_id, location, dataset_uri, display_name, system_instruction):
    client = gda.DataAnalyticsClient()
    agent = {
        "display_name": display_name,
        "description": f"Agente para analizar el dataset {dataset_uri}",
        "system_instruction": system_instruction,
        "data_source": {
            "bigquery_data_source": {
                "dataset_uri": dataset_uri
            }
        }
    }
    parent = f"projects/{project_id}/locations/{location}"
    response = client.create_agent(parent=parent, agent=agent)
    print(f"Agente creado: {response.name}")
    return response

if __name__ == "__main__":
    PROJECT_ID = "tu-proyecto-id"
    LOCATION = "us-central1"
    DATASET_URI = "projects/bigquery-public-data/datasets/san_francisco_trees/tables/tree_census"
    DISPLAY_NAME = "analista-arboles-sf"
    SYSTEM_INSTRUCTION = "Eres un analista de datos especializado en el dataset de árboles de San Francisco."
    crear_agente_bigquery(PROJECT_ID, LOCATION, DATASET_URI, DISPLAY_NAME, SYSTEM_INSTRUCTION)