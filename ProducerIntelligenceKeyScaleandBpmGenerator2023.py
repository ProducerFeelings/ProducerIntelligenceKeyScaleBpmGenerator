import random
import tkinter as tk
import webbrowser

root = tk.Tk()
root.title("Producer Intelligence")
root.configure(bg='black')

# Allow for Instagram add
def open_instagram():
    webbrowser.open("https://www.instagram.com/producerintelligence//")

instagram_label = tk.Label(root, text="Follow us on Instagram!", fg="blue", cursor="hand2")
instagram_label.grid(row=0, column=2, padx=10, pady=10, sticky="e")
instagram_label.bind("<Button-1>", lambda e: open_instagram())

# Define the text strings to be displayed
intro_text = "Hello, Welcome to Producer Intelligence! This section of Producing Intelligence gives\n" \
             "you the key, bpm, and scale for the latest subgenres of\n" \
             "trap beats/instrumentals. We welcome you today to this portion.\n" \
             "Please scroll down below to begin!"
genre_text = "The following subgenres of trap are present:\n" \
             "pain, supertrap, drill, sampled drill, uk drill,\nchicago drill," \
             "afro drill, ny drill, hyperpop, plugnb,\nrage, cloudrap, emo trap, westcoast," \
             "detroit, glo,\ncrunk, " \
             "detroit, old school!"

# Define the label widgets
title_label = tk.Label(root, text="Producer Intelligence's Key Scale and Bpm Generator", font=("Arial", 20, "bold"), fg='white', bg='purple',)
title_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")  # Use sticky="w" to align to the left
intro_label = tk.Label(root, text=intro_text, justify="center", font=("Arial", 14), fg='black', bg='purple')
genre_label = tk.Label(root, text=genre_text, justify="center", font=("Arial", 12), fg='black', bg='purple')
input_label = tk.Label(root, text="Select the name of the subgenre of trap you would like to make today!: ",
                       font=("Arial", 12), fg='black', bg='purple')
drill_label = tk.Label(root, text="What type of drill beat do you want to make today from the selection above!: ",
                       font=("Arial", 12), fg='black', bg='purple')

# Define the entry widget
input_entry = tk.Entry(root, font=("Arial", 12), fg='black', bg='pink')

# Define the function to be called when the button is pressed
def generate_info():
    selection = input_entry.get().lower().replace(" ", "")
    subgenres = {
        "pain": {"bpm": ['120', '145', '149', '150', '178'],
                 "keyscales": ['Ab Minor', 'F Major', '#FMinor', 'C#Major', 'D Major']},
        "supertrap": {"bpm": ['121', '124', '126', '142', '150'],
                      "keyscales": ['A Major', 'B Major', 'C Major', 'D Major', 'G Major']},
        "drill": {"bpm": ['140', '143', '145', '166'], "keyscales": ['Ab Major', 'B Major', 'C Major', 'D Major']},
        "sampleddrill": {"bpm": ['140', '143', '144', '145', '150'],
                         "keyscales": ['Bb Minor', 'D Major', 'C# Major', 'F#Gb']},

        "afrodrill": {"bpm": ['140', '143', '145', '166'], "keyscales": ['Ab Major', 'B Major', 'C Major', 'D Major']},
        "melodicdrill": {"bpm": ['142', '143', '144', '140', '145'],
                         "keyscales": ['F# Major', 'G Major', 'Ab Major', 'Eb Major', 'D Minor']},
        "chicagodrill": {
            "bpm": ['120', '121', '125', '126', '130', '132', '136', '138', '140', '141', '140', '164', '134', '120',
                    '130', '132', '157', '124', '141'],
            "keyscales": ['E Minor', 'F# Minor', 'F Minor', 'D Major', 'A Minor', 'B Major', 'C# Major',
                          'G#Ab Major', 'E Minor', 'F# Minor', 'F Minor', 'D Major', 'A Minor', 'B Major',
                          'C# Major', 'G#Ab Major']},
        "hyperpop": {"bpm": ['141', '146', '139', '147', '149', '143', '136', '160'],
                     "keyscales": ['C Minor', 'Db Major', 'B Major', 'C# Minor', 'F Minor', 'G Major',
                                   'C# Major', 'E Minor']},
        "plugnb": {"bpm": ['149', '150', '142', '138', '130', '117', '145', '141', '81', '146'],
                   "keyscales": ['F Minor', 'C Major', 'F#/Gb Minor', 'C# Major', 'B Minor', 'G Minor', 'G Major',
                                 'F#']},
        "rage": {"bpm": ['77', '140', '76', '118', '117', '139', '147', '138', '142', '80', '144', '150'],
                 "keyscales": ['E Minor', 'Ab Minor', 'C# Major', 'G#/Ab Major', 'C#/Db Major', 'C# Major',
                               'C#/Db Major', 'C# Major', 'F#/Gb Major', 'F# Minor', 'Bb Minor', 'D Major',
                               'Ab Major']},
        "cloudrap": {"bpm": ['122', '124', '135', '150', '158', '115', '120', '145', '140', '135', '93', '78', '140'],
                     "keyscales": ['C Minor', 'Db Major', 'Ab Major', 'E Major', 'Ab Major', 'Ab Major',
                                   'C# Major', 'D Major',
                                   'G#/Ab Major']},
        "emotrap": {"bpm": ['93', '134', '77', '74', '115', '135', '119', '80', '93', '120'],
                    "keyscales": ['G Major', 'C Minor', 'C# Major', 'F# Major', 'C# Major', 'F#/Gb Major',
                                  'A Minor', 'D Major', 'C Major', 'E Minor']},
        "westcoast": {
            "bpm": ['104', '99', '98', '94', '95', '141', '90', '97', '98', '82', '94', '107', '96', '102', '98', ],
            "keyscales": ['C# Major', 'C Minor', 'A Major', 'A Minor', 'G Minor', 'B Minor', 'Bb Major', ]},
        "ukdrill": {"bpm": ['140', '144', '145', '143', ],
                    "keyscales": ['A Major', 'C# Major', 'C#Db Major', 'D#/Eb Major', 'F#/Gb Minor']},
        "oldschool": {"bpm": ['95', '103', '112', '91', '122', '87', '84', '94', '92', '116'],
                      "keyscales": ["A Minor", "G Major", "C#/Db Major", "F#Minor", "Bb Minor", "B Minor",
                                    "A Minor", "C# Major", "D Major"]},

        "crunk": {"bpm": ['77', '140', '101', '84', '160', '102', '144', '76', '88', '144', '75', '93', '142'],
                  "keyscales": ['G Minor', 'C Major', 'B Minor', 'C#/Db Minor', 'C# Minor', 'B Minor', 'E Minor',
                                'F# Major',
                                'B Minor', 'C# Major', 'C Minor', 'G Major', 'D Major', 'B Major', 'C# Minor']},
        "detroit": {"bpm": ['131', '98', '83', '99', '117', '92', '99', '131', '86', '120'],
                    "keyscales": ['D Major', 'Bb Minor', 'B Major', 'C# Minor', 'C# Major', 'F Major',
                                  'G#/Ab Major', 'G Major', 'B Major']},
        "glo": {"bpm": ['122', '132', '142', '153', '77', '144', '133', '140', '130', '134', '91', '136', '155', '65',
                        '140', '137', '128', '145', '150', '75'],
                "keyscales": ['F Minor', 'B Minor', 'C# Major', 'D Major', 'B Major']},
        "nydrill": {"bpm": ['140', '144', '145', '143', ],
                    "keyscales": ['A Major', 'C# Major', 'C#Db Major', 'D#/Eb Major', 'F#/Gb Minor']},

    }
    if selection in subgenres:
        genre_info = subgenres[selection]
        random_bpm = random.choice(genre_info["bpm"])
        random_key_scale = random.choice(genre_info["keyscales"])
        output_text = f"Here is a random key, scale, and bpm for your next  {selection} beat : {random_key_scale} {random_bpm} bpm"
        output_label.config(text=output_text)
    elif selection == "drill":
        output_text = f"Here is a random key, scale, and bpm for your next  {selection} beat : {random_key_scale} {random_bpm} bpm"
        drill_label.config(text=output_text)
        genre_info = subgenres[selection]
        random_bpm = random.choice(genre_info["bpm"])
        random_key_scale = random.choice(genre_info["keyscales"])
    else:
        output_label.config(text="Invalid selection. Please choose one of the following subgenres:\n" + genre_text)


# Define the button widget
submit_button = tk.Button(root, text="Submit", command=generate_info)

# Define the output label widget
output_label = tk.Label(root, text="", font=("Arial", 12))

# Arrange the widgets using the grid geometry manager

genre_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
input_label.grid(row=2, column=0, padx=10, pady=10)
input_entry.grid(row=2, column=1, padx=10, pady=10)
submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
output_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
