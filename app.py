# IMPORTS
from auth import auth_token
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import requests

# pip install openai + api connect
import openai
openai.api_key = auth_token


# Create app
app = tk.Tk()
app.geometry("532x632")
app.title("DALL•E 2 Text-to-Image App")
ctk.set_appearance_mode("dark")

main_image = tk.Canvas(app, width=512, height=512)
main_image.place(x=10, y=110)

# INPUT
# DALL•E 2 Prompt Input
promt_input = ctk.CTkEntry(
    height=40,
    width=512,
    text_font=("Arial", 20),
    text_color="black",
    fg_color="white",
    placeholder_text="Enter a prompt ",
)
promt_input.place(x=10, y=10)


# FUNCTION
# Function that takes the prompt and makes API request
def apply_dalle():
    global tk_img
    global img

    prompt = promt_input.get()
    response = openai.Image.create(prompt=prompt, n=1, size="512x512")
    image_url = response["data"][0]["url"]
    img = Image.open(requests.get(image_url, stream=True).raw)
    tk_img = ImageTk.PhotoImage(img)
    main_image.create_image(0, 0, anchor=tk.NW, image=tk_img)

# Function to save the image


def save_image():
    prompt = promt_input.get().replace(" ", "_")
    img.save(f"img/{prompt}.png")


# BUTTONS
# Button that triggers the above function
dalle_button = ctk.CTkButton(
    height=40,
    width=120,
    text_font=("Arial", 20),
    text_color="white",
    fg_color=("white", "gray38"),
    command=apply_dalle,
)
dalle_button.configure(text="Apply DALL•E 2")
dalle_button.place(x=100, y=60)

# Button to save the image
save_button = ctk.CTkButton(
    height=40,
    width=120,
    text_font=("Arial", 20),
    text_color="white",
    fg_color=("white", "gray38"),
    command=save_image,
)
save_button.configure(text="Save image")
save_button.place(x=266, y=60)


# Running the App
app.mainloop()


# PROMPT EXAMPLE
# Machine learning in a classroom
# World on fire
