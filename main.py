"""Run a deterministic demo: three DVDs cost 63.89 dollars."""
from aims.dvd import DigitalVideoDisc
from aims.cart import Cart


def main():
    cart = Cart()
    for dvd in [
        DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 88, 19.95),
        DigitalVideoDisc("Spirited Away", "Animation", "Hayao Miyazaki", 125, 24.99),
        DigitalVideoDisc("Arrival", "Science fiction", "Denis Villeneuve", 116, 18.95),
    ]:
        cart.add_digital_video_disc(dvd)
    cart.print_cart()


if __name__ == "__main__":
    main()
