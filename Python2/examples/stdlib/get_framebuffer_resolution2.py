import subprocess
import re


def get_framebuffer_resolution(framebuffer_device):
    fbset_output = subprocess.check_output(["fbset", "-s", "-fb", framebuffer_device])

    regexp = re.compile(r"geometry (\d+) (\d+)")

    for line in fbset_output.split("\n"):
        line = line.strip()
        if line.startswith("geometry"):
            print(line)
            parsed = regexp.match(line)
            return (parsed.group(1), parsed.group(2))


print(get_framebuffer_resolution("/dev/fb0"))
