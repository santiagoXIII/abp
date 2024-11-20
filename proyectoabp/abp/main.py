import flet as ft
from flet_core.types import MainAxisAlignment

def main(page: ft.Page):
    #configuracion basica :)
    page.title= "Historia universal y STEM"
    page.bgcolor="#4cb7b9"
    page.window_width="900"
    page.window_height="800"
    
    ciencia=ft.Audio(src="ciencia.mp3",volume=1,balance=0)
    page.overlay.append(ciencia)
    inge=ft.Audio(src="inge.mp3",volume=1,balance=0)
    page.overlay.append(inge)
    mate=ft.Audio(src="mate.mp3",volume=1,balance=0)
    page.overlay.append(mate)
    tec=ft.Audio(src="tec.mp3",volume=1,balance=0)
    page.overlay.append(tec)
    brecha=ft.Audio(src="brechat.mp3",volume=1,balance=0)
    page.overlay.append(brecha)
    fomento=ft.Audio(src="fomento.mp3",volume=1,balance=0)
    page.overlay.append(fomento)
    historia=ft.Audio(src="historia.mp3",volume=1,balance=0)
    page.overlay.append(historia)
    
    def StopAll():
        ciencia.pause()
        inge.pause()
        mate.pause()
        tec.pause()
        brecha.pause()
        fomento.pause()
        historia.pause()
        
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
    
    def play_brecha(e):
        StopAll()
        brecha.play()
    
    def play_historia(e):
        StopAll()
        historia.play()
    
    def play_fomento(e):
        StopAll()
        fomento.play()
    
    volver=ft.ElevatedButton(text="volver",bgcolor="black", color="white",on_click=lambda _: page.go('/menu'))
    btn1= ft.ElevatedButton(text="ciencias",bgcolor="black", color="white", on_click=play_ciencia)
    btn2= ft.ElevatedButton(text="tecnologias",bgcolor="black", color="white", on_click=play_tec)
    btn3= ft.ElevatedButton(text="ingenierias",bgcolor="black", color="white", on_click=play_inge)
    btn4= ft.ElevatedButton(text="matematicas",bgcolor="black", color="white", on_click=play_mate)
    btn5= ft.ElevatedButton(text="las mujeres en las stem",bgcolor="black",color="white",on_click=play_historia)
    btn6=ft.ElevatedButton(text="la brecha laboral",bgcolor="black",color="white",on_click=play_brecha)
    btn7=ft.ElevatedButton(text="fomento de la participacion de mujeres en las STEM",bgcolor="black",color="white",on_click=play_fomento)
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
                                        ft.ElevatedButton(text="Saber mas sobre las stem",bgcolor="black", color="white",on_click=lambda _: page.go('/menu')),
                                        ft.Image(src="stem.png")
                                    ],alignment=MainAxisAlignment.CENTER
                                )
                                ],alignment=MainAxisAlignment.CENTER
                            ),bgcolor=page.bgcolor,expand=True,
                        )
                    ]
                )
            )
        if page.route=='/menu':
            page.views.append(
                ft.View(
                    "/menu",
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
                                    ft.Text("Menú",size=50, color="white"),
                                    ft.ElevatedButton("¿Qué son las stem?",bgcolor='black', color='white',on_click=lambda _: page.go('/stem')),
                                    ft.ElevatedButton("La Revolución Científica (siglos XVI-XVII)",bgcolor='black', color='white',on_click=lambda _: page.go('/RC')),
                                    ft.ElevatedButton("La Revolución Industrial (siglos XVIII-XIX)",bgcolor='black', color='white',on_click=lambda _: page.go('/RI')),
                                    ft.ElevatedButton("La Guerra Fría y la Carrera Espacial (1947-1991)",bgcolor='black', color='white',on_click=lambda _: page.go('/GF')),
                                    ft.ElevatedButton("La Revolución Digital (década de 1970 - presente)",bgcolor='black', color='white',on_click=lambda _: page.go('/RD')),
                                    ft.ElevatedButton("La Teoría de la Evolución y la Biología Moderna",bgcolor='black', color='white',on_click=lambda _: page.go('/TE')),
                                    ft.ElevatedButton("Mujeres en las STEM",bgcolor="black",color="white",on_click=lambda _: page.go("/mujeres")),
                                    ft.ElevatedButton(text="volver",bgcolor="black", color="white",on_click=lambda _: page.go('/'))
                                    
                                ]
                            )
                                ],alignment="CENTER"
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
                                    ft.Text("¿Qué es STEM?",size=30,color="white"),
                                    ft.Text("STEM es el acrónimo en inglés que hace referencia a Science, Technology, Engineering and Mathematics (ciencia, tecnología, ingeniería y matemáticas), y que plantea la integración interdisciplinaria de estas áreas de las ciencias en un contexto asociado a la ingeniería y la tecnología.",max_lines=5),
                                    ft.Image(src="stem2.png",height=300,width=300),
                                    ft.Row(
                                        controls=[
                                            btn1,btn2,btn3,btn4
                                        ]
                                    ),
                                    volver
                                ],alignment="CENTER"
                            ),bgcolor=page.bgcolor,expand=True,
                        )
                    ]
                )
            )
        if page.route=='/RC':
            page.views.append(
                ft.View(
                    "/RC",
                    controls=[
                        ft.AppBar(
                            title=ft.Text("RC",size=15),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ft.Text("La Revolución Científica (siglos XVI-XVII)",size=30),
                                    ft.Text("La Revolución Científica fue un período crucial en la historia de la ciencia, que se extendió desde finales del Renacimiento hasta principios de la Edad Moderna. Durante este tiempo, las bases de la ciencia moderna fueron establecidas, gracias a figuras como Copérnico, Galileo y Newton. La concepción heliocéntrica del universo, la observación astronómica con telescopios y las leyes del movimiento de Newton transformaron radicalmente la forma en que los seres humanos entendían el cosmos y el funcionamiento de la naturaleza. Este movimiento sentó las bases para muchas disciplinas de STEM que dominarían el pensamiento científico y la tecnología en siglos posteriores.",max_lines=5),
                                    ft.Image(src="rc.jpg",height=300,width=300),
                                    volver
                                ],alignment="CENTER"
                            ),bgcolor=page.bgcolor,expand=True,
                        )
                    ]
                )
            )
        if page.route=='/RI':
            page.views.append(
                ft.View(
                    "/RI",
                    controls=[
                        ft.AppBar(
                            title=ft.Text("RI",size=15),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ft.Text("La Revolución Industrial (siglos XVIII-XIX)",size=30),
                                    ft.Text("La Revolución Industrial marcó un cambio fundamental en la historia humana, especialmente en la tecnología y la ingeniería. Comenzó en Gran Bretaña en el siglo XVIII y se expandió por Europa y América. Fue impulsada por avances en la tecnología, como la máquina de vapor de James Watt, la mejora en los procesos de fabricación, y la introducción de maquinaria industrial. Las nuevas invenciones transformaron la producción de bienes, la minería y el transporte, además de contribuir al urbanismo y cambios en las estructuras sociales y económicas. Este fenómeno también aceleró el desarrollo de la ingeniería y la innovación tecnológica en sectores como el textil, el transporte ferroviario y la manufactura.",max_lines=5),
                                    ft.Image(src="ri.jpeg",height=300,width=300),
                                    volver
                                ],alignment="CENTER"
                            ),bgcolor=page.bgcolor,expand=True,
                        )
                    ]
                )
            )
        if page.route=='/GF':
            page.views.append(
                ft.View(
                    "/GF",
                    controls=[
                        ft.AppBar(
                            title=ft.Text("GF",size=15),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ft.Text("La Guerra Fría y la Carrera Espacial (1947-1991)",size=30),
                                    ft.Text("La Guerra Fría, la competencia entre los Estados Unidos y la Unión Soviética después de la Segunda Guerra Mundial, tuvo una gran influencia en el desarrollo de la tecnología, particularmente en el campo espacial. La Carrera Espacial llevó a avances significativos en la ciencia y la ingeniería, con la exploración del espacio como una de sus mayores conquistas. En 1957, la URSS lanzó el Sputnik, el primer satélite artificial, lo que desató una serie de avances tecnológicos en satélites, computadoras y comunicaciones. En 1969, el Apollo 11 de los Estados Unidos llevó al primer ser humano a la luna. La Guerra Fría impulsó la investigación en física, matemáticas y tecnología de cohetes, que continúa influyendo en las ciencias y la ingeniería hoy en día.",max_lines=8),
                                    ft.Image(src="gf.png",width=300,height=300),
                                    volver
                                ],alignment="CENTER"
                            ),bgcolor=page.bgcolor,expand=True,
                        )
                    ]
                )
            )
        if page.route=='/RD':
            page.views.append(
                ft.View(
                    "/RD",
                    controls=[
                        ft.AppBar(
                            title=ft.Text("RD",size=15),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ft.Text("La Revolución Digital (década de 1970 - presente)",size=30,color="white"),
                                    ft.Text("La Revolución Digital, que comenzó en la segunda mitad del siglo XX, está relacionada con la invención de los computadores personales, la red de internet y los avances en microelectrónica. Figuras como Steve Jobs, Bill Gates, y Tim Berners-Lee jugaron roles claves en este cambio, que transformó radicalmente todos los aspectos de la vida humana, desde la comunicación hasta la educación y el trabajo. Las tecnologías digitales impulsaron áreas como la programación, la inteligencia artificial, las ciencias de la información y la ingeniería informática, y continúan cambiando rápidamente las economías y las sociedades globales.",max_lines=5),
                                    ft.Image(src="rd.jpg",height=300,width=300),
                                    volver
                                ],alignment="CENTER"
                            ),bgcolor=page.bgcolor,expand=True,
                        )
                    ]
                )
            )
        if page.route=='/TE':
            page.views.append(
                ft.View(
                    "/TE",
                    controls=[
                        ft.AppBar(
                            title=ft.Text("TE",size=15),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ft.Text("La Teoría de la Evolución y la Biología Moderna",size=30),
                                    ft.Text("En el campo de las ciencias biológicas, la teoría de la evolución propuesta por Charles Darwin en el siglo XIX revolucionó la comprensión de la vida en la Tierra. Según Darwin, las especies evolucionan a lo largo del tiempo mediante un proceso de selección natural. Esta teoría, junto con el desarrollo de la genética y la biología molecular en el siglo XX, transformó nuestra comprensión de la biología, la herencia y la diversidad de las especies. Este avance se consolidó con el descubrimiento de la estructura del ADN por Watson y Crick en 1953, lo que permitió el avance en áreas como la medicina, la biotecnología y la ingeniería genética.Estos cinco temas reflejan cómo los avances en las STEM han influido profundamente en la historia universal y en la manera en que entendemos el mundo, desde la ciencia y la tecnología hasta la política y la sociedad.",max_lines=8),
                                    ft.Image(src="te.png",height=300,width=300),
                                    volver
                                ],alignment="CENTER"
                            ),bgcolor=page.bgcolor,expand=True,
                        )
                    ]
                )
            )
        if page.route=='/mujeres':
            page.views.append(
                ft.View(
                    "/mujeres",
                    controls=[
                        ft.AppBar(
                            title=ft.Text("Mujeres",size=15),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Row(
                                controls=[
                                    ft.Column(
                                        controls=[
                                            ft.Text("Mujeres en las STEM",size=50,color="white"),
                                            ft.Text("Las mujeres en las STEM (Ciencias, Tecnología, Ingeniería y Matemáticas, por sus siglas en inglés) han desempeñado un papel crucial en el avance del conocimiento y la tecnología a lo largo de la historia, aunque su presencia ha sido históricamente menor que la de los hombres en estos campos. Sin embargo, en las últimas décadas, ha habido un creciente interés en fomentar la participación femenina en las STEM, con el objetivo de reducir la brecha de género y aprovechar el potencial de las mujeres en estas áreas.",height=125,width=700,color="white"),
                                            ft.Image(src="mujeres.jpg",width=250,height=250),
                                            ft.Row(
                                                controls=[
                                                    btn5,btn6,btn7
                                                ]
                                            ),
                                            volver                                        
                                            ]
                                    )
                                ],alignment="CENTER"
                            ),bgcolor=page.bgcolor,expand=True,
                        )
                    ]
                )
            )
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)
