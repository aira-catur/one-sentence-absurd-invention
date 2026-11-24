import os

TEXT = "The DozeChute, a tiny parachute clipped to your phone, senses the exact moment you fall asleep scrolling in bed and pops open to lower it gently onto the pillow instead of onto your face."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
