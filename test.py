from lg_hello_imgui import hello_imgui, imgui, implot


COUNT = 0


def my_gui():
    global COUNT
    if imgui.button("Click me"):
        COUNT += 1
    imgui.text(f"Hello, you clicked {COUNT} times")


hello_imgui.run(my_gui)
