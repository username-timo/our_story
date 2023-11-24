def collaborative_storytelling():
    print("Welcome to the Collaborative Storytelling Game!")
    print(
        "Start the story with a sentence. Each person will add a sentence to continue the story."
    )

    story = []
    add_more = True

    while add_more:
        new_sentence = input("Add a sentence to the story: ")
        story.append(new_sentence)

        print("\nHere's the story so far:")
        for sentence in story:
            print(sentence, end=" ")

        print("\n\nDo you want to add more? (yes/no)")
        if input().lower() != "yes":
            add_more = False

    print("\nFinal story:")
    for sentence in story:
        print(sentence, end=" ")


collaborative_storytelling()
