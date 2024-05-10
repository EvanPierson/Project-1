from gui import *


def main():
    window = tk()
    window.title('TV Remote')
    window.geometry('200x400')
    window.resizable(False, False)
    GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
