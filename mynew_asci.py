import os

# Color codes for console
GREEN = '\033[92m'
YELLOW = '\033[93m'
WHITE = '\033[97m'
RESET = '\033[0m'

# Dimensions
CHAR_WIDTH = 12
CHAR_HEIGHT = 10
SPACING = "  "

# Reorganized ASCII data: dictionary mapping character to its 10 rows
ASCII_ART_DICT = {
    'A': ["     A     ", "    A A    ", "   A   A   ", "  AAAAAAA  ", "  A     A  ", " A       A ", " A       A ", "           ", "           ", "           "],
    'B': [" BBBBBB   ", " B     B  ", " B     B  ", " BBBBBB   ", " B     B  ", " B     B  ", " BBBBBB   ", "          ", "          ", "          "],
    'C': ["  CCCCC  ", " C     C ", " C       ", " C       ", " C       ", " C     C ", "  CCCCC  ", "         ", "         ", "         "],
    'D': [" DDDDD   ", " D    D  ", " D     D ", " D     D ", " D     D ", " D    D  ", " DDDDD   ", "         ", "         ", "         "],
    'E': [" EEEEEEE ", " E       ", " E       ", " EEEEEE  ", " E       ", " E       ", " EEEEEEE ", "         ", "         ", "         "],
    'F': [" FFFFFFF ", " F       ", " F       ", " FFFFFF  ", " F       ", " F       ", " F       ", "         ", "         ", "         "],
    'G': ["  GGGGG  ", " G     G ", " G       ", " G  GGG  ", " G     G ", " G     G ", "  GGGGG  ", "         ", "         ", "         "],
    'H': [" H     H ", " H     H ", " H     H ", " HHHHHHH ", " H     H ", " H     H ", " H     H ", "         ", "         ", "         "],
    'I': [" IIIIIII ", "    I    ", "    I    ", "    I    ", "    I    ", "    I    ", " IIIIIII ", "         ", "         ", "         "],
    'J': [" JJJJJJJ ", "      J  ", "      J  ", "      J  ", "      J  ", " J    J  ", "  JJJJ   ", "         ", "         ", "         "],
    'K': [" K    K  ", " K   K   ", " K  K    ", " KKK     ", " K  K    ", " K   K   ", " K    K  ", "         ", "         ", "         "],
    'L': [" L       ", " L       ", " L       ", " L       ", " L       ", " L       ", " LLLLLLL ", "         ", "         ", "         "],
    'M': [" M     M ", " MM   MM ", " M M M M ", " M  M  M ", " M     M ", " M     M ", " M     M ", "         ", "         ", "         "],
    'N': [" N     N ", " NN    N ", " N N   N ", " N  N  N ", " N   N N ", " N    NN ", " N     N ", "         ", "         ", "         "],
    'O': ["  OOOO  ", " O    O ", " O    O ", " O    O ", " O    O ", " O    O ", "  OOOO  ", "         ", "         ", "         "],
    'P': [" PPPPPP  ", " P     P ", " P     P ", " PPPPPP  ", " P       ", " P       ", " P       ", "         ", "         ", "         "],
    'Q': ["  QQQQ  ", " Q    Q ", " Q    Q ", " Q    Q ", " Q  Q Q ", " Q   Q  ", "  QQQ Q ", "         ", "         ", "         "],
    'R': [" RRRRRR  ", " R     R ", " R     R ", " RRRRRR  ", " R   R   ", " R    R  ", " R     R ", "         ", "         ", "         "],
    'S': ["  SSSSS ", " S     S", " S      ", "  SSSSS ", "       S", " S     S", "  SSSSS ", "        ", "        ", "        "],
    'T': [" TTTTTTT ", "    T    ", "    T    ", "    T    ", "    T    ", "    T    ", "    T    ", "         ", "         ", "         "],
    'U': [" U     U ", " U     U ", " U     U ", " U     U ", " U     U ", " U     U ", "  UUUUU  ", "         ", "         ", "         "],
    'V': [" V     V ", " V     V ", " V     V ", "  V   V  ", "   V V   ", "    V    ", "         ", "         ", "         ", "         "],
    'W': [" W     W ", " W     W ", " W  W  W ", " W  W  W ", " W W W W ", " W W W W ", "  W   W  ", "         ", "         ", "         "],
    'X': [" X     X ", "  X   X  ", "   X X   ", "    X    ", "   X X   ", "  X   X  ", " X     X ", "         ", "         ", "         "],
    'Y': [" Y     Y ", "  Y   Y  ", "   Y Y   ", "    Y    ", "    Y    ", "    Y    ", "    Y    ", "         ", "         ", "         "],
    'Z': [" ZZZZZZZ ", "      Z  ", "     Z   ", "    Z    ", "   Z     ", "  Z      ", " ZZZZZZZ ", "         ", "         ", "         "],
    'a': ["         ", "         ", "  aaaa   ", " a    a  ", " a    a  ", " a    a  ", "  aaaa   ", "         ", "         ", "         "],
    'b': [" b       ", " b       ", " bbbbb   ", " b    b  ", " b    b  ", " b    b  ", " bbbbb   ", "         ", "         ", "         "],
    'c': ["         ", "         ", "  cccc   ", " c       ", " c       ", " c       ", "  cccc   ", "         ", "         ", "         "],
    'd': ["       d ", "       d ", " ddddd   ", " d    d  ", " d    d  ", " d    d  ", " ddddd   ", "         ", "         ", "         "],
    'e': ["         ", "         ", "  eeee   ", " e    e  ", " eeeee   ", " e       ", "  eeee   ", "         ", "         ", "         "],
    'f': ["   fff   ", "  f      ", " fffff   ", "  f      ", "  f      ", "  f      ", "  f      ", "         ", "         ", "         "],
    'g': ["         ", " ggggg   ", " g    g  ", " g    g  ", " ggggg   ", "      g  ", " gggg    ", "         ", "         ", "         "],
    'h': [" h       ", " h       ", " hhhh    ", " h    h  ", " h    h  ", " h    h  ", " h    h  ", "         ", "         ", "         "],
    'i': ["    i    ", "         ", "    i    ", "    i    ", "    i    ", "    i    ", "   iii   ", "         ", "         ", "         "],
    'j': ["       j ", "         ", "       j ", "       j ", "       j ", " j    j  ", "  jjj    ", "         ", "         ", "         "],
    'k': [" k       ", " k       ", " k   k   ", " k  k    ", " kkk     ", " k  k    ", " k   k   ", "         ", "         ", "         "],
    'l': ["    l    ", "    l    ", "    l    ", "    l    ", "    l    ", "    l    ", "   ll    ", "         ", "         ", "         "],
    'm': ["         ", "         ", " mmm  m  ", " m m m m ", " m m m m ", " m m m m ", " m m m m ", "         ", "         ", "         "],
    'n': ["         ", "         ", " nnnn    ", " n    n  ", " n    n  ", " n    n  ", " n    n  ", "         ", "         ", "         "],
    'o': ["         ", "         ", "  oooo   ", " o    o  ", " o    o  ", " o    o  ", "  oooo   ", "         ", "         ", "         "],
    'p': ["         ", " pppp    ", " p    p  ", " p    p  ", " pppp    ", " p       ", " p       ", "         ", "         ", "         "],
    'q': ["         ", " qqqqq   ", " q    q  ", " q    q  ", " qqqqq   ", "      q  ", "      q  ", "         ", "         ", "         "],
    'r': ["         ", "         ", " rrr     ", " r   r   ", " r       ", " r       ", " r       ", "         ", "         ", "         "],
    's': ["         ", "         ", "  ssss   ", " s       ", "  sss    ", "      s  ", " sssss   ", "         ", "         ", "         "],
    't': ["    t    ", "    t    ", " ttttt   ", "    t    ", "    t    ", "    t    ", "     t   ", "         ", "         ", "         "],
    'u': ["         ", "         ", " u    u  ", " u    u  ", " u    u  ", " u    u  ", "  uuuu   ", "         ", "         ", "         "],
    'v': ["         ", "         ", " v     v ", "  v   v  ", "  v   v  ", "   v v   ", "    v    ", "         ", "         ", "         "],
    'w': ["         ", "         ", " w  w  w ", " w  w  w ", " w w w w ", "  w w w  ", "   w     ", "         ", "         ", "         "],
    'x': ["         ", "         ", " x    x  ", "  x  x   ", "   xx    ", "  x  x   ", " x    x  ", "         ", "         ", "         "],
    'y': ["         ", " y    y  ", " y    y  ", "  y  y   ", "   yy    ", "    y    ", " y       ", "         ", "         ", "         "],
    'z': ["         ", "         ", " zzzzzz  ", "     z   ", "    z    ", "   z     ", " zzzzzz  ", "         ", "         ", "         "],
    '0': ["  0000  ", " 0    0 ", "0      0", "0      0", "0      0", "0      0", " 0    0 ", "  0000  ", "         ", "         "],
    '1': ["    1   ", "   11   ", "  1 1   ", "    1   ", "    1   ", "    1   ", "  11111 ", "         ", "         ", "         "],
    '2': [" 22222  ", "     2  ", "     2  ", " 22222  ", " 2      ", " 2      ", " 22222  ", "         ", "         ", "         "],
    '3': [" 33333  ", "     3  ", "     3  ", "  3333  ", "     3  ", "     3  ", " 33333  ", "         ", "         ", "         "],
    '4': [" 4   4  ", " 4   4  ", " 4   4  ", " 44444  ", "     4  ", "     4  ", "     4  ", "         ", "         ", "         "],
    '5': [" 55555  ", " 5      ", " 5      ", " 55555  ", "     5  ", "     5  ", " 55555  ", "         ", "         ", "         "],
    '6': ["  6666  ", " 6      ", " 6      ", " 66666  ", " 6    6 ", " 6    6 ", "  6666  ", "         ", "         ", "         "],
    '7': [" 77777  ", "     7  ", "    7   ", "   7    ", "  7     ", " 7      ", " 7      ", "         ", "         ", "         "],
    '8': ["  8888  ", " 8    8 ", " 8    8 ", "  8888  ", " 8    8 ", " 8    8 ", "  8888  ", "         ", "         ", "         "],
    '9': ["  9999  ", " 9    9 ", " 9    9 ", "  99999 ", "      9 ", "      9 ", "  9999  ", "         ", "         ", "         "]
}

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title():
    print(f"{GREEN}ASCII{YELLOW} ART {WHITE}GENERATOR{RESET}")
    print("=" * 30)

def get_menu_choice():
    print("\n--- Select Your choice ---")
    print("1. Mix of uppercase, lowercase, numbers!")
    print("2. Single Character Display!")
    print("3. Exit")
    return input("\nEnter your choice (1-3): ").strip()

def render_text(text):
    """Renders multi-character text using the dictionary, replacing unsupported with spaces."""
    print()
    for row in range(CHAR_HEIGHT):
        row_line = []
        for ch in text:
            row_line.append(ASCII_ART_DICT.get(ch, [" " * CHAR_WIDTH] * CHAR_HEIGHT)[row])
        print(SPACING.join(row_line))

def handle_general():
    text = input("\nEnter your name (A-Z, a-z, 0-9 allowed): ")
    # Replace unsupported characters with space (visually like blank)
    processed = ''.join([c if c in ASCII_ART_DICT else ' ' for c in text])
    render_text(processed)

def handle_single():
    char = input("\nEnter a single character (A-Z, a-z, 0-9): ").strip()
    if len(char) != 1:
        print("Please enter only one character!")
        return
    if char in ASCII_ART_DICT:
        render_text(char)
    else:
        print(f"Character '{char}' not supported!")


# Main program loop
while True:
    clear_console()
    print_title()
    choice = get_menu_choice()

    if choice == '1':
        handle_general()
    elif choice == '2':
        handle_single()
    elif choice == '3':
        print("\nThanks for using ASCII Art Generator!")
        break
    else:
        print("Invalid choice! Please select 1-3.")

    if choice in ['1', '2', '3']:
        if input("\nDo you want to continue? (y/n): ").strip().lower() != 'y':
            break
