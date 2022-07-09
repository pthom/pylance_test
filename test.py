from lg_hello_imgui import hello_imgui, imgui, implot


class AppState:
    count = 0
    show_implot_demo: bool = False
    show_imgui_demo: bool = False


def my_gui(app_state: AppState):

    if imgui.button("Click me"):
        app_state.count += 1
    imgui.text(f"Hello, you clicked {app_state.count} times")

    _, app_state.show_imgui_demo = imgui.checkbox("ImGui demo", app_state.show_imgui_demo)
    _, app_state.show_implot_demo = imgui.checkbox("Implot demo", app_state.show_implot_demo)

    if app_state.show_imgui_demo:
        imgui.show_demo_window()
    if app_state.show_implot_demo:
        implot.show_demo_window()
    

if __name__ == "__main__":
    app_state = AppState()
    implot.create_context()
    hello_imgui.run(lambda: my_gui(app_state))
