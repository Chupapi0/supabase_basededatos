import web
from models.persona_model import PersonaModel

render = web.template.render("views/")

class InsertarController:
    def GET(self):
        return render.insertar({})

    def POST(self):
        form = web.input()
        response = PersonaModel.insertar({
            "nombre": form.get("nombre"),
            "email": form.get("email")
        })

        if hasattr(response, 'error') and response.error:
            return render.insertar({"error": response.error})

        return web.seeother("/")
