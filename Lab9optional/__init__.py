"""Module for CS1302 notebooks."""
import warnings
from typing import List
import inspect
import ipywidgets as widgets

try:  # Optional imports
    import micropip
except ModuleNotFoundError:
    pass

# Default default dependencies
DEPENDENCIES: List[str] = """
divewidgets
ipywidgets
jupyter_ai
""".split()

async def install_dependencies(*args: str, default_deps: List[str] = DEPENDENCIES) -> None:
    """
    Install required dependencies (modules).

    Args:
        *args: Dependencies to install.
        default_deps: A list of default dependencies to install. 
            Defaults to `DEPENDENCIES`.
    """
    def formatwarning(msg: str, *_args, **_kwargs) -> str:
        """Custom format for warnings: only show the message."""
        return str(msg) + "\n"

    # Apply the custom format to warnings
    warnings.formatwarning = formatwarning

    try:
        warned = not micropip
        deps = default_deps + list(args)
        for package in deps:
            try:
                await micropip.install(package)
            except ValueError:
                warned = True
                warnings.warn(f"{package} is not supported.")
        if warned:
            warnings.warn("Some code is expected to fail but it is okay.")
    except NameError:
        pass

def show(object):
    def getvalue(object):
        return str(object)
    def gettype(object):
        return str(type(object))
    def getattributes(object):
        return "\n".join(dir(object))
    topics = [gettype, getattributes, getvalue, inspect.getdoc, inspect.getsource, inspect.getabsfile]
    children = []
    titles = []
    for topic in topics:
        try:
            content = topic(object)
            if len(content) > 0:
                if len(content) >= 80:
                    area = widgets.Textarea(content, layout=widgets.Layout(width="100%", height="20em"))
                else:
                    area = widgets.Text(content, layout=widgets.Layout(width="100%"))
                children.append(area)
                titles.append(topic.__name__)
        except TypeError:
            pass
    pane = widgets.Tab(children)
    for i,title in enumerate(titles):
        pane.set_title(i, title)
    display(pane)