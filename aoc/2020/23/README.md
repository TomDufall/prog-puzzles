# Performance investigation/comparison
The Python version of this had some performance issues at first - ~18s on a desktop PC for the nicely readable version. Optimising this by removing the inner class and reducing calls to `self.` reduced this down to ~7s. I also compared this to someone else's pure Python solution which was ~5s. I then re-implemented it in Go, which runs in ~0.5-0.55s.
