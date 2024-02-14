import time 


class ImageGenerationSpeed:
    def benchmark(pipeline, prompt="a dog"):
        # call the `pipeline` object here on the `prompt` to
        # warm up the hardware.
        _ = pipeline(prompt=prompt)

        # run for five iterations.
        tic = time.time_ns()
        for _ in range(5):
            # call the `pipeline` object here on the `prompt`.
            _ = pipeline(prompt=prompt)
        tok = time.time_ns() 
        # print the total elapsed time.
        print(f"Execution time -- {(tok - tic) / 1e6:.1f} ms\n")

if __name__ == '__main__':
    pass
