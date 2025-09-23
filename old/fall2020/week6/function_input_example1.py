def func(spam, eggs, toast=0, ham=0):   # first 2 required
    print (spam, eggs, toast, ham)

func(1, 2)                              # output: (1, 2, 0, 0)
func(1, ham=1, eggs=0)                  # output: (1, 0, 0, 1)
func(spam=1, eggs=0)                    # output: (1, 0, 0, 0)
func(toast=1, eggs=2, spam=3)           # output: (3, 2, 1, 0)
func(1, 2, 3, 4)                        # output: (1, 2, 3, 4)
