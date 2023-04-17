import openai
import Config
import typer
from rich import print
from rich.table import Table

openai.api_key = Config.Api_Key

# Contexto del asistente
Contexto = {"role": "system", "content": "Eres un asistente muy profesional y útil."}
Mensajes = [Contexto]

print("💬 [bold green]ChatGPT API en Python[/bold green]")

table = Table("[blue]Comando[/blue]", "[yellow]Descripción[/yellow]")
table.add_row("[red]salir[/red]", "Salir de la aplicación")
table.add_row("[green]new[/green]", "Crear una nueva conversación")
print(table)

while True:
    Contenido = typer.prompt("\n¿Sobre qué quieres hablar? ")

    if Contenido.lower() == "salir":
        print("👋 ¡Hasta luego!")
        break

    elif Contenido.lower() == "new":
        print("😉 Nueva conversación creada")
        Mensajes = [Contexto]

    else:
        Mensajes.append({"role": "user", "content": Contenido})
        Respuesta = openai.Completion.create(
            engine="text-davinci-002",
            prompt=Contenido,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        Respuesta_Contenido = Respuesta.choices[0].text.strip()
        Mensajes.append({"role": "assistant", "content": Respuesta_Contenido})
        print(f"[bold green] Asistente 👉🏼 [/bold green] [blue]{Respuesta_Contenido}[/blue]")

