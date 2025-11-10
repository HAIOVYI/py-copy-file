def copy_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) < 3:
        return

    cmd, src, dst = parts
    if cmd != "cp":
        return

    if src == dst:
        return

    try:
        with open(src) as file_in, open(dst, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        pass
