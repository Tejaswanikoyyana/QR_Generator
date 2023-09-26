import qrcode
import gradio as gr
from PIL import Image
from io import BytesIO

def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")

    # Save the image to a BytesIO object
    img_buffer = BytesIO()
    img.save(img_buffer, format="PNG")
    img_pil = Image.open(img_buffer)
    return img_pil

iface = gr.Interface(
    fn=generate_qr_code,
    inputs=gr.inputs.Textbox(default="https://www.lendi.org/", label="URL"),
    outputs=gr.outputs.Image(type="pil"),
    title="QR Code Generator",
    description="Enter a URL to generate a QR code.",
)

iface.launch(inline=True)
