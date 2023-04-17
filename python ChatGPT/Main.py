import openai 
import Config
import typer
from rich import print
from rich.table import Table

def main():

  openai.api_key = Config.Api_Key
  
  print("💬 [bold green]ChatGPT API en Python[/bold green]")

  table = Table("[blue]Comando[/blue]", "[yellow]Descripción[/yellow]")
  table.add_row("[red]exit[/red]", "Salir de la aplicación")
  table.add_row("[green]new[/green]", "Crear una nueva conversación")

  print(table)

# Contexto del asistente
  Contexto = {"role": "system",
               "content": "Eres un asistente muy profesional y útil."}
  Mensajes = [Contexto]


  while True:

   Contenido = __prompt()

# Respuesta del asistente
   if Contenido == "new":
            print("😉 Nueva conversación creada")
            Mensajes = [Contexto]
            Contenido = __prompt()
   
   Mensajes.append({"role": "user" , "content": Contenido})

   Respuesta = openai.ChatCompletion.create(model="gpt-3.5-turbo" ,  messages = [{"role": "user" , "content": Contenido}] )

   Respuesta_Contenido = Respuesta.choises[0].message.content

   Mensajes.append({"role": "assistant" , "content": Respuesta_Contenido})

   print(f"[bold green] Escribe aqui 👉🏼 [/bold green] [blue]{Respuesta_Contenido}[/blue]")

def __prompt() -> str:
    prompt = typer.prompt("\n¿Sobre qué quieres hablar? ")

    if prompt == "salir":
        exit = typer.confirm("✋ ¿Estás seguro?")
        if exit:
            print("👋 ¡Hasta luego!")
            raise typer.Abort()

        return __prompt()

    return prompt

if __name__ == "__main__":
    typer.run(main)