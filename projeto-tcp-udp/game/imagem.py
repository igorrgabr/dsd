from PIL import Image
import gdown

img_urls = [
    "https://drive.google.com/uc?id=1kWDgbY32qg99uw5xyO5rrA7ndvZt7VT1",
    "https://drive.google.com/uc?id=1b31Uf0SedRErU5SXpy8SqMa-pkXa4g0X",
    "https://drive.google.com/uc?id=1YzZT2pWyrDdmcbVaktsP6a85l732SV6k",
    "https://drive.google.com/uc?id=1P6NIBT7pwCaRKxdxYh-vr1LZC4KHyMlY",
    "https://drive.google.com/uc?id=1VkUb9iIibvNNHjspC3TMSomf-NMbs6Wr"
]
img_dicas = [
    "j OGO DA c RIPTOGRAFIA",
    "DOIS ALFABETOS",
    "O NUMERO EH A CHAVE",
    "APENAS UM SE DESLOCA",
    "COM DESLOCAMENTO 3, A LETRA a VIRA LETRA d"
]
img_win_url = "https://drive.google.com/uc?id=1LRNv7wqYWwLCv3TTdsVJqxW3fcfU78jI"
img_lose_url = "https://drive.google.com/uc?id=1pjNmOQz-3zNXLSKjDh3j40ykC-339MWp"

def exec_imagem(count, wl):
    if wl == 1:
        gdown.download(img_win_url, "vincere.png", quiet=False)
        img = Image.open("vincere.png")
    elif wl == 2:
        gdown.download(img_lose_url, "victus.png", quiet=False)
        img = Image.open("victus.png")
    else:
        gdown.download(img_urls[count], f"imago{count}.png")
        img = Image.open(f"imago{count}.png")
    
    img.show()