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
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)
