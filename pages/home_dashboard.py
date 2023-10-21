import flet as ft


def home_dashboard(pg: ft.Page):
    pg.theme_mode = 'light'
    pg.bgcolor = ft.colors.WHITE
    pg.window_width = 380
    pg.window_height = 700
    pg.appbar = ft.AppBar(
        toolbar_height=80,
        leading=ft.Text(""),
        leading_width=100,
        title=ft.Text(""),
        elevation=0,
        bgcolor=ft.colors.WHITE,
        color=ft.colors.BLACK,
        actions=[
            ft.IconButton(ft.icons.SEARCH),
            ft.IconButton(ft.icons.PERSON_OUTLINED),
            ft.IconButton(ft.icons.MORE_VERT_OUTLINED)
        ]
    )
    pg.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME_OUTLINED),
            ft.NavigationDestination(icon=ft.icons.ADD),
            ft.NavigationDestination(icon=ft.icons.PEOPLE_OUTLINE)
        ],
        bgcolor=ft.colors.WHITE,
    )

    community = ft.Column(
        controls=[
            ft.Text(value="See the Communities near you", size=20),
            ft.Row(
                controls=[

                    ft.Container(
                        ft.Image(src=f"images/community.png"),
                        height=100
                    )
                ],
            )
        ]
    )

    column = ft.Column(
        controls=[
            community
        ],
        scroll=ft.ScrollMode.HIDDEN

    )
    pg.add(column)
    pg.update()


ft.app(target=home_dashboard, assets_dir="../assets")
