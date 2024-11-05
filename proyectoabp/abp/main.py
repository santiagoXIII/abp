import flet as ft
from flet import AppBar, ElevatedButton, View
from flet_core.types import MainAxisAlignment



def main(page: ft.Page):
    #configuracion basica :)
    page.title= "Historia universal y STEM"
    page.bgcolor="blue"
    page.window_width="800"
    page.window_height="800"
    def route_change(route):
        # Limpia las vistas anteriores
        page.views.clear()
        
        # Vista de portada
        if page.route == '/':
            page.views.append(
                View(
                    "/",
                    controls=[
                        AppBar(
                            title=ft.Text("La historia de la Informática",size=15),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Row(
                                controls=[
                                    ft.Column(
                                            controls=[
                                                ft.ElevatedButton("¿Que es Steam?",on_click=lambda _: page.go('/STEAM')),
                                                ft.ElevatedButton("Las STEM en la Historia Uiversal",on_click=lambda _: page.go('/historia')),
                                                ft.ElevatedButton("ver participantes",on_click= lambda _: page.go("/participantes"))
                                            ],alignment=MainAxisAlignment.CENTER
                                    )
                                        ],alignment=MainAxisAlignment.CENTER
                                    ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ],
                    bgcolor=page.bgcolor
                )
            )
        #vista que es stem
        if page.route == "/STEAM":
            page.views.append(
                View(
                    "/STEAM",
                    controls=[
                        AppBar(
                            title=ft.Text("¿Que es STEM?",size=15),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Row(
                                controls=[
                                    ft.Column(
                                            controls=[
                                                ft.Text("¿Que es STEM?",size=30),
                                                ft.Text("STEM es el acrónimo en inglés que hace referencia a Science, Technology, Engineering and Mathematics (ciencia, tecnología, ingeniería y matemáticas), y que plantea la integración interdisciplinaria de estas áreas de las ciencias en un contexto asociado a la ingeniería y la tecnología. ", size=15, width=700,height=100,text_align="JUSTIFY"),
                                                ft.Row(controls=[
                                                    ft.ElevatedButton("ciencia"),
                                                    ft.ElevatedButton("tecnologia"),
                                                    ft.ElevatedButton("ingenieria"),
                                                    ft.ElevatedButton("matematicas")]),
                                                ft.ElevatedButton("volver al menu",on_click= lambda _: page.go("/"))
                                            ],alignment=MainAxisAlignment.CENTER
                                    )
                                        ],alignment=MainAxisAlignment.CENTER
                                    ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ],
                    bgcolor=page.bgcolor
                )
            )
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)
