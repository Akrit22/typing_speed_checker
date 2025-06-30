import time
import random
import threading


def typing_test():
    sen = [
        "The quick brown fox jumps over the lazy dog",
        "A journey of a thousand miles begins with a single step",
        "Practice makes perfect in all things you do",
        "The sun sets slowly behind the mountain",
        "A clear sky on a warm summer day",
        "Stars twinkle brightly in the night sky",
        "The river flows gently through the valley",
        "Birds chirp happily in the early morning",
        "A warm breeze rustles the autumn leaves",
        "The moon casts a silver glow over the lake",
        "Children play joyfully in the green meadow",
        "The old oak tree stands tall and strong",
        "Waves crash softly against the sandy shore",
        "A quiet village rests at the foot of the hill",
        "The smell of fresh bread fills the kitchen",
        "Clouds drift lazily across the blue sky",
        "The wind whispers secrets to the ancient trees",
        "A cozy fireplace warms the small cabin",
        "The bright flowers bloom in the garden",
        "A lone wolf howls under the starry night",
        "The golden fields sway in the warm breeze",
        "A gentle rain taps on the windowpane",
        "Morning dew glistens on the green grass",
        "The baker kneads dough with practiced hands",
        "Sunlight dances on the rippling lake surface",
        "Thunder rumbles through the evening sky",
        "The cat stretches lazily on the windowsill",
        "Campfire smoke curls into the cool air",
        "The waterfall thunders down the rocky cliff",
        "Soft snow blankets the quiet countryside",
        "The owl hoots in the stillness of night",
        "The tent flaps in the mountain wind",
        "The sky turns pink at the break of dawn",
        "The clock ticks loudly in the empty room",
        "Raindrops race down the glass like tears",
        "The child laughs as the kite takes flight",
        "The candle flickers in the dark hallway",
        "The wind scatters petals across the path",
        "The engine hums softly on the quiet road",
        "Sunbeams warm the sleepy forest floor",
        "The fog rolls in over the harbor",
        "The squirrel darts across the garden fence",
        "The plane cuts through clouds in the sky",
        "The horse gallops across the open field",
        "The dancer spins gracefully on the stage",
        "The treehouse creaks in the summer breeze",
        "The librarian sorts books in silent rows",
        "The cafe buzzes with morning chatter",
        "The stars shimmer above the desert sands",
        "The artist dips the brush into bright paint",
        "Leaves swirl in circles on the pavement",
        "The breeze carries laughter across the park",
        "The mountain trail leads to a hidden waterfall",
        "The city lights sparkle like distant stars",
        "A soft melody plays in the quiet room",
        "Leaves crunch beneath your feet in the fall",
        "Raindrops create ripples in the puddles",
        "The fireflies dance in the dark summer night",
        "Snowflakes land softly on the window ledge",
        "The lighthouse guides ships through thick fog",
        "Footprints vanish slowly in the shifting sand",
        "Lanterns glow warmly during the evening festival",
        "The kitten purrs while curled on the couch",
        "Books lined neatly on the dusty old shelf",
        "Freshly brewed coffee fills the morning air",
        "The hiker reaches the summit with joy",
        "Ocean waves sing a lullaby to the shore",
        "The painter captures sunsets on canvas",
        "Golden rays peek through the tall trees",
        "Wind chimes sing with the passing breeze",
        "The puppy chases butterflies in the yard",
        "Footsteps echo in the quiet hallway",
        "The lantern flickers in the silent night",
        "A feather floats gently to the ground",
        "The violinist plays a haunting tune"
    ]  # list sen is the list of different sentences

    sel = random.sample(sen, 10)  # random.sample is use for no repitition at a time

    print("\n Type the following 10 sentences exactly, and repeat as many times as you can in 1 minute.\n")
    for i, sentence in enumerate(sel, 1):
        print(f"{i}. {sentence}")

    print("******************************************")
    print("\nPress Enter when you're ready to start...")
    input()

    # Combine all selected sentences
    full_text = " ".join(sel)
    target_words = full_text.split()  # the words selected randomly using random.sample is stored in target_words

    # User input storage
    user_input = []
    stop_typing = False

    def timer():
        nonlocal stop_typing
        time.sleep(60)
        stop_typing = True

    # Start timer in different space
    threading.Thread(target=timer).start()

    print("\n**************Start typing now (1 minute):\n")
    while not stop_typing:
        try:
            line = input()
            user_input.append(line)
        except EOFError:
            break

    # Combine and process user input
    typed_text = " ".join(user_input)
    typed_words = typed_text.split()

    if not typed_words:
        print("******************************************")
        print("\n********* Time's up! You didn't type anything.\n********bye bye*******")
        return

    # Accuracy calculation
    correct_words = 0
    for i in range(min(len(typed_words), len(target_words))):
        if typed_words[i] == target_words[i]:
            correct_words += 1

    total_typed = len(typed_words)
    wpm = correct_words  # Since 1 minute
    accuracy = (correct_words / total_typed) * 100 if total_typed else 0

    print("******************************************")
    print("\n************************** Results:")
    print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Words Typed: {total_typed}")
    print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Correct Words: {correct_words}")
    print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Words Per Minute (WPM): {wpm:.2f}")
    print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Accuracy: {accuracy:.2f}%")


def main():
    print("\t\t\t\t******************************************")
    print("\t\t\t\t******************************************")
    print("\t\t\t\t\t\tHELLO TYPER")
    print("\t\t\t\t\tWelcome to the Typing Speed Test!")
    print("\t\t\t\t******************************************")
    print("\t\t\t\t******************************************")
    while True:
        typing_test()
        print("******************************************")
        print("******************************************")
        choice = input("\nDo you want to try again? (yes/no): ").lower()
        if choice != 'yes':
            print(
                "\nThank you for using the Typing Speed Checker. \n***********bye bye**********\n____________________________________!")
            break


if __name__ == "__main__":
    main()
