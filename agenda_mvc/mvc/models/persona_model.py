from config.supabase_cliente import supabase

class PersonaModel:

    @staticmethod
    def obtener_todos():
        return supabase.table("personas").select("*").execute()

    @staticmethod
    def insertar(data):
        return supabase.table("personas").insert(data).execute()

    @staticmethod
    def obtener(id):
        return supabase.table("personas").select("*").eq("id_persona", id).single().execute()

    @staticmethod
    def actualizar(id, data):
        return supabase.table("personas").update(data).eq("id_persona", id).execute()

    @staticmethod
    def eliminar(id):
        return supabase.table("personas").delete().eq("id_persona", id).execute()
