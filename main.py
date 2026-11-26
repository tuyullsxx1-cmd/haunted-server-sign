import os

LINE = "WARNING: this server room is haunted. Do not unplug anything. The ghosts maintain our 99.99% uptime."

assert "\n" not in LINE
# The 120-character ceiling comes from the bounty brief for this sign.
assert len(LINE) <= 120

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
