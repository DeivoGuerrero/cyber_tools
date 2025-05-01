#!/usr/bin/env python3
# Force Tk to use its own backend instead of relying on XCB
import os
import sys
import subprocess

# Simple function to test if the display is accessible
def test_display():
    """Test if the display is accessible without using X11/XCB"""
    try:
        # Check if DISPLAY is set
        if 'DISPLAY' not in os.environ or not os.environ['DISPLAY']:
            print("Warning: DISPLAY environment variable not set or empty.")
            # Try to set a default display
            os.environ['DISPLAY'] = ':0.0'
            
        # Try to run a simple Xorg test command
        result = subprocess.run(
            ['xset', 'q'], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            timeout=2
        )
        return result.returncode == 0
    except Exception as e:
        print(f"Display test failed: {e}")
        return False

# Only set essential Tk-related environment variables
os.environ['TK_LIBRARY'] = os.environ.get('TK_LIBRARY', '')
os.environ['TCL_LIBRARY'] = os.environ.get('TCL_LIBRARY', '')
os.environ['TCLLIBPATH'] = os.environ.get('TCLLIBPATH', '')

# Disable XCB usage completely
os.environ.pop('XCB_LIBRARY_PATH', None)
os.environ.pop('QT_X11_NO_MITSHM', None)
os.environ.pop('LIBGL_DRI3_DISABLE', None)
os.environ.pop('QT_QPA_PLATFORM', None)
os.environ.pop('GDK_BACKEND', None)
os.environ.pop('QT_XCB_GL_INTEGRATION', None)

# Import modules after environment setup
import tkinter as tk
from tkinter import ttk, messagebox
import traceback

# Try to import password_generator module with error handling
try:
    from password_generator import password_generator
except ImportError as e:
    print(f"Error importing password_generator module: {e}")
    sys.exit(1)
def generate_password():
    """Generate a new password and update the display label"""
    try:
        length = int(length_var.get())
        password = password_generator(
            long_password=length,
            lowercase_op=lowercase_var.get(),
            uppercase_op=uppercase_var.get(),
            numbers_op=numbers_var.get(),
            special_caracters_op=special_var.get()
        )
        password_var.set(password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")



# Initialize the main window with error handling
try:
    # First test the display
    if not test_display():
        print("Warning: Display test failed. Trying to continue anyway...")
    
    # Create a simpler initialization for Tk
    try:
        # Tell Tk to avoid XCB if possible
        tk.tix = None  # Disable Tix extension which can trigger XCB issues
        
        # Create the root window
        root = tk.Tk(className="PasswordGenerator")
        
        # Immediately withdraw the window and update it to process any pending events
        # This can help avoid XCB issues on some systems
        root.withdraw()
        root.update()
        
        # Now make it visible again
        root.deiconify()
    except tk.TclError as e:
        print(f"Failed to initialize Tkinter: {e}")
        print("Trying alternative initialization...")
        
        # Last resort: try with minimal initialization
        os.environ['DISPLAY'] = ':0.0'
        root = tk.Tk(sync=True)  # sync=True can help with display issues
    
    # Configure the root window
    root.title("Password Generator")
    root.geometry("400x300")
    root.resizable(False, False)
    
    # Add basic error handling
    def handle_tk_error(exc, val, tb):
        print(f"Tkinter error: {val}")
        traceback.print_tb(tb)
        try:
            messagebox.showerror("Error", f"An error occurred:\n{val}")
        except:
            print("Could not display error dialog")
    
    root.report_callback_exception = handle_tk_error
    
except Exception as e:
    print(f"Failed to create GUI: {e}")
    traceback.print_exc()
    sys.exit(1)

# Create a frame for the settings
settings_frame = ttk.LabelFrame(root, text="Password Settings")
settings_frame.pack(padx=10, pady=10, fill="x")

# Password length
length_var = tk.IntVar(value=12)
ttk.Label(settings_frame, text="Length:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
length_spinbox = ttk.Spinbox(settings_frame, from_=8, to=20, width=5, textvariable=length_var)
length_spinbox.grid(row=0, column=1, sticky="w", padx=5, pady=5)

# Character options
lowercase_var = tk.BooleanVar(value=True)
uppercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

ttk.Checkbutton(settings_frame, text="Lowercase (a-z)", variable=lowercase_var).grid(row=1, column=0, sticky="w", padx=5, pady=2)
ttk.Checkbutton(settings_frame, text="Uppercase (A-Z)", variable=uppercase_var).grid(row=2, column=0, sticky="w", padx=5, pady=2)
ttk.Checkbutton(settings_frame, text="Numbers (0-9)", variable=numbers_var).grid(row=1, column=1, sticky="w", padx=5, pady=2)
ttk.Checkbutton(settings_frame, text="Special (!@#$)", variable=special_var).grid(row=2, column=1, sticky="w", padx=5, pady=2)

# Create password display frame
display_frame = ttk.LabelFrame(root, text="Generated Password")
display_frame.pack(padx=10, pady=10, fill="x")

# Password display
password_var = tk.StringVar()
password_label = ttk.Label(
    display_frame, 
    textvariable=password_var,
    font=("Courier", 14),
    background="#f0f0f0",
    relief="sunken",
    padding=10
)
password_label.pack(fill="x", padx=10, pady=10)

# Create button frame
button_frame = ttk.Frame(root)
button_frame.pack(padx=10, pady=10, fill="x")

# Generate button
generate_btn = ttk.Button(
    button_frame, 
    text="Generate Password", 
    command=generate_password
)
generate_btn.pack(side="left", fill="x", expand=True, padx=5)

# Copy button
def copy_to_clipboard():
    """Copy the generated password to clipboard"""
    password = password_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

copy_btn = ttk.Button(
    button_frame, 
    text="Copy to Clipboard", 
    command=copy_to_clipboard
)
copy_btn.pack(side="right", fill="x", expand=True, padx=5)

# Generate an initial password
generate_password()
# Start the main loop with simple error handling
try:
    # Start main loop with minimal error-triggering activity
    print("Starting Password Generator application...")
    # Use update() periodically instead of mainloop() for more control
    # This can help avoid XCB issues on some systems
    root.update()
    root.after(100, lambda: None)  # Schedule a dummy event
    root.mainloop()
except KeyboardInterrupt:
    print("Application terminated by user.")
    sys.exit(0)
except Exception as e:
    print(f"Error in main loop: {e}")
    traceback.print_exc()
    sys.exit(1)
    sys.exit(1)
