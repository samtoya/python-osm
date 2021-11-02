from parrot import Parrot

if __name__ == '__main__':
    try:
        p = Parrot()
        p.chirp()
    except KeyboardInterrupt:
        print('You cancelled the operation')
