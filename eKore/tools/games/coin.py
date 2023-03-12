import random
import tkinter as tk
import os
from PIL import Image, ImageTk

def main():
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'output'))

    window = tk.Tk()
    window.geometry("350x450")
    window.title("Coin Flipper")
    window.configure(bg='#333333')

    edge_count = 0
    head_count = 0
    tail_count = 0
    total_flips = 0
    auto_flipping = False

    heads_gif = Image.open(file_path + "\\headsRS.gif")
    tails_gif = Image.open(file_path + "\\tailsRS.gif")

    heads_gif_frames = []
    for i in range(heads_gif.n_frames):
        heads_gif.seek(i)
        img = ImageTk.PhotoImage(heads_gif.copy())
        heads_gif_frames.append(img)

    tails_gif_frames = []
    for i in range(tails_gif.n_frames):
        tails_gif.seek(i)
        img = ImageTk.PhotoImage(tails_gif.copy())
        tails_gif_frames.append(img)

    result_label = tk.Label(text="")

    total_label = tk.Label(text=f"Total: {total_flips} | Heads flipped: {head_count} | Tails flipped: {tail_count} | Edges flipped: {edge_count}", bg='#333333', fg="white")
    total_label.pack()

    heads_prob_label = tk.Label(text="Probability of heads: 50.00%", bg='#333333', fg="white")
    heads_prob_label.pack()

    tails_prob_label = tk.Label(text="Probability of tails: 50.00%", bg='#333333', fg="white")
    tails_prob_label.pack()

    coin_label = tk.Label(window, image=heads_gif_frames[0])
    coin_label.heads_gif_frames = heads_gif_frames
    coin_label.tails_gif_frames = tails_gif_frames
    coin_label.pack()

    result_label = tk.Label(window, text="")
    result_label.pack(pady=10)

    
    def toggle_auto_flip():
        nonlocal auto_flipping
        auto_flipping = not auto_flipping
        if auto_flipping:
            auto_flip()

    def auto_flip():
        if auto_flipping:
            flip_coin()
            window.after(500, auto_flip)

    def flip_coin():
        nonlocal head_count, tail_count, total_flips, total_label, edge_count

        outcome = random.choices(["Heads", "Tails", "Edge"], weights=[0.5, 0.5, 0.0001667])[0] #1 in 6000 chance for edge
        if outcome == "Heads":
            coin_label.config(image=heads_gif_frames[0])
            head_count += 1
            #tail_count = 0
            total_flips += 1
        elif outcome == "Tails":
            coin_label.config(image=tails_gif_frames[0])
            tail_count += 1
            #head_count = 0
            total_flips += 1
        else:
            edge_count += 1
            total_flips += 1

        result_label.config(text=f"The coin landed on: {outcome}")
            
        if outcome == "Heads":
            for frame in heads_gif_frames:
                coin_label.config(image=frame)
                window.update()
        elif outcome == "Tails":
            for frame in tails_gif_frames:
                coin_label.config(image=frame)
                window.update()
        else:
            window.after(2000, lambda: coin_label.config(image=heads_gif_frames[0]))

        if total_flips > 0:
            heads_prob = "{:.2f}".format((head_count / total_flips) * 100)
            tails_prob = "{:.2f}".format((tail_count / total_flips) * 100)
            #heads_prob_label.config(text=f"Probability of heads: {heads_prob}%")
            #tails_prob_label.config(text=f"Probability of tails: {tails_prob}%")
            total_label.config(text=f"Total: {total_flips} | Heads flipped: {head_count} | Tails flipped: {tail_count} | Edges flipped: {edge_count}", bg='#333333', fg="white")
    
    button = tk.Button(window, text="Flip the coin", command=flip_coin, bg='#333333', fg="white")
    button.pack()

    button1 = tk.Button(window, text="Auto flip", command=toggle_auto_flip, bg='#333333', fg="white")
    button1.pack(pady=10)

    result_label.configure(bg='#333333', fg="white")

    window.mainloop() 

if __name__ == "__main__":
    main()