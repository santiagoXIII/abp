import flet as ft
from flet import AppBar, ElevatedButton, View
from flet_core.types import MainAxisAlignment

def main(page: ft.Page):
    #configuracion basica :)
    page.title= "Historia universal y STEM"
    page.bgcolor="#268057"
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
                                                ft.Text("Proyecto ABP",size=40,color="#05411c"),
                                                ft.ElevatedButton("¿Que es Steam?",bgcolor="#05411c", color="#0cf596",on_click=lambda _: page.go('/STEAM')),
                                                ft.ElevatedButton("Las STEM en la Historia Uiversal",bgcolor="#05411c",color="#0cf596",on_click=lambda _: page.go('/historia')),
                                                ft.ElevatedButton("ver participantes",bgcolor="#05411c",color="#0cf596",on_click= lambda _: page.go("/participantes"))
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
        #vista de que es stem
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
                                                ft.Text("¿Que es STEM?",size=30,color="#05411c"),
                                                ft.Text("STEM es el acrónimo en inglés que hace referencia a Science, Technology, Engineering and Mathematics (ciencia, tecnología, ingeniería y matemáticas), y que plantea la integración interdisciplinaria de estas áreas de las ciencias en un contexto asociado a la ingeniería y la tecnología. ", size=15,color="#05411c", width=500,height=120,text_align="JUSTIFY"),
                                                ft.Row(controls=[
                                                    ft.ElevatedButton("ciencia",bgcolor="#05411c", color="#0cf596",),
                                                    ft.ElevatedButton("tecnologia",bgcolor="#05411c", color="#0cf596",),
                                                    ft.ElevatedButton("ingenieria",bgcolor="#05411c", color="#0cf596",),
                                                    ft.ElevatedButton("matematicas",bgcolor="#05411c", color="#0cf596",)]),
                                                ft.ElevatedButton("volver al menu",bgcolor="#05411c", color="#0cf596",on_click= lambda _: page.go("/"))
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
        # vista de historia 
        if page.route== "/historia":
            page.views.append(
                View(
                    "/historia",
                    controls=[
                        AppBar(
                            title=ft.Text("Las STEM en la historia universal",size=15),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Row(
                                controls=[
                                    ft.Column(
                                        controls=[
                                            ft.Text("STEM en la historia universal",color="#05411c",size=30),
                                            ft.ElevatedButton("Las Mujeres en STEM",bgcolor="#05411c", color="#0cf596",on_click= lambda _: page.go("/mujeres")),
                                            ft.ElevatedButton("Movimiento STEM en latinoamerica",bgcolor="#05411c", color="#0cf596",on_click=lambda _: page.go("/Latam")),
                                            ft.ElevatedButton("volver al menu",bgcolor="#05411c", color="#0cf596",on_click= lambda _: page.go("/"))
                                        ],alignment=MainAxisAlignment.CENTER
                                    )
                                ],alignment=MainAxisAlignment.CENTER
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        #vista de participantes
        if page.route=="/participantes":
            page.views.append(
                View(
                    "/participantes",
                    controls=[
                        AppBar(
                            title=ft.Text("participantes del proyecto"),
                            bgcolor="gray",
                        ),
                        ft.Container(
                            ft.Row(
                                controls=[
                                    ft.Column(
                                        controls=[
                                            ft.Text("Participantes del proyecto:",color="#05411c",size=30),
                                            ft.Text(">Beltran Gonzalez Bruno Javier",color="#05411c"),
                                            ft.Text(">Cruz Mote Romina ",color="#05411c"),
                                            ft.Text(">Vazquez Basilio Angel Santiago",color="#05411c"),
                                            ft.Text(">Yepez Roman Cesar Manuel",color="#05411c"),
                                            ft.ElevatedButton("volver al menu",bgcolor="#05411c", color="#0cf596",on_click= lambda _: page.go("/"))
                                        ],alignment=MainAxisAlignment.CENTER
                                    ),
                                ],alignment=MainAxisAlignment.CENTER
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        #vista mujeres
        if page.route=="/mujeres":
            page.views.append(
                View(
                    "/mujeres",
                    controls=[
                        AppBar(
                            title=ft.Text("Las Mujeres en STEM",size=15),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Row(
                                controls=[
                                    ft.Column(
                                        controls=[
                                            ft.Text("Las Mujeres en STEM",color="#05411c",size=30),
                                            ft.Text("Se acerca una transformación laboral que requerirá profesionistas con habilidades vinculadas con la ciencia, la tecnología, la ingeniería y las matemáticas (STEM, por sus siglas en inglés). De acuerdo con el Foro Económico Mundial, para 2025 surgirán 97 millones de nuevos empleos adaptados a la nueva relación entre máquinas y personas. Sin embargo, en México las mujeres se han quedado atrás en la formación de estas habilidades para el futuro. En 2022, el Instituto Mexicano para la Competitividad (IMCO) encontró que solo tres de cada 10 profesionistas en STEM son mujeres.",size=15,color="#05411c",width=500,height=200,text_align="JUSTIFY"),
                                            ft.Image(src="mujer.png"),
                                            ft.ElevatedButton("volver",bgcolor="#05411c", color="#0cf596",on_click= lambda _: page.go("/historia")),
                                        ],alignment=MainAxisAlignment.CENTER
                                    )
                                ],alignment=MainAxisAlignment.CENTER
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        ),
                        
                    ]
                )
            )
        #vista de latam
        if page.route=="/Latam":
            page.views.append(
                View(
                    "/Latam",
                    controls=[
                        AppBar(
                            title=ft.Text("Movimiento STEM en latam"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Row(
                                controls=[
                                    ft.Column(
                                        controls=[
                                            ft.Text("Movimiento STEM en latinoamerica",size=30,color="#05411c",),
                                            ft.ElevatedButton("volver",bgcolor="#05411c", color="#0cf596",on_click= lambda _: page.go("/historia"))
                                        ],alignment=MainAxisAlignment.CENTER
                                    )
                                ],alignment=MainAxisAlignment.CENTER
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)
