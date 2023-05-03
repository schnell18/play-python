import cowsay
import sys

from sayings import hello

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])
    cowsay.trex("Hello, " + sys.argv[1])
    cowsay.turkey("Hello, " + sys.argv[1])
    cowsay.turtle("Hello, " + sys.argv[1])
    cowsay.tux("Hello, " + sys.argv[1])
    cowsay.beavis("Hello, " + sys.argv[1])
    cowsay.cheese("Hello, " + sys.argv[1])
    cowsay.daemon("Hello, " + sys.argv[1])
    cowsay.dragon("Hello, " + sys.argv[1])
    cowsay.fox("Hello, " + sys.argv[1])
    cowsay.ghostbusters("Hello, " + sys.argv[1])
    cowsay.kitty("Hello, " + sys.argv[1])
    cowsay.meow("Hello, " + sys.argv[1])
    cowsay.miki("Hello, " + sys.argv[1])
    cowsay.milk("Hello, " + sys.argv[1])
    cowsay.pig("Hello, " + sys.argv[1])
    cowsay.stegosaurus("Hello, " + sys.argv[1])
    cowsay.stimpy("Hello, " + sys.argv[1])
    hello("Hello, " + sys.argv[1])
