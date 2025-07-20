import os

def generate_invitations(template, attendees):
    # Verificar tipos de entrada
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # Verificar entradas vacías
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Procesar cada asistente
    for idx, person in enumerate(attendees, start=1):
        # Copiar plantilla original
        output = template
        # Reemplazar cada marcador
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = person.get(key)
            if not value:
                value = "N/A"
            output = output.replace(f"{{{key}}}", str(value))

        # Guardar en archivo
        filename = f"output_{idx}.txt"
        with open(filename, "w") as f:
            f.write(output)
