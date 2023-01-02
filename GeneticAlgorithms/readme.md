# Solve maze with genetic algorithms

Your goal is to use genetic algorithms to find a path out of any maze, represented as
a vector of strings, where `#` characters represent walls, `.` represent empty spaces,
and S and E represent the starting and ending points, as in a given example below.

```
maze = list("####E######",
            "##...#.####",
            "#..#.#.####",
            "#.##...####",
            "#.##.#..S##",
            "###########")
```

You can move through the maze in four different directions:

- left (`L`)
- right (`R`)
- up (`U`)
- down (`D`).

In the example above, the shortest path from the starting position `S` to the exit `E` is
composed of the following moves: **`LLULLUUU`**.
