from tkinter import *  # Importing all classes and functions from tkinter
from tkinter import messagebox  # Importing messagebox for displaying messages
from PIL import ImageTk  # Importing ImageTk from PIL for image handling

# Creating the main window
window = Tk()

# Configuring the window size, disabling resizing, setting background color, and title
window.geometry("1280x700+0+0")  # Set window size and position
window.resizable(False, False)  # Disable resizing
window.config(bg="white")  # Set background color to white
window.title("Login System of Student Management System")  # Set window title

# Setting the icon for the window
window.iconbitmap(r"C:\Users\Abhinash Kumar\Downloads\130manstudent2_100617.ico")

# Loading and displaying the background image
backgroundImage = ImageTk.PhotoImage(file=r"C:\Users\Abhinash Kumar\Downloads\pexels-goumbik-590022.jpg")
bgLabel = Label(window)  # Creating a label for the background image
bgLabel.place(x=0, y=0)  # Placing the image at the top-left corner

# Creating a frame for the login section
loginFrame = Frame(window, bg='white')  # White background for the login frame
loginFrame.place(x=400, y=150)  # Positioning the login frame

# Function to handle login logic
def login():
    # Check if username or password fields are empty
    if usernameEntry.get() == "" or passwordEntry.get() == "":
        messagebox.showerror("Error", "Fields cannot be empty")  # Display error if fields are empty
    
    # Verify credentials
    elif usernameEntry.get() == "Avinash" and passwordEntry.get() == "1234":
        messagebox.showinfo("Successfully", "Welcome")  # Display success message
        window.destroy()  # Close the current login window
        import sms  # Import the 'sms' module (assuming it starts the main application)
    
    else:
        messagebox.showerror("Error", "Invalid username or password")  # Error for incorrect credentials

# Loading and displaying the logo image
logoImage = PhotoImage(file=r"C:\Users\Abhinash Kumar\Downloads\graduated.png")
logoLabel = Label(loginFrame, image=logoImage)  # Creating label to hold the logo
logoLabel.grid(row=0, column=0, columnspan=2, pady=10)  # Positioning the logo

# Username section with image and input field
usernameImage = PhotoImage(file=r"C:\Users\Abhinash Kumar\Downloads\user.png")
usernameLabel = Label(loginFrame, image=usernameImage, text="Username", compound=LEFT, 
                      font=("times new roman", 20, "bold"), bg="white")  # Label with username text and image
usernameLabel.grid(row=1, column=0, pady=10, padx=20)  # Positioning the label
usernameEntry = Entry(loginFrame, font=("times new roman", 20, "bold"), relief="sunken", 
                      bd=5, fg="royalblue")  # Input field for username
usernameEntry.grid(row=1, column=1, pady=10, padx=20)  # Positioning the input field

# Password section with image and input field
passwordImage = PhotoImage(file=r"C:\Users\Abhinash Kumar\Downloads\padlock.png")
passwordLabel = Label(loginFrame, image=passwordImage, text="Password", compound=LEFT, 
                      font=("times new roman", 20, "bold"), bg="white")  # Label with password text and image
passwordLabel.grid(row=2, column=0, pady=10, padx=20)  # Positioning the label
passwordEntry = Entry(loginFrame, font=("times new roman", 20, "bold"), relief="sunken", 
                      bd=5, fg="royalblue")  # Input field for password
passwordEntry.grid(row=2, column=1, pady=10, padx=20)  # Positioning the input field

# Login button with styling and command to trigger the login function
loginButton = Button(loginFrame, text="Login", font=("times new roman", 14, "bold"), width=15, 
                     bg="cornflowerblue", fg="white", activebackground="cornflowerblue", 
                     activeforeground="white", cursor="hand2", command=login)  # Button for login
loginButton.grid(row=3, column=1, pady=10)  # Positioning the button

# Starting the main event loop to display the window
window.mainloop()
