from gui import GUI
from parrot import Parrot

if __name__ == '__main__':
    try:
        # ui = GUI()
        # ui.open_window()
        p = Parrot()
        p.chirp()
    except KeyboardInterrupt:
        print('You cancelled the operation')
