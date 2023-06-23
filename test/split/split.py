from PIL import Image
from pathlib import Path
import numpy as np

img_p = Path(__file__).parent / "img_00231.jpeg"
img_in = Image.open(img_p)

arr = np.array(img_in)
arr_out = np.block([[[arr[:1024]], [arr[1024:2048]]], [[arr[2048:3072]], [arr[3072:]]]])
img_out = Image.fromarray(arr_out)
img_out.save(Path(__file__).parent / "img_00231_split.jpeg")
