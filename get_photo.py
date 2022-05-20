
from parsing import Parser

def main():
    par = Parser()
    images = par.get_images(key_word="Funny Cats")
    imagess = par.get_images(key_word="Funny Dogs")

    del images
    del imagess

if __name__ == '__main__':
    main()