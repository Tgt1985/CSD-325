# Sean Dudley
# CSD-325 - Module 10 - Tkinter.GUI Forms
# 5/18/2025

import tkinter as tk
import tkinter.messagebox as msg


class Todo(tk.Tk):


    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        self.tasks_canvas = tk.Canvas(self)

        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)

        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)    

        self.title("Dudley-To-Do App v1")   
        self.geometry("500x600")
        self.create_menu()

        self.task_create = tk.Text(self.text_frame, height=3, bg="blue", fg="gold")

        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="n")

        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        todol = tk.Label(self.tasks_frame, text="---Left Click to Add tasks, Right Click to Remove tasks ---", bg="cyan2", fg="red", pady=10)
        todol.bind("<Button-1>", self.add_task)

        self.tasks.append(todol)




        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

            self.bind("<Button-1>", self.add_task)
            self.bind("<Button-3>", self.remove_task)                      
            self.bind("<Configure>", self.on_frame_configure)
            self.tasks_canvas.bind("<Configure>", self.task_width)                                   


            self.colour_schemes = [{"bg": "blue", "fg": "green2"}, {"bg": "gold", "fg": "gray10"}]

    def create_menu(self):
        filebar = tk.Menu(self)

        file_menu = tk.Menu(filebar, tearoff=0)
        file_menu.add_command(label="New Task", command=self.add_task)
        file_menu.add_command(label="Exit", command=self.quit)
        filebar.add_cascade(label="File", menu=file_menu)

        self.config(menu=filebar)


    def add_task(self, event=None):
        task_text = self.task_create.get(1.0,tk.END).strip()

        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)

            self.set_task_colour(len(self.tasks), new_task)

            new_task.bind("<Button-1>", self.add_task)
            new_task.bind("<Button-3>", self.remove_task)            
            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)

        self.task_create.delete(1.0, tk.END)    
                                  
            
    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):  
            self.tasks.remove(event.widget)
            event.widget.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)

        my_scheme_choice = self.colour_schemes[task_style_choice]

        task.configure(bg=my_scheme_choice["bg"])
        task.configure(fg=my_scheme_choice["fg"])

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width = canvas_width)

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        else:
            if event.num == 5:
                move = 1
            else:
                move = -1    

            self.tasks_canvas.yview_scroll(move, "units")


          
if __name__== "__main__":            
    todo = Todo()
    todo.mainloop()