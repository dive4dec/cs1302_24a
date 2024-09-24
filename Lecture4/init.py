async def install_dependencies():
    try:
        import micropip
        await micropip.install('divewidgets')
        await micropip.install('ipywidgets')
    except ModuleNotFoundError:
        pass