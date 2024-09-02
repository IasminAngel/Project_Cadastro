import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.window_maximized = True
    page.window_resizable = False
    
    login = ft.Column([
        ft.Container(
            bgcolor=ft.colors.GREEN_200,
            width=page.window_width - 10,
            height=page.window_height - 10,
            border_radius=10,
            
            content=ft.Column([
                
                ft.Container(
                    
                    bgcolor=ft.colors.WHITE70,
                    width=400,
                    height=320,
                    border_radius=10,
                    
                    content=ft.Column([
                        ft.Container(
                            padding = ft.padding.only(
                                top= 10,
                                bottom = 12
                            ),
                            
                        content = ft.Column([
                            ft.Text(
                                value='Sign-In',
                                weight='bold',
                                size=20,
                                color= '#A9A9A9'
                            )
                         ])
                    ),
                        
                        
                        ft.Column([
                            ft.TextField(
                                hint_text = 'Digite o seu e-mail',
                                color= '#A9A9A9',
                                width = 300,
                                height = 40,
                                border_radius= 40,
                                prefix_icon= ft.icons.PERSON,
                                text_vertical_align=1,
                                keyboard_type= ft.KeyboardType.EMAIL
                            ), 
                            ft.TextField(
                                hint_text = 'Digite a sua senha',
                                width = 300,
                                color= '#A9A9A9',
                                height = 40,
                                border_radius= 40,
                                prefix_icon= ft.icons.LOCK,
                                text_vertical_align=1,
                                password = True,
                                can_reveal_password=True,
                                keyboard_type= ft.KeyboardType.VISIBLE_PASSWORD
                            ), 
                            
                            
                            ft.ElevatedButton(
                                text= 'Sign-In',
                                bgcolor= ft.colors.GREEN_200,
                                color= '#FFFAFA',
                                on_hover= ft.colors.WHITE70,
                                width=300,
                                height=40
                            ),
                            
                            ft.Row([
                                ft.TextButton('Recuperar Conta'),
                                ft.TextButton('Criar nova conta')
                            ], width=300,alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                            
                        ], spacing=8)
                        
                    ], horizontal_alignment='center')
                )
            ], horizontal_alignment='center', alignment='center')
        )
    ])
    
    register = ft.Column([])
    
    page.add(login)

if __name__ == '__main__':
    ft.app(target=main)
