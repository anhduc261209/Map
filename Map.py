import tkintermapview as tkmap
import customtkinter as ctk
import tkinter as tk

markers = []
paths = []

def lookup():
    lookup_dialog = ctk.CTkInputDialog(master = None, text = "Type in the address you want to look up:", title = "My Map")
    map_widget.set_address(lookup_dialog.get_input())

def zoom(value):
    map_widget.set_zoom(value)

def marker():
    marker_dialog = ctk.CTkInputDialog(master = None, text = "Type in the name of the marker:", title = "My Map")
    current_pos = map_widget.get_position()
    markers.append(map_widget.set_marker(current_pos[0], current_pos[1], text=marker_dialog.get_input()))

def add_marker_event(coords):
    marker_dialog = ctk.CTkInputDialog(master = None, text = "Type in the name of the marker:", title = "My Map")
    markers.append(map_widget.set_marker(coords[0], coords[1], text=marker_dialog.get_input()))

def clear_marker():
    for marker in markers:
        marker.delete()

def path():
    path_dialog = ctk.CTkInputDialog(master = None, text = "Type in two markers you want to create a path: (Ex: 1-2, 1-3, 2-3,...)", title = "My Map")
    chosen_markers = path_dialog.get_input().split("-")
    chosen_markers[0], chosen_markers[1] = int(chosen_markers[0])-1, int(chosen_markers[1])-1
    paths.append(map_widget.set_path([markers[chosen_markers[0]].position, markers[chosen_markers[1]].position], color = "green"))

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("800x600")
root.title("My Map by Anh Duc")

map_widget = tkmap.TkinterMapView(master=root, width=780, height=520, corner_radius=7)
map_widget.pack()
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=19)
map_widget.set_zoom(10)
map_widget.set_address("hanoi")

map_widget.add_right_click_menu_command(label = "Add marker", command = add_marker_event, pass_coords=True)

frame = ctk.CTkFrame(master = root, width = 875, height = 60, corner_radius = 7)
frame.pack(padx = 10, pady = 10)

lookup_btn = ctk.CTkButton(master=frame, text="Lookup", command=lookup, width = 20, text_font = ("Segoe UI", 10))
lookup_btn.grid(row = 0, column = 0, padx = 10)

slider = ctk.CTkSlider(master=frame, from_=0, to = 19, command = zoom, width = 150)
slider.grid(row = 0, column = 1, padx = 10)

marker_btn = ctk.CTkButton(master=frame, text="Set marker", command = marker, width = 20, text_font = ("Segoe UI", 10))
marker_btn.grid(row = 0, column = 2, padx = 10)

clear_marker_btn = ctk.CTkButton(master=frame, text="Clear marker", command = clear_marker, width = 20, text_font = ("Segoe UI", 10))
clear_marker_btn.grid(row = 0, column = 3, padx = 10)

path_btn = ctk.CTkButton(master=frame, text="Set path", command = path, width = 20, text_font = ("Segoe UI", 10))
path_btn.grid(row = 0, column = 4, padx = 10)

exit_btn = ctk.CTkButton(master=frame, text="Exit", command = root.destroy, width = 20, text_font = ("Segoe UI", 10))
exit_btn.grid(row = 0, column = 5, padx = 10)

root.mainloop()