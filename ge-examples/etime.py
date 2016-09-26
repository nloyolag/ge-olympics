def print_elapsed_time(start_time, stop_time):
    elapsed_time = stop_time - start_time
    if elapsed_time < 60:
        print("Elapsed time:", elapsed_time, "seconds")
    else:
        print("Elapsed time:", elapsed_time / 60, "minutes")
