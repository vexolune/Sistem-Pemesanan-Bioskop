import mysql.connector
import customtkinter as ctk
import tkinter
import warnings
from CTkTable import *
from PIL import ImageTk, Image
from CTkMessagebox import CTkMessagebox

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
warnings.filterwarnings("ignore", message=".*Image can not be scaled on HighDPI displays.*")

# Database connection setup
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",  # Your MySQL host
        user="root",       # Your MySQL username
        password="",  # Your MySQL password
        database="cinema_system"
    )

def CenterWindowToDisplay(Screen, width, height, scale_factor=1.0):
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width / 2) - (width / 2)) * scale_factor)
    y = int(((screen_height / 2) - (height / 1.5)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"

class CinemaTicketSystem(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Cinema Ticket System")
        window_scaling = self._get_window_scaling()
        self.geometry(CenterWindowToDisplay(self, 600, 600, window_scaling))
        self.previous_frame = None  # Keep track of the previous frame
        self.init_ui()

    def init_ui(self):

        # Custom frame for main menu
        frame = ctk.CTkFrame(master=self, width=320, height=300, corner_radius=15, fg_color="transparent")
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Load and display logo
        logo_path = "./assets/logo.png"
        try:
            logo_image = Image.open(logo_path)
            logo_image = logo_image.resize((150, 150), Image.Resampling.LANCZOS)  # Updated resizing method
            self.logo_photo = ImageTk.PhotoImage(logo_image)
            self.logo_label = ctk.CTkLabel(frame, image=self.logo_photo, text="")  # Set text to empty
            self.logo_label.pack(pady=(10, 0))
        except Exception as e:
            print(f"Error loading logo: {e}")

        # Title with bold font
        self.title_label = ctk.CTkLabel(frame, text="Synema", font=("Mont", 24, "bold"))
        self.title_label.pack(pady=20)

        self.login_button = ctk.CTkButton(frame, text="Login", command=self.show_login_menu, font=("Mont", 14), fg_color="#1f6aa5", text_color="white")
        self.login_button.pack(pady=10)

        self.register_button = ctk.CTkButton(frame, text="Register", command=self.show_register_menu, font=("Mont", 14), fg_color="#1f6aa5", text_color="white")
        self.register_button.pack(pady=10)

        self.exit_button = ctk.CTkButton(frame, text="Exit", command=self.exit, font=("Mont", 14), fg_color="#1f6aa5",text_color="white")
        self.exit_button.pack(pady=10)

    def show_login_menu(self):
        self.clear_frame()
        self.login_menu = LoginMenu(self)

    def show_register_menu(self):
        self.clear_frame()
        self.register_menu = RegisterMenu(self)

    def exit(self):
        msg = CTkMessagebox(master=self.master, title="Exit?", message="Do you want to close the program?", icon="question", option_1="No", option_2="Yes")
        response = msg.get()
        
        if response=="Yes":
            self.destroy()       
        else:
            print("Pressed No")

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def set_previous_frame(self, frame):
        self.previous_frame = frame

    def base_window_size(self):
        self.update_idletasks()  # Ensure all widgets are rendered
        self.geometry("600x600")
        self.update()

    def book_window_size(self):
        self.update_idletasks()  # Ensure all widgets are rendered
        self.geometry("1120x600")
        self.update()

class LoginMenu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.set_previous_frame(self)
        self.master.geometry("600x600")
        self.master.title("Login")

        # Background image
        img1 = ImageTk.PhotoImage(Image.open("./assets/pattern.png"))
        bg_label = ctk.CTkLabel(master=self.master, image=img1)
        bg_label.image = img1  # Keep a reference to prevent garbage collection
        bg_label.pack()

        # Custom frame
        frame = ctk.CTkFrame(master=bg_label, width=320, height=400, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        title_label = ctk.CTkLabel(master=frame, text="Log into your Account", font=("Mont", 20, "bold"))
        title_label.place(x=50, y=45)

        self.username_entry = ctk.CTkEntry(master=frame, width=220, placeholder_text='Username', font=('Mont',12))
        self.username_entry.place(x=50, y=110)

        self.password_entry = ctk.CTkEntry(master=frame, width=220, placeholder_text='Password', font=('Mont',12), show="*")
        self.password_entry.place(x=50, y=165)

        # Login button
        login_button = ctk.CTkButton(master=frame, width=220, text="Login", font=('Mont',14), command=self.login, corner_radius=6)
        login_button.place(x=50, y=240)

        l3=ctk.CTkLabel(master=frame, text="Forgot password?", font=('Mont',12))
        l3.place(x=155,y=195)

        # Back button
        back_button = ctk.CTkButton(master=frame, width=220, text="Back", font=('Mont',14), command=self.back, corner_radius=6)
        back_button.place(x=50, y=290)

        img2 = ctk.CTkImage(Image.open("./assets/google.webp").resize((20, 20), Image.Resampling.LANCZOS))
        google_button = ctk.CTkButton(master=frame, image=img2, text="Google", font=('Mont',12), width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
        google_button.place(x=50, y=340)

        img3 = ctk.CTkImage(Image.open("./assets/facebook.png").resize((20, 20), Image.Resampling.LANCZOS))
        fb_button = ctk.CTkButton(master=frame, image=img3, text="Facebook", font=('Mont',12), width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
        fb_button.place(x=170, y=340)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Validate credentials from MySQL database
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT role FROM users WHERE username = %s AND password = %s", (username, password))
        result = cursor.fetchone()

        if result:
            role = result[0]
            print(f"Logged in as {role.capitalize()}: {username}")
            self.master.username = username

            if role == "customer":
                self.master.clear_frame()
                self.customer_menu = CustomerMenu(self.master)
            elif role == "admin":
                self.master.clear_frame()
                self.admin_menu = AdminMenu(self.master)
        else:
            print("Login failed. Please check your credentials.")
            CTkMessagebox(master=self.master, title="Error", message="Login failed. Please check your credentials.", icon="cancel", justify="center")


        cursor.close()
        connection.close()

    def back(self):
        self.master.clear_frame()
        self.master.init_ui()
        self.master.base_window_size()

class RegisterMenu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.geometry("600x600")
        self.master.title("Register")

        # Background image
        img1 = ImageTk.PhotoImage(Image.open("./assets/pattern.png"))
        bg_label = ctk.CTkLabel(master=self.master, image=img1)
        bg_label.image = img1  # Keep a reference to prevent garbage collection
        bg_label.pack()


        # Custom frame
        frame = ctk.CTkFrame(master=bg_label, width=320, height=400, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        title_label = ctk.CTkLabel(master=frame, text="Register", font=("Mont", 24, "bold"))
        title_label.place(x=115, y=45)

        self.username_entry = ctk.CTkEntry(master=frame, width=220, placeholder_text='Username')
        self.username_entry.place(x=50, y=110)

        self.password_entry = ctk.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
        self.password_entry.place(x=50, y=165)

        # Register button
        customer_button = ctk.CTkButton(master=frame, width=220, text="Sign Up", font=("Mont", 14), command=self.register_customer, corner_radius=6)
        customer_button.place(x=50, y=240)

        # admin_button = ctk.CTkButton(master=frame, width=220, text="Register as Admin", command=self.register_admin, corner_radius=6)
        # admin_button.place(x=50, y=290)

        img2 = ctk.CTkImage(Image.open("./assets/google.webp").resize((20, 20), Image.Resampling.LANCZOS))
        google_button = ctk.CTkButton(master=frame, image=img2, text="Google", font=('Mont',12), width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
        google_button.place(x=50, y=290)

        img3 = ctk.CTkImage(Image.open("./assets/facebook.png").resize((20, 20), Image.Resampling.LANCZOS))
        fb_button = ctk.CTkButton(master=frame, image=img3, text="Facebook", font=('Mont',12), width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
        fb_button.place(x=170, y=290)

        # Back button
        back_button = ctk.CTkButton(master=frame, width=220, text="Back", font=("Mont", 14), command=self.back, corner_radius=6)
        back_button.place(x=50, y=350)


    def register_customer(self):
        self.register_user(role="customer")

    def register_admin(self):
        self.register_user(role="admin")

    def register_user(self, role):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            print("Please fill in all fields.")
            CTkMessagebox(master=self.master, title="Error", message="Please fill in all fields.", icon="cancel")
            return

        connection = get_db_connection()
        cursor = connection.cursor()

        # Use MySQL-compatible syntax with %s placeholders
        cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s", (username,))
        if cursor.fetchone()[0] > 0:
            print(f"Username {username} already exists.")
            CTkMessagebox(master=self.master, title="Error", message=(f"Username {username} already exists."), icon="cancel")
        else:
            cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
                        (username, password, role))
            connection.commit()
            print(f"Registered as {role.capitalize()}: {username}")
            CTkMessagebox(master=self.master, message=(f"Registered as {role.capitalize()}: {username}"), icon="check", option_1="Okay")

        cursor.close()
        connection.close()

    def back(self):
        self.master.clear_frame()
        self.master.init_ui()
        self.master.base_window_size()

class CustomerMenu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.set_previous_frame(self)

        self.label = ctk.CTkLabel(self, text="Customer Menu", font=("Mont", 15, "bold"))
        self.label.pack(pady=20)

        self.view_movies_button = ctk.CTkButton(self, text="View Movies", font=("Mont", 12), command=self.view_movies)
        self.view_movies_button.pack(pady=5)

        self.book_ticket_button = ctk.CTkButton(self, text="Book Ticket", font=("Mont", 12), command=self.book_ticket)
        self.book_ticket_button.pack(pady=5)

        self.view_booked_button = ctk.CTkButton(self, text="View Booked Tickets", font=("Mont", 12), command=self.view_booked)
        self.view_booked_button.pack(pady=5)

        self.cancel_booking_button = ctk.CTkButton(self, text="Cancel Booking", font=("Mont", 12), command=self.cancel_booking)
        self.cancel_booking_button.pack(pady=5)

        self.back_button = ctk.CTkButton(self, text="Logout", font=("Mont", 12), command=self.logout)
        self.back_button.pack(pady=5)

        self.pack()
        self.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def logout(self):
        # Clear the current frame and go back to the login menu
        self.master.clear_frame()
        self.master.show_login_menu()

    # View Movies
    def view_movies(self):
        print("Viewing movies...")
        self.clear_current_frame()

        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT id, title, genre, duration FROM movies")
        movies = cursor.fetchall()

        for movie in movies:
            ctk.CTkLabel(self, text=f"{movie[1]} ({movie[2]}, {movie[3]} minutes)").pack(pady=5)

        cursor.close()
        connection.close()

        self.back_button = ctk.CTkButton(self, text="Back", command=self.back)
        self.back_button.pack(pady=5)

    # Book Ticket
    def book_ticket(self):
        print("Booking ticket...")
        self.clear_current_frame()

        self.select_movie_label = ctk.CTkLabel(self, text="Select Movie")
        self.select_movie_label.pack(pady=5)

        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT id, title FROM movies")
        movies = cursor.fetchall()

        self.movie_menu = ctk.CTkOptionMenu(self, values=[movie[1] for movie in movies], command=self.select_movie)
        self.movie_menu.pack(pady=5)

        self.ticket_quantity_entry = ctk.CTkEntry(self, placeholder_text="Quantity")
        self.ticket_quantity_entry.pack(pady=5)

        self.book_button = ctk.CTkButton(self, text="Book Ticket", command=self.submit_booking)
        self.book_button.pack(pady=10)

        cursor.close()
        connection.close()

        self.back_button = ctk.CTkButton(self, text="Back", command=self.back)
        self.back_button.pack(pady=5)

    def select_movie(self, movie_title):
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT id FROM movies WHERE title = %s", (movie_title,))
        self.selected_movie_id = cursor.fetchone()[0]

        cursor.close()
        connection.close()

    def submit_booking(self):
        quantity = self.ticket_quantity_entry.get()

        if quantity:
            connection = get_db_connection()
            cursor = connection.cursor()

            cursor.execute("INSERT INTO bookings (username, movie_id, quantity) VALUES (%s, %s, %s)",
                        (self.master.username, self.selected_movie_id, int(quantity)))
            connection.commit()
            print(f"Successfully booked {quantity} tickets.")

            cursor.close()
            connection.close()
        else:
            print("Please specify the quantity.")

    # View Booked Tickets
    def view_booked(self):
        print("Viewing booked tickets...")
        self.clear_current_frame()

        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT b.booking_time, b.quantity, m.title 
            FROM bookings b
            JOIN movies m ON b.movie_id = m.id
            WHERE b.username = %s
            ORDER BY b.booking_time DESC
        """, (self.master.username,))
        bookings = cursor.fetchall()

        for booking in bookings:
            ctk.CTkLabel(self, text=f"Movie: {booking[2]}, Quantity: {booking[1]}, Time: {booking[0]}").pack(pady=5)

        cursor.close()
        connection.close()

        self.back_button = ctk.CTkButton(self, text="Back", command=self.back)
        self.back_button.pack(pady=5)

    # Cancel Booking
    def cancel_booking(self):
        print("Cancelling booking...")
        self.clear_current_frame()

        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT b.id, m.title, b.quantity, b.booking_time 
            FROM bookings b
            JOIN movies m ON b.movie_id = m.id
            WHERE b.username = %s
        """, (self.master.username,))
        bookings = cursor.fetchall()

        for booking in bookings:
            ctk.CTkButton(self, text=f"Cancel {booking[1]} ({booking[2]} tickets)", command=lambda b_id=booking[0]: self.submit_cancel(b_id)).pack(pady=5)

        cursor.close()
        connection.close()

        self.back_button = ctk.CTkButton(self, text="Back", command=self.back)
        self.back_button.pack(pady=5)

    def submit_cancel(self, booking_id):
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("DELETE FROM bookings WHERE id = %s", (booking_id,))
        connection.commit()
        print(f"Booking cancelled.")
        self.cancel_booking()

        cursor.close()
        connection.close()

    def back(self):
        print("Back...")
        self.master.clear_frame()
        self.master.customer_menu = CustomerMenu(self.master)
        self.master.base_window_size()

    def clear_current_frame(self):
        # Clear current frame but avoid destroying the main window
        for widget in self.winfo_children():
            widget.pack_forget()

class AdminMenu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.set_previous_frame(self)

        self.label = ctk.CTkLabel(self, text="Admin Menu", font=("Mont", 15, "bold"))
        self.label.pack(pady=20)
        

        self.add_movie_button = ctk.CTkButton(self, text="Add Movie", font=("Mont", 12), command=self.add_movie)
        self.add_movie_button.pack(pady=5)

        self.schedule_movie_button = ctk.CTkButton(self, text="Schedule Movie", font=("Mont", 12), command=self.schedule_movie)
        self.schedule_movie_button.pack(pady=5)

        self.view_booking_history_button = ctk.CTkButton(self, text="View Booking History", font=("Mont", 12), command=self.view_booking_history)
        self.view_booking_history_button.pack(pady=5)

        self.back_button = ctk.CTkButton(self, text="Logout", font=("Mont", 12), command=self.logout)
        self.back_button.pack(pady=5)

        self.pack()
        self.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        

    def logout(self):
        self.master.clear_frame()
        self.master.show_login_menu()

    # Add Movie
    def add_movie(self):
        print("Tambahkan Film...")

        self.clear_current_frame()  # Clear the current frame before adding new widgets

        # Add widgets to the current frame (use 'self' instead of 'self.master' to add widgets to the current frame)
        self.movie_title_entry = ctk.CTkEntry(self, placeholder_text="Movie Title")
        self.movie_title_entry.pack(pady=5)
        
        self.movie_genre_entry = ctk.CTkEntry(self, placeholder_text="Genre")
        self.movie_genre_entry.pack(pady=5)
        
        self.movie_duration_entry = ctk.CTkEntry(self, placeholder_text="Duration (minutes)")
        self.movie_duration_entry.pack(pady=5)
        
        self.movie_show_time_entry = ctk.CTkEntry(self, placeholder_text="Show Time (HH:MM:SS)")
        self.movie_show_time_entry.pack(pady=5)
        
        self.submit_button = ctk.CTkButton(self, text="Add Movie", command=self.submit_add_movie)
        self.submit_button.pack(pady=5)

        self.back_button = ctk.CTkButton(self, text="Back", command=self.back)
        self.back_button.pack(pady=5)

    def submit_add_movie(self):
        title = self.movie_title_entry.get()
        genre = self.movie_genre_entry.get()
        duration = self.movie_duration_entry.get()
        show_time = self.movie_show_time_entry.get()

        # Insert movie into the database
        if title and genre and duration and show_time:
            connection = get_db_connection()
            cursor = connection.cursor()

            cursor.execute("INSERT INTO movies (title, genre, duration, show_time) VALUES (%s, %s, %s, %s)",
                        (title, genre, int(duration), show_time))
            connection.commit()
            print(f"Movie '{title}' added successfully.")
            cursor.close()
            connection.close()
        else:
            print("Please fill in all fields.")

    # Schedule Movie
    def schedule_movie(self):
        print("Atur Jadwal Film...")
        self.clear_current_frame()

        # Create the Schedule Movie form
        self.select_movie_label = ctk.CTkLabel(self, text="Select Movie")
        self.select_movie_label.pack(pady=5)

        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT id, title FROM movies")
        movies = cursor.fetchall()

        self.movie_menu = ctk.CTkOptionMenu(self, values=[movie[1] for movie in movies], command=self.select_movie)
        self.movie_menu.pack(pady=5)

        self.schedule_show_time_entry = ctk.CTkEntry(self, placeholder_text="Schedule Show Time (HH:MM:SS)")
        self.schedule_show_time_entry.pack(pady=5)

        self.schedule_button = ctk.CTkButton(self, text="Schedule Movie", command=self.submit_schedule_movie)
        self.schedule_button.pack(pady=10)

        cursor.close()
        connection.close()

        self.back_button = ctk.CTkButton(self, text="Back", command=self.back)
        self.back_button.pack(pady=5)


    def select_movie(self, movie_title):
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT id FROM movies WHERE title = %s", (movie_title,))
        self.selected_movie_id = cursor.fetchone()[0]

        cursor.close()
        connection.close()

    def submit_schedule_movie(self):
        show_time = self.schedule_show_time_entry.get()

        if show_time:
            connection = get_db_connection()
            cursor = connection.cursor()

            cursor.execute("INSERT INTO movie_schedule (movie_id, show_time) VALUES (%s, %s)",
                        (self.selected_movie_id, show_time))
            connection.commit()
            print(f"Movie scheduled successfully for {show_time}.")
            cursor.close()
            connection.close()
            self.master.clear_frame()
            self.customer_menu = AdminMenu(self.master)
        else:
            print("Please provide a show time.")

    # View Booking History
    def view_booking_history(self):
        print("Lihat Riwayat Pemesanan...")
        self.master.book_window_size()
        
        self.clear_current_frame()

        # Create a scrollable frame
        scrollable_frame = ctk.CTkScrollableFrame(self, width=1120, height=600)
        scrollable_frame.pack(fill="both", expand=True)

        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT b.id, u.username, m.id, m.title, m.genre, m.duration, b.quantity, b.booking_time
            FROM bookings b
            JOIN movies m ON b.movie_id = m.id
            JOIN users u ON b.username = u.username
        """)
        bookings = cursor.fetchall()

        # Create header table (match new header order)
        headers = ["Booking ID", "Username", "Movie ID", "Movie Title", "Genre", "Duration", "Quantity", "Booking Time", "Actions"]
        for col, header in enumerate(headers):
            ctk.CTkLabel(scrollable_frame, text=header, font=("Mont", 12, "bold")).grid(row=0, column=col, padx=10, pady=5, sticky="w")

        self.entries = []  # List to store references to the CTkEntry widgets
        # Fill the table with booking data
        for row, booking in enumerate(bookings, start=1):
            # Populate each column with corresponding values
            for col, value in enumerate(booking):
                entry = ctk.CTkEntry(scrollable_frame, textvariable=ctk.StringVar(value=str(value)), width=100)
                entry.grid(row=row, column=col, padx=10, pady=5, sticky="w")
                self.entries.append(entry)

            # Add "Save" button for each row
            ctk.CTkButton(
                scrollable_frame,
                text="Save",
                command=lambda b_id=booking[0], row=row: self.save_booking_changes(b_id, row),
                width=40,
                height=20
            ).grid(row=row, column=len(headers)-1, padx=10, pady=5)

            # Add "Delete" button for each row
            ctk.CTkButton(
                scrollable_frame,
                text="Delete",
                fg_color="red",
                command=lambda b_id=booking[0]: self.delete_booking(b_id),
                width=40,   # Set the width of the button
                height=20
            ).grid(row=row, column=len(headers), padx=10, pady=5)

        cursor.close()
        connection.close()

        # Add "Back" button
        back_button = ctk.CTkButton(scrollable_frame, text="Back", command=self.back)
        back_button.grid(row=len(bookings) + 1, column=0, columnspan=len(headers), pady=10)

    def save_booking_changes(self, booking_id, row):
        # Retrieve the updated values from the Entry widgets for the specific row
        updated_username = self.entries[(row - 1) * 8 + 1].get()  # Username Entry in this row
        updated_movie_id = self.entries[(row - 1) * 8 + 2].get()  # Movie ID Entry
        updated_movie_title = self.entries[(row - 1) * 8 + 3].get()  # Movie Title Entry
        updated_genre = self.entries[(row - 1) * 8 + 4].get()  # Genre Entry
        updated_duration = self.entries[(row - 1) * 8 + 5].get()  # Duration Entry
        updated_quantity = self.entries[(row - 1) * 8 + 6].get()  # Quantity Entry
        updated_booking_time = self.entries[(row - 1) * 8 + 7].get()  # Booking Time Entry

        # Ensure quantity is an integer and booking time is properly formatted (optional)
        try:
            updated_quantity = int(updated_quantity)
        except ValueError:
            print("Invalid quantity entered. Please enter a valid integer.")
            return

        # Check if the movie_id is valid (if it's provided by the user)
        if updated_movie_id:
            # Check if the movie_id exists in the database
            connection = get_db_connection()
            cursor = connection.cursor()

            cursor.execute("SELECT id FROM movies WHERE id = %s", (updated_movie_id,))
            movie_id_exists = cursor.fetchone()

            if not movie_id_exists:
                print(f"Invalid Movie ID '{updated_movie_id}' entered. Please enter a valid Movie ID.")
                cursor.close()
                connection.close()
                self.view_booking_history()  # Refresh the window without making changes
                return  # Exit the method if the movie_id is invalid

            movie_id = updated_movie_id  # Use the provided movie_id if it's valid
        else:
            # If movie_id is not provided, find it by movie_title
            cursor.execute("SELECT id FROM movies WHERE title = %s", (updated_movie_title,))
            movie_id = cursor.fetchone()

            if movie_id:
                movie_id = movie_id[0]  # Extract the movie_id from the result
            else:
                print(f"Movie title '{updated_movie_title}' not found in the database.")
                cursor.close()
                connection.close()
                self.view_booking_history()  # Refresh the window without making changes
                return  # Exit the method if the movie title is not found

        # Check if the username exists in the database
        cursor.execute("SELECT username FROM users WHERE username = %s", (updated_username,))
        user_exists = cursor.fetchone()

        if not user_exists:
            print(f"Username '{updated_username}' does not exist in the database.")
            cursor.close()
            connection.close()
            self.view_booking_history()  # Refresh the window without making changes
            return  # Exit the method if the username is not found

        # Update the booking record in the database with all fields
        cursor.execute("""
            UPDATE bookings 
            SET username = %s, movie_id = %s, quantity = %s, booking_time = %s
            WHERE id = %s
        """, (updated_username, movie_id, updated_quantity, updated_booking_time, booking_id))

        print(f"Executing SQL: UPDATE bookings SET username = {updated_username}, movie_id = {movie_id}, quantity = {updated_quantity}, booking_time = {updated_booking_time} WHERE id = {booking_id}")

        # Commit the transaction to the database
        connection.commit()  
        print(f"Booking {booking_id} updated successfully.")

        cursor.close()
        connection.close()

        # Refresh the view after saving changes
        self.view_booking_history()

    def delete_booking(self, booking_id):
        try:
            # Establish database connection
            connection = get_db_connection()
            cursor = connection.cursor()

            # Delete the booking from the database
            cursor.execute("DELETE FROM bookings WHERE id = %s", (booking_id,))
            connection.commit()

            # Close the cursor and connection
            cursor.close()
            connection.close()

            # Refresh the booking history after deletion
            self.view_booking_history()

        except Exception as e:
            # Handle any errors
            print(f"Error deleting booking: {e}")


    def back(self):
        print("Back...")
        self.master.clear_frame()
        self.master.customer_menu = AdminMenu(self.master)
        self.master.base_window_size()

    def clear_current_frame(self):
        for widget in self.winfo_children():
            widget.pack_forget()

if __name__ == "__main__":
    app = CinemaTicketSystem()
    app.mainloop()
