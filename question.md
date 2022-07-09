I'm having issues with Visual Studio Code python language server, which cannot find the stubs for a library I am developing.

I made a minimum reproductible example here: https://github.com/pthom/pylance_test

When using PyCharm or CLion, I can easily navigate to the stubs I defined for my library.

However, when using Visual Studio Code, it is less reliable.

Based on what I saw, I cannot 

````
.venv/lib/python3.9/site-packages/lg_hello_imgui/
├── __init__.py
├── _lg_hello_imgui.cpython-39-darwin.so*
├── hello_imgui.pyi
├── imgui.pyi
├── implot.pyi
└── py.typed
````


init.py

````python
from lg_hello_imgui._lg_hello_imgui import imgui
from lg_hello_imgui._lg_hello_imgui import hello_imgui
from lg_hello_imgui._lg_hello_imgui import implot
````

pybind11 c++ definition:
````cpp
PYBIND11_MODULE(_lg_hello_imgui, m)
{
    auto module_imgui =  m.def_submodule("imgui");
    py_init_module_imgui(module_imgui);

    auto module_himgui =  m.def_submodule("hello_imgui");
    py_init_module_hello_imgui(module_himgui);

    auto module_implot =  m.def_submodule("implot");
    py_init_module_implot(module_implot);
}
````