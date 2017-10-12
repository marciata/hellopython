import pyperclip

# joga o conteudo no clippboard do computador (igual ctrl+c)
pyperclip.copy('Hello world')

# cola o conteudo do clippboard do computador (igual ctrl+v)
print(pyperclip.paste())