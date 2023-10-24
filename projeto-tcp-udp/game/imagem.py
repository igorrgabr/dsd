from PIL import Image
import gdown

def exec_imagem(url, nome):
    gdown.download(url, nome, quiet=False)
    img = Image.open(nome)
    img.show()
