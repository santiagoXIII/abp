import flet as ft
from flet_core.types import MainAxisAlignment

def main(page: ft.Page):
    #configuracion basica :)
    page.title= "Historia universal y STEM"
    page.bgcolor="#4cb7b9"
    page.window_width="800"
    page.window_height="800"
    
    ciencia=ft.Audio(src="ciencia.mp3",volume=1,balance=0)
    page.overlay.append(ciencia)
    inge=ft.Audio(src="inge.mp3",volume=1,balance=0)
    page.overlay.append(inge)
    mate=ft.Audio(src="mate.mp3",volume=1,balance=0)
    page.overlay.append(mate)
    tec=ft.Audio(src="tec.mp3",volume=1,balance=0)
    page.overlay.append(tec)
    
    def StopAll():
        ciencia.pause()
        inge.pause()
        mate.pause()
        tec.pause()
        
    def play_ciencia(e):
        StopAll()
        ciencia.play()
    
    def play_mate(e):
        StopAll()
        mate.play()
    
    def play_inge(e):
        StopAll()
        inge.play()
    
    def play_tec(e):
        StopAll()
        tec.play()
    
    volver=ft.ElevatedButton(text="volver",bgcolor="black", color="white",on_click=lambda _: page.go('/'))
    btn1= ft.ElevatedButton(text="ciencias",bgcolor="black", color="white", on_click=play_ciencia)
    btn2= ft.ElevatedButton(text="tecnologias",bgcolor="black", color="white", on_click=play_tec)
    btn3= ft.ElevatedButton(text="ingenierias",bgcolor="black", color="white", on_click=play_inge)
    btn4= ft.ElevatedButton(text="matematicas",bgcolor="black", color="white", on_click=play_mate)
    
    def route_change(route):
        # Limpia las vistas anteriores
        page.views.clear()
        # Vista de portada
        if page.route == '/':
            page.views.append(
                ft.View(
                    "/",
                    controls=[
                        ft.AppBar(
                            title=ft.Text("menu",size=15),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Row(
                                controls=[
                            ft.Column(
                                controls=[
                                        ft.Text("Las STEM",color="white", size=60,),
                                        ft.ElevatedButton(text="Saber mas sobre las stem",bgcolor="black", color="white",on_click=lambda _: page.go('/stem')),
                                        ft.ElevatedButton(text="Cuestionario sobre las STEM", bgcolor="black",color="white",on_click=lambda _: page.go('/cuestionario' )),
                                        ft.Image(src="stem.png")
                                    ],alignment=MainAxisAlignment.CENTER
                                )
                                ],alignment=MainAxisAlignment.CENTER
                            ),bgcolor=page.bgcolor,expand=True,
                        )
                    ]
                )
            )
        if page.route=='/stem':
            page.views.append(
                ft.View(
                    "/stem",
                    controls=[
                        ft.AppBar(
                            title=ft.Text("STEM",size=15),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ft.Text("STEM",size=30),
                                    ft.Text("STEM es el acrónimo en inglés que hace referencia a Science, Technology, Engineering and Mathematics (ciencia, tecnología, ingeniería y matemáticas), y que plantea la integración interdisciplinaria de estas áreas de las ciencias en un contexto asociado a la ingeniería y la tecnología.",max_lines=5),
                                    ft.Image(src="stem2.png"),
                                    ft.Row(
                                        controls=[
                                            btn1,btn2,btn3,btn4
                                        ]
                                    ),
                                    volver
                                ],alignment=MainAxisAlignment.CENTER
                            ),bgcolor=page.bgcolor,expand=True,
                        )
                    ]
                )
            )
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)
