import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
import os
import shutil
import tkinter.font as tkFont
from PIL import Image, ImageTk

class ImageWatermarkApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Image Watermark Tool")
        width = 600
        height = 600
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) // 2,
            (screenheight - height) // 2,
        )
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class, **kwargs):
        new_frame = frame_class(self, **kwargs)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.place(x=0, y=0, relwidth=1, relheight=1)

class StartPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        title_font = tkFont.Font(family='Helvetica', size=30, weight='bold')
        font = tkFont.Font(family='Helvetica', size=15, weight='bold')
        
        button_frame = tk.Frame(self)
        button_frame.place(x=0,y=0,width=600,height=600)

        tk.Label(self, text="Image Watermark Tool", font=title_font).place(x=0, y=50, width=600, height=65)
        choose_button = tk.Button(button_frame,text="Choose Image",font=font,bg="#000000",fg="#ffffff",justify="center",command=lambda: master.switch_frame(TypePage))
        exit_button = tk.Button(button_frame,text="Exit",font=font,bg="#000000",fg="#ffffff",justify="center",command=master.destroy)
        choose_button.place(x=180,y=270,width=266,height=41)
        exit_button.place(x=280,y=350,width=80,height=39)

            

class TypePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        font = tkFont.Font(family='Helvetica', size=10, weight='bold')
        
        button_frame = tk.Frame(self)
        button_frame.place(x=0, y=0, width=600, height=600)

        test_w_button = tk.Button(button_frame,text="Text Watermark",font=font,bg="#000000",fg="#ffffff",justify="center")
        Logo_w_button = tk.Button(button_frame,text="Logo Watermark",font=font,bg="#000000",fg="#ffffff",justify="center",command=lambda: self.switch_to_logo_watermark(master))
        test_w_button.place(x=170, y=170, width=260, height=40)
        Logo_w_button.place(x=170, y=250, width=260, height=40)

    def switch_to_logo_watermark(self, master):
        fileToCopy = fd.askopenfilename(
            title="Select a Image to be Watermarked", filetypes=[("All files", "*.*")]
        )
        file_name = fileToCopy.split("/")[-1]
        directoryToPaste = f"./Backup_images/{file_name}"
        bg_image = f"./Backup_images/{file_name}"

        try:
            if not "Backup_images" in os.listdir():
                os.makedirs("Backup_images/")
            shutil.copy(fileToCopy, directoryToPaste)
            master.switch_frame(logoWatermark, bg_image=bg_image)
        except Exception as e:
            print(e)

class logoWatermark(tk.Frame):
    def __init__(self, master, bg_image):
        super().__init__(master)
        font = tkFont.Font(family='Helvetica', size=10, weight='bold')
        self.bg_image = bg_image
        self.fg_image = fd.askopenfilename(
            title="Select a watermark to be added", filetypes=[("All files", "*.*")]
        )

        screen_frame = tk.Frame(self)
        screen_frame.place(x=0,y=0,width=600,height=600)

        tk.Label(self, text="Enter Watermark size in %: ", font=font).grid(row=0, column=0)
        
        self.sbox = tk.Spinbox(self, from_=0, to=100, command=self.on_spinbox_change, width =3)
        self.sbox.grid(row=0, column=1)
        # See How it looks
        self.view_button = tk.Button(self,text="See How it looks",font=font,bg="#000000",fg="#ffffff",justify="center",command=self.on_spinbox_change)
        self.view_button.grid(row=0, column=2)
        # Open in app
        self.open_in_app = tk.Button(self,text="Open in app",font=font,bg="#000000",fg="#ffffff",justify="center",command=self.show_in_app)
        self.open_in_app.grid(row=0, column=3)
        # Exit
        self.exit_button = tk.Button(self,text="Exit",font=font,bg="#000000",fg="#ffffff",justify="center",command=master.destroy)
        self.exit_button.grid(row=0, column=4)
        # Save
        self.save_button = tk.Button(self,text="Save",font=font,bg="#000000",fg="#ffffff",justify="center",command=self.save_to_device)
        self.save_button.grid(row=0, column=4)
        # HomeHome
        self.save_button = tk.Button(self,text="Home",font=font,bg="#000000",fg="#ffffff",justify="center",command=lambda: master.switch_frame(StartPage))
        self.save_button.grid(row=0, column=5)
        self.panel = tk.Label(self)
        self.panel.grid(row=1, columnspan=6)
        self.fgimg = Image.open(self.fg_image).convert('RGBA')

        self.bgimg = Image.open(self.bg_image) 
        width, height = self.bgimg.size
        print("orig image size:",self.bgimg.size)
        self.fg_ratio = self.fgimg.size[0]/self.fgimg.size[1]
        
        
        
    def save_to_device(self):
        self.value = int(self.sbox.get())
        if self.value < 1:
            return None

        # Resize the foreground image based on the value from the spinbox
        new_height = int(self.bgimg.size[1] / 100 * self.value)
        new_width = int(self.fg_ratio * new_height)
        self.fgimg = self.fgimg.resize((new_width, new_height))

        # Create a copy of the background image to apply the watermark
        bg_img_to_save = self.bgimg.copy()

        # Calculate the position to paste the watermark
        paste_position = (bg_img_to_save.size[0] - self.fgimg.size[0], bg_img_to_save.size[1] - self.fgimg.size[1])

        # Paste the watermark onto the background image
        bg_img_to_save.paste(self.fgimg, paste_position, self.fgimg)

        # Save the watermarked image
        save_path = fd.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if save_path:
            bg_img_to_save.save("Backup_images/"+save_path.split('/')[-1])
            bg_img_to_save.save(self.bg_image)
            messagebox.showinfo("Save Successful", "Image saved successfully.")
    
    
    def show_in_app(self):
        self.value = int(self.sbox.get())
        if self.value < 1:
            return None
        width, height = self.bgimg.size
        new_height = int(height/100 * self.value)
        new_width = int(self.fg_ratio * new_height)
                    
        self.fgimg = self.fgimg.resize((new_width, new_height))

        self.bgimg.paste(self.fgimg, (width-self.fgimg.size[0], height-self.fgimg.size[1]), self.fgimg)
        self.bgimg.show()

    def on_spinbox_change(self):
        self.value = int(self.sbox.get())
        if self.value < 1:
            return None
        width, height = self.bgimg.size
        new_height = int(height/100 * self.value)
        new_width = int(self.fg_ratio * new_height)
                    
        self.fgimg = self.fgimg.resize((new_width, new_height))

        self.bgimg.paste(self.fgimg, (width-self.fgimg.size[0], height-self.fgimg.size[1]), self.fgimg)
        max_width = 580
        max_height = 580
        
        if width > height:
            new_width = max_width
            new_height = (height * max_width) // width
        else:
            new_height = max_height
            new_width = (width * max_height) // height
            
        self.bgimg = self.bgimg.resize((int(new_width),int(new_height)),resample=Image.NEAREST)
        
        print("resized image size:",self.bgimg.size)
        
        img = ImageTk.PhotoImage(self.bgimg)
        
        self.panel.grid_forget() 
        self.update_idletasks()
        self.panel = tk.Label(self)
        self.panel.grid(row=1, columnspan=5)
        
        
        self.panel.configure(image = img)
        self.panel.img = img
        

if __name__ == "__main__":
    app = ImageWatermarkApp()
    app.mainloop()