import time


def timing_decorator(func):
    """Decorator to calculate the runtime of a function."""

    def wrapper(*args, **kwargs):
        # Record the start time
        start_time = time.time()

        # Call the original function
        result = func(*args, **kwargs)

        # Record the end time
        end_time = time.time()

        # Calculate the elapsed time
        elapsed_time = end_time - start_time

        # Print the elapsed time
        print(
            # f"Function '{func.__name__}' took {elapsed_time:.4f} seconds to complete."
            f"Function '{func.__name__}' took {elapsed_time:.10f} seconds to complete."
        )

        # Return the result of the original function
        return result

    return wrapper
