import web

urls = (
    '/(.*)', 'mvc.controllers.visitas.Visitas'
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()