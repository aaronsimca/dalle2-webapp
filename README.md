# dalle2-webapp

## Prerequisite
- [Install Python & PIP](python.org)
- [OpenAI DALLE•2 API KEY](https://beta.openai.com/)



---

## Step-by-step Guide (Run Locally)
- Create a new folder ```dalle2-webapp ```
- Change directory ```cd dalle2-webapp ```
- Create a new file ```auth.py``` inside dalle2-webapp folder
- Create a new file ```app.py``` inside dalle2-webapp folder
- Create a new folder ```img``` inside dalle2-webapp folder


---
### Install Python Module
- Install Python OpenAI Module (using pip)
```bash
  pip install openai
```
- Install Python customtkinter Module (using pip)
```bash
  pip install customtkinter
```
- Incase any other modules are missing locally, use:
```bash
  pip install <MODULE_NAME> 
```


---
### auth.py file
- Open the ```auth.py``` file and add: 
```bash
  auth_token = "YOUR_AUTH_TOKEN"
```
Create, Copy & Replace the API Key from OpenAI website under 'User the Setting > View API Keys'. The 'auth.py' file would look like this: `auth_token = "sk-7yGeq3lkQoNXFw8yZvdjkb&DVJSJBD798yUBDNKNSdss"`


---
### app.py file
- Open the ```app.py``` file 

- ADD IMPORTS: 
```bash
from auth import auth_token
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import requests
```
jnn

- IMPORT OpenAI + CONNECT API: 
```bash
import openai
openai.api_key = auth_token
```

- CREATE APP CODE (Paste below all above code): 
```bash
app = tk.Tk()
app.geometry("532x632")
app.title("DALL•E 2 Text-to-Image App")
ctk.set_appearance_mode("dark")

main_image = tk.Canvas(app, width=512, height=512)
main_image.place(x=10, y=110)
``` 


- ADD PROMPT INPUT CODE
```bash
promt_input = ctk.CTkEntry(
    height=40,
    width=512,
    text_font=("Arial", 20),
    text_color="black",
    fg_color="white",
    placeholder_text="Enter a prompt ",
)
promt_input.place(x=10, y=10)
``` 

- ADD PROMPT API REQUEST FUNCTION
```bash
def apply_dalle():
    global tk_img
    global img

    prompt = promt_input.get()
    response = openai.Image.create(prompt=prompt, n=1, size="512x512")
    image_url = response["data"][0]["url"]
    img = Image.open(requests.get(image_url, stream=True).raw)
    tk_img = ImageTk.PhotoImage(img)
    main_image.create_image(0, 0, anchor=tk.NW, image=tk_img)
``` 

- ADD SAVE IMAGE FUNCTION 
```bash
def save_image():
    prompt = promt_input.get().replace(" ", "_")
    img.save(f"img/{prompt}.png")
``` 

- ADD IMAGES GENERATION BUTTON
```bash
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
``` 

- ADD SAVE IMAGE BUTTON
```bash
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
```

- RUN APP FUNCTION
```bash
app.mainloop()
```

---
### Run The App
- From the root directory of 'app.py', run in terminal" 
```bash
  python app.py
```
or
```bash
  python3 app.py
```
