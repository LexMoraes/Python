from abc import ABC, abstractmethod
from tkinter import *
from tkinter.messagebox import showinfo, showerror
from tkinter.ttk import Treeview
from types import SimpleNamespace

from actions import AgendaActions
from model import Contact


class BaseView(ABC):
    def __init__(self, title, width, height):
        self.root = Tk()
        self.root.title(title)
        self.root.resizable(False, False)

        self._center_window(width=width, height=height)

    def _center_window(self, width, height):

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculates coordinates to center the window
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Sets the size and position of the window
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    @abstractmethod
    def window_setup(self):
        pass

    def run_view(self):
        self.root.mainloop()


class AgendaView(BaseView):

    def __init__(self):
        super().__init__(title='Agenda', width=300, height=250)
        self._btn_new_contact = Button(self.root, text='New contact')
        self._btn_contact_list = Button(self.root, text='Contact list')
        self._btn_exit = Button(self.root, text='Exit')

        # load setup window
        self.window_setup()

    def window_setup(self):
        # settings widgets button _btn_new_contact
        self._btn_new_contact.grid(column=0, row=0, padx=10, pady=3)
        self._btn_new_contact['width'] = 30
        self._btn_new_contact['height'] = 4
        self._btn_new_contact['font'] = ("Verdana", "10", "italic", "bold")
        self._btn_new_contact['command'] = self._command_new_contact

        # settings widgets button _btn_contact_list
        self._btn_contact_list.grid(column=0, row=1, padx=10, pady=3)
        self._btn_contact_list['width'] = 30
        self._btn_contact_list['height'] = 4
        self._btn_contact_list['font'] = ("Verdana", "10", "italic", "bold")
        self._btn_contact_list['command'] = self._command_contact_list

        # settings widgets button _btn_exit
        self._btn_exit.grid(column=0, row=2, padx=10, pady=3)
        self._btn_exit['width'] = 30
        self._btn_exit['height'] = 4
        self._btn_exit['font'] = ("Verdana", 10, "italic", "bold")
        self._btn_exit['command'] = self.root.quit

    @staticmethod
    def _command_new_contact():
        agenda_new_contact_view = AgendaNewContactView()
        agenda_new_contact_view.run_view()

    @staticmethod
    def _command_contact_list():
        agenda_contact_list_view = AgendaContactListView()
        agenda_contact_list_view.run_view()


class AgendaNewContactView(BaseView):
    def __init__(self, contact=None):
        super().__init__(title='Agenda - New contact', width=700, height=600)
        self._contact = contact
        self._pan_main = Frame(self.root)
        self._lbl_name = Label(self._pan_main, text='Name:')
        self._txt_name = Entry(self._pan_main)
        self._lbl_email = Label(self._pan_main, text='Email:')
        self._txt_email = Entry(self._pan_main)
        self._lbl_cell_phone = Label(self._pan_main, text='Cell phone:')
        self._txt_cell_phone = Entry(self._pan_main)
        self._lbl_zip_code = Label(self._pan_main, text='Zip code:')
        self._txt_zip_code = Entry(self._pan_main)
        self._lbl_street = Label(self._pan_main, text='Street:')
        self._txt_street = Entry(self._pan_main)
        self._lbl_neighborhood = Label(self._pan_main, text='Neighborhood:')
        self._txt_neighborhood = Entry(self._pan_main)
        self._lbl_city = Label(self._pan_main, text='City:')
        self._txt_city = Entry(self._pan_main)
        self._lbl_state = Label(self._pan_main, text='State:')
        self._txt_state = Entry(self._pan_main)
        self._btn_search_zip_code = Button(self.root, text='Search zip code')
        self._btn_save = Button(self.root, text='Save')
        self._btn_exit = Button(self.root, text='Exit')

        # load setup window
        self.window_setup()
        self._state_fields(state='disabled')

    def window_setup(self):
        # settings container _pan_main
        self._pan_main['bd'] = 2
        self._pan_main['bg'] = 'lightgrey'
        self._pan_main.pack(pady=20, padx=20, fill="both", expand=True)

        # settings widgets label _lbl_name
        self._lbl_name.place(x=10, y=10)
        self._lbl_name['width'] = 16
        self._lbl_name['height'] = 2
        self._lbl_name['font'] = ("Verdana", 10)

        # settings widgets entry _txt_name
        self._txt_name.place(x=160, y=10)
        self._txt_name['width'] = 30
        self._txt_name['font'] = ("Verdana", 19)

        # settings widgets label _lbl_email
        self._lbl_email.place(x=10, y=60)
        self._lbl_email['width'] = 16
        self._lbl_email['height'] = 2
        self._lbl_email['font'] = ("Verdana", 10)

        # settings widgets entry _txt_email
        self._txt_email.place(x=160, y=60)
        self._txt_email['width'] = 30
        self._txt_email['font'] = ("Verdana", 19)

        # settings widgets label _lbl_cell_phone
        self._lbl_cell_phone.place(x=10, y=110)
        self._lbl_cell_phone['width'] = 16
        self._lbl_cell_phone['height'] = 2
        self._lbl_cell_phone['font'] = ("Verdana", 10)

        # settings widgets entry _txt_cell_phone
        self._txt_cell_phone.place(x=160, y=110)
        self._txt_cell_phone['width'] = 16
        self._txt_cell_phone['font'] = ("Verdana", 19)

        # settings widgets label _lbl_zip_code
        self._lbl_zip_code.place(x=10, y=160)
        self._lbl_zip_code['width'] = 16
        self._lbl_zip_code['height'] = 2
        self._lbl_zip_code['font'] = ("Verdana", 10)

        # settings widgets entry _txt_zip_code
        self._txt_zip_code.place(x=160, y=160)
        self._txt_zip_code['width'] = 16
        self._txt_zip_code['font'] = ("Verdana", 19)

        # settings widgets button _btn_search_zip_code
        self._btn_search_zip_code.place(x=460, y=180)
        self._btn_search_zip_code['width'] = 16
        self._btn_search_zip_code['height'] = 2
        self._btn_search_zip_code['command'] = self._command_search_zip_code

        # settings widgets label _lbl_street
        self._lbl_street.place(x=10, y=210)
        self._lbl_street['width'] = 16
        self._lbl_street['height'] = 2
        self._lbl_street['font'] = ("Verdana", 10)

        # settings widgets entry _txt_street
        self._txt_street.place(x=160, y=210)
        self._txt_street['width'] = 30
        self._txt_street['font'] = ("Verdana", 19)

        # settings widgets label _lbl_neighborhood
        self._lbl_neighborhood.place(x=10, y=260)
        self._lbl_neighborhood['width'] = 16
        self._lbl_neighborhood['height'] = 2
        self._lbl_neighborhood['font'] = ("Verdana", 10)

        # settings widgets entry _txt_neighborhood
        self._txt_neighborhood.place(x=160, y=260)
        self._txt_neighborhood['width'] = 30
        self._txt_neighborhood['font'] = ("Verdana", 19)

        # settings widgets label _lbl_city
        self._lbl_city.place(x=10, y=310)
        self._lbl_city['width'] = 16
        self._lbl_city['height'] = 2
        self._lbl_city['font'] = ("Verdana", 10)

        # settings widgets entry _txt_city
        self._txt_city.place(x=160, y=310)
        self._txt_city['width'] = 30
        self._txt_city['font'] = ("Verdana", 19)

        # settings widgets label _lbl_state
        self._lbl_state.place(x=10, y=360)
        self._lbl_state['width'] = 16
        self._lbl_state['height'] = 2
        self._lbl_state['font'] = ("Verdana", 10)

        # settings widgets entry _txt_state
        self._txt_state.place(x=160, y=360)
        self._txt_state['width'] = 30
        self._txt_state['font'] = ("Verdana", 19)

        # setting buttons
        self._btn_save.place(x=400, y=520)
        self._btn_save['width'] = 16
        self._btn_save['height'] = 2
        self._btn_save['command'] = self._command_save

        self._btn_exit.place(x=540, y=520)
        self._btn_exit['width'] = 16
        self._btn_exit['height'] = 2
        self._btn_exit["command"] = self.root.quit

    def _state_fields(self, state):
        self._txt_street.config(state=state)
        self._txt_neighborhood.config(state=state)
        self._txt_city.config(state=state)
        self._txt_state.config(state=state)

    def _command_search_zip_code(self):
        _zip_code_value = self._txt_zip_code.get()

        if _zip_code_value or len(_zip_code_value) == 8:
            data = AgendaActions.get_zip_code(zip_code=_zip_code_value)
            self._state_fields('normal')
            if data:
                self._txt_street.insert(0, data.get('logradouro'))
                self._txt_neighborhood.insert(0, data.get('bairro'))
                self._txt_city.insert(0, data.get('localidade'))
                self._txt_state.insert(0, data.get('estado'))
            else:
                showinfo("Info", "Zip code not found!")
        else:
            showinfo("Info", "The zip code field is empty!")

    def _command_save(self):
        contact = Contact()
        contact.name = self._txt_name.get()
        contact.email = self._txt_email.get()
        contact.cell_phone = self._txt_cell_phone.get()
        contact.zip_code = self._txt_zip_code.get()
        contact.street = self._txt_street.get()
        contact.neighborhood = self._txt_neighborhood.get()
        contact.city = self._txt_city.get()
        contact.state = self._txt_state.get()

        result = AgendaActions.save_contact(contact=contact)

        showinfo("Info", result)
        self.root.quit()

    def _load_contact(self):
        self._state_fields(state='normal')
        self._txt_name.insert(0, self._contact.name)
        self._txt_email.insert(0, self._contact.email)
        self._txt_cell_phone.insert(0, self._contact.cell_phone)
        self._txt_zip_code.insert(0, self._contact.zip_code)
        self._txt_street.insert(0, self._contact.street)
        self._txt_neighborhood.insert(0, self._contact.neighborhood)
        self._txt_city.insert(0, self._contact.city)
        self._txt_state.insert(0, self._contact.state)

    def run_view(self):
        if self._contact:
            self._load_contact()
        super().run_view()

class AgendaContactListView(BaseView):

    def __init__(self):
        super().__init__(title='Agenda - List contacts', width=700, height=600)
        self._tree_table = Treeview(self.root)
        self._columns = ('id', 'name', 'email', 'cell_phone', 'zip_code', 'street', 'neighborhood', 'city', 'state')

        self.window_setup()
        self._list_contacts()

    def window_setup(self):
        self._tree_table['columns'] = self._columns

        self._tree_table.heading('id', text='ID')
        self._tree_table.heading('name', text='Name')
        self._tree_table.heading('email', text='Email')
        self._tree_table.heading('cell_phone', text='Cell phone')
        self._tree_table.heading('zip_code', text='Zip code')
        self._tree_table.heading('street', text='Street')
        self._tree_table.heading('neighborhood', text='Neighborhood')
        self._tree_table.heading('city', text='City')
        self._tree_table.heading('state', text='State')

        self._tree_table.column('id', width=5)
        self._tree_table.column('name', width=50)
        self._tree_table.column('email', width=50)
        self._tree_table.column('cell_phone', width=20)
        self._tree_table.column('zip_code', width=20)
        self._tree_table.column('street', width=40)
        self._tree_table.column('neighborhood', width=30)
        self._tree_table.column('city', width=30)
        self._tree_table.column('state', width=30)

        self._tree_table.bind('<ButtonRelease-1>', self._command_get_selected_item)

        self._tree_table['show'] = 'headings'
        self._tree_table.pack(expand=True, fill='both')

    def _list_contacts(self):
        data = AgendaActions.list_contacts()
        for item in data:
            self._tree_table.insert('', 'end', values=(
                item.id,
                item.name,
                item.email,
                item.cell_phone,
                item.zip_code,
                item.street,
                item.neighborhood,
                item.city,
                item.state
            ))
            self._tree_table.pack(pady=10, padx=10)

    def _command_get_selected_item(self, event):
        item = self._tree_table.selection()[0]
        print(item)
        values = self._tree_table.item(item, 'values')
        print(values)

        item_dict = dict(zip(self._columns, values))
        print(item_dict)
        contact = SimpleNamespace(**item_dict)

        agendaNewContactView = AgendaNewContactView(contact=contact)
        agendaNewContactView.run_view()

        