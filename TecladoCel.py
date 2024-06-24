
import flet as ft
from flet import TextField, ElevatedButton, Text, Row, Column

def main(page: ft.Page):
    page.title = "Teclado Virtual"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window_height = 640
    page.window_width = 480
    page.window_resizable = True
    alto = 35
    ancho = 35
    
    txtInput = ft.TextField(width=300, text_align=ft.TextAlign.CENTER)
    
    def presionarTecla(evento):
        txtInput.value += evento.control.text
        page.update()
    
    def presionarEspacio(evento):
        txtInput.value += " "
        page.update()
    
    def presionarBorrar(evento):
        txtInput.value = txtInput.value[:-1]
        page.update()
    
    # Variables que contienen las teclas del teclado
    firstRow = "QWERTYUIOP"
    secondRow = "ASDFGHJKLÑ"
    thirdRow = "ZXCVBNM"
    fourthRow = ["\u02C0a", "\u02C0aa", "\u02C0e", "\u02C0ee", "\u02C0i", "\u02C0ii", "\u02C0u", "\u02C0uu", "\u02C0\u0268", "\u02C0\u0268\u0268"]
    
    # smallTxtStyle = ft.TextStyle(size = 10)
    allButtonStyles = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=7))
    
    btnSpace = ft.ElevatedButton(
        text = "_________________",
        on_click = presionarEspacio,
        width = 200,
        height = 35,
        style = allButtonStyles,
    )
    
    btnDelete = ft.IconButton(
        ft.icons.BACKSPACE,
        icon_size = 20,
        on_click = presionarBorrar,
        width = 50,
        height = alto,
        style = allButtonStyles,
    )
    
    teclas1 = [
        ft.ElevatedButton(
            content = ft.Text(tecla, text_align=ft.TextAlign.CENTER, size=12),
            on_click = presionarTecla, 
            width = ancho, 
            height = alto,
            style = allButtonStyles,
        ) 
        for tecla in firstRow
    ]
    
    teclas2 = [
        ft.ElevatedButton(
            content = ft.Text(tecla, text_align=ft.TextAlign.CENTER, size=12),
            on_click = presionarTecla, 
            width = ancho, 
            height = alto,
            style = allButtonStyles,
        ) 
        for tecla in secondRow
    ]
    
    teclas3 = [
        ft.ElevatedButton(
            content = ft.Text(tecla, text_align=ft.TextAlign.CENTER, size=12),
            on_click = presionarTecla, 
            width = ancho, 
            height = alto,
            style = allButtonStyles,
        ) 
        for tecla in thirdRow
    ]
    teclas3.append(btnDelete)
    
    teclas4 = [
        ft.ElevatedButton(
            content = ft.Text(tecla, text_align=ft.TextAlign.CENTER, size=12),
            on_click = presionarTecla, 
            width = ancho, 
            height = alto,
            style = allButtonStyles,
        ) 
        for tecla in fourthRow
    ]
    
    top = Row(controls=[txtInput], alignment=ft.MainAxisAlignment.CENTER)
    fila1 = Row(controls=teclas1, alignment=ft.MainAxisAlignment.CENTER)
    fila2 = Row(controls=teclas2, alignment=ft.MainAxisAlignment.CENTER)
    fila3 = Row(controls=teclas3, alignment=ft.MainAxisAlignment.CENTER)
    fila4 = Row(controls=teclas4, alignment=ft.MainAxisAlignment.CENTER)
    bottom = Row(controls=[btnSpace], alignment=ft.MainAxisAlignment.CENTER)
    
    page.add(top, fila1, fila2, fila3, fila4, bottom)

if __name__ == "__main__":
    ft.app(target=main)