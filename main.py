from tkinter import *
from tkinter import messagebox
from zillow_website_scrapping import ZILLOW_DATA

def start_extracting_data():
    url = url_entry.get()
    extract = False
    zillow = ZILLOW_DATA(url)
    while True:
        soup = zillow.validate_url()
        if soup:
            extract = True
            zillow.extract_data(soup)
            zillow.update_url()
        else:
            if not extract:
                messagebox.showerror(title="INVALID URL", message="PLEASE ENTER A VALID ZILLOW URL.")
            break
    if extract:
        zillow.upload_data_to_csv_sheet()
        zillow.upload_data_to_json_file()
        messagebox.showinfo(title="SUCCESSFUL", message="DATA has been extracted successfully and uploaded to both JSON and CSV directory.")


############# GUI ###############
COLOR_1 = "#afe1fa"
COLOR_2 = "#2567b1"
window = Tk()
img = PhotoImage(file="img.png")
window.title("EXTRACT ZILLOW WEBSITE INFO")
window.geometry("900x650")
window.resizable(False, False)
canvas = Canvas(window, width=900, height=650)
canvas.create_image(450, 325, image=img)
canvas.place(x=0, y=0)
enter_url_label = Label(text="ENTER URL: ", background=COLOR_1, foreground=COLOR_2, font=("Arial", 18, "bold"))
enter_url_label.place(x=100, y=140)
url_entry = Entry(width=57, font=("Arial", 14), foreground="#2174ba",)
url_entry.place(x=100, y=177)
url_entry.focus()

extract_data_button = Button(window, text="Extract Data", width=10,  height=1, font=("Arial", 18, "bold"), background=COLOR_2,
                             activebackground="#2174ba", activeforeground="white", foreground="white", command=start_extracting_data)
extract_data_button.place(x=568, y=220)
window.mainloop()